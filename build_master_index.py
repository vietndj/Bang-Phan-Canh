#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HỆ THỐNG MASTER HUB SCANNER & INDEX BUILDER TỰ ĐỘNG
===================================================
Tự động quét toàn bộ các file .html trong repo Bang-Phan-Canh,
trích xuất metadata và biên dịch trang chủ index.html cập nhật 100% các dự án.
"""

import os
import re
import glob
from datetime import datetime

REPO_DIR = "/Users/vietmac/Documents/CODE/Bang-Phan-Canh"
R2_MEDIA_BASE = "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien"

# 1. Danh mục định nghĩa chi tiết (nếu có sẵn thông tin phong phú)
KNOWN_SCRIPTS = {
    "tu_dot_tien_den_tu_tin_xuat_hien.html": {
        "num": "GỐC",
        "title": "Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện",
        "tag": "CHỦ SHOP & BÁN ONLINE",
        "category": "Kinh Doanh & Bán Hàng",
        "badge_color": "#38bdf8",
        "target_audience": "Chủ shop, người bán hàng online phụ thuộc chạy Ads",
        "context_desc": "Bối cảnh: Phòng học / Điện thoại • Chạm vào: Bế tắc vì phụ thuộc Ads",
        "hook_dialogue": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
        "summary": "Nỗi đau chi phí quảng cáo tăng gấp đôi, tiền nạp ăn hết lãi. Chuyển dịch tư duy sang tự quay video xuất hiện để xây dựng niềm tin thật."
    },
    "kich_ban_01_ngoi_ca_phe_10h_toi.html": {
        "num": "01",
        "title": "Ngồi Cà Phê 10h Tối",
        "tag": "LÀM VIỆC ĐÊM & BẾ TẮC",
        "category": "Tâm Lý & Áp Lực Kiệt Sức",
        "badge_color": "#6366f1",
        "target_audience": "Người trẻ làm nghề, freelancer cày đêm vì bất an",
        "context_desc": "Bối cảnh: Góc bàn cafe / Bàn học đêm • Chạm vào: Áp lực FOMO & Kiệt sức",
        "hook_dialogue": "10h tối, ngồi ở góc quán này không phải vì chăm chỉ...",
        "summary": "Bóc trần thói quen 'cố tỏ ra bận rộn' để xoa dịu nỗi sợ tụt hậu của giới trẻ và dân làm nghề."
    },
    "kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach.html": {
        "num": "02",
        "title": "Tiền Mặt Bằng & Cửa Hàng Vắng Khách",
        "tag": "CHỦ SHOP & MỞ TIỆM",
        "category": "Kinh Doanh Cửa Hàng & Bán Lẻ",
        "badge_color": "#e11d48",
        "target_audience": "Chủ shop offline, chủ tiệm dịch vụ chịu áp lực mặt bằng",
        "context_desc": "Bối cảnh: Phòng học / Bàn làm việc • Chạm vào: Áp lực chi phí mặt bằng & vắng khách",
        "hook_dialogue": "Sáng Chủ Nhật, tôi ngồi ở lớp này không phải vì rảnh rỗi...",
        "summary": "Cửa hàng vắng khách nhưng tiền thuê nhà vẫn trừ đều mỗi tháng. Muốn khách ghé tiệm thì chủ shop phải xuất hiện trước."
    },
    "kich_ban_03_chung_lai_sau_tuoi_30.html": {
        "num": "03",
        "title": "Chững Lại Sau Tuổi 30",
        "tag": "NGƯỜI LÀM VĂN PHÒNG",
        "category": "Phát Triển Bản Thân & Nghề Nghiệp",
        "badge_color": "#f59e0b",
        "target_audience": "Người làm văn phòng 30+, người sợ tụt hậu công nghệ",
        "context_desc": "Bối cảnh: Phòng học / Laptop • Chạm vào: Khủng hoảng tuổi 30 & Sợ tụt hậu",
        "hook_dialogue": "Hơn 30 tuổi, ngồi trong căn phòng này cùng mọi người...",
        "summary": "Khủng hoảng tuổi 30 khi thu nhập đứng yên mà chi phí tăng. Quyết tâm học lại từ đầu để không bị tụt lại phía sau."
    },
    "kich_ban_04_tien_quang_cao_an_het_tien_lai.html": {
        "num": "04",
        "title": "Tiền Quảng Cáo Ăn Hết Tiền Lãi",
        "tag": "BÁN HÀNG ONLINE",
        "category": "Kinh Doanh & Bán Hàng Online",
        "badge_color": "#38bdf8",
        "target_audience": "Người kinh doanh online phụ thuộc hoàn toàn vào Ads",
        "context_desc": "Bối cảnh: Phòng học / Điện thoại • Chạm vào: Bế tắc vì phụ thuộc chạy Ads",
        "hook_dialogue": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
        "summary": "Tiền nạp vào ăn gần hết tiền lãi. Tự quay video xuất hiện để khách hàng tin mình trước khi mua."
    },
    "kich_ban_05_het_khach_tu_moi_quan_he_quen.html": {
        "num": "05",
        "title": "Hết Khách Từ Mối Quan Hệ Quen",
        "tag": "FREELANCER & DỊCH VỤ",
        "category": "Khai Thác Khách Hàng & Dịch Vụ",
        "badge_color": "#10b981",
        "target_audience": "Dân làm dịch vụ, tư vấn viên, người làm nghề tự do",
        "context_desc": "Bối cảnh: Phòng học / Sổ tay • Chạm vào: Cạn kiệt nguồn khách quen",
        "hook_dialogue": "Tôi từng nghĩ chỉ cần làm tốt, khách quen sẽ tự giới thiệu...",
        "summary": "Khai thác hết người quen thì doanh thu rơi tự do. Phải xuất hiện trên internet để tiếp cận người lạ."
    },
    "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach.html": {
        "num": "06",
        "title": "Tay Nghề Tốt Nhưng Vẫn Vắng Khách",
        "tag": "CHUYÊN GIA & LÀM NGHỀ",
        "category": "Xây Dựng Thương Hiệu Cá Nhân",
        "badge_color": "#8b5cf6",
        "target_audience": "Thợ lành nghề, chuyên gia kỹ thuật, người có chuyên môn sâu",
        "context_desc": "Bối cảnh: Phòng học / Lớp đào tạo • Chạm vào: Nghịch lý giỏi nghề nhưng ế khách",
        "hook_dialogue": "Làm nghề gần chục năm, tay nghề không thua kém ai...",
        "summary": "Người làm dở nhưng chịu xuất hiện thì kín lịch, người làm kỹ lại ế khách. Giỏi nghề thôi chưa đủ, phải biết xuất hiện."
    },
    "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc.html": {
        "num": "07",
        "title": "Bị Cạnh Tranh Bởi Tổng Kho & Giá Gốc",
        "tag": "THƯƠNG MẠI & BÁN LẺ",
        "category": "Cạnh Tranh & Định Vị",
        "badge_color": "#ec4899",
        "target_audience": "Người bán hàng nhập lẻ, đại lý phân phối nhỏ",
        "context_desc": "Bối cảnh: Phòng học / Điện thoại • Chạm vào: Cuộc chiến phá giá & tổng kho",
        "hook_dialogue": "Nhìn tổng kho họ livestream bán giá bằng đúng giá mình nhập...",
        "summary": "Càng đua giảm giá càng chết nhanh. Khách mua vì tin con người đứng sau sản phẩm chứ không chỉ vì giá rẻ."
    },
    "kich_ban_08_bat_dau_lai_tu_con_so_0.html": {
        "num": "08",
        "title": "Bắt Đầu Lại Từ Con Số 0",
        "tag": "KHỞI NGHIỆP LẠI",
        "category": "Bản Lĩnh Vượt Khó & Tái Khởi Nghiệp",
        "badge_color": "#f97316",
        "target_audience": "Người từng thất bại kinh doanh, người chuyển đổi ngành nghề",
        "context_desc": "Bối cảnh: Phòng học / Bàn gỗ • Chạm vào: Nỗi sợ xấu hổ khi bắt đầu lại",
        "hook_dialogue": "Từng có cửa hàng, từng có nhân viên... Giờ ngồi đây học lại từ đầu.",
        "summary": "Vứt bỏ cái tôi và sĩ diện của quá khứ. Cầm máy lên quay là cách rẻ nhất và bền nhất để làm lại từ đầu."
    },
    "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html": {
        "num": "09",
        "title": "Hàng Làm Kỹ Nhưng Bị So Sánh Giá",
        "tag": "SẢN XUẤT & ĐỒ KỸ",
        "category": "Giá Trị Thực & Định Giá",
        "badge_color": "#06b6d4",
        "target_audience": "Xưởng sản xuất chất lượng, người làm sản phẩm thủ công / kỹ lưỡng",
        "context_desc": "Bối cảnh: Phòng học / Bàn làm việc • Chạm vào: Bị so sánh với hàng chợ kém chất lượng",
        "hook_dialogue": "Nhập nguyên liệu xịn, làm từng chi tiết cẩn thận... nhưng khách chỉ hỏi 'Sao đắt thế?'.",
        "summary": "Làm kỹ mà không quay lại quy trình cho khách xem thì không ai biết. Phải quay lại độ tinh xảo để khách thấy xứng đáng."
    }
}

def scan_all_storyboards():
    """Tự động quét toàn bộ file .html trong repo."""
    all_files = sorted(glob.glob(os.path.join(REPO_DIR, "*.html")))
    storyboards = []
    
    for fpath in all_files:
        fname = os.path.basename(fpath)
        if fname == "index.html":
            continue
            
        # Đọc nội dung HTML
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Trích xuất metadata tự động từ file HTML
        title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        raw_title = title_m.group(1) if title_m else fname
        
        # Làm sạch title
        clean_title = re.sub(r'Bảng Phân Cảnh Storyboard:\s*', '', raw_title)
        clean_title = re.sub(r'\s*\|\s*AI Storyboard Studio', '', clean_title)
        
        # Lấy thông tin từ cấu hình đã biết hoặc fallback tự động
        info = KNOWN_SCRIPTS.get(fname, {})
        num = info.get("num", "KB")
        title = info.get("title", clean_title)
        tag = info.get("tag", "STORYBOARD 9:16")
        category = info.get("category", "Kinh Doanh & Đời Sống")
        badge_color = info.get("badge_color", "#38bdf8")
        target_audience = info.get("target_audience", "Người làm kinh doanh, sáng tạo nội dung ngắn")
        context_desc = info.get("context_desc", "Bối cảnh: Không gian thực tế Times City & Studio")
        
        # Tìm câu hook quote
        hook_m = re.search(r'class="director-bubble"[^>]*>.*?"(.*?)"', content, re.DOTALL)
        if not hook_m:
            hook_m = re.search(r'class="card-quote"[^>]*>.*?🎙️\s*"(.*?)"', content, re.DOTALL)
        hook_dialogue = info.get("hook_dialogue", hook_m.group(1) if hook_m else "Cầm máy lên và tự tin xuất hiện trước khách hàng...")
        
        summary = info.get("summary", "Bảng phân cảnh điện ảnh 9:16 băm nhỏ 15 beat chi tiết.")
        
        # Thu thập 15 frames thumbnail
        frames = []
        for s in range(1, 6):
            for b in range(1, 4):
                frames.append(f"{R2_MEDIA_BASE}/assets/frames/scene{s}_beat{b}.jpg")
                
        thumb_url = frames[0]
        
        storyboards.append({
            "file_name": fname,
            "num": num,
            "title": title,
            "tag": tag,
            "category": category,
            "badge_color": badge_color,
            "target_audience": target_audience,
            "context_desc": context_desc,
            "hook_dialogue": hook_dialogue,
            "summary": summary,
            "thumb_url": thumb_url,
            "mini_frames": frames,
            "duration": "30 Giây",
            "beats_count": 15,
            "scenes_count": 5
        })
        
    return storyboards

def generate_master_hub_html(storyboards):
    categories = sorted(list(set(s["category"] for s in storyboards)))
    total_scenes = sum(s["scenes_count"] for s in storyboards)
    total_beats = sum(s["beats_count"] for s in storyboards)
    build_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>Kho Bảng Phân Cảnh Điện Ảnh 9:16 | Master Storyboard Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #0a0e17;
      --bg-surface: #111827;
      --bg-card: #162032;
      --bg-card-hover: #1c2a42;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.35);
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.15);
      --amber: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.15);
      --emerald: #10b981;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-primary);
      line-height: 1.6;
      padding-bottom: 80px;
    }}
    .container {{ max-width: 1300px; margin: 0 auto; padding: 0 20px; }}
    
    /* Top Header */
    .top-header {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(10, 14, 23, 0.92);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 14px 24px;
      display: flex; justify-content: space-between; align-items: center; gap: 16px;
    }}
    .brand-group {{ display: flex; align-items: center; gap: 10px; }}
    .brand-badge {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .header-title {{ font-size: 16px; font-weight: 700; color: var(--text-primary); }}
    .header-controls {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
    .header-link {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); color: var(--text-secondary);
      font-size: 12px; font-weight: 600; padding: 7px 14px; border-radius: var(--radius-sm); text-decoration: none; transition: all 0.2s;
    }}
    .header-link:hover {{ background: var(--cyan); color: #000; border-color: var(--cyan); }}
    
    /* Hero Section */
    .hero {{
      background: linear-gradient(180deg, #131d2e 0%, #0d1522 100%);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      margin: 30px auto;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    .hero::before {{
      content: ''; position: absolute; top: -50%; left: 50%; transform: translateX(-50%);
      width: 600px; height: 300px; background: radial-gradient(circle, rgba(56, 189, 248, 0.12) 0%, transparent 70%);
      pointer-events: none;
    }}
    .hero-badge {{
      display: inline-flex; align-items: center; gap: 6px;
      background: var(--cyan-glow); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 12px; border-radius: 9999px; font-size: 11.5px; font-weight: 700; margin-bottom: 14px;
    }}
    .hero h1 {{
      font-size: 32px; font-weight: 800; color: #fff; margin-bottom: 12px; line-height: 1.3;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hero-desc {{
      color: var(--text-secondary); font-size: 15px; max-width: 820px; margin: 0 auto 24px;
    }}
    
    /* Stats Bar */
    .stats-bar {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px;
      background: rgba(0, 0, 0, 0.3); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 16px 20px;
    }}
    .stat-item {{ text-align: center; }}
    .stat-label {{ font-size: 11px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px; }}
    .stat-val {{ font-size: 22px; font-weight: 800; color: var(--text-primary); }}
    
    /* Filter Bar */
    .filter-bar {{
      display: flex; justify-content: space-between; align-items: center; gap: 16px; margin: 32px 0 20px; flex-wrap: wrap;
    }}
    .search-box {{ position: relative; flex: 1; min-width: 260px; max-width: 400px; }}
    .search-input {{
      width: 100%; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm);
      padding: 10px 14px 10px 36px; color: #fff; font-size: 13px; outline: none; transition: border-color 0.2s;
    }}
    .search-input:focus {{ border-color: var(--cyan); }}
    .search-icon {{ position: absolute; left: 12px; top: 50%; transform: translateY(-50%); font-size: 14px; color: var(--text-muted); }}
    .filter-tags {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .filter-tag {{
      background: var(--bg-surface); border: 1px solid var(--border-subtle); color: var(--text-secondary);
      padding: 6px 14px; border-radius: 9999px; font-size: 12px; font-weight: 600; cursor: pointer; transition: all 0.2s;
    }}
    .filter-tag:hover, .filter-tag.active {{ background: var(--cyan); color: #000; border-color: var(--cyan); font-weight: 700; }}
    
    /* Storyboard Grid */
    .storyboards-grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(580px, 1fr)); gap: 24px;
    }}
    @media (max-width: 700px) {{ .storyboards-grid {{ grid-template-columns: 1fr; }} }}
    
    .sb-card {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
      overflow: hidden; display: flex; flex-direction: column; transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    }}
    .sb-card:hover {{
      transform: translateY(-4px); border-color: var(--border-accent); box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }}
    
    .card-top {{ display: flex; gap: 18px; padding: 22px; border-bottom: 1px solid var(--border-subtle); }}
    @media (max-width: 500px) {{ .card-top {{ flex-direction: column; }} }}
    
    .card-thumb-wrap {{
      flex: 0 0 140px; aspect-ratio: 9 / 16; background: #000; border-radius: var(--radius-sm);
      overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); position: relative;
    }}
    .card-thumb-wrap img {{ width: 100%; height: 100%; object-fit: cover; }}
    .card-badge-tag {{
      position: absolute; top: 6px; left: 6px; font-size: 9px; font-weight: 800;
      padding: 2px 6px; border-radius: 4px; text-transform: uppercase; background: rgba(0, 0, 0, 0.75); color: #fff;
    }}
    
    .card-info {{ flex: 1; display: flex; flex-direction: column; }}
    .card-meta-row {{ display: flex; gap: 8px; margin-bottom: 8px; flex-wrap: wrap; }}
    .pill {{ font-size: 10.5px; font-weight: 700; padding: 2px 8px; border-radius: 4px; }}
    .card-title {{ font-size: 18px; font-weight: 800; color: #fff; margin-bottom: 6px; line-height: 1.3; }}
    .card-summary {{ font-size: 12.5px; color: var(--text-secondary); line-height: 1.4; margin-bottom: 10px; }}
    .card-quote {{
      background: rgba(0, 0, 0, 0.35); border-left: 3px solid var(--cyan); padding: 8px 12px;
      font-size: 12px; font-style: italic; color: #e2e8f0; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin-top: auto;
    }}
    
    .card-strip {{
      padding: 12px 22px; background: rgba(0, 0, 0, 0.15); display: flex; gap: 6px; overflow-x: auto;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .card-strip::-webkit-scrollbar {{ height: 4px; }}
    .card-strip::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,0.15); border-radius: 2px; }}
    .card-strip-thumb {{
      flex: 0 0 54px; aspect-ratio: 9 / 16; border-radius: 4px; overflow: hidden; background: #000;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .card-strip-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
    
    .card-bottom {{
      padding: 14px 22px; display: flex; justify-content: space-between; align-items: center; gap: 10px; flex-wrap: wrap;
    }}
    .card-metrics-mini {{ font-size: 11.5px; color: var(--text-muted); }}
    .view-btn {{
      background: linear-gradient(135deg, #0284c7, #2563eb); color: #fff; font-size: 12px; font-weight: 700;
      padding: 8px 16px; border-radius: var(--radius-sm); text-decoration: none; display: inline-flex; align-items: center; gap: 6px;
      transition: all 0.2s;
    }}
    .view-btn:hover {{ background: linear-gradient(135deg, #38bdf8, #0284c7); color: #000; transform: translateY(-1px); }}
    
    /* Guide Section */
    .guide-box {{
      background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
      padding: 28px; margin-top: 40px;
    }}
    .guide-title {{ font-size: 18px; font-weight: 800; color: #fff; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; }}
    .guide-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }}
    .guide-card {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 16px;
    }}
    .guide-card-title {{ font-size: 13px; font-weight: 700; color: var(--cyan); margin-bottom: 6px; }}
    .guide-card-text {{ font-size: 12px; color: var(--text-secondary); line-height: 1.5; }}
    .guide-code {{ background: #000; color: #38bdf8; font-family: 'JetBrains Mono', monospace; font-size: 11px; padding: 4px 8px; border-radius: 4px; display: block; margin-top: 6px; }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">Master Hub</span>
      <div class="header-title">🎬 Bảng Phân Cảnh AI Studio (vietndj/Bang-Phan-Canh)</div>
    </div>
    <div class="header-controls">
      <a href="https://github.com/vietndj/Bang-Phan-Canh" target="_blank" class="header-link">🐙 GitHub Repo</a>
      <a href="https://fedu.vn/Bang-Phan-Canh/" class="header-link">🌐 Cổng fedu.vn</a>
    </div>
  </header>

  <div class="container">
    
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-badge">⚡ Automated 9:16 Vertical Storyboard Engine</div>
      <h1>Kho Bảng Phân Cảnh Điện Ảnh 9:16 Tự Động</h1>
      <p class="hero-desc">
        Hệ thống tự động hóa chuyển đổi kịch bản nói và ảnh bối cảnh thành bảng phân cảnh 3 nhịp (In-point, Main action, Out-point), đồng bộ lưu trữ Cloudflare R2 CDN và xuất bản trực tuyến.
      </p>
      
      <div class="stats-bar">
        <div class="stat-item">
          <div class="stat-label">Tổng Kịch Bản</div>
          <div class="stat-val">{len(storyboards)} Dự Án</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">Tổng Phân Cảnh</div>
          <div class="stat-val">{total_scenes} Cảnh Chính</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">Khung Hình Chi Tiết</div>
          <div class="stat-val">{total_beats} Micro-Beats</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">Cập Nhật Mới Nhất</div>
          <div class="stat-val" style="color: var(--cyan); font-size: 15px; font-family: 'JetBrains Mono';">{build_time}</div>
        </div>
      </div>
    </section>

    <!-- Filter Bar -->
    <div class="filter-bar">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm theo tiêu đề, lời thoại, target audience..." onkeyup="filterCards()">
      </div>
      <div class="filter-tags">
        <button class="filter-tag active" onclick="filterCategory('all', this)">Tất cả ({len(storyboards)})</button>
"""

    for cat in categories:
        html += f"""        <button class="filter-tag" onclick="filterCategory('{cat}', this)">{cat}</button>\n"""

    html += f"""      </div>
    </div>

    <!-- Storyboard Grid -->
    <div class="storyboards-grid" id="storyboardList">
"""

    for sb in storyboards:
        html += f"""
      <div class="sb-card" data-category="{sb['category']} {sb['tag']} {sb['title']} {sb['hook_dialogue']}">
        <div class="card-top">
          <div class="card-thumb-wrap">
            <img src="{sb['thumb_url']}" alt="{sb['title']}">
            <span class="card-badge-tag">KB {sb['num']}</span>
          </div>
          <div class="card-info">
            <div class="card-meta-row">
              <span class="pill" style="background: {sb['badge_color']}22; color: {sb['badge_color']}; border: 1px solid {sb['badge_color']}55;">{sb['tag']}</span>
              <span class="pill" style="background: rgba(255,255,255,0.06); color: var(--text-muted);">{sb['duration']} • {sb['beats_count']} Beats</span>
            </div>
            <h2 class="card-title">{sb['title']}</h2>
            <p class="card-summary">{sb['context_desc']}</p>
            <div class="card-quote">🎙️ "{sb['hook_dialogue']}"</div>
          </div>
        </div>
        
        <div class="card-strip">
"""
        for mf in sb["mini_frames"]:
            html += f"""          <div class="card-strip-thumb"><img src="{mf}" alt="f"></div>\n"""

        html += f"""
        </div>
        
        <div class="card-bottom">
          <div class="card-metrics-mini">
            <span>🎯 Target: <b>{sb['target_audience']}</b></span>
          </div>
          <a href="{sb['file_name']}" class="view-btn">🎬 Mở Bảng Phân Cảnh ➔</a>
        </div>
      </div>
"""

    html += """
    </div>

    <!-- Guide Section -->
    <section class="guide-box">
      <h2 class="guide-title">💡 Cách Tạo Thêm Bảng Phân Cảnh Mới Tự Động</h2>
      <div class="guide-grid">
        <div class="guide-card">
          <div class="guide-card-title">1. Gửi qua Telegram Bot (@nova0410_bot)</div>
          <div class="guide-card-text">
            Gửi 1–3 ảnh bối cảnh kèm caption kịch bản hoặc gõ lệnh:
            <span class="guide-code">/storyboard [Dán kịch bản hoặc link online]</span>
          </div>
        </div>
        <div class="guide-card">
          <div class="guide-card-title">2. Giao việc trong Antigravity IDE</div>
          <div class="guide-card-text">
            Nhắn trực tiếp trong chat:
            <span class="guide-code">"Lên bảng phân cảnh cho kịch bản này giúp tôi..."</span>
          </div>
        </div>
        <div class="guide-card">
          <div class="guide-card-title">3. Tự động xuất bản GitHub Pages & R2</div>
          <div class="guide-card-text">
            Hệ thống tự động băm nhỏ 15 beat, đẩy media lên Cloudflare R2 và cập nhật vào Master Hub này.
          </div>
        </div>
      </div>
    </section>

  </div>

  <script>
    function filterCategory(cat, btn) {
      document.querySelectorAll('.filter-tag').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      const cards = document.querySelectorAll('.sb-card');
      cards.forEach(c => {
        if (cat === 'all') {
          c.style.display = 'flex';
        } else {
          const text = c.getAttribute('data-category').toLowerCase();
          c.style.display = text.includes(cat.toLowerCase()) ? 'flex' : 'none';
        }
      });
    }

    function filterCards() {
      const q = document.getElementById('searchInput').value.toLowerCase();
      const cards = document.querySelectorAll('.sb-card');
      cards.forEach(c => {
        const text = c.getAttribute('data-category').toLowerCase();
        c.style.display = text.includes(q) ? 'flex' : 'none';
      });
    }
  </script>
</body>
</html>
"""
    return html

def main():
    print("=" * 60)
    print("🚀 ĐANG TỰ ĐỘNG QUÉT TOÀN BỘ FILE HTML TRONG REPO...")
    print("=" * 60)
    
    storyboards = scan_all_storyboards()
    print(f"✅ Đã tìm thấy {len(storyboards)} bảng phân cảnh:")
    for s in storyboards:
        print(f"   • [{s['num']}] {s['file_name']} -> {s['title']}")
        
    html_output = generate_master_hub_html(storyboards)
    index_path = os.path.join(REPO_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_output)
        
    print(f"\n🎉 Đã cập nhật thành công {index_path} với đầy đủ {len(storyboards)} dự án!")

if __name__ == "__main__":
    main()
