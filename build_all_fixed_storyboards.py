import os
import json

TEMPLATE_FILE = "/Users/vietmac/Documents/CODE/Bang-Phan-Canh/kich_ban_03_chung_lai_sau_tuoi_30.html"

# -------------------------------------------------------------
# 1. DATA FOR KB01: TỪ ĐỐT TIỀN QUẢNG CÁO ĐẾN TỰ TIN XUẤT HIỆN
# -------------------------------------------------------------
kb01_data = {
    "project_title": "Bảng Phân Cảnh Storyboard: Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện (Kịch Bản 01)",
    "project_slug": "tu_dot_tien_den_tu_tin_xuat_hien",
    "total_duration_sec": 30,
    "scenes_count": 5,
    "beats_count": 15,
    "aspect_ratio": "9:16 (TikTok / Reels)",
    "input_context": {
        "source": "Kịch Bản Thực Chiến 01 • Kinh Doanh & Quảng Cáo Online",
        "url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/9_kich_ban_thuc_chien.html#kb01",
        "timestamp": "21/08/2026 11:15:00",
        "raw_text": """KỊCH BẢN 01 • CHỦ SHOP & BÁN HÀNG ONLINE
Tiêu đề: Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện
Bối cảnh: Bàn làm việc / Góc lớp học • Chạm vào: Áp lực chi phí quảng cáo tăng cao & bế tắc đơn hàng

3 TẦNG SỰ THẬT:
• Tầng 1 (Đãi bôi): "Tôi đi học để cập nhật thêm các phương pháp tiếp cận khách hàng mới."
• Tầng 2 (Cảm giác thật): "Mấy tháng nay tiền quảng cáo tăng gấp đôi, tiền nạp ăn gần hết tiền lãi mà không dám tắt ads."
• Tầng 3 (Ngượng miệng): "Càng đốt tiền càng thấy mình như đang đánh bạc. Nếu không tự biết cách làm video để xây niềm tin thật, thì sớm muộn cũng phá sản."

5 PHÂN CẢNH QUAY CHI TIẾT (30 GIÂY):
- Cảnh 1 (00:00 - 00:03, 3s) • [Đặc tả]: Ngón tay bấm sáng màn hình điện thoại rồi lại tắt đi trên mặt bàn học.
  🎙️ Lời thoại: "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần..."
- Cảnh 2 (00:03 - 00:07, 4s) • [Trung cảnh]: Ngồi ở góc bàn lớp học, cầm điện thoại lướt xem số liệu.
  🎙️ Lời thoại: "...Người ngoài nhìn vào tưởng mình bận rộn chốt đơn trả lời khách."
- Cảnh 3 (00:07 - 00:15, 8s) • [Cận cảnh]: Màn hình điện thoại hiển thị chi phí ads tăng vọt.
  🎙️ Lời thoại: "Nhưng thật ra là đang sốt ruột. Mấy tháng nay tiền quảng cáo tăng gấp đôi, tiền nạp vào ăn gần hết tiền lãi."
- Cảnh 4 (00:15 - 00:25, 10s) • [Góc nghiêng]: Quay góc nghiêng mặt mình nhìn lên bảng giảng bài đăm chiêu.
  🎙️ Lời thoại: "Trước đây cứ nghĩ chỉ cần nạp tiền chạy ads là xong việc. Giờ mới thấm: nếu không tự biết cách làm video để người ta tin, thì có bao nhiêu tiền vốn cũng không bù nổi chi phí."
- Cảnh 5 (00:25 - 00:30, 5s) • [Trực diện]: Cầm máy ngang tầm mắt, nói dứt khoát vào camera.
  🎙️ Lời thoại: "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi."

💡 ĐIỂM MẤU CHỐT:
Chuyển hóa từ trạng thái bất an phụ thuộc vào tiền quảng cáo sang hành động chủ động tự xuất hiện trước khách hàng.""",
        "ref_images": [
            {
                "title": "Ảnh Bối Cảnh Bàn Học & Góc Làm Việc",
                "url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/reference/ref_01_classroom.jpg",
                "desc": "Bàn gỗ tối màu, sổ tay, bút máy, màn hình điện thoại hiển thị số liệu."
            },
            {
                "title": "Ảnh Nhân Vật Mặc Định (Anh Việt)",
                "url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/reference/ref_02_character.jpg",
                "desc": "Anh Việt - Diễn giả/Chủ doanh nghiệp 30s, áo sơ mi/áo thun tối giản, thần thái tự tin, điềm đạm."
            }
        ]
    },
    "three_truth_tiers": [
        {
            "tier": 1,
            "title": "Tầng 1: Đãi bôi (Lý do bề nổi)",
            "badge": "Lý do xã giao",
            "content": "Tôi đi học để cập nhật thêm các phương pháp tiếp cận khách hàng mới."
        },
        {
            "tier": 2,
            "title": "Tầng 2: Cảm giác thật (Nỗi đau âm ỉ)",
            "badge": "Cảm giác thật",
            "content": "Mấy tháng nay tiền quảng cáo tăng gấp đôi, tiền nạp ăn gần hết tiền lãi mà không dám tắt ads."
        },
        {
            "tier": 3,
            "title": "Tầng 3: Ngượng miệng (Sự thật trần trụi)",
            "badge": "Nỗi sợ sâu kín",
            "content": "Càng đốt tiền càng thấy mình như đang đánh bạc. Nếu không tự biết cách làm video để xây niềm tin thật, thì sớm muộn cũng phá sản."
        }
    ],
    "scenes": [
        {
            "scene_id": 1,
            "time_range": "00:00 - 00:03s",
            "duration": "3s",
            "title": "Bật / Tắt Màn Hình Điện Thoại",
            "main_shot_type": "Đặc tả",
            "director_core_intent": "Thiết lập trạng thái tâm lý bồn chồn, thói quen vô thức kiểm tra điện thoại.",
            "voiceover": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
            "beats": [
                {
                    "beat_id": "1.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "0.0s - 1.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
                    "shot_type": "Cận cảnh (Close-Up)",
                    "angle": "Góc nghiêng 45° từ trên xuống",
                    "camera_motion": "Máy tĩnh bắt nét ngón tay chạm màn hình",
                    "composition": "Quy tắc 1/3, điện thoại nằm cạnh sổ tay",
                    "director_note": "Mở đầu phân cảnh 1: Bắt trọn khoảnh khắc ngón tay vừa bấm sáng màn hình điện thoại."
                },
                {
                    "beat_id": "1.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "1.0s - 2.2s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat2.jpg",
                    "shot_type": "Đặc tả cực cận (Extreme Close-Up)",
                    "angle": "Trực diện 60°",
                    "camera_motion": "Push-in chậm dồn sự chú ý",
                    "composition": "Tâm điểm thị giác là màn hình sáng trong ánh sáng mờ ảo",
                    "director_note": "Cao trào phân cảnh 1: Nhấn mạnh sự chờ đợi mòn mỏi những thông báo doanh thu không xuất hiện."
                },
                {
                    "beat_id": "1.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "2.2s - 3.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat3.jpg",
                    "shot_type": "Cận cảnh ngắt nhịp (Close-Up Cut)",
                    "angle": "Góc ngang mặt bàn",
                    "camera_motion": "Tilt nhẹ và rút tay dứt khoát",
                    "composition": "Màn hình tắt đen phản chiếu bóng người",
                    "director_note": "Điểm ngắt nhịp: Màn hình phụt tắt tạo Match-cut chuyển sang không gian lớp học Cảnh 2."
                }
            ]
        },
        {
            "scene_id": 2,
            "time_range": "00:03 - 00:07s",
            "duration": "4s",
            "title": "Ngồi Góc Lớp Lướt Số Liệu",
            "main_shot_type": "Trung cảnh",
            "director_core_intent": "Vỏ bọc bận rộn che giấu nỗi lo âu bên trong.",
            "voiceover": "...Người ngoài nhìn vào tưởng mình bận rộn chốt đơn trả lời khách.",
            "beats": [
                {
                    "beat_id": "2.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "3.0s - 4.4s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
                    "shot_type": "Trung cảnh (Medium Shot)",
                    "angle": "Ngang tầm mắt (Eye Level)",
                    "camera_motion": "Trôi nhẹ sang ngang (Drift)",
                    "composition": "1/3 bên trái khung hình, hậu cảnh lớp học",
                    "director_note": "Thiết lập bối cảnh lớp học đông đúc nhưng nhân vật ngồi tách biệt, tập trung vào điện thoại."
                },
                {
                    "beat_id": "2.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "4.4s - 6.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat2.jpg",
                    "shot_type": "Trung cận qua vai (Over-the-Shoulder)",
                    "angle": "Góc qua vai trái 30°",
                    "camera_motion": "Handheld nhịp thở nhẹ",
                    "composition": "Màn hình điện thoại ở trung tâm, ngón tay lướt liên tục",
                    "director_note": "Khắc họa vẻ mặt nghiêm túc chăm chú gõ máy làm người khác hiểu lầm là nhiều việc."
                },
                {
                    "beat_id": "2.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "6.0s - 7.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat3.jpg",
                    "shot_type": "Cận cảnh bàn tay (Tight Close-Up)",
                    "angle": "Góc hếch nhẹ từ dưới lên",
                    "camera_motion": "Push-in dồn dập vào ngón tay",
                    "composition": "Bàn tay nắm chặt viền máy sốt ruột",
                    "director_note": "Điểm dừng tay chuẩn bị hé lộ con số chi phí thực sự ở Cảnh 3."
                }
            ]
        },
        {
            "scene_id": 3,
            "time_range": "00:07 - 00:15s",
            "duration": "8s",
            "title": "Màn Hình Chi Phí Ads Tăng Vọt",
            "main_shot_type": "Cận cảnh",
            "director_core_intent": "Đánh thẳng vào nỗi đau: Tiền quảng cáo tăng gấp đôi, tiền nạp ăn mòn lợi nhuận.",
            "voiceover": "Nhưng thật ra là đang sốt ruột. Mấy tháng nay tiền quảng cáo tăng gấp đôi, tiền nạp vào ăn gần hết tiền lãi.",
            "beats": [
                {
                    "beat_id": "3.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "7.0s - 9.8s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
                    "shot_type": "Đặc tả màn hình (POV UI)",
                    "angle": "Trực diện 90° vào màn hình",
                    "camera_motion": "Push-in từ từ",
                    "composition": "Biểu đồ chi phí ads màu đỏ vọt lên chiếm trọn",
                    "director_note": "Trực quan hóa con số chi phí tăng vọt đè nặng tâm lý người làm chủ."
                },
                {
                    "beat_id": "3.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "9.8s - 13.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat2.jpg",
                    "shot_type": "Cận cảnh chân dung (Facial Close-Up)",
                    "angle": "Góc trực diện hơi thấp hắt sáng",
                    "camera_motion": "Máy tĩnh tạo cảm giác ngột ngạt",
                    "composition": "Khuôn mặt anh Việt chiếm trọn khung hình với nét mặt đăm chiêu",
                    "director_note": "Bắt trọn ánh mắt lo âu và sự bất an khi nhìn vào kết quả chiến dịch quảng cáo."
                },
                {
                    "beat_id": "3.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "13.0s - 15.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat3.jpg",
                    "shot_type": "Trung cận nghiêng (Medium Close-Up)",
                    "angle": "Góc nghiêng cạnh bàn",
                    "camera_motion": "Pan êm hướng mắt nhìn lên bảng",
                    "composition": "Hạ máy úp xuống bàn, chuyển hướng nhìn",
                    "director_note": "Động tác úp máy và ngẩng đầu làm mồi nối hoàn hảo sang Cảnh 4 giác ngộ."
                }
            ]
        },
        {
            "scene_id": 4,
            "time_range": "00:15 - 00:25s",
            "duration": "10s",
            "title": "Góc Nghiêng Nhìn Lên Bảng Suy Tư",
            "main_shot_type": "Góc nghiêng",
            "director_core_intent": "Khoảnh khắc giác ngộ: Không thể đốt tiền mãi, phải tự làm video xây dựng lòng tin.",
            "voiceover": "Trước đây cứ nghĩ chỉ cần nạp tiền chạy ads là xong việc. Giờ mới thấm: nếu không tự biết cách làm video để người ta tin, thì có bao nhiêu tiền vốn cũng không bù nổi chi phí.",
            "beats": [
                {
                    "beat_id": "4.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "15.0s - 18.5s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
                    "shot_type": "Cận góc nghiêng (Tight Side Profile)",
                    "angle": "Góc nghiêng 90°",
                    "camera_motion": "Arc shot xoay nhẹ quanh trục",
                    "composition": "Mặt hướng về 1/3 bên phải, ánh sáng xiên cửa sổ",
                    "director_note": "Góc nghiêng điện ảnh khắc họa suy nghĩ trăn trở của người làm kinh doanh."
                },
                {
                    "beat_id": "4.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "18.5s - 22.5s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat2.jpg",
                    "shot_type": "Cận ánh mắt (Insight Eye Close-Up)",
                    "angle": "Góc 3/4 trực diện",
                    "camera_motion": "Push-in chậm thể hiện sự giác ngộ",
                    "composition": "Đôi mắt sáng ở 1/3 trên khung hình",
                    "director_note": "Biểu cảm chuyển từ lo lắng sang kiên định, thấu hiểu quy luật xây dựng niềm tin."
                },
                {
                    "beat_id": "4.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "22.5s - 25.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat3.jpg",
                    "shot_type": "Trung cảnh chuẩn bị (Medium Setup)",
                    "angle": "Góc ngang tầm mắt",
                    "camera_motion": "Cầm máy giơ lên trước mặt",
                    "composition": "Màn hình selfie sẵn sàng ghi hình",
                    "director_note": "Động tác nhấc máy lên ngang tầm mắt làm mồi nối bùng nổ sang cảnh 5 trực diện."
                }
            ]
        },
        {
            "scene_id": 5,
            "time_range": "00:25 - 00:30s",
            "duration": "5s",
            "title": "Trực Diện Camera Tuyên Bố",
            "main_shot_type": "Trực diện",
            "director_core_intent": "Kêu gọi hành động mạnh mẽ: Tự tin xuất hiện trước khách hàng thay vì dựa dẫm vào quảng cáo.",
            "voiceover": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi.",
            "beats": [
                {
                    "beat_id": "5.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "25.0s - 26.8s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg",
                    "shot_type": "Cận trực diện (Frontal Close-Up)",
                    "angle": "Trực diện ngang tầm mắt",
                    "camera_motion": "Handheld vững chắc",
                    "composition": "Center Framing 1-1, gương mặt anh Việt ở trung tâm",
                    "director_note": "Nhìn thẳng vào ống kính máy quay với ánh mắt chân thành và kiên định."
                },
                {
                    "beat_id": "5.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "26.8s - 28.8s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat2.jpg",
                    "shot_type": "Cận cảnh truyền lửa (Conviction Shot)",
                    "angle": "Trực diện hất nhẹ 5°",
                    "camera_motion": "Punch-in nhẹ 10%",
                    "composition": "Năng lượng mạnh mẽ, khẩu hình dứt khoát",
                    "director_note": "Truyền tải thông điệp cốt lõi: Tự tin xuất hiện, xây dựng niềm tin thật."
                },
                {
                    "beat_id": "5.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "28.8s - 30.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat3.jpg",
                    "shot_type": "Trung cận kết thúc (Outro Frame)",
                    "angle": "Ngang tầm mắt",
                    "camera_motion": "Tĩnh giữ frame 0.5s",
                    "composition": "Chừa 1/3 dưới cho Brand Tag & CTA",
                    "director_note": "Nụ cười nhẹ điềm đạm khép lại video đầy cảm hứng và thuyết phục."
                }
            ]
        }
    ]
}

# -------------------------------------------------------------
# 2. DATA FOR KB02: TIỀN MẶT BẰNG & CỬA HÀNG VẮNG KHÁCH (ẢNH MỚI)
# -------------------------------------------------------------
kb02_data = {
    "project_title": "Bảng Phân Cảnh Storyboard: Tiền Mặt Bằng & Cửa Hàng Vắng Khách (Kịch Bản 02)",
    "project_slug": "tien_mat_bang_va_cua_hang_vang_khach",
    "total_duration_sec": 30,
    "scenes_count": 5,
    "beats_count": 15,
    "aspect_ratio": "9:16 (TikTok / Reels)",
    "input_context": {
        "source": "9 Kịch Bản Thực Chiến 3 Tầng Sự Thật",
        "url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/9_kich_ban_thuc_chien.html#kb02",
        "timestamp": "21/08/2026 11:15:00",
        "raw_text": """KỊCH BẢN 02 • CHỦ SHOP & MỞ TIỆM
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
Hình ảnh phòng học thể hiện sự tập trung — Lời thoại mang sức nặng sinh tồn cơm áo gạo tiền.""",
        "ref_images": [
            {
                "title": "Ảnh Bối Cảnh Lớp Học & Bàn Gỗ",
                "url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/reference/ref_01_classroom.jpg",
                "desc": "Bàn gỗ tự nhiên, sổ tay ghi chép, bút máy, ánh sáng xiên cửa sổ phòng học."
            },
            {
                "title": "Ảnh Nhân Vật Mặc Định (Anh Việt)",
                "url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/reference/ref_02_character.jpg",
                "desc": "Anh Việt - Diễn giả/Chủ cửa hàng 30s, dáng runner, áo thun trắng/sơ mi tối giản."
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
            "title": "Tầng 2: Cảm giác thật (Nỗi đau âm ỉ)",
            "badge": "Cảm giác thật",
            "content": "Tháng vừa rồi khách vắng hẳn, ngồi ở cửa hàng thấy sốt ruột như lửa đốt."
        },
        {
            "tier": 3,
            "title": "Tầng 3: Ngượng miệng (Sự thật trần trụi)",
            "badge": "Nỗi sợ sâu kín",
            "content": "Cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ việc văn phòng ra làm chủ tưởng tự do, ai ngờ tự làm thuê cho mình 16h/ngày."
        }
    ],
    "scenes": [
        {
            "scene_id": 1,
            "time_range": "00:00 - 00:03s",
            "duration": "3s",
            "title": "Gạch Số Tiền Chi Phí Trên Sổ",
            "main_shot_type": "Cận cảnh",
            "director_core_intent": "Đánh mạnh vào tâm lý sốt ruột: Gạch bỏ các con số chi phí mặt bằng nặng nề.",
            "voiceover": "Sáng Chủ Nhật, tôi ngồi ở lớp này không phải vì rảnh rỗi...",
            "beats": [
                {
                    "beat_id": "1.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "0.0s - 1.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene1_beat1.jpg",
                    "shot_type": "Cận cảnh bàn tay (Close-Up)",
                    "angle": "Góc nghiêng 45° từ trên xuống",
                    "camera_motion": "Máy tĩnh bắt nét sâu ngòi bút và con số 20 triệu",
                    "composition": "Quy tắc 1/3, sổ tay đặt giữa ánh đèn bàn",
                    "director_note": "Mở đầu phân cảnh 1: Tay anh Việt cầm bút gạch mạnh con số chi phí mặt bằng 20,000,000đ trên sổ."
                },
                {
                    "beat_id": "1.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "1.0s - 2.2s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene1_beat2.jpg",
                    "shot_type": "Đặc tả cực cận (Extreme Close-Up)",
                    "angle": "Góc nhìn 60° từ trên xuống",
                    "camera_motion": "Push-in chậm vào nét mực bị gạch",
                    "composition": "Tâm điểm thị giác là vết mực đen hằn sâu trên trang giấy",
                    "director_note": "Cao trào phân cảnh 1: Nét mực gạch đè lên con số tiền mặt bằng thể hiện áp lực tài chính đè nặng."
                },
                {
                    "beat_id": "1.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "2.2s - 3.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene1_beat3.jpg",
                    "shot_type": "Cận cảnh ngắt nhịp (Close-Up Cut)",
                    "angle": "Góc ngang mặt bàn",
                    "camera_motion": "Tilt-up nhẹ + dừng bút",
                    "composition": "Bàn tay dừng trên trang giấy, ánh sáng ban mai qua cửa sổ",
                    "director_note": "Điểm ngắt nhịp: Tay buông nhẹ bút, ngẩng đầu làm mồi Match-cut sang Cảnh 2 góc nhìn lớp học."
                }
            ]
        },
        {
            "scene_id": 2,
            "time_range": "00:03 - 00:07s",
            "duration": "4s",
            "title": "Bóng Mình Ngồi Giữa Lớp Học",
            "main_shot_type": "Toàn cảnh",
            "director_core_intent": "Vỏ bọc chăm chỉ đi học thêm để giấu đi bế tắc doanh số cửa hàng.",
            "voiceover": "...Người ngoài nhìn vào tưởng mình chăm chỉ đi học thêm cái mới.",
            "beats": [
                {
                    "beat_id": "2.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "3.0s - 4.4s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene2_beat1.jpg",
                    "shot_type": "Toàn cảnh từ sau lưng (Wide OTS Back)",
                    "angle": "Góc từ sau lưng bao quát lớp học",
                    "camera_motion": "Máy tĩnh bắt nét bóng lưng anh Việt",
                    "composition": "Bóng lưng anh Việt ở trung tâm, màn chiếu phía trước",
                    "director_note": "Thiết lập bối cảnh lớp học đông người nhưng bóng dáng nhân vật toát lên vẻ cô đơn trĩu nặng."
                },
                {
                    "beat_id": "2.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "4.4s - 6.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene2_beat2.jpg",
                    "shot_type": "Trung cận qua vai (Over-the-Shoulder)",
                    "angle": "Góc qua vai 30°",
                    "camera_motion": "Handheld nhẹ tự nhiên",
                    "composition": "Anh Việt chống cằm lắng nghe, nét mặt trầm tư",
                    "director_note": "Cao trào phân cảnh 2: Vẻ ngoài có vẻ như chăm chú học tập nhưng trong lòng là cả mớ bòng bong."
                },
                {
                    "beat_id": "2.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "6.0s - 7.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene2_beat3.jpg",
                    "shot_type": "Trung cận góc nghiêng (Medium Side Profile)",
                    "angle": "Góc nghiêng 3/4 mặt",
                    "camera_motion": "Pan êm hướng mắt nhìn xuống điện thoại",
                    "composition": "Khuôn mặt anh Việt chiếm 1/3 trái, ánh sáng xiên mờ",
                    "director_note": "Động tác cụp mắt nhìn xuống màn hình điện thoại dẫn dắt sang Cảnh 3 xem số liệu."
                }
            ]
        },
        {
            "scene_id": 3,
            "time_range": "00:07 - 00:15s",
            "duration": "8s",
            "title": "Màn Hình Doanh Thu Vắng Khách",
            "main_shot_type": "Đặc tả",
            "director_core_intent": "Sự thật xót xa: Cửa hàng vắng khách, ruột gan như lửa đốt.",
            "voiceover": "Nhưng thật ra tháng vừa rồi cửa hàng vắng khách quá, ngồi ở tiệm mà ruột gan như lửa đốt.",
            "beats": [
                {
                    "beat_id": "3.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "7.0s - 9.8s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene3_beat1.jpg",
                    "shot_type": "Đặc tả màn hình (POV UI)",
                    "angle": "Trực diện 90° vào smartphone",
                    "camera_motion": "Push-in từ từ",
                    "composition": "Màn hình hiển thị doanh thu 0đ và lượt khách hàng chạm đáy",
                    "director_note": "Trực diện con số doanh thu ảm đạm của cửa hàng trong tháng vừa qua."
                },
                {
                    "beat_id": "3.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "9.8s - 13.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene3_beat2.jpg",
                    "shot_type": "Cận cảnh chân dung lo lắng (Facial Anxiety Close-Up)",
                    "angle": "Trực diện hơi thấp, ánh sáng gắt",
                    "camera_motion": "Slow Creep-In",
                    "composition": "Khuôn mặt anh Việt toát mồ hôi, ánh mắt căng thẳng tột độ",
                    "director_note": "Cao trào phân cảnh 3: Khắc họa trần trụi cảm giác ruột gan như lửa đốt của người chủ tiệm."
                },
                {
                    "beat_id": "3.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "13.0s - 15.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene3_beat3.jpg",
                    "shot_type": "Trung cận ôm đầu (Frustration Cut)",
                    "angle": "Góc ngang tầm bàn",
                    "camera_motion": "Máy tĩnh giữ nhịp thở nặng nề",
                    "composition": "Hai tay ôm trán, điện thoại úp mặt trên bàn",
                    "director_note": "Tư thế bế tắc tạo khoảng lặng trước khi chuyển sang suy ngẫm ở Cảnh 4."
                }
            ]
        },
        {
            "scene_id": 4,
            "time_range": "00:15 - 00:25s",
            "duration": "10s",
            "title": "Nhìn Ra Cửa Sổ Suy Tư Tiền Mặt Bằng",
            "main_shot_type": "Góc nghiêng",
            "director_core_intent": "Áp lực tiền nhà 20 triệu & hiện thực làm thuê cho chính mình 16h/ngày.",
            "voiceover": "Sợ nhất là cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ công việc văn phòng ra mở riêng tưởng nhẹ đầu, ai ngờ cày từ sáng đến đêm mà không dám nghỉ ngày nào.",
            "beats": [
                {
                    "beat_id": "4.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "15.0s - 18.5s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene4_beat1.jpg",
                    "shot_type": "Cận góc nghiêng cửa sổ (Side Profile Window)",
                    "angle": "Góc nghiêng 90° nhìn ra cửa kính",
                    "camera_motion": "Arc shot nhẹ từ từ",
                    "composition": "Anh Việt chống cằm nhìn ra cửa sổ mưa rơi, ánh sáng tự nhiên",
                    "director_note": "Góc quay trầm buồn khắc họa nỗi sợ cố hữu: Ngày 30 hàng tháng phải đóng 20 triệu tiền mặt bằng."
                },
                {
                    "beat_id": "4.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "18.5s - 22.5s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene4_beat2.jpg",
                    "shot_type": "Cận cảnh ánh mắt giác ngộ (Insight Eyes)",
                    "angle": "Góc 3/4 hắt sáng",
                    "camera_motion": "Push-in chậm",
                    "composition": "Ánh mắt chuyển từ hoang mang sang kiên định, chấp nhận sự thật",
                    "director_note": "Nét mặt bừng sáng khi nhận ra không thể trốn tránh, phải hành động để tự cứu cửa hàng."
                },
                {
                    "beat_id": "4.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "22.5s - 25.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene4_beat3.jpg",
                    "shot_type": "Trung cảnh đứng dậy (Standing Up Setup)",
                    "angle": "Góc ngang tầm ngực",
                    "camera_motion": "Đứng thẳng người, cầm sổ tay",
                    "composition": "Dáng người vững chãi bên bàn làm việc",
                    "director_note": "Động tác đứng dậy dứt khoát làm bàn đạp chuyển thẳng sang tuyên bố ở Cảnh 5."
                }
            ]
        },
        {
            "scene_id": 5,
            "time_range": "00:25 - 00:30s",
            "duration": "5s",
            "title": "Nhìn Thẳng Camera Tuyên Bố Điềm Đạm",
            "main_shot_type": "Trực diện",
            "director_core_intent": "Quyết tâm sinh tồn: Cái gì giúp duy trì được cửa hàng thì phải bắt tay vào học.",
            "voiceover": "Đến lúc này thì cái gì giúp mình duy trì được cửa hàng thì phải bắt tay vào học thôi.",
            "beats": [
                {
                    "beat_id": "5.1",
                    "beat_type": "in_point",
                    "beat_label": "🔰 Đầu cảnh (In-point)",
                    "timestamp": "25.0s - 26.8s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene5_beat1.jpg",
                    "shot_type": "Cận trực diện (Frontal Eye-Level Close-Up)",
                    "angle": "Trực diện ngang tầm mắt",
                    "camera_motion": "Handheld vững vàng",
                    "composition": "Center framing 1-1, ánh nhìn trực diện chân thực",
                    "director_note": "Nhìn thẳng vào mắt khán giả với sự chân thành của một người chủ đang nỗ lực cứu lấy tâm huyết của mình."
                },
                {
                    "beat_id": "5.2",
                    "beat_type": "main_action",
                    "beat_label": "🔥 Chi tiết / Cao trào (Main Action)",
                    "timestamp": "26.8s - 28.8s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene5_beat2.jpg",
                    "shot_type": "Cận cảnh nói dứt khoát (Conviction Close-Up)",
                    "angle": "Trực diện hất nhẹ 5°",
                    "camera_motion": "Punch-in nhẹ 10%",
                    "composition": "Khẩu hình dứt khoát, bàn tay đưa lên nhấn mạnh",
                    "director_note": "Khẳng định tinh thần học hỏi thực chiến: Học để sinh tồn và phát triển cửa hàng."
                },
                {
                    "beat_id": "5.3",
                    "beat_type": "out_point",
                    "beat_label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)",
                    "timestamp": "28.8s - 30.0s",
                    "image": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene5_beat3.jpg",
                    "shot_type": "Trung cận nụ cười tự tin (Confident Outro Frame)",
                    "angle": "Ngang tầm mắt",
                    "camera_motion": "Tĩnh giữ frame 0.5s",
                    "composition": "Nụ cười tự tin, hậu cảnh không gian làm việc hiện đại",
                    "director_note": "Nụ cười rạng rỡ và tự tin khép lại video, tạo động lực mạnh mẽ cho người xem."
                }
            ]
        }
    ]
}

def render_storyboard_html(data, output_filepath):
    # Đọc template từ file kịch bản 3 có sẵn
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        tmpl = f.read()

    # Trích xuất CSS styling và JS logic từ template
    css_match = tmpl.split("<style>")[1].split("</style>")[0]
    js_match = tmpl.split("<script>")[1].split("</script>")[0]

    # Render HTML content
    ref_imgs_html = ""
    for r in data["input_context"]["ref_images"]:
        ref_imgs_html += f"""
            <div class="ref-item" onclick="openLightbox('{r['url']}', '{r['title']}', '{r['desc']}')">
              <div class="ref-thumb-box">
                <span class="ref-label-badge">📍 Tham Chiếu</span>
                <img src="{r['url']}" alt="{r['title']}" loading="lazy">
              </div>
              <div class="ref-caption">
                <strong>{r['title']}</strong>
                <span>{r['desc']}</span>
              </div>
            </div>"""

    tiers_html = ""
    tier_classes = ["t1", "t2", "t3"]
    for idx, t in enumerate(data.get("three_truth_tiers", [])):
        c = tier_classes[idx % 3]
        tiers_html += f"""
          <div class="tier-card {c}">
            <span class="tier-badge-label">{t['badge']}</span>
            <div style="font-weight:700; color:#fff; font-size:12px; margin-bottom:4px;">{t['title']}</div>
            <div class="tier-text">"{t['content']}"</div>
          </div>"""

    scenes_html = ""
    filmstrip_html = ""
    for sc in data["scenes"]:
        beats_cards_html = ""
        for b in sc["beats"]:
            badge_class = "badge-inpoint" if b["beat_type"] == "in_point" else ("badge-mainaction" if b["beat_type"] == "main_action" else "badge-outpoint")
            beats_cards_html += f"""
            <div class="beat-card">
              <div class="beat-media-box" onclick="openLightbox('{b['image']}', '{b['beat_label']} - Cảnh {sc['scene_id']}', '{b['director_note']}')">
                <img src="{b['image']}" alt="{b['beat_label']}" class="beat-img" loading="lazy">
                <div class="beat-badge-tag {badge_class}">{b['beat_label']}</div>
                <div class="beat-ts">{b['timestamp']}</div>
              </div>
              <div class="beat-body">
                <div class="meta-row">
                  <span class="meta-label">Cỡ cảnh:</span>
                  <span class="meta-val highlight">{b['shot_type']}</span>
                </div>
                <div class="meta-row">
                  <span class="meta-label">Góc máy:</span>
                  <span class="meta-val">{b['angle']}</span>
                </div>
                <div class="meta-row">
                  <span class="meta-label">Chuyển động:</span>
                  <span class="meta-val">{b['camera_motion']}</span>
                </div>
                <div class="meta-row">
                  <span class="meta-label">Bố cục:</span>
                  <span class="meta-val">{b['composition']}</span>
                </div>
                <div class="director-note">
                  🎬 <b>Đạo diễn:</b> {b['director_note']}
                </div>
              </div>
            </div>"""

            filmstrip_html += f"""
        <div class="strip-frame" onclick="openLightbox('{b['image']}', '{b['beat_label']} - Cảnh {sc['scene_id']}', '{b['director_note']}')">
          <img src="{b['image']}" alt="{b['beat_label']}" class="strip-frame-img" loading="lazy">
          <div class="strip-meta">
            <div class="strip-title">C{sc['scene_id']} • Beat {b['beat_id'].split('.')[-1]}</div>
            <div class="strip-ts">{b['timestamp']}</div>
          </div>
        </div>"""

        scenes_html += f"""
    <!-- SCENE {sc['scene_id']} -->
    <section class="scene-section" id="scene-{sc['scene_id']}">
      <div class="scene-header">
        <div class="scene-header-left">
          <div class="scene-number">CẢNH {sc['scene_id']}</div>
          <div>
            <div class="scene-title">{sc['title']}</div>
            <div class="scene-sub">{sc['director_core_intent']}</div>
          </div>
        </div>
        <div class="scene-meta-badges">
          <span class="badge-time">⏱️ {sc['time_range']} ({sc['duration']})</span>
          <span class="badge-shot">🎥 {sc['main_shot_type']}</span>
        </div>
      </div>

      <div class="voiceover-box">
        <div class="voiceover-title">🎙️ LỜI THOẠI & ÂM THANH TRỌNG TÂM</div>
        <div class="voiceover-text">"{sc['voiceover']}"</div>
      </div>

      <div class="beats-grid">
        {beats_cards_html}
      </div>
    </section>"""

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['project_title']} | AI Storyboard Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
{css_match}
  </style>
</head>
<body>

  <!-- Top Sticky Header -->
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">Bảng Phân Cảnh AI</span>
      <div class="header-title">🎬 {data['project_title']}</div>
    </div>
    <div class="header-controls">
      <a href="index.html" class="nav-btn">🏠 Master Hub</a>
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
          <span class="orig-badge">{data['project_slug']}</span>
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
            🖼️ Bối cảnh tham chiếu (Cloudflare R2):
          </div>
          <div class="ref-gallery">
            {ref_imgs_html}
          </div>
        </div>
      </div>

      <!-- 3 Tầng Sự Thật -->
      <div class="tiers-box">
        {tiers_html}
      </div>
    </section>

    <!-- HERO OVERVIEW -->
    <section class="hero">
      <div class="hero-tags">
        <span class="tag tag-cyan">🎯 Tỷ lệ {data['aspect_ratio']}</span>
        <span class="tag tag-amber">⚡ Thời lượng {data['total_duration_sec']} Giây</span>
        <span class="tag tag-emerald">🎬 {data['scenes_count']} Cảnh • {data['beats_count']} Micro-Beats</span>
        <span class="tag tag-cyan">👤 Nhân vật: Anh Việt (Mặc định)</span>
      </div>
      <h1>{data['project_title']}</h1>
      <p class="hero-desc">
        Hệ thống phân cảnh điện ảnh 3 nhịp: <b>🔰 Đầu cảnh (In-point)</b> ➔ <b>🔥 Cao trào (Main Action)</b> ➔ <b>🔄 Mồi chuyển (Out-point Lead)</b>.
        Tối ưu tuyệt đối cho định dạng Video Ngắn 9:16 giữ chân người xem từng 1.5 giây.
      </p>
    </section>

    <!-- 5 PHÂN CẢNH CHI TIẾT -->
    {scenes_html}

    <!-- FILMSTRIP TIMELINE -->
    <section class="timeline-wrapper" id="filmstrip-view">
      <div style="font-size: 13px; font-weight: 800; color: #fff; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
        <span>🎞️ Dải Timeline Filmstrip 15 Micro-Beats (Liên Tục 0 - 30s)</span>
      </div>
      <div class="filmstrip">
        {filmstrip_html}
      </div>
    </section>

  </div>

  <!-- LIGHTBOX MODAL -->
  <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
    <button class="lightbox-close" onclick="closeLightbox(event)">×</button>
    <div class="lightbox-content" onclick="event.stopPropagation()">
      <div class="lightbox-img-box">
        <img src="" alt="Phóng to" id="lightbox-img">
      </div>
      <div class="lightbox-details">
        <h3 id="lightbox-title" style="color: #fff; font-size: 16px; font-weight: 700;"></h3>
        <p id="lightbox-desc" style="color: var(--text-secondary); font-size: 13px; line-height: 1.6;"></p>
        <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid var(--border-subtle); display: flex; justify-content: space-between; font-size: 11px; color: var(--text-muted);">
          <span>📐 Tỷ lệ 9:16 Vertical Storyboard</span>
          <span>⚡ Cloudflare R2 CDN</span>
        </div>
      </div>
    </div>
  </div>

  <script>
{js_match}
  </script>
</body>
</html>"""

    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ Đã tạo thành công: {output_filepath}")

# Render file KB01 và KB02
render_storyboard_html(kb01_data, "/Users/vietmac/Documents/CODE/Bang-Phan-Canh/tu_dot_tien_den_tu_tin_xuat_hien.html")
render_storyboard_html(kb02_data, "/Users/vietmac/Documents/CODE/Bang-Phan-Canh/tien_mat_bang_va_cua_hang_vang_khach.html")

