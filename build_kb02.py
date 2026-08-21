import json
import os
import shutil

R2_BASE = "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach"

raw_input_text = """KỊCH BẢN 02 • CHỦ SHOP & MỞ TIỆM
Tiêu đề: Tiền Mặt Bằng & Cửa Hàng Vắng Khách
Bối cảnh: Phòng học / Bàn làm việc • Chạm vào: Áp lực chi phí mặt bằng & vắng khách

3 TẦNG SỰ THẬT:
• Tầng 1 (Đãi bôi): "Tôi đi học để cập nhật thêm cách tiếp cận khách hàng mới cho cửa hàng."
• Tầng 2 (Cảm giác thật): "Tháng vừa rồi khách vắng hẳn, ngồi ở cửa hàng thấy sốt ruột như lửa đốt."
• Tầng 3 (Ngượng miệng): "Cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ việc văn phòng ra làm chủ tưởng tự do, ai ngờ tự làm thuê cho mình 16h/ngày."

5 PHÂN CẢNH QUAY CHI TIẾT (30 GIÂY):
- Cảnh 1 (00:00 - 00:03, 3s) • [Cận cảnh]: Tay cầm bút gạch mạnh một con số trên sổ bài tập.
  🎙️ Lời thoại: "Sáng Chủ Nhật, tôi ngồi ở lớp này không phải vì rảnh rỗi..."
- Cảnh 2 (00:03 - 00:07, 4s) • [Toàn cảnh]: Quay từ sau lưng, thấy bóng mình ngồi giữa lớp.
  🎙️ Lời thoại: "...Người ngoài nhìn vào tưởng mình chăm chỉ đi học thêm cái mới."
- Cảnh 3 (00:07 - 00:15, 8s) • [Đặc tả]: Màn hình điện thoại mở bảng doanh thu hoặc tin nhắn.
  🎙️ Lời thoại: "Nhưng thật ra tháng vừa rồi cửa hàng vắng khách quá, ngồi ở tiệm mà ruột gan như lửa đốt."
- Cảnh 4 (00:15 - 00:25, 10s) • [Góc nghiêng]: Nhìn ra cửa sổ phòng học đầy suy tư.
  🎙️ Lời thoại: "Sợ nhất là cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ công việc văn phòng ra mở riêng tưởng nhẹ đầu, ai ngờ cày từ sáng đến đêm mà không dám nghỉ ngày nào."
- Cảnh 5 (00:25 - 00:30, 5s) • [Trực diện]: Nhìn thẳng camera nói điềm đạm.
  🎙️ Lời thoại: "Đến lúc này thì cái gì giúp mình duy trì được cửa hàng thì phải bắt tay vào học thôi."

💡 ĐIỂM MẤU CHỐT:
Hình ảnh phòng học thể hiện sự tập trung — Lời thoại mang sức nặng sinh tồn cơm áo gạo tiền."""

data = {
  "project_title": "Bảng Phân Cảnh Storyboard: Tiền Mặt Bằng & Cửa Hàng Vắng Khách (Kịch Bản 02)",
  "project_slug": "tien_mat_bang_va_cua_hang_vang_khach",
  "total_duration_sec": 30,
  "scenes_count": 5,
  "beats_count": 15,
  "aspect_ratio": "9:16 (Vertical TikTok / Reels)",
  "input_context": {
    "source": "9 Kịch Bản Thực Chiến 3 Tầng Sự Thật",
    "url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/9_kich_ban_thuc_chien.html#kb02",
    "timestamp": "21/08/2026 10:10:00",
    "raw_text": raw_input_text,
    "ref_images": [
      {
        "title": "Ảnh Bối Cảnh Lớp Học & Bàn Gỗ",
        "url": f"{R2_BASE}/assets/reference/ref_01_classroom.jpg",
        "desc": "Bàn gỗ tự nhiên, sổ tay ghi chép, bút máy, ánh sáng xiên cửa sổ phòng học."
      },
      {
        "title": "Ảnh Nhân Vật Tham Chiếu (Chủ Tiệm)",
        "url": f"{R2_BASE}/assets/reference/ref_02_character.jpg",
        "desc": "Nam chủ tiệm/chủ shop ngoài 30 tuổi, áo sơ mi tối giản, nét mặt sâu sắc và từng trải."
      }
    ]
  },
  "three_truth_tiers": [
    {
      "tier": 1,
      "title": "Tầng 1: Đãi bôi (Lý do bề nổi)",
      "badge": "Lý do xã giao",
      "content": "Tôi đi học để cập nhật thêm cách tiếp cận khách hàng mới cho cửa hàng."
    },
    {
      "tier": 2,
      "title": "Tầng 2: Cảm giác thật (Nỗi đau nội tâm)",
      "badge": "Cảm giác thật",
      "content": "Tháng vừa rồi khách vắng hẳn, ngồi ở cửa hàng thấy sốt ruột như lửa đốt."
    },
    {
      "tier": 3,
      "title": "Tầng 3: Ngượng miệng (Sự thật trần trụi)",
      "badge": "Sự thật sống còn",
      "content": "Cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ việc văn phòng ra làm chủ tưởng tự do, ai ngờ tự làm thuê cho mình 16h/ngày."
    }
  ],
  "scenes": [
    {
      "scene_id": 1,
      "time_range": "00:00 - 00:03",
      "duration": "3s",
      "title": "Gạch Bút Lên Sổ Bài Tập • Phủ Nhận Sự Rảnh Rỗi",
      "main_shot_type": "Cận cảnh (Close-Up / High-Angle Desk)",
      "voiceover": "Sáng Chủ Nhật, tôi ngồi ở lớp này không phải vì rảnh rỗi...",
      "audio_rhythm": "Tiếng ngòi bút kim loại miết sột soạt trên mặt giấy, giọng nói trầm ấm mở màn dứt khoát.",
      "director_core_intent": "Tạo móc câu (Hook) gây bất ngờ ngay 3 giây đầu: Phá vỡ định kiến đi học vì rảnh rỗi bằng hành động gạch số dứt khoát.",
      "beats": [
        {
          "beat_id": "1.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "0.0s - 1.0s",
          "image": f"{R2_BASE}/assets/frames/scene1_beat1.jpg",
          "shot_type": "Cận cảnh bàn học (Close-Up Desk)",
          "angle": "Góc nghiêng 45° từ trên xuống",
          "camera_motion": "Tĩnh (Static), bắt nét sâu vào ngòi bút máy",
          "composition": "Bàn tay cầm bút ở 1/3 dưới, sổ tay mở rộng, hậu cảnh lớp học mờ ấm",
          "director_note": "Thiết lập bối cảnh lớp học sáng Chủ Nhật, tay đặt bút sẵn sàng viết."
        },
        {
          "beat_id": "1.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "1.0s - 2.2s",
          "image": f"{R2_BASE}/assets/frames/scene1_beat2.jpg",
          "shot_type": "Đặc tả cực cận (Extreme Close-Up)",
          "angle": "Góc nhìn từ trên xuống 60° (Top-Down Focus)",
          "camera_motion": "Push-in chậm dồn vào ngòi bút",
          "composition": "Ngòi bút gạch một đường dứt khoát đè lên con số trên trang sổ",
          "director_note": "Cú gạch bút mạnh mẽ khớp với từ 'không phải vì rảnh rỗi', tạo lực nhấn thị giác."
        },
        {
          "beat_id": "1.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "2.2s - 3.0s",
          "image": f"{R2_BASE}/assets/frames/scene1_beat3.jpg",
          "shot_type": "Cận cảnh ngắt nhịp (Close-Up Lift)",
          "angle": "Góc ngang mặt bàn (Eye-Level Desk)",
          "camera_motion": "Tilt-up nhẹ + Tay giữ chắc thân bút",
          "composition": "Ngòi bút nhấc lên khỏi mặt giấy, ánh sáng xiên rọi rõ vân gỗ",
          "director_note": "Động tác dừng bút làm nhịp ngắt mượt mà để cắt sang toàn cảnh Cảnh 2."
        }
      ]
    },
    {
      "scene_id": 2,
      "time_range": "00:03 - 00:07",
      "duration": "4s",
      "title": "Bóng Mình Giữa Lớp Học • Vỏ Bọc Chăm Chỉ",
      "main_shot_type": "Toàn cảnh qua vai (Wide Over-The-Shoulder)",
      "voiceover": "...Người ngoài nhìn vào tưởng mình chăm chỉ đi học thêm cái mới.",
      "audio_rhythm": "Giọng kể chậm rãi, có chút tự trào; âm thanh môi trường lớp học nền nhẹ nhàng.",
      "director_core_intent": "Vạch ra sự tương phản giữa góc nhìn của người ngoài ('chăm chỉ cập nhật kiến thức') và sự ngột ngạt nội tâm.",
      "beats": [
        {
          "beat_id": "2.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "3.0s - 4.5s",
          "image": f"{R2_BASE}/assets/frames/scene2_beat1.jpg",
          "shot_type": "Toàn cảnh sau lưng (Wide Over-Shoulder)",
          "angle": "Góc cao sau lưng bao quát lớp học",
          "camera_motion": "Trôi nhẹ ngang (Subtle lateral drift)",
          "composition": "Nhân vật áo xanh navy ngồi trung tâm, các học viên xung quanh đang chăm chú nghe giảng",
          "director_note": "Bức tranh toàn cảnh một buổi học nghiêm túc, tạo vẻ ngoài chuẩn mực của một chủ shop chăm chỉ."
        },
        {
          "beat_id": "2.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "4.5s - 6.0s",
          "image": f"{R2_BASE}/assets/frames/scene2_beat2.jpg",
          "shot_type": "Trung cận qua vai (Over-the-Shoulder Medium)",
          "angle": "Góc qua vai trái 30°",
          "camera_motion": "Cầm tay nhịp thở nhẹ (Handheld breathing)",
          "composition": "Bờ vai trái chiếm 1/3 góc nhìn, tay vừa cầm sổ bài tập vừa kín đáo cầm smartphone",
          "director_note": "Hành vi cầm điện thoại hé lộ sự phân tâm và lo âu ngấm ngầm giữa không khí lớp học."
        },
        {
          "beat_id": "2.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "6.0s - 7.0s",
          "image": f"{R2_BASE}/assets/frames/scene2_beat3.jpg",
          "shot_type": "Cận cảnh tay & điện thoại (Tight Desk Shot)",
          "angle": "Góc hếch nhẹ từ dưới lên (Low-Angle Desk Level)",
          "camera_motion": "Push-in dồn vào màn hình điện thoại",
          "composition": "Bàn tay nhấc điện thoại lên khỏi mặt bàn cạnh cuốn sổ ghi chép",
          "director_note": "Động tác cầm điện thoại lên làm mồi nối thẳng sang giao diện màn hình Cảnh 3."
        }
      ]
    },
    {
      "scene_id": 3,
      "time_range": "00:07 - 00:15",
      "duration": "8s",
      "title": "Màn Hình Doanh Thu Lao Dốc • Ruột Gan Như Lửa Đốt",
      "main_shot_type": "Đặc tả POV (Screen POV & Tension Close-Up)",
      "voiceover": "Nhưng thật ra tháng vừa rồi cửa hàng vắng khách quá, ngồi ở tiệm mà ruột gan như lửa đốt.",
      "audio_rhythm": "Giọng hạ tông trầm, đầy sức nặng và áp lực cơm áo gạo tiền đè nặng.",
      "director_core_intent": "Bóc trần Tầng 2 Sự Thật: Doanh thu cửa hàng lao dốc, nỗi sợ vắng khách và cảm giác bất an ăn mòn tâm trí.",
      "beats": [
        {
          "beat_id": "3.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "7.0s - 9.5s",
          "image": f"{R2_BASE}/assets/frames/scene3_beat1.jpg",
          "shot_type": "Cận cảnh màn hình POV (Direct UI Close-Up)",
          "angle": "Trực diện 90° vào màn hình điện thoại",
          "camera_motion": "Push-in từ từ (Slow Creep-In)",
          "composition": "Bảng Sales Dashboard với biểu đồ đỏ cắm dốc (-94%), New Customers: 0",
          "director_note": "Bằng chứng số liệu trực quan gây sốc: Cửa hàng hoàn toàn vắng bóng khách mới."
        },
        {
          "beat_id": "3.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "9.5s - 12.5s",
          "image": f"{R2_BASE}/assets/frames/scene3_beat2.jpg",
          "shot_type": "Đặc tả cực cận UI & Ngón tay (Extreme Close-Up UI)",
          "angle": "Góc nghiêng 45° vào màn hình",
          "camera_motion": "Máy tĩnh bắt trọn từng con số đỏ rực (-45% Revenue, No new orders)",
          "composition": "Ngón tay cái lướt chậm trong bất lực trên dòng thông báo rỗng",
          "director_note": "Khắc họa cảm giác 'ruột gan như lửa đốt' khi nhìn vào doanh thu thực tế."
        },
        {
          "beat_id": "3.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "12.5s - 15.0s",
          "image": f"{R2_BASE}/assets/frames/scene3_beat3.jpg",
          "shot_type": "Trung cận căng thẳng (Medium Close-Up Tension)",
          "angle": "Góc trực diện ngang tầm mắt (Eye Level)",
          "camera_motion": "Máy tĩnh giữ khung hình ngột ngạt",
          "composition": "Bàn tay siết chặt thành nắm đấm trên mặt bàn gỗ, tay kia úp điện thoại, nét mặt nhíu chặt",
          "director_note": "Nắm đấm siết chặt thể hiện sự dồn nén cảm xúc, chuẩn bị hướng mắt ra cửa sổ Cảnh 4."
        }
      ]
    },
    {
      "scene_id": 4,
      "time_range": "00:15 - 00:25",
      "duration": "10s",
      "title": "Nhìn Ra Cửa Sổ Phòng Học • Áp Lực Tiền Mặt Bằng 20 Triệu",
      "main_shot_type": "Góc nghiêng (Side Profile / Window Insight)",
      "voiceover": "Sợ nhất là cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ công việc văn phòng ra mở riêng tưởng nhẹ đầu, ai ngờ cày từ sáng đến đêm mà không dám nghỉ ngày nào.",
      "audio_rhythm": "Khoảng lặng cảm xúc sâu nhất video; giọng kể chân thật, trần trụi từng từ 'tiền mặt bằng 20 triệu'.",
      "director_core_intent": "Chạm sâu vào Tầng 3 Sự Thật: Áp lực tiền thuê mặt bằng cố định hàng tháng và nghịch lý khởi nghiệp làm chủ nhưng lại làm thuê 16h/ngày cho chính mình.",
      "beats": [
        {
          "beat_id": "4.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "15.0s - 18.0s",
          "image": f"{R2_BASE}/assets/frames/scene4_beat1.jpg",
          "shot_type": "Cận góc nghiêng cửa sổ (Side Profile Close-Up)",
          "angle": "Góc nghiêng 90° đón ánh nắng cửa sổ kính",
          "camera_motion": "Arc shot xoay nhẹ góc nhìn",
          "composition": "Nhân vật ngồi tựa cằm nhìn ra cửa sổ lớn, vệt nắng xiên làm nổi bật đường nét suy tư",
          "director_note": "Khung cảnh lắng đọng, người xem cảm nhận trọn vẹn gánh nặng chi phí cố định 20 triệu/tháng."
        },
        {
          "beat_id": "4.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "18.0s - 22.0s",
          "image": f"{R2_BASE}/assets/frames/scene4_beat2.jpg",
          "shot_type": "Đặc tả cận ánh mắt (Insight Eye Close-Up)",
          "angle": "Cận cảnh 3/4 trực diện (Tight 3/4 Face)",
          "camera_motion": "Push-in chậm vào đôi mắt trĩu nặng âu lo",
          "composition": "Đôi mắt và vầng trán nhăn lại, ánh nhìn xa xăm chứa đựng sự mệt mỏi sau chuỗi ngày cày cuốc không nghỉ",
          "director_note": "Sức nặng cảm xúc đạt đỉnh: Bỏ việc văn phòng tưởng tự do nhưng thực tế bị giam cầm trong áp lực sinh tồn."
        },
        {
          "beat_id": "4.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
          "timestamp": "22.0s - 25.0s",
          "image": f"{R2_BASE}/assets/frames/scene4_beat3.jpg",
          "shot_type": "Trung cảnh quay người (Medium Turnaround)",
          "angle": "Góc ngang tầm mắt 3/4",
          "camera_motion": "Pan theo động tác quay đầu dứt khoát",
          "composition": "Nhân vật quay đầu lại từ khung cửa sổ, ngồi thẳng lưng nhìn về phía bảng giảng bài",
          "director_note": "Chuyển biến tâm lý: Từ trầm tư bế tắc sang quyết định hành động dứt khoát, mồi cho Cảnh 5."
        }
      ]
    },
    {
      "scene_id": 5,
      "time_range": "00:25 - 00:30",
      "duration": "5s",
      "title": "Trực Diện Camera Điềm Đạm • Bắt Tay Vào Học Để Sống Còn",
      "main_shot_type": "Trực diện (Frontal Talking Head / Eye-Level Resolution)",
      "voiceover": "Đến lúc này thì cái gì giúp mình duy trì được cửa hàng thì phải bắt tay vào học thôi.",
      "audio_rhythm": "Giọng nói điềm đạm, chắc nịch, không hô hào sáo rỗng mà thể hiện sự kiên định thực tế.",
      "director_core_intent": "Kết bài mạnh mẽ, thực tế: Học không phải vì mốt hay phong trào, mà học là vũ khí duy nhất để cứu sống và phát triển cửa hàng.",
      "beats": [
        {
          "beat_id": "5.1",
          "beat_type": "in_point",
          "beat_label": "🔰 Đầu cảnh (In-point)",
          "timestamp": "25.0s - 27.0s",
          "image": f"{R2_BASE}/assets/frames/scene5_beat1.jpg",
          "shot_type": "Trung cận trực diện (Frontal Medium Close-Up)",
          "angle": "Trực diện ngang tầm mắt (Eye-Level Center Framing)",
          "camera_motion": "Handheld vững chắc (Steady Handheld)",
          "composition": "Gương mặt nằm chính giữa trung tâm khung hình, ánh mắt chân thành khóa thẳng ống kính",
          "director_note": "Tạo kết nối thị giác 1-to-1 chân thành, phong thái người làm chủ điềm tĩnh sau khi đã thấu suốt."
        },
        {
          "beat_id": "5.2",
          "beat_type": "main_action",
          "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
          "timestamp": "27.0s - 29.0s",
          "image": f"{R2_BASE}/assets/frames/scene5_beat2.jpg",
          "shot_type": "Cận trực diện truyền cảm hứng (Passionate Conviction Close-Up)",
          "angle": "Trực diện hất nhẹ 5° (Direct Frontal)",
          "camera_motion": "Punch-in nhẹ 10% theo nhịp câu nói",
          "composition": "Cận cảnh biểu cảm kiên định, lời nói phát ra dứt khoát và tràn đầy năng lượng thực chiến",
          "director_note": "Câu chốt mang tính thức tỉnh: 'Cái gì giúp mình duy trì được cửa hàng thì phải bắt tay vào học thôi!'."
        },
        {
          "beat_id": "5.3",
          "beat_type": "out_point",
          "beat_label": "🔄 Cuối cảnh / Kết thúc (Outro CTA / Hold)",
          "timestamp": "29.0s - 30.0s",
          "image": f"{R2_BASE}/assets/frames/scene5_beat3.jpg",
          "shot_type": "Trung cận kết thúc (Medium Close-Up Outro Frame)",
          "angle": "Ngang tầm mắt (Eye Level)",
          "camera_motion": "Tĩnh giữ khung hình (Static Hold 0.5s)",
          "composition": "Nhân vật mỉm cười nhẹ tự tin, khoảng trống 1/3 bên dưới dành cho Brand Tag / CTA",
          "director_note": "Nụ cười chân thực gieo niềm tin trọn vẹn. Dừng hình 0.5s để người xem tiếp nhận thông điệp."
        }
      ]
    }
  ]
}

# Save JSON data
with open('/Users/vietmac/Documents/CODE/Bang-Phan-Canh/storyboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

html_code = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['project_title']} | AI Storyboard Studio</title>
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

    /* 3 Tiers Box */
    .tiers-box {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-top: 18px;
    }}

    @media (max-width: 900px) {{
      .tiers-box {{
        grid-template-columns: 1fr;
      }}
    }}

    .tier-card {{
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      border-left: 3px solid var(--cyan);
    }}

    .tier-card.t1 {{ border-left-color: var(--rose); }}
    .tier-card.t2 {{ border-left-color: var(--amber); }}
    .tier-card.t3 {{ border-left-color: var(--emerald); }}

    .tier-badge-label {{
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
      display: block;
    }}
    .tier-card.t1 .tier-badge-label {{ color: var(--rose); }}
    .tier-card.t2 .tier-badge-label {{ color: var(--amber); }}
    .tier-card.t3 .tier-badge-label {{ color: var(--emerald); }}

    .tier-text {{
      font-size: 12px;
      color: var(--text-secondary);
      line-height: 1.5;
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
    .tag-rose {{ background: rgba(244, 63, 94, 0.15); color: var(--rose); border: 1px solid rgba(244, 63, 94, 0.3); }}

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
      <div class="header-title">🎬 Kịch Bản 02 • Tiền Mặt Bằng & Cửa Hàng Vắng Khách</div>
    </div>
    <div class="header-controls">
      <a href="#orig-msg" class="nav-btn">📩 Kịch Bản Gốc</a>
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
          <h2 class="orig-title">📩 Kịch Bản Gốc & Bối Cảnh Thực Chiến</h2>
          <span class="orig-badge">Kịch Bản Số 02</span>
        </div>
        <div class="orig-meta">
          <span>📱 Nguồn: <b>9 Kịch Bản Thực Chiến 3 Tầng Sự Thật</b></span>
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
            🖼️ Bối cảnh tham chiếu (Cloudflare R2):
          </div>
          <div class="ref-gallery">
"""

for ref in data['input_context']['ref_images']:
    html_code += f"""
            <div class="ref-item" onclick="openLightbox('{ref['url']}', '{ref['title']}', '{ref['desc']}')">
              <div class="ref-thumb-box">
                <span class="ref-label-badge">📍 Tham Chiếu</span>
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

      <!-- 3 Tầng Sự Thật -->
      <div class="tiers-box">
"""

for t in data['three_truth_tiers']:
    t_class = f"t{t['tier']}"
    html_code += f"""
        <div class="tier-card {t_class}">
          <span class="tier-badge-label">{t['badge']}</span>
          <strong style="color: #fff; font-size: 12.5px; display: block; margin-bottom: 4px;">{t['title']}</strong>
          <p class="tier-text">"{t['content']}"</p>
        </div>
"""

html_code += f"""
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
        Bảng phân cảnh điện ảnh 9:16 chuyên sâu bóc tách từ Kịch Bản 02. Mỗi cảnh được băm nhỏ thành 3 nhịp thị giác (Đầu cảnh, Cao trào chi tiết, Mồi chuyển cảnh). 
        Toàn bộ khung hình được lưu trữ trên Cloudflare R2 CDN và đồng bộ trực tuyến lên GitHub Pages.
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
          <span class="metric-value">1.5s - 2.0s / Beat</span>
        </div>
      </div>
    </section>
"""

# Render 5 Scenes
for scene in data['scenes']:
    badge_color = "tag-cyan"
    if scene['scene_id'] == 1: badge_color = "tag-amber"
    elif scene['scene_id'] == 3: badge_color = "tag-rose"
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
        Cuộn ngang để kiểm tra nhịp điệu thị giác (Visual Rhythm) và các điểm chuyển cảnh (Match Cuts) giữa 5 phân cảnh:
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
