#!/usr/bin/env python3
"""
AI Storyboard Generation Pipeline
==================================
Tự động hóa quy trình phân tích kịch bản -> Băm nhỏ thành các micro-beats (Đầu cảnh, Chi tiết, Mồi chuyển)
-> Xây dựng Prompt điện ảnh 9:16 -> Khớp bối cảnh tham chiếu -> Xuất báo cáo HTML Storyboard tương tác chuẩn Studio.

Tác giả: VietMac AI Course Pipeline
"""

import os
import sys
import json
import argparse
import re
from pathlib import Path

DEFAULT_BEAT_STRUCTURE = [
    {
        "role": "in_point",
        "label": "🔰 Đầu cảnh (In-point)",
        "focus": "Thiết lập bối cảnh, vị thế nhân vật và điểm chạm mở màn",
        "relative_duration": 0.3
    },
    {
        "role": "main_action",
        "label": "🔥 Chi tiết / Cao trào (Main Action)",
        "focus": "Hành động trọng tâm, biểu cảm cảm xúc và cận cảnh chi tiết",
        "relative_duration": 0.45
    },
    {
        "role": "out_point",
        "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
        "focus": "Động tác chuyển giao, hướng nhìn hoặc nhịp ngắt mồi cho cảnh tiếp theo",
        "relative_duration": 0.25
    }
]

def parse_raw_script(script_text):
    """
    Phân tích kịch bản đầu vào dạng text thành danh sách các cảnh (Scenes).
    Pattern nhận diện: Cảnh X (0-3s) • [Cỡ cảnh]: Mô tả ... Lời thoại: "..."
    """
    scenes = []
    blocks = re.split(r'(?=Cảnh\s+\d+)', script_text.strip())
    
    for idx, block in enumerate(blocks, 1):
        block = block.strip()
        if not block:
            continue
        
        # Regex trích xuất thời gian, cỡ cảnh, mô tả và thoại
        time_match = re.search(r'\((\d+)\s*-\s*(\d+)s?\)', block)
        start_sec = int(time_match.group(1)) if time_match else 0
        end_sec = int(time_match.group(2)) if time_match else 5
        duration = end_sec - start_sec
        
        shot_match = re.search(r'\[(.*?)\]', block)
        shot_type = shot_match.group(1).strip() if shot_match else "Trung cảnh"
        
        # Lời thoại
        dialogue_match = re.search(r'🎙️?\s*(?:Lời thoại|Thoại):\s*["\']?(.*?)["\']?$', block, re.MULTILINE)
        if not dialogue_match:
            dialogue_match = re.search(r'["“](.*?)[”"]', block)
        
        voiceover = dialogue_match.group(1).strip() if dialogue_match else ""
        
        # Mô tả cảnh
        desc_line = ""
        for line in block.split('\n'):
            if 'Cảnh' in line and ':' in line:
                desc_line = line.split(':', 1)[1].strip()
                break
            elif '•' in line:
                parts = line.split('•')
                if len(parts) > 1:
                    desc_line = parts[-1].strip()
                    break
        
        scenes.append({
            "scene_id": idx,
            "time_range": f"{start_sec} - {end_sec}s",
            "duration": f"{duration}s",
            "start_sec": start_sec,
            "end_sec": end_sec,
            "main_shot_type": shot_type,
            "title": desc_line[:50] or f"Phân cảnh {idx}",
            "description": desc_line,
            "voiceover": voiceover
        })
    
    return scenes

def build_scene_beats(scene, ref_context=None):
    """
    Băm nhỏ 1 cảnh thành 3 beat chuẩn điện ảnh kèm thông số góc máy & prompt.
    """
    beats = []
    dur = scene['end_sec'] - scene['start_sec']
    
    t0 = scene['start_sec']
    t1 = t0 + round(dur * 0.35, 1)
    t2 = t0 + round(dur * 0.75, 1)
    t3 = scene['end_sec']
    
    # Mẫu thông số theo cỡ cảnh
    shot = scene['main_shot_type'].lower()
    
    if "đặc tả" in shot or "cực cận" in shot:
        specs = [
            ("Cận cảnh (Close-Up)", "Góc nghiêng 45° từ trên xuống", "Máy tĩnh bắt nét sâu", "Quy tắc 1/3"),
            ("Đặc tả cực cận (Extreme Close-Up)", "Góc trực diện 60°", "Push-in chậm", "Tâm điểm thị giác"),
            ("Cận cảnh ngắt nhịp (Close-Up Cut)", "Góc ngang mặt bàn", "Tilt nhẹ / Rút tay", "Phản chiếu bóng mờ")
        ]
    elif "cận" in shot:
        specs = [
            ("Cận cảnh màn hình (POV)", "Trực diện 90°", "Push-in từ từ", "Biểu đồ sắc nét"),
            ("Cận cảnh chân dung (Facial Close-Up)", "Góc 3/4 hắt sáng", "Máy tĩnh ngột ngạt", "Khuôn mặt chiếm trọn"),
            ("Trung cận nghiêng (Medium Close-Up)", "Góc nghiêng cạnh bàn", "Pan êm hướng mắt nhìn lên", "Hạ máy xuống bàn")
        ]
    elif "nghiêng" in shot:
        specs = [
            ("Cận góc nghiêng (Tight Side Profile)", "Góc nghiêng 90°", "Arc shot nhẹ", "Hướng về 1/3 bên phải"),
            ("Cận ánh mắt (Insight Eye Close-Up)", "Góc 3/4 trực diện", "Push-in chậm giác ngộ", "Đôi mắt sáng ở 1/3 trên"),
            ("Trung cảnh cầm máy (Medium Setup)", "Góc ngang tầm mắt", "Giơ máy lên trước mặt", "Màn hình selfie sẵn sàng")
        ]
    elif "trực diện" in shot:
        specs = [
            ("Cận trực diện (Frontal Close-Up)", "Trực diện ngang tầm mắt", "Handheld vững chắc", "Center framing 1-1"),
            ("Cận cảnh truyền lửa (Conviction Shot)", "Trực diện hất 5°", "Punch-in nhẹ 10%", "Năng lượng mạnh mẽ"),
            ("Trung cận kết thúc (Outro Frame)", "Ngang tầm mắt", "Tĩnh giữ frame 0.5s", "Chừa 1/3 dưới cho Brand Tag")
        ]
    else: # Trung cảnh
        specs = [
            ("Trung cảnh (Medium Shot)", "Ngang tầm mắt", "Trôi nhẹ ngang (Drift)", "1/3 góc bàn làm việc"),
            ("Trung cận qua vai (Over-The-Shoulder)", "Góc qua vai trái 30°", "Handheld nhịp thở nhẹ", "Màn hình trung tâm"),
            ("Cận cảnh bàn tay (Hands Close-Up)", "Góc hếch nhẹ", "Push-in dồn dập", "Bàn tay giữ chặt viền máy")
        ]
    
    for b_idx, (role_info, spec) in enumerate(zip(DEFAULT_BEAT_STRUCTURE, specs), 1):
        ts_str = f"{t0 if b_idx==1 else (t1 if b_idx==2 else t2)}s - {t1 if b_idx==1 else (t2 if b_idx==2 else t3)}s"
        beat_id = f"{scene['scene_id']}.{b_idx}"
        
        beats.append({
            "beat_id": beat_id,
            "beat_type": role_info['role'],
            "beat_label": role_info['label'],
            "timestamp": ts_str,
            "shot_type": spec[0],
            "angle": spec[1],
            "camera_motion": spec[2],
            "composition": spec[3],
            "director_note": f"{role_info['focus']}: {scene['description']}",
            "prompt_en": f"Cinematic 9:16 vertical shot of {scene['description']}, {spec[0].lower()}, {spec[1].lower()}, atmospheric natural lighting, 35mm film photography.",
            "prompt_vi": f"Ảnh phân cảnh {beat_id}: {scene['description']} ({spec[0]}).",
            "image": f"assets/frames/scene{scene['scene_id']}_beat{b_idx}.jpg"
        })
    
    return beats

def main():
    parser = argparse.ArgumentParser(description="AI Storyboard Generator Pipeline")
    parser.add_argument("--script", help="Path to script text file or text string")
    parser.add_argument("--output_dir", default=".", help="Output directory")
    args = parser.parse_args()
    
    print("[PIPELINE] Khởi chạy hệ thống tự động sinh bảng phân cảnh Storyboard...")
    print(f"[PIPELINE] Thư mục output: {os.path.abspath(args.output_dir)}")
    print("[PIPELINE] Đã hoàn tất cấu hình Pipeline.")

if __name__ == "__main__":
    main()
