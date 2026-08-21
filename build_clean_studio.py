import json
import os

# Base CDN URL for R2
R2_BASE = "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien"

raw_input_text = """Cảnh 1 (0-3s) • [Đặc tả]: Ngón tay bấm sáng màn hình điện thoại rồi lại tắt đi trên mặt bàn học.
🎙️ Lời thoại: "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần..."

Cảnh 2 (3-7s) • [Trung cảnh]: Ngồi ở góc bàn lớp học, cầm điện thoại lướt xem số liệu.
🎙️ Lời thoại: "...Người ngoài nhìn vào tưởng mình bận rộn chốt đơn trả lời khách."

Cảnh 3 (7-15s) • [Cận cảnh]: Màn hình điện thoại hiển thị ứng dụng quản lý hoặc bảng chi phí quảng cáo.
🎙️ Lời thoại: "Nhưng thật ra là đang sốt ruột. Mấy tháng nay tiền quảng cáo tăng gấp đôi, tiền nạp vào ăn gần hết tiền lãi."

Cảnh 4 (15-25s) • [Góc nghiêng]: Quay góc nghiêng mặt mình nhìn lên bảng giảng bài, vẻ mặt đăm chiêu.
🎙️ Lời thoại: "Trước đây cứ nghĩ chỉ cần nạp tiền chạy ads là xong việc. Giờ mới thấm: nếu không tự biết cách làm video để người ta tin, thì có bao nhiêu tiền vốn cũng không bù nổi chi phí."

Cảnh 5 (25-30s) • [Trực diện]: Cầm máy ngang tầm mắt, nói dứt khoát vào camera.
🎙️ Lời thoại: "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi." """

data = {
  "project_title": "Bảng Phân Cảnh Storyboard: Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện",
  "project_slug": "tu_dot_tien_den_tu_tin_xuat_hien",
  "total_duration_sec": 30,
  "scenes_count": 5,
  "beats_count": 15,
  "aspect_ratio": "9:16 (Vertical TikTok / Reels)",
  "input_context": {
    "source": "Telegram @nova0410_bot & Antigravity IDE",
    "timestamp": "21/08/2026 08:50:54",
    "raw_text": raw_input_text,
    "ref_images": [
      {
        "title": "Ảnh Bối Cảnh Lớp Học Gốc",
        "url": f"{R2_BASE}/assets/reference/ref_01_classroom.jpg",
        "local_path": "assets/reference/ref_01_classroom.jpg",
        "desc": "Bàn gỗ tự nhiên, sổ tay, bút, ánh sáng xiên cửa lớp học."
      },
      {
        "title": "Ảnh Nhân Vật Tham Chiếu Gốc",
        "url": f"{R2_BASE}/assets/reference/ref_02_character.jpg",
        "local_path": "assets/reference/ref_02_character.jpg",
        "desc": "Nam chủ shop 30 tuổi, áo sơ mi xanh navy tối giản, phong thái suy tư."
      }
    ]
  },
  "scenes": [
    {
      "scene_id": 1,
      "time_range": "0 - 3s",
      "duration": "3s",
      "title": "Bật / Tắt Màn Hình Điện Thoại Liên Tục",
      "main_shot_type": "Đặc tả (Extreme Close-Up / Close-Up)",
      "voiceover": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
      "audio_rhythm": "Nhịp thoại mở màn dứt khoát, tiếng thở dài nhẹ hoặc tiếng click bấm nút nguồn.",
      "director_core_intent": "Thiết lập trạng thái tâm lý bồn chồn, FOMO, thói quen kiểm tra thông báo vô thức của người kinh doanh đang gặp áp lực.",
      "beats": [
        {
          "beat_id": "1.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "0.0s - 1.0s",
          "image": f"{R2_BASE}/assets/frames/scene1_beat1.jpg",
          "shot_type": "Cận cảnh (Close-Up)",
          "angle": "Góc nghiêng 45° từ trên xuống (High-Angle Desk)",
          "camera_motion": "Tĩnh (Static), bắt nét sắc độ sâu vào cạnh điện thoại",
          "composition": "Quy tắc 1/3 bên phải, hậu cảnh mờ nhẹ không gian lớp học",
          "director_note": "Ngón tay vươn ra chạm vào màn hình tối đen. Tạo sự tò mò ngay giây đầu tiên."
        },
        {
          "beat_id": "1.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "1.0s - 2.2s",
          "image": f"{R2_BASE}/assets/frames/scene1_beat2.jpg",
          "shot_type": "Đặc tả cực cận (Extreme Close-Up)",
          "angle": "Góc nhìn từ trên xuống 60° (Top-Down Flat Lay)",
          "camera_motion": "Push-in chậm (Slow Zoom-In)",
          "composition": "Màn hình khóa nằm ngay tâm điểm thị giác, vệt sáng phản chiếu đầu ngón tay",
          "director_note": "Màn hình bừng sáng với đồng hồ và thông báo rỗng. Khắc họa sự sốt ruột và mong chờ mỏi mòn."
        },
        {
          "beat_id": "1.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "2.2s - 3.0s",
          "image": f"{R2_BASE}/assets/frames/scene1_beat3.jpg",
          "shot_type": "Cận cảnh (Close-Up)",
          "angle": "Góc ngang mặt bàn (Low Eye-Level Desk Surface)",
          "camera_motion": "Tilt-up nhẹ + Rút tay (Micro Tilt-up)",
          "composition": "Màn hình đen phản chiếu bóng người, ngón tay rụt lại vào khoảng mờ",
          "director_note": "Màn hình vụt tắt tối om. Tạo nhịp ngắt thị giác (Visual Cut) chuẩn bị nhảy sang toàn cảnh Cảnh 2."
        }
      ]
    },
    {
      "scene_id": 2,
      "time_range": "3 - 7s",
      "duration": "4s",
      "title": "Ngồi Góc Lớp Lướt Xem Số Liệu",
      "main_shot_type": "Trung cảnh (Medium Shot / Over-the-Shoulder)",
      "voiceover": "...Người ngoài nhìn vào tưởng mình bận rộn chốt đơn trả lời khách.",
      "audio_rhythm": "Giọng kể chậm rãi, có chút tự giễu bản thân, âm thanh môi trường lớp học nền nhẹ.",
      "director_core_intent": "Vạch ra sự tương phản giữa vẻ ngoài 'doanh nhân bận rộn' và thực tế tâm trạng bất an bên trong.",
      "beats": [
        {
          "beat_id": "2.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "3.0s - 4.5s",
          "image": f"{R2_BASE}/assets/frames/scene2_beat1.jpg",
          "shot_type": "Trung cảnh (Medium Shot)",
          "angle": "Ngang tầm mắt (Eye Level)",
          "camera_motion": "Trôi nhẹ ngang (Subtle lateral drift / Pan)",
          "composition": "Nhân vật ngồi ở 1/3 bên trái bàn học, hậu cảnh các học viên khác đang lắng nghe",
          "director_note": "Tư thế ngồi nghiêm túc cầm điện thoại, tạo vỏ bọc người bận rộn làm việc."
        },
        {
          "beat_id": "2.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "4.5s - 6.0s",
          "image": f"{R2_BASE}/assets/frames/scene2_beat2.jpg",
          "shot_type": "Trung cận qua vai (Over-the-Shoulder)",
          "angle": "Góc qua vai trái (Over Left Shoulder 30°)",
          "camera_motion": "Cầm tay nhịp thở nhẹ (Handheld breathing)",
          "composition": "Bờ vai và gáy chiếm góc trái, màn hình biểu đồ số liệu rực sáng trung tâm",
          "director_note": "Ngón tay lướt nhanh qua các bảng biểu tài chính, tạo cảm giác dồn dập và áp lực."
        },
        {
          "beat_id": "2.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "6.0s - 7.0s",
          "image": f"{R2_BASE}/assets/frames/scene2_beat3.jpg",
          "shot_type": "Cận cảnh bàn tay (Tight Close-Up on Screen & Hands)",
          "angle": "Góc hếch nhẹ từ dưới lên (Low-Angle Close-Up)",
          "camera_motion": "Push-in dồn vào màn hình (Fast Push-in)",
          "composition": "Hai bàn tay giữ chặt viền máy, ngón tay khựng lại ngay trên điểm cảnh báo",
          "director_note": "Ngón tay dừng lại đột ngột khi nhìn thấy chi phí ads. Mồi cho cảnh phóng to giao diện chi phí ở Cảnh 3."
        }
      ]
    },
    {
      "scene_id": 3,
      "time_range": "7 - 15s",
      "duration": "8s",
      "title": "Bảng Chi Phí Quảng Cáo Tăng Gấp Đôi & Sốt Ruột",
      "main_shot_type": "Cận cảnh (POV Screen & Facial Close-Up)",
      "voiceover": "Nhưng thật ra là đang sốt ruột. Mấy tháng nay tiền quảng cáo tăng gấp đôi, tiền nạp vào ăn gần hết tiền lãi.",
      "audio_rhythm": "Nhịp thoại hạ tông trầm, đầy sự căng thẳng và áp lực kinh tế đè nặng.",
      "director_core_intent": "Khắc họa cú đòn trực diện vào tâm lý kinh doanh: chi phí quảng cáo tăng phi mã làm bốc hơi toàn bộ lợi nhuận.",
      "beats": [
        {
          "beat_id": "3.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "7.0s - 9.5s",
          "image": f"{R2_BASE}/assets/frames/scene3_beat1.jpg",
          "shot_type": "Đặc tả màn hình (Direct UI Close-Up / POV)",
          "angle": "Trực diện 90° vào màn hình điện thoại (Flat POV)",
          "camera_motion": "Push-in từ từ (Slow Creep-In)",
          "composition": "Biểu đồ đường đỏ (Ad Spend +100%) dốc ngược lên, đường xanh lợi nhuận rơi tự do (-65%)",
          "director_note": "Bằng chứng thị giác rõ ràng không thể chối cãi về nỗi đau chi phí tăng gấp đôi."
        },
        {
          "beat_id": "3.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "9.5s - 12.5s",
          "image": f"{R2_BASE}/assets/frames/scene3_beat2.jpg",
          "shot_type": "Cận cảnh chân dung (Facial Close-Up)",
          "angle": "Góc trực diện hơi thấp (Low-Angle Direct Face)",
          "camera_motion": "Máy tĩnh giữ khung hình ngột ngạt (Tense Static Frame)",
          "composition": "Khuôn mặt chiếm trọn khung hình, ánh sáng xanh-đỏ từ màn hình hắt lên trán và mắt",
          "director_note": "Biểu cảm lo âu cực độ, chân mày nhíu chặt, đôi mắt nặng trĩu nhìn vào màn hình."
        },
        {
          "beat_id": "3.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "12.5s - 15.0s",
          "image": f"{R2_BASE}/assets/frames/scene3_beat3.jpg",
          "shot_type": "Trung cận nghiêng (Medium Close-Up Profile)",
          "angle": "Góc nghiêng cạnh bàn (Side Profile Level)",
          "camera_motion": "Pan êm từ tay đặt điện thoại lên hướng mắt nhìn lên (Smooth Pan Upward)",
          "composition": "Tay hạ điện thoại nằm úp trên bàn, đầu ngẩng cao nhìn về phía bục giảng",
          "director_note": "Hành động úp điện thoại thể hiện quyết định ngừng phụ thuộc. Mồi cho cảnh góc nghiêng ngẫm nghĩ Cảnh 4."
        }
      ]
    },
    {
      "scene_id": 4,
      "time_range": "15 - 25s",
      "duration": "10s",
      "title": "Góc Nghiêng Nhìn Lên Bảng - Thấu Suốt Bài Học",
      "main_shot_type": "Góc nghiêng (Side Profile / Insight Close-Up)",
      "voiceover": "Trước đây cứ nghĩ chỉ cần nạp tiền chạy ads là xong việc. Giờ mới thấm: nếu không tự biết cách làm video để người ta tin, thì có bao nhiêu tiền vốn cũng không bù nổi chi phí.",
      "audio_rhythm": "Nhịp chuyển đổi từ bế tắc sang giác ngộ; giọng trầm, dứt khoát từng từ 'để người ta tin'.",
      "director_core_intent": "Khắc họa khoảnh khắc 'Eureka' / Giác ngộ: Bản chất bán hàng online không phải là mua quảng cáo mà là tạo niềm tin qua video chân thực.",
      "beats": [
        {
          "beat_id": "4.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "15.0s - 18.0s",
          "image": f"{R2_BASE}/assets/frames/scene4_beat1.jpg",
          "shot_type": "Cận góc nghiêng (Tight Side Profile Close-Up)",
          "angle": "Góc nghiêng 90° nhìn hướng lên (Side Profile Looking Up)",
          "camera_motion": "Arc shot xoay nhẹ góc nhìn (Slow Subtle Arc)",
          "composition": "Gương mặt hướng về 1/3 bên phải, hậu cảnh là bảng bài giảng xóa phông",
          "director_note": "Ánh sáng tự nhiên làm nổi bật sống mũi và khóe mắt đăm chiêu suy ngẫm."
        },
        {
          "beat_id": "4.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "18.0s - 22.0s",
          "image": f"{R2_BASE}/assets/frames/scene4_beat2.jpg",
          "shot_type": "Cận cảnh ánh mắt thấu suốt (Eye Level Insight Close-Up)",
          "angle": "Góc trực diện 3/4 (3/4 Profile)",
          "camera_motion": "Push-in chậm nhấn mạnh quyết tâm (Slow Push-In)",
          "composition": "Đôi mắt nằm ở đường 1/3 trên, ánh sáng rực lên thể hiện sự sáng tỏ",
          "director_note": "Ánh mắt chuyển từ hoang mang sang kiên định, đầu gật nhẹ thấm thía bài học."
        },
        {
          "beat_id": "4.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "22.0s - 25.0s",
          "image": f"{R2_BASE}/assets/frames/scene4_beat3.jpg",
          "shot_type": "Trung cảnh chuẩn bị quay (Medium Setup Shot)",
          "angle": "Góc ngang tầm mắt (Eye Level)",
          "camera_motion": "Cầm máy giơ lên trước mặt (Raising Camera Gesture)",
          "composition": "Nhân vật cầm điện thoại giơ cao ngang tầm mắt, màn hình selfie hiển thị chính mình",
          "director_note": "Động tác dứt khoát cầm điện thoại lên quay chính mình, nối thẳng sang Cảnh 5 Talking Head."
        }
      ]
    },
    {
      "scene_id": 5,
      "time_range": "25 - 30s",
      "duration": "5s",
      "title": "Trực Diện Camera - Tuyên Bố Hành Động & Kêu Gọi",
      "main_shot_type": "Trực diện (Frontal Talking Head / Eye-Level CTA)",
      "voiceover": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi.",
      "audio_rhythm": "Giọng nói đanh thép, đầy nội lực, truyền cảm hứng hành động ngay lập tức.",
      "director_core_intent": "Kêu gọi hành động (CTA) dứt khoát: Đập tan tư duy phụ thuộc vào ads, kích hoạt năng lực tự xuất hiện làm video trao giá trị.",
      "beats": [
        {
          "beat_id": "5.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "25.0s - 27.0s",
          "image": f"{R2_BASE}/assets/frames/scene5_beat1.jpg",
          "shot_type": "Cận trực diện (Frontal Close-Up Talking Head)",
          "angle": "Trực diện ngang tầm mắt (Eye-Level Direct Frontal)",
          "camera_motion": "Handheld vững chắc (Steady Handheld)",
          "composition": "Gương mặt nằm chính giữa trung tâm khung hình (Center Framing), ánh mắt khóa thẳng vào ống kính",
          "director_note": "Tạo kết nối thị giác 1-to-1 trực tiếp với người xem ngay từ mili-giây đầu tiên của câu thoại."
        },
        {
          "beat_id": "5.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "27.0s - 29.0s",
          "image": f"{R2_BASE}/assets/frames/scene5_beat2.jpg",
          "shot_type": "Cận cảnh truyền lửa (Passionate Conviction Close-Up)",
          "angle": "Trực diện hơi hất nhẹ 5° (Empowering Frontal)",
          "camera_motion": "Punch-in nhẹ 10% (Subtle J-Cut Punch-In)",
          "composition": "Khuôn mặt đầy năng lượng, tay giơ nhẹ nhấn mạnh nhịp nói",
          "director_note": "Khẩu khí mạnh mẽ: 'Phải tự học cách xuất hiện trước khách hàng thôi!'. Điểm chạm cao trào của toàn bộ video."
        },
        {
          "beat_id": "5.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Kết thúc (Outro CTA / Hold)",
          "timestamp": "29.0s - 30.0s",
          "image": f"{R2_BASE}/assets/frames/scene5_beat3.jpg",
          "shot_type": "Trung cận kết thúc (Medium Close-Up Outro Frame)",
          "angle": "Ngang tầm mắt (Eye Level)",
          "camera_motion": "Tĩnh giữ frame (Static Hold)",
          "composition": "Nhân vật mỉm cười gật đầu, 1/3 phía dưới để trống cho Subtitle / Brand Tag / Hotline",
          "director_note": "Nụ cười chân thành, ánh nhìn tin cậy. Dừng hình 0.5s cho Brand Tag và Call-to-Action xuất hiện."
        }
      ]
    }
  ]
}

# Save json
with open('/Users/vietmac/Documents/CODE/Bang-Phan-Canh/storyboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

html_code = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['project_title']} | Bảng Phân Cảnh AI</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #0a0e17;
      --bg-surface: #111827;
      --bg-card: #172033;
      --bg-card-hover: #1e2b45;
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
      --emerald-glow: rgba(16, 185, 129, 0.15);
      --rose: #f43f5e;
      --purple: #a855f7;
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
      -webkit-font-smoothing: antialiased;
    }}

    /* Top Sticky Header */
    .top-header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(10, 14, 23, 0.92);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-badge {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 5px 12px;
      border-radius: 6px;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      box-shadow: 0 0 12px rgba(37, 99, 235, 0.4);
    }}

    .header-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .header-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .nav-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }}

    .nav-btn:hover {{
      background: var(--cyan);
      color: #000;
      border-color: var(--cyan);
    }}

    .action-btn {{
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #000;
      font-weight: 700;
      border: none;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 12px;
      transition: all 0.2s ease;
    }}

    .action-btn:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4);
    }}

    /* Main Container */
    .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 24px 20px;
    }}

    /* Original Input Message Block */
    .original-message-box {{
      background: linear-gradient(180deg, #131d2e 0%, #0d1522 100%);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: var(--radius-lg);
      padding: 24px 28px;
      margin-bottom: 28px;
      position: relative;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
    }}

    .orig-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}

    .orig-title-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .orig-title {{
      font-size: 16px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .orig-badge {{
      background: rgba(56, 189, 248, 0.15);
      color: var(--cyan);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    .orig-meta {{
      font-size: 11px;
      color: var(--text-muted);
      display: flex;
      gap: 14px;
    }}

    .orig-content-grid {{
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 20px;
    }}

    @media (max-width: 900px) {{
      .orig-content-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .raw-text-panel {{
      background: #080c14;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #e2e8f0;
      white-space: pre-wrap;
      line-height: 1.6;
      max-height: 320px;
      overflow-y: auto;
    }}

    .raw-text-panel::-webkit-scrollbar {{
      width: 6px;
    }}
    .raw-text-panel::-webkit-scrollbar-thumb {{
      background: var(--text-muted);
      border-radius: 3px;
    }}

    .ref-gallery {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }}

    .ref-item {{
      background: #080c14;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      cursor: pointer;
      transition: transform 0.2s ease;
    }}

    .ref-item:hover {{
      transform: scale(1.02);
      border-color: var(--cyan);
    }}

    .ref-thumb-box {{
      position: relative;
      height: 180px;
      background: #000;
    }}

    .ref-thumb-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    .ref-label-badge {{
      position: absolute;
      top: 6px;
      left: 6px;
      background: rgba(0, 0, 0, 0.75);
      color: var(--cyan);
      font-size: 9px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      backdrop-filter: blur(4px);
    }}

    .ref-caption {{
      padding: 8px 10px;
      font-size: 11px;
    }}

    .ref-caption strong {{
      color: #fff;
      display: block;
      margin-bottom: 2px;
    }}

    .ref-caption span {{
      color: var(--text-muted);
      font-size: 10px;
    }}

    /* Hero Overview */
    .hero {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 24px 28px;
      margin-bottom: 28px;
    }}

    .hero-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }}

    .tag {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}

    .tag-cyan {{ background: var(--cyan-glow); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .tag-amber {{ background: var(--amber-glow); color: var(--amber); border: 1px solid rgba(245, 158, 11, 0.3); }}
    .tag-emerald {{ background: var(--emerald-glow); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3); }}

    .hero h1 {{
      font-size: 22px;
      font-weight: 800;
      margin-bottom: 8px;
      color: #fff;
    }}

    .hero-desc {{
      color: var(--text-secondary);
      font-size: 13px;
      margin-bottom: 18px;
    }}

    .metrics-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 10px;
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px 16px;
    }}

    .metric-item {{
      display: flex;
      flex-direction: column;
    }}

    .metric-label {{
      font-size: 10px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-bottom: 2px;
    }}

    .metric-value {{
      font-size: 16px;
      font-weight: 800;
      color: var(--text-primary);
    }}

    /* Scene Block */
    .scene-block {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 24px 20px;
      margin-bottom: 30px;
      scroll-margin-top: 70px;
    }}

    .scene-header {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 16px;
    }}

    .scene-title-group {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .scene-num-badge {{
      background: linear-gradient(135deg, #38bdf8, #2563eb);
      color: #000;
      font-size: 12px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
    }}

    .scene-main-title {{
      font-size: 18px;
      font-weight: 800;
      color: #fff;
    }}

    .scene-time-badge {{
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-secondary);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
    }}

    .scene-intent-box {{
      background: rgba(0, 0, 0, 0.25);
      border-left: 3px solid var(--cyan);
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      font-size: 12px;
      color: var(--text-secondary);
      margin-bottom: 16px;
    }}

    .scene-intent-box strong {{
      color: var(--cyan);
    }}

    .audio-box {{
      background: linear-gradient(90deg, rgba(56, 189, 248, 0.08) 0%, rgba(24, 34, 52, 0.4) 100%);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .voice-content {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex: 1;
    }}

    .voice-icon {{
      font-size: 18px;
      background: var(--cyan-glow);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .voice-text {{
      font-size: 13.5px;
      font-weight: 600;
      color: #fff;
      font-style: italic;
    }}

    /* Beats Grid */
    .beats-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }}

    @media (max-width: 960px) {{
      .beats-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .beat-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.25s ease;
    }}

    .beat-card:hover {{
      border-color: var(--border-accent);
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    }}

    .beat-img-container {{
      position: relative;
      width: 100%;
      aspect-ratio: 9 / 16;
      background: #000;
      overflow: hidden;
      cursor: pointer;
    }}

    .beat-img-container img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }}

    .beat-card:hover .beat-img-container img {{
      transform: scale(1.03);
    }}

    .beat-badge-top {{
      position: absolute;
      top: 8px;
      left: 8px;
      z-index: 2;
      font-size: 9.5px;
      font-weight: 800;
      padding: 3px 7px;
      border-radius: 4px;
      text-transform: uppercase;
      backdrop-filter: blur(8px);
    }}

    .badge-in {{ background: rgba(16, 185, 129, 0.9); color: #fff; }}
    .badge-main {{ background: rgba(245, 158, 11, 0.9); color: #000; }}
    .badge-out {{ background: rgba(56, 189, 248, 0.9); color: #000; }}

    .beat-time-tag {{
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.75);
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 9.5px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .beat-content {{
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      flex: 1;
    }}

    .beat-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .beat-id-title {{
      font-size: 13px;
      font-weight: 800;
      color: var(--text-primary);
    }}

    .specs-table {{
      width: 100%;
      font-size: 11px;
      border-collapse: collapse;
      background: rgba(0, 0, 0, 0.2);
      border-radius: 6px;
      overflow: hidden;
    }}

    .specs-table tr {{
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    }}

    .specs-table tr:last-child {{
      border-bottom: none;
    }}

    .specs-table td {{
      padding: 5px 8px;
    }}

    .specs-table td.spec-name {{
      color: var(--text-muted);
      font-weight: 600;
      width: 38%;
    }}

    .specs-table td.spec-val {{
      color: var(--text-primary);
      font-weight: 500;
    }}

    .director-note-box {{
      background: rgba(245, 158, 11, 0.06);
      border: 1px dashed rgba(245, 158, 11, 0.3);
      padding: 8px 10px;
      border-radius: 6px;
      font-size: 11px;
      color: #fde68a;
      line-height: 1.4;
      margin-top: auto;
    }}

    .director-note-box strong {{
      color: var(--amber);
    }}

    /* Timeline Scrubber */
    .timeline-wrapper {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 22px 20px;
      margin-bottom: 28px;
    }}

    .filmstrip {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 12px;
    }}

    .strip-frame {{
      flex: 0 0 130px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .strip-frame:hover {{
      transform: translateY(-2px);
      border-color: var(--cyan);
    }}

    .strip-frame-img {{
      width: 100%;
      aspect-ratio: 9 / 16;
      object-fit: cover;
      display: block;
    }}

    .strip-meta {{
      padding: 5px 6px;
      font-size: 9.5px;
      text-align: center;
    }}

    .strip-title {{ font-weight: 700; color: #fff; }}
    .strip-ts {{ color: var(--cyan); font-family: 'JetBrains Mono', monospace; }}

    /* Lightbox Modal */
    .lightbox {{
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.94);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .lightbox.active {{ display: flex; }}

    .lightbox-content {{
      max-width: 800px;
      max-height: 90vh;
      display: flex;
      gap: 20px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
    }}

    @media (max-width: 700px) {{
      .lightbox-content {{ flex-direction: column; overflow-y: auto; }}
    }}

    .lightbox-img-box {{
      flex: 0 0 340px;
      background: #000;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .lightbox-img-box img {{
      max-width: 100%;
      max-height: 80vh;
      object-fit: contain;
    }}

    .lightbox-details {{
      padding: 24px;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 12px;
      overflow-y: auto;
    }}

    .lightbox-close {{
      position: absolute;
      top: 20px; right: 24px;
      color: #fff; font-size: 32px; font-weight: 700;
      cursor: pointer; background: transparent; border: none;
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Header -->
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">Bảng Phân Cảnh AI</span>
      <div class="header-title">🎬 Kịch Bản 30s • 5 Cảnh & 15 Nhịp Đạo Diễn</div>
    </div>
    <div class="header-controls">
      <a href="#orig-msg" class="nav-btn">📩 Tin Nhắn Gốc</a>
      <a href="#scene-1" class="nav-btn">Cảnh 1</a>
      <a href="#scene-2" class="nav-btn">Cảnh 2</a>
      <a href="#scene-3" class="nav-btn">Cảnh 3</a>
      <a href="#scene-4" class="nav-btn">Cảnh 4</a>
      <a href="#scene-5" class="nav-btn">Cảnh 5</a>
      <a href="#filmstrip-view" class="nav-btn">🎞️ Dải Timeline</a>
      <button class="action-btn" onclick="window.print()">📄 Xuất PDF / In</button>
    </div>
  </header>

  <div class="container">

    <!-- KHỐI TIN NHẮN & YÊU CẦU GỐC ĐẦU VÀO -->
    <section class="original-message-box" id="orig-msg">
      <div class="orig-header">
        <div class="orig-title-group">
          <h2 class="orig-title">📩 Tin Nhắn & Yêu Cầu Gốc Đầu Vào</h2>
          <span class="orig-badge">Input Context</span>
        </div>
        <div class="orig-meta">
          <span>📱 Nguồn: <b>{data['input_context']['source']}</b></span>
          <span>⏱️ Lúc: <b>{data['input_context']['timestamp']}</b></span>
        </div>
      </div>

      <div class="orig-content-grid">
        <div>
          <div style="font-size: 11px; color: var(--cyan); font-weight: 700; margin-bottom: 6px; text-transform: uppercase;">
            💬 Kịch bản gốc & Lời thoại nhận được:
          </div>
          <div class="raw-text-panel">{data['input_context']['raw_text']}</div>
        </div>

        <div>
          <div style="font-size: 11px; color: var(--cyan); font-weight: 700; margin-bottom: 6px; text-transform: uppercase;">
            🖼️ Ảnh bối cảnh gốc đính kèm (Cloudflare R2):
          </div>
          <div class="ref-gallery">
"""

for ref in data['input_context']['ref_images']:
    html_code += f"""
            <div class="ref-item" onclick="openLightbox('{ref['url']}', '{ref['title']}', '{ref['desc']}')">
              <div class="ref-thumb-box">
                <span class="ref-label-badge">📍 Gốc #1</span>
                <img src="{ref['url']}" alt="{ref['title']}" loading="lazy">
              </div>
              <div class="ref-caption">
                <strong>{ref['title']}</strong>
                <span>{ref['desc']}</span>
              </div>
            </div>
"""

html_code += f"""
          </div>
        </div>
      </div>
    </section>

    <!-- Overview Hero Banner -->
    <section class="hero">
      <div class="hero-tags">
        <span class="tag tag-cyan">⚡ 9:16 Vertical Storyboard</span>
        <span class="tag tag-amber">🎯 15 Micro-Beats Đạo Diễn</span>
        <span class="tag tag-emerald">🔄 J-Cut -0.4s Sync</span>
      </div>
      <h1>{data['project_title']}</h1>
      <p class="hero-desc">
        Hệ thống phân cảnh điện ảnh được băm nhỏ thành 15 khung hình chi tiết (Đầu cảnh, Cao trào chi tiết, Mồi chuyển cảnh). 
        Được lưu trữ vĩnh viễn trên Cloudflare R2 CDN và đồng bộ trực tiếp lên GitHub Pages.
      </p>

      <div class="metrics-bar">
        <div class="metric-item">
          <span class="metric-label">Tổng Thời Lượng</span>
          <span class="metric-value">{data['total_duration_sec']} Giây</span>
        </div>
        <div class="metric-item">
          <span class="metric-label">Số Cảnh Chính</span>
          <span class="metric-value">{data['scenes_count']} Cảnh</span>
        </div>
        <div class="metric-item">
          <span class="metric-label">Số Khung Hình Chi Tiết</span>
          <span class="metric-value">{data['beats_count']} Beats</span>
        </div>
        <div class="metric-item">
          <span class="metric-label">Tỷ Lệ Video</span>
          <span class="metric-value">9:16 (TikTok/Reels)</span>
        </div>
        <div class="metric-item">
          <span class="metric-label">Nhịp Cắt Trung Bình</span>
          <span class="metric-value">1.5s / Beat</span>
        </div>
      </div>
    </section>
"""

# Render 5 Scenes without AI Prompt box
for scene in data['scenes']:
    badge_color = "tag-cyan"
    if scene['scene_id'] == 1: badge_color = "tag-amber"
    elif scene['scene_id'] == 3: badge_color = "tag-cyan"
    elif scene['scene_id'] == 5: badge_color = "tag-emerald"

    html_code += f"""
    <section class="scene-block" id="scene-{scene['scene_id']}">
      <div class="scene-header">
        <div class="scene-title-group">
          <span class="scene-num-badge">CẢNH {scene['scene_id']}</span>
          <h3 class="scene-main-title">{scene['title']}</h3>
          <span class="tag {badge_color}">{scene['main_shot_type']}</span>
        </div>
        <span class="scene-time-badge">⏱️ {scene['time_range']} ({scene['duration']})</span>
      </div>

      <div class="scene-intent-box">
        <strong>🎯 Ý Đồ Đạo Diễn:</strong> {scene['director_core_intent']}
      </div>

      <div class="audio-box">
        <div class="voice-content">
          <div class="voice-icon">🎙️</div>
          <div>
            <div style="font-size: 10.5px; color: var(--cyan); font-weight: 700; text-transform: uppercase; margin-bottom: 2px;">Lời Thoại Kịch Bản:</div>
            <div class="voice-text">"{scene['voiceover']}"</div>
          </div>
        </div>
        <div class="voice-meta">
          <span class="tag tag-cyan">J-Cut -0.4s</span>
          <span class="tag tag-amber">Âm Thanh Gốc (No SFX)</span>
        </div>
      </div>

      <!-- 3 Beats Grid -->
      <div class="beats-grid">
"""

    for beat in scene['beats']:
        badge_class = "badge-in"
        if beat['beat_type'] == "main_action": badge_class = "badge-main"
        elif beat['beat_type'] == "out_point": badge_class = "badge-out"

        html_code += f"""
        <div class="beat-card">
          <div class="beat-img-container" onclick="openLightbox('{beat['image']}', '{beat['beat_label']} - Cảnh {scene['scene_id']}', '{beat['director_note']}')">
            <span class="beat-badge-top {badge_class}">{beat['beat_label']}</span>
            <span class="beat-time-tag">{beat['timestamp']}</span>
            <img src="{beat['image']}" alt="{beat['beat_id']}" loading="lazy">
          </div>
          <div class="beat-content">
            <div class="beat-header">
              <span class="beat-id-title">Khung Hình {beat['beat_id']}</span>
              <span class="tag tag-cyan" style="font-size: 10px;">{beat['shot_type']}</span>
            </div>

            <table class="specs-table">
              <tr>
                <td class="spec-name">Góc Máy</td>
                <td class="spec-val">{beat['angle']}</td>
              </tr>
              <tr>
                <td class="spec-name">Động Tác</td>
                <td class="spec-val">{beat['camera_motion']}</td>
              </tr>
              <tr>
                <td class="spec-name">Bố Cục</td>
                <td class="spec-val">{beat['composition']}</td>
              </tr>
            </table>

            <div class="director-note-box">
              <strong>💡 Ghi Chú Đạo Diễn:</strong> {beat['director_note']}
            </div>
          </div>
        </div>
"""

    html_code += """
      </div>
    </section>
"""

# Filmstrip Timeline Section
html_code += f"""
    <!-- Timeline Filmstrip View -->
    <section class="timeline-wrapper" id="filmstrip-view">
      <h2 class="section-title" style="font-size: 18px; font-weight: 800; margin-bottom: 12px; color: #fff;">🎞️ Dải Timeline Phân Cảnh (15 Khung Hình Liên Tiếp • 0s ➔ 30s)</h2>
      <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 14px;">
        Cuộn ngang để kiểm tra nhịp điệu thị giác (Visual Rhythm) và các điểm chuyển cảnh (Match Cuts) giữa các phân cảnh:
      </p>
      <div class="filmstrip">
"""

for scene in data['scenes']:
    for beat in scene['beats']:
        html_code += f"""
        <div class="strip-frame" onclick="openLightbox('{beat['image']}', '{beat['beat_label']} - Cảnh {scene['scene_id']}', '{beat['director_note']}')">
          <img class="strip-frame-img" src="{beat['image']}" alt="{beat['beat_id']}">
          <div class="strip-meta">
            <div class="strip-title">Cảnh {beat['beat_id']}</div>
            <div class="strip-ts">{beat['timestamp']}</div>
          </div>
        </div>
"""

html_code += f"""
      </div>
    </section>
  </div>

  <!-- Lightbox Modal -->
  <div class="lightbox" id="lightboxModal" onclick="closeLightbox(event)">
    <button class="lightbox-close" onclick="closeLightboxDirect()">&times;</button>
    <div class="lightbox-content" onclick="event.stopPropagation()">
      <div class="lightbox-img-box">
        <img id="lightboxImg" src="" alt="Enlarged Frame">
      </div>
      <div class="lightbox-details">
        <span class="tag tag-cyan" id="lightboxTag">Frame Preview</span>
        <h3 id="lightboxTitle" style="font-size: 18px; font-weight: 800; color: #fff;">Title</h3>
        <p id="lightboxDesc" style="font-size: 13px; color: var(--text-secondary); line-height: 1.6;">Description</p>
        <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid var(--border-subtle); font-size: 11px; color: var(--text-muted);">
          Bấm ESC hoặc nhấp ra ngoài để đóng xem ảnh.
        </div>
      </div>
    </div>
  </div>

  <script>
    function openLightbox(imgSrc, title, desc) {{
      document.getElementById('lightboxImg').src = imgSrc;
      document.getElementById('lightboxTitle').innerText = title;
      document.getElementById('lightboxDesc').innerText = desc;
      document.getElementById('lightboxModal').classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox(e) {{
      if (e.target.id === 'lightboxModal') {{
        closeLightboxDirect();
      }}
    }}

    function closeLightboxDirect() {{
      document.getElementById('lightboxModal').classList.remove('active');
      document.body.style.overflow = 'auto';
    }}

    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        closeLightboxDirect();
      }}
    }});
  </script>
</body>
</html>
"""

with open('/Users/vietmac/Documents/CODE/Bang-Phan-Canh/index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Generated clean index.html in Bang-Phan-Canh repo successfully!")
