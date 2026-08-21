#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HỆ THỐNG TỰ ĐỘNG HÓA TẠO BẢNG PHÂN CẢNH CHO CÁC KỊCH BẢN TỪ 4 TRONG 9_KICH_BAN_THUC_CHIEN.HTML
Chuẩn Storyboard Studio Điện Ảnh 9:16 - 3 Micro-Beats / Cảnh (15 Beats / Video 30s)
"""

import os
import json
import subprocess
from datetime import datetime

REPO_DIR = "/Users/vietmac/Documents/CODE/Bang-Phan-Canh"
R2_MEDIA_BASE = "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien"

# DỮ LIỆU ĐẦY ĐỦ 9 KỊCH BẢN THỰC CHIẾN
scripts_data = [
    {
        "id": "kb01",
        "num": 1,
        "slug": "kich_ban_01_ngoi_ca_phe_10h_toi",
        "file_name": "kich_ban_01_ngoi_ca_phe_10h_toi.html",
        "title": "Ngồi Cà Phê 10h Tối",
        "tag": "LÀM VIỆC ĐÊM & BẾ TẮC",
        "category": "Tâm Lý & Áp Lực Kiệt Sức",
        "badge_color": "#6366f1",
        "target_audience": "Người trẻ làm nghề, freelancer cày đêm vì bất an",
        "context_desc": "Bối cảnh: Góc bàn cafe / Bàn học đêm • Chạm vào: Áp lực FOMO & Kiệt sức",
        "takeaway": "Bóc trần thói quen 'cố tỏ ra bận rộn' để xoa dịu nỗi sợ tụt hậu của giới trẻ và dân làm nghề.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Ra quán cà phê đổi gió cho dễ tập trung chạy deadline."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Ở nhà ngột ngạt quá, nằm một chỗ thấy sốt ruột và tội lỗi."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Đang kiệt sức và bế tắc, nhưng không dám nghỉ vì sợ mình tụt lại phía sau."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Tay khuấy nhẹ ống hút trong ly nước đá tan",
                "voiceover": "10h tối, ngồi ở góc quán này không phải vì chăm chỉ...",
                "intent": "Mở màn chân thật: Bóc trần sự thật đằng sau thói quen ngồi cafe đêm làm việc.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh ly nước (Close-Up)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét đá tan", "comp": "1/3 góc bàn cafe đêm", "note": "Bắt đầu bằng cử chỉ vô thức khuấy ly nước, ánh đèn quán cafe vàng ấm."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả ống hút (Extreme Close-Up)", "angle": "Góc trực diện 60°", "motion": "Push-in chậm vào đầu ngón tay", "comp": "Tâm điểm viên đá tan chảy", "note": "Đầu ngón tay gõ nhẹ lên thành cốc, thể hiện sự mông lung trong suy nghĩ."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh ngắt nhịp (Close-Up)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ hướng lên màn hình", "comp": "Vệt sáng màn hình laptop mờ ảo", "note": "Nhấc ngón tay rời khỏi cốc, ánh mắt hướng về phía màn hình laptop."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Ngồi trước laptop, màn hình sáng đèn giữa phòng",
                "voiceover": "...Người ngoài nhìn vào tưởng mình đang cày việc vì đam mê.",
                "intent": "Tạo sự tương phản giữa vẻ ngoài hào nhoáng đam mê và sự trống rỗng bên trong.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh ngang vai (Medium OTS)", "angle": "Góc ngang tầm mắt", "motion": "Trôi nhẹ sang ngang (Drift)", "comp": "Nhân vật ngồi lệch 1/3 trái", "note": "Màn hình laptop sáng rực giữa không gian quán tối tĩnh lặng."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận qua vai (Over-the-Shoulder)", "angle": "Góc qua vai trái 30°", "motion": "Handheld nhịp thở nhẹ", "comp": "Màn hình trình duyệt nhiều tab", "note": "Mở hàng chục tab nhưng không gõ thêm được dòng code hay bài viết nào."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận bàn tay gõ phím (Keyboard Shot)", "angle": "Góc hếch nhẹ", "motion": "Push-in dồn dập", "comp": "Bàn tay ngập ngừng trên phím", "note": "Ngón tay dừng lại giữa không trung, chuẩn bị đưa lên xoa trán."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Bàn tay xoa trán mệt mỏi, mắt nhìn màn hình",
                "voiceover": "Nhưng thật ra ở nhà ngột ngạt quá. Nằm xuống thì thấy sốt ruột và tội lỗi, mà ngồi vào bàn thì đầu óc trống rỗng.",
                "intent": "Chạm vào nỗi đau ngột ngạt nội tâm: Nằm thì tội lỗi, ngồi vào bàn thì bế tắc.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Cận cảnh chân dung (Facial Close-Up)", "angle": "Góc trực diện hơi thấp", "motion": "Máy tĩnh ngột ngạt", "comp": "Khuôn mặt chiếm trọn 2/3", "note": "Bàn tay đưa lên xoa nhẹ vùng thái dương, đôi mắt mỏi mệt vì ánh sáng xanh."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Đặc tả đôi mắt (Eye Extreme Close-Up)", "angle": "Trực diện 90° vào ánh mắt", "motion": "Push-in từ từ", "comp": "Ánh sáng màn hình phản chiếu trong mắt", "note": "Khắc họa cảm giác 'đầu óc trống rỗng' dù đang rất muốn hoàn thành công việc."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận nghiêng (Medium Close-Up)", "angle": "Góc nghiêng cạnh bàn", "motion": "Pan êm hướng ra cửa kính", "comp": "Nhân vật buông tay, thở dài", "note": "Hạ tay xuống bàn, quay đầu nhìn ra khung cửa kính tối đen ngoài phố."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Góc nghiêng mặt nhìn ra ngoài cửa kính đêm",
                "voiceover": "Sự thật là người mệt lả rồi nhưng không dám nghỉ. Thấy bạn bè xung quanh ai cũng kiếm tiền tốt, mình sợ chỉ cần dừng lại một hôm là tụt lại phía sau.",
                "intent": "Bóc trần sự thật ngượng miệng: Nỗi sợ FOMO bị bỏ lại phía sau khi thấy người khác kiếm tiền tốt.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng (Tight Side Profile)", "angle": "Góc nghiêng 90° phản chiếu qua kính", "motion": "Arc shot xoay nhẹ góc", "comp": "Khuôn mặt suy tư ở 1/3 phải", "note": "Góc nghiêng phản chiếu bóng người trên mặt kính cùng vệt đèn xe đêm."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Cận cảnh ánh mắt (Insight Close-Up)", "angle": "Góc 3/4 trực diện", "motion": "Push-in chậm giác ngộ", "comp": "Đôi mắt kiên định dần xuất hiện", "note": "Nhìn thấu nỗi bất an của bản thân: Cố cày đêm để chạy trốn sự sợ hãi tụt hậu."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh chuẩn bị (Medium Setup)", "angle": "Góc ngang tầm mắt", "motion": "Cầm máy giơ lên trước mặt", "comp": "Góc máy selfie thẳng mặt", "note": "Xoay người lại đối diện máy quay, chuẩn bị nói thẳng vào camera."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Nhìn thẳng camera nói điềm đạm",
                "voiceover": "Nhiều khi cố cày đêm không phải để giàu lên, mà chỉ là liều thuốc an thần cho sự bất an của chính mình.",
                "intent": "Đúc kết thông điệp đắt giá (Takeaway): Thừa nhận sự thật để dừng vòng lặp bận rộn vô nghĩa.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Giao tiếp mắt trực diện 100% với người xem, thần thái điềm tĩnh sâu sắc."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh truyền lửa (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Gương mặt sáng rõ uy tín", "note": "Nói dứt khoát câu chốt: 'Liều thuốc an thần cho sự bất an của chính mình'."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Brand Tag", "note": "Ánh mắt ấm áp, gật đầu nhẹ để kết thúc video đầy dư âm đọng lại."}
                ]
            }
        ]
    },
    {
        "id": "kb02",
        "num": 2,
        "slug": "kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach",
        "file_name": "kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach.html",
        "title": "Tiền Mặt Bằng & Cửa Hàng Vắng Khách",
        "tag": "CHỦ SHOP & MỞ TIỆM",
        "category": "Kinh Doanh Cửa Hàng & Bán Lẻ",
        "badge_color": "#e11d48",
        "target_audience": "Chủ shop offline, chủ tiệm dịch vụ chịu áp lực mặt bằng",
        "context_desc": "Bối cảnh: Phòng học / Bàn làm việc • Chạm vào: Áp lực chi phí mặt bằng & vắng khách",
        "takeaway": "Hình ảnh phòng học thể hiện sự tập trung — Lời thoại mang sức nặng sinh tồn cơm áo gạo tiền.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Tôi đi học để cập nhật thêm cách tiếp cận khách hàng mới cho cửa hàng."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Tháng vừa rồi khách vắng hẳn, ngồi ở cửa hàng thấy sốt ruột như lửa đốt."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ việc văn phòng ra làm chủ tưởng tự do, ai ngờ tự làm thuê cho mình 16h/ngày."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Tay cầm bút gạch mạnh một con số trên sổ bài tập",
                "voiceover": "Sáng Chủ Nhật, tôi ngồi ở lớp này không phải vì rảnh rỗi...",
                "intent": "Phá vỡ định kiến đi học vì rảnh bằng cú gạch bút dứt khoát.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh bàn học (Close-Up Desk)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét sâu vào ngòi bút máy", "comp": "Bàn tay cầm bút ở 1/3 dưới, sổ tay mở rộng", "note": "Thiết lập bối cảnh lớp học sáng Chủ Nhật, tay đặt bút sẵn sàng viết."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả cực cận (Extreme Close-Up)", "angle": "Góc nhìn từ trên xuống 60°", "motion": "Push-in chậm dồn vào ngòi bút", "comp": "Ngòi bút gạch một đường dứt khoát đè lên con số", "note": "Cú gạch bút mạnh mẽ khớp với từ 'không phải vì rảnh rỗi', tạo lực nhấn thị giác."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh ngắt nhịp (Close-Up Lift)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ + Tay giữ chắc thân bút", "comp": "Ngòi bút nhấc lên khỏi mặt giấy", "note": "Động tác dừng bút làm nhịp ngắt mượt mà để cắt sang toàn cảnh Cảnh 2."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Toàn cảnh (Wide Shot)",
                "title": "Quay từ sau lưng, thấy bóng mình ngồi giữa lớp",
                "voiceover": "...Người ngoài nhìn vào tưởng mình chăm chỉ đi học thêm cái mới.",
                "intent": "Vạch ra sự tương phản giữa vẻ ngoài chăm chỉ và nỗi bất an bên trong.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Toàn cảnh sau lưng (Wide Over-Shoulder)", "angle": "Góc cao sau lưng bao quát lớp học", "motion": "Trôi nhẹ ngang (Subtle lateral drift)", "comp": "Nhân vật ngồi trung tâm lớp học", "note": "Bức tranh toàn cảnh một buổi học nghiêm túc, tạo vẻ ngoài chuẩn mực."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận qua vai (Over-the-Shoulder)", "angle": "Góc qua vai trái 30°", "motion": "Handheld nhịp thở nhẹ", "comp": "Bờ vai trái chiếm 1/3 góc nhìn, tay cầm smartphone", "note": "Hành vi cầm điện thoại hé lộ sự phân tâm và lo âu ngấm ngầm giữa lớp."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh tay & điện thoại (Tight Desk Shot)", "angle": "Góc hếch nhẹ từ dưới lên", "motion": "Push-in dồn vào màn hình điện thoại", "comp": "Bàn tay nhấc điện thoại lên khỏi mặt bàn", "note": "Động tác cầm điện thoại lên làm mồi nối thẳng sang giao diện Cảnh 3."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Màn hình điện thoại mở bảng doanh thu hoặc tin nhắn",
                "voiceover": "Nhưng thật ra tháng vừa rồi cửa hàng vắng khách quá, ngồi ở tiệm mà ruột gan như lửa đốt.",
                "intent": "Bóc trần Tầng 2 Sự Thật: Doanh thu lao dốc, nỗi sợ vắng khách và cảm giác bất an.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Cận cảnh màn hình POV (Direct UI Close-Up)", "angle": "Trực diện 90° vào màn hình", "motion": "Push-in từ từ (Slow Creep-In)", "comp": "Bảng Dashboard với biểu đồ đỏ cắm dốc", "note": "Bằng chứng số liệu trực quan gây sốc: Cửa hàng hoàn toàn vắng khách."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Đặc tả cực cận UI (Extreme Close-Up UI)", "angle": "Góc nghiêng 45° vào màn hình", "motion": "Máy tĩnh bắt trọn từng con số đỏ", "comp": "Ngón tay lướt chậm trên dòng thông báo rỗng", "note": "Khắc họa cảm giác 'ruột gan như lửa đốt' khi nhìn vào thực tế."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận căng thẳng (Medium Close-Up)", "angle": "Góc trực diện ngang tầm mắt", "motion": "Máy tĩnh giữ khung hình ngột ngạt", "comp": "Bàn tay siết chặt trên bàn gỗ, úp điện thoại", "note": "Nắm đấm siết chặt thể hiện sự dồn nén, chuẩn bị nhìn ra cửa sổ Cảnh 4."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Nhìn ra cửa sổ phòng học đầy suy tư",
                "voiceover": "Sợ nhất là cuối tháng tiền mặt bằng 20 triệu đến hạn. Bỏ công việc văn phòng ra mở riêng tưởng nhẹ đầu, ai ngờ cày từ sáng đến đêm mà không dám nghỉ ngày nào.",
                "intent": "Chạm sâu vào Tầng 3 Sự Thật: Áp lực tiền mặt bằng 20 triệu và nghịch lý làm chủ nhưng làm thuê 16h/ngày.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng cửa sổ (Side Profile)", "angle": "Góc nghiêng 90° đón ánh nắng", "motion": "Arc shot xoay nhẹ góc nhìn", "comp": "Nhân vật ngồi tựa cằm nhìn ra cửa sổ", "note": "Khung cảnh lắng đọng, người xem cảm nhận trọn vẹn gánh nặng 20 triệu/tháng."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Đặc tả cận ánh mắt (Insight Eye Close-Up)", "angle": "Cận cảnh 3/4 trực diện", "motion": "Push-in chậm chắt lọc cảm xúc", "comp": "Ánh mắt đăm chiêu nhưng kiên định", "note": "Nỗi trăn trở về con đường khởi nghiệp tự thân đầy chông gai."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh góc nghiêng chuyển hướng", "angle": "Góc nghiêng 45°", "motion": "Pan nhanh từ cửa sổ về thẳng camera", "comp": "Tư thế ngồi thẳng lưng, ánh mắt hướng về máy", "note": "Động tác chuyển hướng dứt khoát làm mồi nối hoàn hảo sang Cảnh 5."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Nhìn thẳng camera nói điềm đạm",
                "voiceover": "Đến lúc này thì cái gì giúp mình duy trì được cửa hàng thì phải bắt tay vào học thôi.",
                "intent": "Hành động thực tế: Bỏ sĩ diện hão, học kỹ năng mới để duy trì sự sống còn cho cửa hàng.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Nhìn thẳng vào ống kính với ánh mắt chân thành và quyết tâm cao độ."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh quyết tâm (Conviction Close-Up)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Gương mặt chiếm trọn khung hình", "note": "Khẳng định lập trường thực chiến: Phải tự cứu lấy cửa hàng của mình."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Brand Tag", "note": "Nụ cười nhẹ tự tin, gật đầu khẳng định quyết tâm trước khi hết video."}
                ]
            }
        ]
    },
    {
        "id": "kb03",
        "num": 3,
        "slug": "kich_ban_03_chung_lai_sau_tuoi_30",
        "file_name": "kich_ban_03_chung_lai_sau_tuoi_30.html",
        "title": "Chững Lại Sau Tuổi 30",
        "tag": "NGƯỜI LÀM VĂN PHÒNG",
        "category": "Phát Triển Bản Thân & Nghề Nghiệp",
        "badge_color": "#f59e0b",
        "target_audience": "Người làm văn phòng 30+, người sợ tụt hậu công nghệ",
        "context_desc": "Bối cảnh: Phòng học / Laptop • Chạm vào: Khủng hoảng tuổi 30 & Sợ tụt hậu",
        "takeaway": "Dũng cảm thừa nhận sự chững lại trong công việc giúp tạo ra sự đồng cảm và tin tưởng tự nhiên.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Tranh thủ đi học thêm kỹ năng để công việc sau này thuận lợi hơn."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Công việc làm chục năm nay đang chững lại, thu nhập đứng yên mà chi phí thì tăng."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Sợ mình bị tụt hậu. Mọi người thích nghi công nghệ mới rất nhanh, còn mình giữ thói quen cũ thì vài năm nữa khó theo kịp."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Tay khuấy nhẹ ống hút trong cốc cafe trên bàn",
                "voiceover": "Hơn 30 tuổi, ngồi trong căn phòng này cùng mọi người...",
                "intent": "Khắc họa thói quen vô thức khi ngồi lẫn giữa đám đông, chạm đúng nỗi niềm tuổi 30 đi học lại.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh (Close-Up)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét cạnh ly cafe", "comp": "1/3 góc bàn làm việc", "note": "Khởi đầu bằng ly cafe đá tan trên bàn học, gợi cảm giác trôi qua của thời gian."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả cực cận (Extreme Close-Up)", "angle": "Góc trực diện 60°", "motion": "Push-in chậm vào đầu ngón tay", "comp": "Tâm điểm ống hút & đá tan", "note": "Hành động khuấy cafe vô thức thể hiện nỗi niềm suy tư lắng đọng."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh ngắt nhịp (Close-Up)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ hướng lên người", "comp": "Bóng đổ trầm ngâm", "note": "Ngẩng đầu lên nhìn về phía chiếc laptop đang mở."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Ngồi trước laptop, gõ vài nhịp bàn phím",
                "voiceover": "...Ai hỏi thì bảo tranh thủ đi học thêm kỹ năng mới.",
                "intent": "Bộc lộ lớp vỏ bọc an toàn 'đi học thêm' để giấu đi sự bế tắc trong công việc.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh (Medium Shot)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Trôi nhẹ sang ngang (Drift)", "comp": "1/3 bên trái khung hình", "note": "Bối cảnh người làm việc văn phòng nghiêm túc, gõ từng nhịp bàn phím."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận qua vai (Over-the-Shoulder)", "angle": "Góc qua vai trái 30°", "motion": "Handheld nhịp thở nhẹ", "comp": "Màn hình laptop trung tâm", "note": "Màn hình bài giảng và tài liệu học tập, ánh sáng phản chiếu gương mặt."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh bàn phím (Keyboard Close-Up)", "angle": "Góc hếch nhẹ từ dưới lên", "motion": "Push-in dồn dập", "comp": "Bàn tay gõ nhịp ngập ngừng", "note": "Ngón tay dừng lại trên bàn phím, chuyển sang tư thế chống cằm."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Tay chống cằm nhìn lên bài giảng suy nghĩ",
                "voiceover": "Nhưng thật ra trong lòng đang rất sốt ruột. Công việc làm chục năm nay đang chững lại, thu nhập đứng yên mà chi phí ngày càng tăng.",
                "intent": "Đánh thẳng vào nỗi đau: thu nhập chững lại, chi phí gia đình đè nặng sau 10 năm đi làm.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Cận cảnh chân dung (Facial Close-Up)", "angle": "Góc nghiêng 3/4", "motion": "Máy tĩnh ngột ngạt", "comp": "Khuôn mặt chiếm trọn", "note": "Bàn tay chống cằm, ánh mắt nhìn xa xăm đượm vẻ trăn trở."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Cận cảnh tay chống cằm (Thoughtful)", "angle": "Trực diện hơi thấp", "motion": "Slow Creep-In", "comp": "Đôi mắt nặng trĩu suy tư", "note": "Khắc họa cảm giác sốt ruột khi thu nhập đứng yên giữa thời bão giá."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận nghiêng (Medium Close-Up)", "angle": "Góc nghiêng cạnh bàn", "motion": "Pan êm hướng mắt nhìn lên bảng", "comp": "Thở dài ngẫm nghĩ", "note": "Ánh mắt chuyển động hướng theo máy quay sang cuốn sổ tay."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Cảnh lia (Pan Shot)",
                "title": "Lia máy từ phòng học quay về phía cuốn sổ tay",
                "voiceover": "Sợ nhất là mình bị tụt hậu. Thấy mọi người thích nghi công nghệ mới nhanh quá, còn mình cứ giữ mãi thói quen cũ thì sớm muộn cũng bị bỏ lại phía sau.",
                "intent": "Nỗi sợ bị đào thải trước làn sóng công nghệ mới nếu không chịu thay đổi.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cảnh lia mở đầu (Pan Establishing)", "angle": "Góc rộng lia ngang 60°", "motion": "Lia máy mượt từ lớp học sang sổ", "comp": "Khung cảnh lớp học mờ ảo", "note": "Cú lia máy kết nối không gian lớp học sôi nổi với góc bàn cá nhân."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Cận cảnh trang sổ ghi chép", "angle": "Góc 45° từ trên xuống", "motion": "Push-in chậm nhấn mạnh từ khóa", "comp": "Dòng chữ công nghệ mới", "note": "Ngòi bút gạch dưới các từ khóa AI và Video ngắn, thể hiện quyết tâm học."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh chuẩn bị (Medium Setup)", "angle": "Góc ngang tầm mắt", "motion": "Cầm máy giơ lên ngang mặt", "comp": "Màn hình selfie sẵn sàng", "note": "Nhấc máy quay lên ngang tầm mắt để chuẩn bị nói thẳng vào camera."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Cầm máy ngang tầm mắt, nói tự nhiên",
                "voiceover": "Bớt ngại đi, chịu khó học lại từ đầu còn hơn cứ ngồi yên nhìn công việc của mình đi xuống.",
                "intent": "Kêu gọi hành động: Bớt ngại, đối diện thực tế, học lại từ đầu để lội ngược dòng.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Nhìn thẳng vào ống kính với thái độ tự tin, không còn e ngại."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh truyền lửa (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Năng lượng mạnh mẽ dứt khoát", "note": "Nhấn mạnh thông điệp 'học lại từ đầu' với ánh mắt đầy quyết đoán."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Subtitle & CTA", "note": "Gật đầu nhẹ mỉm cười đầy tự tin trước khi hạ máy."}
                ]
            }
        ]
    },
    {
        "id": "kb04",
        "num": 4,
        "slug": "kich_ban_04_tien_quang_cao_an_het_tien_lai",
        "file_name": "kich_ban_04_tien_quang_cao_an_het_tien_lai.html",
        "title": "Tiền Quảng Cáo Ăn Hết Tiền Lãi",
        "tag": "BÁN HÀNG ONLINE",
        "category": "Kinh Doanh & Bán Hàng Online",
        "badge_color": "#38bdf8",
        "target_audience": "Chủ shop, người bán hàng online phụ thuộc chạy Ads",
        "context_desc": "Bối cảnh: Phòng học / Điện thoại • Chạm vào: Bế tắc vì phụ thuộc chạy Ads",
        "takeaway": "Nói trúng bế tắc của việc phụ thuộc công cụ trả phí để nhấn mạnh giá trị của việc tự xuất hiện.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Tôi đi học để tìm thêm hướng đi mới, tối ưu chi phí tiếp thị cho bài bản."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Cứ 5 phút lại mở điện thoại xem tài khoản ads, tiền trừ đều mà tin nhắn khách không thấy đâu."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Trước đây kiếm được tiền là nhờ quảng cáo rẻ. Giờ chi phí đắt đỏ mới nhận ra: nếu không tự quay video để khách tin, bao nhiêu tiền cũng bốc hơi hết."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Ngón tay bấm sáng màn hình điện thoại rồi lại tắt đi",
                "voiceover": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
                "intent": "Tạo móc câu (Hook) thị giác: Thói quen sốt ruột mở tắt điện thoại liên tục khi chạy Ads.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh bàn tay & smartphone (Close-Up)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét cạnh viền kim loại điện thoại", "comp": "Chiếc smartphone đặt cạnh cuốn sổ bài tập", "note": "Ngón tay cái đặt hờ trên nút nguồn, màn hình đen phản chiếu ánh đèn trần."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả ngón tay bấm phím nguồn (Extreme Close-Up)", "angle": "Góc nhìn từ trên xuống 60°", "motion": "Push-in chậm dồn vào màn hình vừa bật sáng", "comp": "Màn hình lockscreen sáng rực: 0 thông báo mới", "note": "Màn hình sáng lên rồi ngón tay lại bấm tắt ngay trong sự thất vọng."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh ngắt nhịp (Close-Up)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ theo bàn tay cầm máy", "comp": "Bàn tay nhấc máy lên khỏi mặt bàn gỗ", "note": "Nhấc hẳn điện thoại lên tay, làm mồi chuyển sang góc nhìn trung cảnh Cảnh 2."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Ngồi ở góc bàn lớp học, cầm điện thoại lướt số liệu",
                "voiceover": "...Người ngoài nhìn vào tưởng mình bận rộn chốt đơn trả lời khách.",
                "intent": "Phơi bày sự tương phản giữa ảo tưởng 'bận rộn chốt đơn' và thực tế ngồi chờ tin nhắn.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh ngang tầm mắt (Medium Shot)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Trôi nhẹ sang ngang (Drift êm)", "comp": "Nhân vật ngồi góc bàn lớp học, dáng ngồi chăm chú", "note": "Không gian lớp học nghiêm túc, tạo ấn tượng một chủ shop đang xử lý đơn hàng."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận qua vai (Over-the-Shoulder)", "angle": "Góc qua vai trái 30°", "motion": "Handheld nhịp thở nhẹ", "comp": "Màn hình điện thoại hiển thị giao diện Ads Manager", "note": "Ngón tay lướt qua lại giữa các tab chiến dịch nhưng không có lượt chuyển đổi."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh bàn tay giữ máy (Tight Frame)", "angle": "Góc hếch nhẹ từ dưới lên", "motion": "Push-in dồn dập vào màn hình", "comp": "Ngón tay dừng lại tại con số chi phí chiến dịch", "note": "Bàn tay siết nhẹ viền máy, sẵn sàng phóng to số liệu Ads ở Cảnh 3."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Màn hình điện thoại hiển thị app quản lý chi phí ads",
                "voiceover": "Nhưng thật ra là đang sốt ruột. Mấy tháng nay tiền quảng cáo tăng gấp đôi, tiền nạp vào ăn gần hết tiền lãi.",
                "intent": "Bóc trần Tầng 2 Sự Thật: Nỗi đau tiền quảng cáo bào mòn toàn bộ lợi nhuận kinh doanh.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Đặc tả màn hình POV (Direct UI Close-Up)", "angle": "Trực diện 90° vào màn hình điện thoại", "motion": "Push-in từ từ (Slow Creep-In)", "comp": "Bảng Dashboard chi phí Ads: CPM +120%, ROI giảm mạnh", "note": "Số liệu Ads đỏ rực đập thẳng vào mắt người xem, minh chứng trực quan đắt giá."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Cận cảnh biểu cảm chân dung (Facial Close-Up)", "angle": "Góc trực diện hơi thấp", "motion": "Máy tĩnh giữ khung hình ngột ngạt", "comp": "Khuôn mặt nhíu mày, ánh sáng màn hình hắt lên mắt", "note": "Biểu cảm sốt ruột và bất lực khi thấy từng triệu đồng nạp vào trôi đi vô ích."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận nghiêng (Medium Close-Up)", "angle": "Góc nghiêng cạnh bàn", "motion": "Pan êm hướng mắt nhìn lên bảng", "comp": "Bàn tay hạ điện thoại úp xuống mặt bàn gỗ", "note": "Động tác úp màn hình điện thoại xuống bàn, ngẩng đầu nhìn lên bảng giảng bài."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Nhìn lên bảng giảng bài, vẻ mặt đăm chiêu",
                "voiceover": "Trước đây cứ nghĩ chỉ cần nạp tiền chạy ads là xong việc. Giờ mới thấm: nếu không tự biết cách làm video để người ta tin, thì có bao nhiêu tiền vốn cũng không bù nổi chi phí.",
                "intent": "Chạm vào Tầng 3 Sự Thật: Giác ngộ sâu sắc — Nếu không tự tạo niềm tin bằng video, vốn bao nhiêu cũng hết.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng (Tight Side Profile)", "angle": "Góc nghiêng 90° bắt sáng xiên cửa sổ", "motion": "Arc shot xoay nhẹ góc nhìn", "comp": "Gương mặt nhìn chăm chú về hướng bảng bài giảng", "note": "Khoảnh khắc trầm ngâm lắng đọng, tiếp thu tư duy mới về xây dựng nội dung."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Cận cảnh ánh mắt giác ngộ (Insight Close-Up)", "angle": "Góc 3/4 trực diện", "motion": "Push-in chậm chắt lọc cảm xúc", "comp": "Đôi mắt sáng lên khi hiểu ra nút thắt của vấn đề", "note": "Nhận ra cốt lõi: Khách hàng mua vì niềm tin vào con người chứ không phải quảng cáo ép mua."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh chuẩn bị tư thế (Medium Setup)", "angle": "Góc ngang tầm mắt", "motion": "Cầm máy điện thoại giơ lên trước ngực", "comp": "Màn hình camera trước mở sẵn, khung hình selfie", "note": "Chủ động giơ máy lên ngang tầm mắt, chuẩn bị bước vào cảnh tuyên bố dứt khoát."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Cầm máy ngang tầm mắt, nói dứt khoát vào camera",
                "voiceover": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi.",
                "intent": "Kêu gọi hành động mạnh mẽ: Tự tin xuất hiện trước ống kính để làm chủ kênh bán hàng.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc không rung lắc", "comp": "Center Framing 1-1 cân đối", "note": "Nhìn thẳng vào ống kính máy quay, phong thái tự tin và quyết đoán."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh truyền cảm hứng (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10% tạo lực nhấn", "comp": "Năng lượng mạnh mẽ, gương mặt sáng rõ", "note": "Nói dứt khoát câu tuyên ngôn: 'Phải tự học cách xuất hiện trước khách hàng thôi'."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Call-To-Action & Tên kênh", "note": "Ánh mắt ấm áp, mỉm cười nhẹ đầy bản lĩnh trước khi chuyển cảnh kết thúc."}
                ]
            }
        ]
    },
    {
        "id": "kb05",
        "num": 5,
        "slug": "kich_ban_05_het_khach_tu_moi_quan_he_quen",
        "file_name": "kich_ban_05_het_khach_tu_moi_quan_he_quen.html",
        "title": "Hết Khách Từ Mối Quan Hệ Quen",
        "tag": "LÀM TỰ DO & TƯ VẤN",
        "category": "Tự Do & Dịch Vụ Tư Vấn",
        "badge_color": "#a855f7",
        "target_audience": "Freelancer, chuyên viên tư vấn, người làm dịch vụ cạn mối quen",
        "context_desc": "Bối cảnh: Phòng học / Danh bạ Zalo • Chạm vào: Cạn nguồn khách giới thiệu",
        "takeaway": "Bóc trần sự thụ động khi chỉ sống nhờ vào mối quan hệ quen và áp lực phải tự tìm khách lạ.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Tôi đi học để mở rộng tệp khách hàng tiềm năng trên không gian số."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Lướt danh bạ Zalo tính nhắn tin hỏi thăm mối quen mà ngại, sợ người ta nghĩ mình ế việc."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Mấy năm trước sống khỏe nhờ người quen mách nước. Giờ mối quen cạn dần mới hiểu: không tiếp cận được khách lạ thì tháng tới hết việc."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Ngón tay lướt danh bạ Zalo rồi dừng lại không bấm",
                "voiceover": "Ngồi trong lớp, tôi vừa mở danh bạ tính nhắn tin cho vài người quen...",
                "intent": "Chạm đúng tâm lý e ngại: Muốn nhắn tin tìm việc nhưng sợ bị đánh giá là ế ẩm.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh màn hình Zalo (Close-Up)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét danh sách tin nhắn cũ", "comp": "Màn hình danh bạ Zalo chia đôi với bàn tay", "note": "Ngón tay lướt qua danh sách tên các khách hàng cũ từng làm việc."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả ngón tay ngập ngừng (Extreme Close-Up)", "angle": "Góc 60° từ trên xuống", "motion": "Push-in chậm vào khung soạn tin nhắn trống", "comp": "Con trỏ nhấp nháy trên khung chat rỗng", "note": "Ngón tay dừng lại trên bàn phím ảo, không bấm gửi vì cảm giác tự ái ngượng ngùng."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh rút tay (Close-Up Release)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ theo hướng rút tay", "comp": "Bàn tay buông khỏi màn hình điện thoại", "note": "Rút tay lại, chuẩn bị cho động tác úp máy xuống bàn ở Cảnh 2."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Đặt điện thoại úp xuống bàn học, thở dài nhẹ",
                "voiceover": "...Xong lại thôi, vì ngại người ta nghĩ mình dạo này ế việc đi nhờ vả.",
                "intent": "Phơi bày sự giằng xé nội tâm: Tự ái của người làm nghề khi công việc bắt đầu cạn nguồn.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh (Medium Shot)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Trôi nhẹ ngang (Drift)", "comp": "Nhân vật ngồi thẳng lưng giữa phòng học", "note": "Động tác đặt dứt khoát chiếc điện thoại úp mặt xuống bàn gỗ."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận biểu cảm (Medium Close-Up)", "angle": "Góc nghiêng 3/4 khuôn mặt", "motion": "Handheld nhịp thở nhẹ", "comp": "Bờ vai hơi chùng xuống, tiếng thở dài nhẹ", "note": "Nét mặt thoáng vẻ tự trào và bế tắc trước thực tế cạn nguồn khách quen."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh bàn tay mở sổ (Desk Action)", "angle": "Góc hếch nhẹ từ dưới lên", "motion": "Push-in vào cuốn sổ tay lịch hẹn", "comp": "Bàn tay lật sang một trang sổ mới", "note": "Tay đưa sang lật trang sổ tay làm mồi nối trực tiếp sang Cảnh 3."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Bàn tay lật sang trang sổ trắng tinh chưa có lịch hẹn",
                "voiceover": "Trước giờ tôi toàn sống nhờ mối quen giới thiệu. Đến khi việc ít dần mới nhận ra: không tự tìm được khách lạ thì công việc bấp bênh vô cùng.",
                "intent": "Bóc trần Tầng 2 Sự Thật: Nghịch lý sống nhờ giới thiệu — khi mối quen cạn thì công việc đóng băng.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Cận cảnh trang sổ trống (Close-Up Desk)", "angle": "Trực diện 90° từ trên xuống", "motion": "Push-in từ từ", "comp": "Trang sổ lịch làm việc tuần tới hoàn toàn để trống", "note": "Hình ảnh trang giấy trắng tinh không có lịch hẹn khách hàng tạo ấn tượng thị giác mạnh."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Đặc tả bàn tay miết mép sổ (Extreme Close-Up)", "angle": "Góc nghiêng 45°", "motion": "Máy tĩnh bắt trọn từng nếp giấy", "comp": "Ngón tay miết nhẹ dọc mép trang giấy trắng", "note": "Cảm giác bất an và chông chênh khi nhận ra mô hình kinh doanh quá phụ thuộc mối quen."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận ngẩng đầu (Medium Lift)", "angle": "Góc trực diện hơi thấp", "motion": "Tilt-up từ trang sổ lên ánh mắt", "comp": "Ánh mắt dời khỏi trang sổ nhìn về phía máy chiếu", "note": "Ngẩng cao đầu hướng mắt lên màn hình máy chiếu phòng học ở Cảnh 4."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Nhìn lên màn hình máy chiếu phòng học, vẻ tập trung",
                "voiceover": "Hôm nay ngồi đây học làm video, không phải để làm người nổi tiếng, mà là để khách lạ nhìn thấy năng lực của mình mà tự tìm đến.",
                "intent": "Chạm vào Tầng 3 Sự Thật: Làm video không phải để nổi tiếng hão, mà để khách lạ tin tưởng năng lực.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng màn chiếu (Side Profile)", "angle": "Góc nghiêng 90° phản chiếu ánh sáng slide", "motion": "Arc shot xoay nhẹ góc nhìn", "comp": "Gương mặt đón nhận luồng sáng bài giảng", "note": "Không khí tập trung cao độ, tiếp thu phương pháp xây kênh tiếp cận khách hàng lạ."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Cận cảnh ánh mắt thấu suốt (Insight Close-Up)", "angle": "Góc 3/4 trực diện", "motion": "Push-in chậm chắt lọc cảm xúc", "comp": "Đôi mắt kiên định, xóa bỏ hoàn toàn sự ngại ngùng", "note": "Nhận ra chân lý: Video là cầu nối tự động giúp khách lạ hiểu và tin mình trước khi gặp."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh sẵn sàng (Medium Action Setup)", "angle": "Góc ngang tầm mắt", "motion": "Xoay người trực diện camera", "comp": "Tư thế ngồi thẳng thắn, biểu cảm chủ động", "note": "Xoay người sang góc chính diện, chuẩn bị truyền tải thông điệp kết nối ở Cảnh 5."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Nhìn thẳng camera nói điềm đạm",
                "voiceover": "Chủ động xuất hiện để tìm việc, còn hơn ngồi chờ sự giúp đỡ từ người khác.",
                "intent": "Đúc kết thông điệp cốt lõi: Chủ động tạo cơ hội cho mình thay vì chờ đợi mối quan hệ quen ban ơn.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Ánh mắt điềm tĩnh, ấm áp nhưng tràn đầy sự chủ động và tự chủ."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh đĩnh đạc (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Gương mặt toát lên sự đĩnh đạc của người có chuyên môn", "note": "Nói rõ từng chữ: 'Chủ động xuất hiện để tìm việc, còn hơn ngồi chờ sự giúp đỡ'."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Brand Tag", "note": "Nụ cười tự tin và cái gật đầu dứt khoát kết lại toàn bộ hành trình tâm lý."}
                ]
            }
        ]
    },
    {
        "id": "kb06",
        "num": 6,
        "slug": "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach",
        "file_name": "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach.html",
        "title": "Tay Nghề Tốt Nhưng Vẫn Vắng Khách",
        "tag": "THỢ & NGHỀ KỸ THUẬT",
        "category": "Tay Nghề & Kỹ Thuật Chuyên Môn",
        "badge_color": "#f97316",
        "target_audience": "Thợ thủ công, kỹ sư, chuyên gia giỏi nghề nhưng ngại làm truyền thông",
        "context_desc": "Bối cảnh: Phòng học / Sách kỹ thuật • Chạm vào: Tự ái của người làm nghề",
        "takeaway": "Đập tan định kiến bảo thủ của thợ lành nghề: làm tốt mà không truyền thông thì tự đánh mất khách.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Hữu xạ tự nhiên hương, cứ làm thật tốt thì khách hàng sẽ tự tìm đến."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Thấy người ta làm nghề bình thường mà lên mạng nói hay nên đông khách, thấy khó chịu trong lòng."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Cứ ôm cái tự ái chê người khác làm màu. Nhưng sự thật là mình vừa lười vừa ngại xuất hiện, để rồi khách tốt rơi hết vào tay người biết làm video."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Bàn tay lật cuốn tài liệu kỹ thuật trên bàn học",
                "voiceover": "Tôi làm nghề cả chục năm nay, tay nghề không thua kém ai...",
                "intent": "Thiết lập vị thế chuyên gia: Tự tin vào tay nghề nhiều năm kinh nghiệm tích lũy.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh cuốn tài liệu kỹ thuật (Close-Up)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét trang sách kỹ thuật", "comp": "Cuốn sổ tay dày cộp với các sơ đồ bản vẽ", "note": "Bàn tay phong sương của người làm nghề cẩn thận lật từng trang tài liệu."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả ngón tay chỉ bản vẽ (Extreme Close-Up)", "angle": "Góc 60° từ trên xuống", "motion": "Push-in chậm theo ngón tay", "comp": "Đầu ngón tay dừng lại tại một sơ đồ phức tạp", "note": "Minh chứng cho năng lực thực tế: Sự hiểu biết sâu sắc về mặt chuyên môn."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh gấp nhẹ mép sách (Close-Up)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ sang bàn tay cầm bút", "comp": "Cây bút kim loại gõ nhẹ lên mặt bàn", "note": "Cây bút gõ nhẹ lên bàn tạo âm thanh ngắt nhịp chuyển sang Cảnh 2."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Ngồi nhìn quanh lớp học, tay cầm bút gõ nhẹ bàn",
                "voiceover": "...Trước đây tôi luôn nghĩ: cứ làm tốt đi rồi khách tự tìm đến, cần gì lên mạng làm màu.",
                "intent": "Bóc trần định kiến bảo thủ thâm căn cố đế: 'Hữu xạ tự nhiên hương, chê người làm video là làm màu'.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh (Medium Shot)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Trôi nhẹ sang ngang", "comp": "Nhân vật ngồi tựa lưng nhẹ, vẻ mặt có chút tự phụ", "note": "Thể hiện cái tôi của người giỏi nghề, từng cho rằng chất lượng tự nó sẽ bán được."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận góc nghiêng (Medium Side)", "angle": "Góc nghiêng 30°", "motion": "Handheld nhịp thở nhẹ", "comp": "Bàn tay xoay nhẹ cây bút trên mặt bàn gỗ", "note": "Cử chỉ xoay bút thể hiện sự kiên định với quan điểm cũ trước khi bị lung lay."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh với lấy điện thoại (Reach Shot)", "angle": "Góc hếch nhẹ từ dưới lên", "motion": "Push-in vào chiếc smartphone bên cạnh", "comp": "Bàn tay với lấy điện thoại đang sáng màn hình", "note": "Cầm điện thoại lên để xem các video của đối thủ cùng ngành ở Cảnh 3."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Điện thoại mở một video của người cùng ngành nhiều view",
                "voiceover": "Cho đến khi thấy người khác tay nghề bình thường nhưng biết làm video nên khách nườm nượp, tôi mới nhận ra mình sai.",
                "intent": "Cú sốc thực tế: Chứng kiến người tay nghề bình thường lại đông khách nhờ biết truyền thông.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Đặc tả màn hình video triệu view (UI POV)", "angle": "Trực diện 90° vào màn hình", "motion": "Push-in từ từ", "comp": "Video của đối thủ với hàng trăm nghìn tim và bình luận hỏi mua", "note": "Hình ảnh trực quan về một video ngành có lượt tương tác khổng lồ đập vào mắt."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Cận cảnh ánh mắt thẫn thờ (Shock Close-Up)", "angle": "Góc trực diện hơi thấp", "motion": "Máy tĩnh ngột ngạt", "comp": "Khuôn mặt nhíu mày, nét khó chịu chuyển dần sang suy ngẫm", "note": "Khắc họa sự đấu tranh nội tâm giữa cái tôi tự ái và sự thật thị trường."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận nghiêng (Medium Close-Up)", "angle": "Góc nghiêng cạnh bàn", "motion": "Pan êm từ điện thoại sang cuốn sổ", "comp": "Hạ máy xuống bàn, mở trang sổ ghi chép", "note": "Quyết định buông bỏ tự ái, cầm bút bắt đầu ghi chép bài học Cảnh 4."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Nhìn thẳng vào cuốn sổ ghi chép, vẻ nghiêm túc",
                "voiceover": "Sự thật là tôi đang tự ái và lười thay đổi. Mình làm tốt mà không chịu nói cho người ta biết, thì trách ai được khi khách chọn người khác.",
                "intent": "Bóc trần Tầng 3 Sự Thật: Dũng cảm thừa nhận mình vừa lười vừa tự ái, không thể trách khách hàng.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng sổ ghi chép (Side Profile)", "angle": "Góc nghiêng 90°", "motion": "Arc shot xoay nhẹ góc nhìn", "comp": "Khuôn mặt chăm chú nhìn vào từng dòng ghi chép", "note": "Sự nghiêm túc của một người thợ lành nghề khi bắt đầu học kỹ năng mới."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Đặc tả dòng chữ 'Kể câu chuyện làm nghề' (Note ECU)", "angle": "Góc 45° từ trên xuống", "motion": "Push-in chậm nhấn mạnh ngòi bút", "comp": "Ngòi bút nắn nót ghi lại phương pháp truyền thông", "note": "Hành động ghi chép đánh dấu bước ngoặt thay đổi hoàn toàn về tư duy."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh đặt bút (Medium Setup)", "angle": "Góc ngang tầm mắt", "motion": "Đặt bút xuống bàn, ngẩng mặt lên", "comp": "Tư thế ngồi thẳng, ánh mắt kiên định hướng về camera", "note": "Đặt bút xuống dứt khoát, sẵn sàng chia sẻ bài học ở Cảnh 5."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Nhìn thẳng vào máy, nói dứt khoát",
                "voiceover": "Bỏ cái tôi xuống, làm nghề giỏi thì càng phải biết cách kể cho khách hàng hiểu.",
                "intent": "Thông điệp đắt giá cho người làm nghề: Giỏi chuyên môn + Biết truyền thông = Độc tôn thị trường.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Ánh mắt mạnh mẽ của một người thợ bản lĩnh đã vượt qua cái tôi cá nhân."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh truyền cảm (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Năng lượng tự tin, chân thành", "note": "Nói dứt khoát: 'Bỏ cái tôi xuống, làm nghề giỏi thì càng phải biết cách kể'."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Brand Tag", "note": "Mỉm cười nhẹ đầy tự hào về nghề nghiệp của mình."}
                ]
            }
        ]
    },
    {
        "id": "kb07",
        "num": 7,
        "slug": "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc",
        "file_name": "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc.html",
        "title": "Bị Cạnh Tranh Bởi Tổng Kho & Giá Gốc",
        "tag": "ĐẠI LÝ BÁN LẺ",
        "category": "Đại Lý & Chuỗi Phân Phối",
        "badge_color": "#ef4444",
        "target_audience": "Chủ đại lý phân phối, cửa hàng bán lẻ bị tổng kho bán phá giá",
        "context_desc": "Bối cảnh: Phòng học / Livestream • Chạm vào: Nguy cơ mất đất sống của trung gian",
        "takeaway": "Nhấn mạnh việc xây dựng uy tín cá nhân khi thị trường bán lẻ bị cạnh tranh gay gắt bởi tổng kho xả hàng.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Xây dựng kênh truyền thông để tăng độ nhận diện cho đại lý phân phối."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Thấy tổng kho và xưởng tự lên mạng bán thẳng giá rẻ, thấy bất lực vì không cạnh tranh nổi về giá."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Trước đây chỉ quen ăn chênh lệch giá. Giờ nếu khách không mua vì tin con người mình thì đại lý của mình sớm muộn cũng bị xóa sổ."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Màn hình điện thoại hiển thị livestream bán hàng xả kho",
                "voiceover": "Nhìn các tổng kho tự lên livestream bán giá gốc...",
                "intent": "Cú sốc thị trường: Tổng kho và xưởng sản xuất tự livestream bán lẻ giá tận gốc.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh màn hình livestream TikTok/Shopee", "angle": "Trực diện 90° vào màn hình", "motion": "Push-in từ từ", "comp": "Màn hình livestream với giá xả kho giảm 70% và rổ hàng nhảy liên tục", "note": "Hình ảnh các phiên live xả kho quy mô lớn tạo áp lực đè nặng lên các khâu trung gian."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả ngón tay lướt qua mức giá rẻ sốc (ECU)", "angle": "Góc nghiêng 45°", "motion": "Máy tĩnh bắt trọn mức giá", "comp": "Mức giá gốc thấp hơn cả giá nhập sỉ của đại lý", "note": "Sự chênh lệch giá không thể tưởng tượng khiến người bán lẻ bất lực."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh bàn tay chống cằm (Close-Up Lift)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ sang tư thế người ngồi", "comp": "Bàn tay chống cằm, ánh mắt nhìn trân trối", "note": "Chuyển dần góc nhìn từ màn hình sang sự bế tắc của nhân vật ở Cảnh 2."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Đang ngồi ở bàn học, chống tay nhìn điện thoại",
                "voiceover": "...Tôi biết cách bán hàng trung gian ăn chênh lệch giá sắp hết thời rồi.",
                "intent": "Thừa nhận sự thật nghiệt ngã: Kỷ nguyên làm đại lý chỉ ăn chênh lệch giá đã chấm dứt.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh (Medium Shot)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Trôi nhẹ sang ngang", "comp": "Nhân vật ngồi đơn độc bên góc bàn học", "note": "Dáng ngồi trầm tư phản ánh sự biến đổi dữ dội của chuỗi cung ứng hiện đại."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận qua vai (Over-the-Shoulder)", "angle": "Góc qua vai 30°", "motion": "Handheld nhịp thở nhẹ", "comp": "Chiếc điện thoại nhỏ bé đặt cạnh cuốn sổ dày", "note": "Khoảnh khắc giác ngộ: Không thể tiếp tục cạnh tranh theo lối mòn cũ."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh cầm bút ghi chép (Action Shot)", "angle": "Góc hếch nhẹ", "motion": "Push-in vào ngòi bút", "comp": "Ngòi bút chuẩn bị hạ xuống mặt giấy", "note": "Bắt đầu cầm bút viết để tìm kiếm lối thoát mới ở Cảnh 3."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Bàn tay ghi dòng chữ 'Giá trị cá nhân' vào vở",
                "voiceover": "Khách hàng bây giờ chỉ cần một nút bấm là mua được tận xưởng, mình không thể đua giảm giá mãi với họ được.",
                "intent": "Bóc trần Tầng 2 Sự Thật: Đua giảm giá với tổng kho là tự sát — Lối thoát duy nhất là Giá Trị Cá Nhân.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Cận cảnh nét chữ trên sổ (Close-Up Note)", "angle": "Trực diện 90° từ trên xuống", "motion": "Push-in chậm theo nét mực", "comp": "Dòng chữ 'GIÁ TRỊ CÁ NHÂN & DỊCH VỤ' nổi bật trên trang giấy", "note": "Nét bút nắn nót ghi lại định hướng sống còn cho đại lý bán lẻ."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Đặc tả ngòi bút gạch chân 2 đường (ECU)", "angle": "Góc nghiêng 45°", "motion": "Máy tĩnh bắt trọn đường gạch dứt khoát", "comp": "Hai đường gạch chân đè đậm dưới chữ 'Giá trị cá nhân'", "note": "Hành động thể hiện sự kiên định: Phải trở thành chuyên gia tư vấn mà khách tin tưởng."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận ngẩng đầu nhìn lớp học", "angle": "Góc trực diện hơi thấp", "motion": "Tilt-up từ trang sổ lên khuôn mặt", "comp": "Ánh mắt sáng rõ, không còn vẻ hoang mang", "note": "Ngẩng đầu nhìn quanh không gian lớp học ở Cảnh 4."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Nhìn ra không gian lớp học, suy ngẫm",
                "voiceover": "Hôm nay ngồi đây học, tôi hiểu ra: nếu khách không mua vì tin tưởng con người mình, thì cửa hàng của mình không còn lý do gì để tồn tại.",
                "intent": "Chạm vào Tầng 3 Sự Thật: Nếu khách chỉ mua vì giá rẻ thì đại lý sẽ bị xóa sổ — Phải để khách mua vì TIN CON NGƯỜI MÌNH.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng suy tư (Side Profile)", "angle": "Góc nghiêng 90°", "motion": "Arc shot xoay nhẹ góc nhìn", "comp": "Khuôn mặt đón nhận ánh sáng ấm áp", "note": "Nhìn thấu quy luật sinh tồn mới của ngành bán lẻ hiện đại."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Cận cảnh ánh mắt thấu hiểu (Insight Close-Up)", "angle": "Góc 3/4 trực diện", "motion": "Push-in chậm chắt lọc cảm xúc", "comp": "Ánh mắt kiên định và đầy chiều sâu", "note": "Khách hàng sẵn sàng trả thêm tiền để nhận được sự tư vấn am hiểu và hậu mãi tận tâm."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh chuyển mình (Medium Shift)", "angle": "Góc ngang tầm mắt", "motion": "Xoay người thẳng về hướng ống kính", "comp": "Tư thế đĩnh đạc của một người làm chủ", "note": "Chuyển tư thế sẵn sàng cho phát biểu đúc kết ở Cảnh 5."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Nhìn vào camera, nói điềm đạm",
                "voiceover": "Không cạnh tranh được bằng giá rẻ, thì phải cạnh tranh bằng sự am hiểu và tận tâm của chính mình.",
                "intent": "Vũ khí cạnh tranh tối thượng: Sự am hiểu chuyên sâu và thái độ tận tâm của người bán hàng.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Nhìn thẳng vào ống kính máy quay với phong thái vững vàng, chân thành."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh khẳng định (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Gương mặt toát lên uy tín và sự tận tâm", "note": "Khẳng định: 'Cạnh tranh bằng sự am hiểu và tận tâm của chính mình'."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Brand Tag & Địa chỉ cửa hàng", "note": "Nụ cười ấm áp tạo niềm tin tuyệt đối cho khách hàng."}
                ]
            }
        ]
    },
    {
        "id": "kb08",
        "num": 8,
        "slug": "kich_ban_08_bat_dau_lai_tu_con_so_0",
        "file_name": "kich_ban_08_bat_dau_lai_tu_con_so_0.html",
        "title": "Bắt Đầu Lại Từ Con Số 0",
        "tag": "CHUYỂN NGHỀ & LÀM LẠI",
        "category": "Chuyển Nghề & Tái Khởi Nghiệp",
        "badge_color": "#10b981",
        "target_audience": "Người bỏ việc cũ chuyển ngành, người khởi nghiệp lại từ đầu",
        "context_desc": "Bối cảnh: Phòng học / Sổ mới • Chạm vào: Nỗi bất an tài chính & sợ bàn tán",
        "takeaway": "Phơi bày nỗi bất an tài chính và sự e ngại ánh nhìn của người quen khi khởi đầu một công việc mới.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Dám bước ra khỏi vùng an toàn để theo đuổi mục tiêu mới của bản thân."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Nghỉ công việc cũ rồi, làm cái mới nhưng không dám đăng lên trang cá nhân vì sợ người quen hỏi han."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Tiền dự phòng vơi dần từng ngày trong khi dự án mới chưa ra đâu vào đâu. Sợ nhất thất bại thì không biết giấu mặt vào đâu."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Bàn tay mở cuốn sổ tay sang một trang giấy mới",
                "voiceover": "Rời công việc quen thuộc sau nhiều năm để bắt đầu lại từ con số 0...",
                "intent": "Mở đầu lắng đọng: Cảm giác chênh vênh khi bước chân vào một hành trình hoàn toàn mới mẻ.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh mở trang sổ mới tinh (Close-Up)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét trang giấy trắng", "comp": "Cuốn sổ da mới đặt giữa bàn học", "note": "Bàn tay chậm rãi lật mở một trang giấy trắng tinh khôi, tượng trưng cho khởi đầu từ số 0."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả ngón tay vuốt phẳng trang giấy (ECU)", "angle": "Góc 60° từ trên xuống", "motion": "Push-in chậm dồn vào mép giấy", "comp": "Bàn tay vuốt phẳng từng thớ giấy mộc", "note": "Cử chỉ nâng niu và thận trọng, chất chứa bao kỳ vọng lẫn lo âu."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh đặt tay lên cốc nước (Action Shot)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ sang cốc nước", "comp": "Bàn tay với lấy cốc nước lọc trên bàn", "note": "Đưa tay cầm cốc nước lên uống một ngụm ở Cảnh 2."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Cầm cốc nước uống một ngụm, nhìn quanh phòng học",
                "voiceover": "...Nhiều người bảo tôi dũng cảm, nhưng thật ra trong lòng đang rất lo.",
                "intent": "Bóc trần lớp vỏ 'dũng cảm': Đằng sau danh xưng bước ra khỏi vùng an toàn là nỗi lo thắt ruột.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh (Medium Shot)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Trôi nhẹ sang ngang", "comp": "Nhân vật nâng cốc nước uống chậm rãi giữa lớp học", "note": "Uống một ngụm nước để trấn tĩnh tâm trạng lo âu ngấm ngầm."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận ánh mắt nhìn quanh (Medium Close-Up)", "angle": "Góc nghiêng 3/4", "motion": "Handheld nhịp thở nhẹ", "comp": "Ánh mắt nhìn lướt qua các học viên trẻ trung xung quanh", "note": "Cảm giác có chút lạc lõng và áp lực khi phải bắt đầu lại từ vạch xuất phát."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh đặt cốc nước xuống (Desk Return)", "angle": "Góc hếch nhẹ", "motion": "Push-in vào cây bút trên bàn", "comp": "Đặt cốc nước xuống, tay cầm lấy cây bút", "note": "Cầm bút chuẩn bị viết dòng chữ mục tiêu ở Cảnh 3."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Bút gạch chân dòng chữ 'Bắt đầu kênh mới'",
                "voiceover": "Tiền tiết kiệm thì vơi dần, dự án mới thì chưa đâu vào đâu. Đến cái việc đăng bài lên trang cá nhân tôi còn không dám vì sợ người quen bàn tán.",
                "intent": "Bóc trần Tầng 2 Sự Thật: Tiền dự phòng vơi dần + Sợ người quen bàn tán xì xào.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Cận cảnh dòng chữ 'Bắt đầu kênh mới' (Note ECU)", "angle": "Trực diện 90° từ trên xuống", "motion": "Push-in chậm theo ngòi bút", "comp": "Dòng chữ 'BẮT ĐẦU KÊNH MỚI' được viết nắn nót", "note": "Dòng chữ thể hiện quyết định bước ra ánh sáng của người làm lại từ đầu."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Đặc tả nét gạch chân kép (Extreme Close-Up)", "angle": "Góc nghiêng 45°", "motion": "Máy tĩnh bắt trọn lực nhấn ngòi bút", "comp": "Hai đường gạch chân đậm nét đè dưới dòng chữ", "note": "Khắc họa tâm lý sợ người quen đánh giá nhưng vẫn quyết tâm phải làm."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận ngẩng mặt suy tư", "angle": "Góc trực diện hơi thấp", "motion": "Tilt-up hướng lên bảng giảng bài", "comp": "Ánh mắt ánh lên tia nhìn kiên định", "note": "Dứt khoát ngẩng đầu nhìn về phía trước ở Cảnh 4."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Nhìn về phía bảng giảng bài, ánh mắt kiên định hơn",
                "voiceover": "Nhưng ngồi nghĩ mãi thì tiền không tự sinh ra. Sợ người khác đánh giá không giúp mình trả được chi phí hàng tháng.",
                "intent": "Chạm vào Tầng 3 Sự Thật: Sự thật trần trụi — Sợ người khác bàn tán không giúp mình trả được hóa đơn.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng đón nắng (Side Profile)", "angle": "Góc nghiêng 90°", "motion": "Arc shot xoay nhẹ góc nhìn", "comp": "Gương mặt sáng rõ với đường nét cương nghị", "note": "Xua tan mọi nỗi e ngại vô bổ của dư luận xung quanh."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Cận cảnh ánh mắt rực lửa (Conviction Eye Close-Up)", "angle": "Góc 3/4 trực diện", "motion": "Push-in chậm chắt lọc năng lượng", "comp": "Đôi mắt bừng sáng ý chí tự thân vận động", "note": "Nhận thức rõ ràng: Chỉ có hành động thật mới giải quyết được bài toán sinh tồn."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh tư thế sẵn sàng (Medium Action Setup)", "angle": "Góc ngang tầm mắt", "motion": "Cầm máy điện thoại giơ ngang mặt", "comp": "Khung hình cân đối sẵn sàng ghi hình", "note": "Cầm máy lên đối diện thẳng thắn với ống kính ở Cảnh 5."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Cầm máy ngang tầm mắt, nói dứt khoát",
                "voiceover": "Đã chọn đi đường mới thì phải dám đối mặt, làm từ việc nhỏ nhất để nuôi sống lựa chọn của mình.",
                "intent": "Lời tuyên thệ tự thân: Dám chọn, dám đối mặt, làm từ việc nhỏ nhất để nuôi sống ước mơ.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Giao tiếp mắt kiên định, không né tránh bất kỳ ánh nhìn nào."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh truyền cảm hứng mạnh mẽ (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Năng lượng tích cực, gương mặt bừng sáng", "note": "Nói rõ từng chữ: 'Làm từ việc nhỏ nhất để nuôi sống lựa chọn của mình'."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Brand Tag", "note": "Nụ cười tự tin và cái gật đầu khẳng định tương lai tươi sáng."}
                ]
            }
        ]
    },
    {
        "id": "kb09",
        "num": 9,
        "slug": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia",
        "file_name": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html",
        "title": "Hàng Làm Kỹ Nhưng Bị So Sánh Giá",
        "tag": "SẢN PHẨM LÀM KỸ",
        "category": "Sản Phẩm & Nghệ Nhân Tận Tâm",
        "badge_color": "#ec4899",
        "target_audience": "Người làm sản phẩm kỹ, hàng thủ công/chất lượng cao bị so giá với hàng chợ",
        "context_desc": "Bối cảnh: Phòng học / Mẫu sản phẩm • Chạm vào: Mâu thuẫn giữa chất lượng & giá rẻ",
        "takeaway": "Biến sự bức xúc khi bị so sánh giá thành hành động quay lại quy trình làm thật để chứng minh giá trị sản phẩm.",
        "tiers": [
            {"tier": 1, "badge": "Tầng 1: Đãi bôi", "content": "Kiên định với chất lượng thật, chỉ bán sản phẩm an toàn và nguồn gốc rõ ràng."},
            {"tier": 2, "badge": "Tầng 2: Cảm giác thật", "content": "Mỗi lần báo giá xong khách im lặng hoặc so sánh với hàng trôi nổi giá rẻ, thấy vừa hụt hẫng vừa bực mình."},
            {"tier": 3, "badge": "Tầng 3: Ngượng miệng", "content": "Từng nghĩ hay là giảm bớt chất lượng đi cho dễ bán. Nhưng làm thế cắn rứt lương tâm, mà giữ chất lượng thì không biết giải thích sao cho khách hiểu."}
        ],
        "scenes": [
            {
                "scene_id": 1, "time_range": "00:00 - 00:03", "duration": "3s", "start_sec": 0, "end_sec": 3,
                "main_shot_type": "Đặc tả (Extreme Close-Up)",
                "title": "Bàn tay xoay nhẹ một hộp sản phẩm nhỏ mang theo trên bàn học",
                "voiceover": "Làm ra một món đồ kỹ lưỡng, nguyên liệu chọn lọc từng chút một...",
                "intent": "Mở đầu tinh tế: Thể hiện sự nâng niu và tâm huyết dành cho sản phẩm làm kỹ.",
                "beats": [
                    {"id": "1.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "0.0s - 1.0s", "shot": "Cận cảnh hộp sản phẩm mẫu (Product Close-Up)", "angle": "Góc nghiêng 45° từ trên xuống", "motion": "Máy tĩnh bắt nét chất liệu bao bì cao cấp", "comp": "Mẫu sản phẩm nhỏ tinh xảo đặt trên mặt bàn gỗ", "note": "Bàn tay nâng niu chạm vào từng đường nét sắc sảo của bao bì sản phẩm."},
                    {"id": "1.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "1.0s - 2.2s", "shot": "Đặc tả xoay nhẹ góc sản phẩm (Product ECU)", "angle": "Góc nhìn 60° từ trên xuống", "motion": "Push-in chậm theo vòng xoay", "comp": "Ánh sáng xiên rọi rõ vân bề mặt sản phẩm", "note": "Hành động xoay nhẹ sản phẩm làm nổi bật chất lượng hoàn thiện tỉ mỉ."},
                    {"id": "1.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "2.2s - 3.0s", "shot": "Cận cảnh đặt sản phẩm xuống bàn (Desk Rest)", "angle": "Góc ngang mặt bàn", "motion": "Tilt-up nhẹ sang bàn tay buông lơi", "comp": "Sản phẩm đứng vững chãi, bàn tay rút lại", "note": "Rút tay lại và tựa người ra sau ghế ở Cảnh 2."}
                ]
            },
            {
                "scene_id": 2, "time_range": "00:03 - 00:07", "duration": "4s", "start_sec": 3, "end_sec": 7,
                "main_shot_type": "Trung cảnh (Medium Shot)",
                "title": "Ngồi tựa lưng vào ghế, thở dài nhìn xuống bàn",
                "voiceover": "...Nhưng cứ báo giá là khách lại hỏi: 'Sao chỗ kia bán rẻ bằng nửa chỗ em?'.",
                "intent": "Nỗi đau bị so sánh giá: Cảm giác hụt hẫng và bất lực khi khách đem hàng chợ ra ép giá.",
                "beats": [
                    {"id": "2.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "3.0s - 4.5s", "shot": "Trung cảnh (Medium Shot)", "angle": "Ngang tầm mắt (Eye Level)", "motion": "Trôi nhẹ sang ngang", "comp": "Nhân vật tựa lưng vào ghế, vẻ mặt thoáng buồn", "note": "Nét mặt trĩu nặng khi nhớ lại những lần bị khách chê đắt so với hàng dạt."},
                    {"id": "2.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "4.5s - 6.0s", "shot": "Trung cận qua vai (Over-the-Shoulder)", "angle": "Góc qua vai 30°", "motion": "Handheld nhịp thở nhẹ", "comp": "Chiếc điện thoại đang mở đoạn chat khách hàng im lặng", "note": "Khắc họa cảm giác nghẹn đắng khi công sức chăm chút bị đánh đồng với hàng xả."},
                    {"id": "2.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "6.0s - 7.0s", "shot": "Cận cảnh ngón tay lướt màn hình chat", "angle": "Góc hếch nhẹ", "motion": "Push-in vào dòng tin nhắn", "comp": "Dòng tin nhắn 'Sao bên kia bán có nửa giá?'", "note": "Phóng to màn hình tin nhắn khách ở Cảnh 3."}
                ]
            },
            {
                "scene_id": 3, "time_range": "00:07 - 00:15", "duration": "8s", "start_sec": 7, "end_sec": 15,
                "main_shot_type": "Cận cảnh (Close-Up)",
                "title": "Màn hình điện thoại hiển thị tin nhắn khách im lặng",
                "voiceover": "Nhiều lúc nản, tôi cũng từng nghĩ hay là bớt chất lượng đi cho dễ bán. Nhưng nghĩ lại thấy không đành lòng.",
                "intent": "Bóc trần Tầng 2 & 3 Sự Thật: Từng có lúc muốn giảm chất lượng để dễ bán nhưng lương tâm không cho phép.",
                "beats": [
                    {"id": "3.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "7.0s - 9.5s", "shot": "Đặc tả màn hình chat khách im lặng (UI POV)", "angle": "Trực diện 90° vào màn hình", "motion": "Push-in từ từ", "comp": "Dòng trạng thái 'Đã xem' và không có câu trả lời", "note": "Sự im lặng của khách hàng sau khi nhận báo giá là nỗi ám ảnh của người làm đồ kỹ."},
                    {"id": "3.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "9.5s - 12.5s", "shot": "Cận cảnh chân dung giằng xé nội tâm (Facial ECU)", "angle": "Góc trực diện hơi thấp", "motion": "Máy tĩnh ngột ngạt", "comp": "Khuôn mặt đăm chiêu, cái lắc đầu nhẹ", "note": "Khẳng định lập trường đạo đức: Thà bán ít chứ dứt khoát không làm hàng kém chất lượng."},
                    {"id": "3.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "12.5s - 15.0s", "shot": "Trung cận ngẩng đầu nhìn bài giảng", "angle": "Góc nghiêng cạnh bàn", "motion": "Pan êm hướng mắt nhìn lên màn chiếu", "comp": "Ánh mắt chuyển từ bế tắc sang hy vọng", "note": "Ngẩng đầu nhìn lên bài giảng về cách quay video quy trình Cảnh 4."}
                ]
            },
            {
                "scene_id": 4, "time_range": "00:15 - 00:25", "duration": "10s", "start_sec": 15, "end_sec": 25,
                "main_shot_type": "Góc nghiêng (Side Profile)",
                "title": "Nhìn lên bài giảng về cách quay video chi tiết quy trình",
                "voiceover": "Khách chê đắt không phải vì họ tiếc tiền, mà vì mình chỉ biết báo giá chứ chưa từng cho họ thấy cái công mình làm kỹ thế nào.",
                "intent": "Giác ngộ bản chất: Khách chê đắt vì mình chưa chứng minh được công sức và quy trình làm kỹ.",
                "beats": [
                    {"id": "4.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "15.0s - 18.0s", "shot": "Cận góc nghiêng bài giảng quy trình (Side Profile)", "angle": "Góc nghiêng 90°", "motion": "Arc shot xoay nhẹ góc nhìn", "comp": "Slide bài giảng chiếu sơ đồ: 'Show The Process, Not Just The Price'", "note": "Hiểu ra nút thắt: Phải kể câu chuyện công đoạn sản xuất thay vì chỉ gửi bảng giá trơ trọi."},
                    {"id": "4.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "18.0s - 22.0s", "shot": "Cận cảnh ánh mắt thấu suốt (Insight Close-Up)", "angle": "Góc 3/4 trực diện", "motion": "Push-in chậm chắt lọc cảm xúc", "comp": "Đôi mắt sáng ngời niềm tin vào giá trị thật", "note": "Khi khách nhìn thấy từng công đoạn nhặt hạt, kiểm định, họ sẽ tự hiểu vì sao giá xứng đáng."},
                    {"id": "4.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "22.0s - 25.0s", "shot": "Trung cảnh nhấc sản phẩm lên (Product Lift)", "angle": "Góc ngang tầm mắt", "motion": "Cầm hộp sản phẩm giơ ngang trước ngực", "comp": "Mẫu sản phẩm và khuôn mặt cùng chung khung hình", "note": "Cầm sản phẩm tự tin chuẩn bị bước vào cảnh kết thúc ở Cảnh 5."}
                ]
            },
            {
                "scene_id": 5, "time_range": "00:25 - 00:30", "duration": "5s", "start_sec": 25, "end_sec": 30,
                "main_shot_type": "Trực diện (Frontal Shot)",
                "title": "Nhìn thẳng camera nói chân thành",
                "voiceover": "Thay vì ngồi bực mình khi bị so sánh, tôi chọn quay lại từng công đoạn thật để khách tự nhìn thấy giá trị.",
                "intent": "Giải pháp hành động thực chiến: Quay lại toàn bộ quy trình làm thật để giá trị tự lên tiếng.",
                "beats": [
                    {"id": "5.1", "label": "🔰 Đầu cảnh (In-point)", "ts": "25.0s - 26.8s", "shot": "Cận trực diện (Frontal Close-Up)", "angle": "Trực diện ngang tầm mắt", "motion": "Handheld vững chắc", "comp": "Center Framing 1-1", "note": "Nhìn thẳng vào ống kính với nụ cười tự hào và ánh mắt đầy sự tự tin."},
                    {"id": "5.2", "label": "🔥 Chi tiết / Cao trào (Main Action)", "ts": "26.8s - 28.8s", "shot": "Cận cảnh truyền cảm hứng (Conviction Shot)", "angle": "Trực diện hất nhẹ 5°", "motion": "Punch-in nhẹ 10%", "comp": "Gương mặt và sản phẩm cùng tỏa sáng niềm tin", "note": "Khẳng định: 'Tôi chọn quay lại từng công đoạn thật để khách tự nhìn thấy giá trị'."},
                    {"id": "5.3", "label": "🔄 Cuối cảnh / Mồi chuyển (Out-point Lead)", "ts": "28.8s - 30.0s", "shot": "Trung cận kết thúc (Outro Frame)", "angle": "Ngang tầm mắt", "motion": "Tĩnh giữ frame 0.5s", "comp": "Chừa 1/3 dưới cho Brand Tag & Cam kết chất lượng", "note": "Nụ cười rạng rỡ, cái gật đầu chân thành khép lại video đầy thuyết phục."}
                ]
            }
        ]
    }
]

def render_storyboard_html(sb):
    slug = sb["slug"]
    title = sb["title"]
    num = sb["num"]
    tag = sb["tag"]
    cat = sb["category"]
    color = sb["badge_color"]
    desc = sb["context_desc"]
    takeaway = sb["takeaway"]
    tiers = sb["tiers"]
    scenes = sb["scenes"]
    
    raw_script_formatted = f"""KỊCH BẢN 0{num} • {tag}
Tiêu đề: {title}
{desc}

3 TẦNG SỰ THẬT:
• {tiers[0]['badge']}: "{tiers[0]['content']}"
• {tiers[1]['badge']}: "{tiers[1]['content']}"
• {tiers[2]['badge']}: "{tiers[2]['content']}"

5 PHÂN CẢNH QUAY CHI TIẾT (30 GIÂY):
"""
    for sc in scenes:
        raw_script_formatted += f"- Cảnh {sc['scene_id']} ({sc['time_range']}, {sc['duration']}) • [{sc['main_shot_type']}]: {sc['title']}\n  🎙️ Lời thoại: \"{sc['voiceover']}\"\n"
    raw_script_formatted += f"\n💡 ĐIỂM MẤU CHỐT:\n{takeaway}"

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bảng Phân Cảnh Storyboard: Kịch Bản 0{num} • {title} | AI Storyboard Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #0a0e17;
      --bg-surface: #111827;
      --bg-card: #172033;
      --bg-card-hover: #1e2a44;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: {color}88;
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --accent: {color};
      --accent-glow: {color}25;
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
    .top-header {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(10, 14, 23, 0.92);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 24px;
      display: flex; justify-content: space-between; align-items: center; gap: 16px;
    }}
    .brand-group {{ display: flex; align-items: center; gap: 10px; }}
    .brand-badge {{
      background: linear-gradient(135deg, {color}, #2563eb);
      color: #fff; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .header-title {{ font-size: 15px; font-weight: 700; color: var(--text-primary); }}
    .header-controls {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .nav-btn {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); color: var(--text-secondary);
      font-size: 12px; font-weight: 600; padding: 6px 12px; border-radius: var(--radius-sm); text-decoration: none; transition: all 0.2s;
    }}
    .nav-btn:hover {{ background: var(--accent); color: #000; font-weight: 700; }}
    .action-btn {{
      background: linear-gradient(135deg, #f59e0b, #d97706); color: #000; font-weight: 700; border: none;
      padding: 6px 14px; border-radius: var(--radius-sm); cursor: pointer; font-size: 12px;
    }}
    .hub-link {{
      background: rgba(56, 189, 248, 0.15); border: 1px solid var(--cyan); color: var(--cyan);
      font-size: 12px; font-weight: 700; padding: 6px 14px; border-radius: var(--radius-sm); text-decoration: none;
    }}
    .hub-link:hover {{ background: var(--cyan); color: #000; }}
    .container {{ max-width: 1400px; margin: 0 auto; padding: 24px 20px; }}
    
    /* Original Message Box */
    .original-message-box {{
      background: linear-gradient(180deg, #131d2e 0%, #0d1522 100%);
      border: 1px solid rgba(56, 189, 248, 0.25); border-radius: var(--radius-lg); padding: 24px 28px; margin-bottom: 28px;
    }}
    .orig-header {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 18px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); }}
    .orig-title {{ font-size: 16px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 8px; }}
    .orig-badge {{ background: var(--accent-glow); color: var(--accent); font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; border: 1px solid var(--accent); }}
    .orig-content-grid {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 20px; }}
    @media (max-width: 900px) {{ .orig-content-grid {{ grid-template-columns: 1fr; }} }}
    .raw-text-panel {{
      background: #080c14; border: 1px solid rgba(255, 255, 255, 0.06); border-radius: var(--radius-md);
      padding: 16px 18px; font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #e2e8f0; white-space: pre-wrap; line-height: 1.6; max-height: 320px; overflow-y: auto;
    }}
    .ref-gallery {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
    .ref-item {{ background: #080c14; border: 1px solid rgba(255, 255, 255, 0.06); border-radius: var(--radius-md); overflow: hidden; }}
    .ref-thumb-box {{ height: 180px; background: #000; }}
    .ref-thumb-box img {{ width: 100%; height: 100%; object-fit: cover; }}
    .ref-caption {{ padding: 8px 10px; font-size: 11px; }}
    .ref-caption strong {{ color: #fff; display: block; margin-bottom: 2px; }}
    .ref-caption span {{ color: var(--text-muted); font-size: 10px; }}
    
    /* Hero */
    .hero {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 24px 28px; margin-bottom: 28px; }}
    .hero-tags {{ display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }}
    .tag {{ font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; display: inline-flex; align-items: center; gap: 4px; }}
    .tag-cyan {{ background: var(--cyan-glow); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .tag-amber {{ background: var(--amber-glow); color: var(--amber); border: 1px solid rgba(245, 158, 11, 0.3); }}
    .tag-emerald {{ background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3); }}
    .tag-accent {{ background: var(--accent-glow); color: var(--accent); border: 1px solid var(--accent); }}
    .hero h1 {{ font-size: 24px; font-weight: 800; margin-bottom: 8px; color: #fff; line-height: 1.3; }}
    .metrics-bar {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 10px; background: rgba(0, 0, 0, 0.3); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 12px 16px; margin-top: 14px; }}
    .metric-label {{ font-size: 10px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; }}
    .metric-value {{ font-size: 16px; font-weight: 800; color: var(--text-primary); }}
    
    /* 3 Tiers Box */
    .tiers-box {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 28px; }}
    .tier-card {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 16px 18px; }}
    .tier-card.t1 {{ border-left: 4px solid #ef4444; }}
    .tier-card.t2 {{ border-left: 4px solid #f59e0b; }}
    .tier-card.t3 {{ border-left: 4px solid #10b981; }}
    .tier-card-head {{ font-size: 11px; font-weight: 800; text-transform: uppercase; margin-bottom: 6px; }}
    .tier-card.t1 .tier-card-head {{ color: #f87171; }}
    .tier-card.t2 .tier-card-head {{ color: #fbbf24; }}
    .tier-card.t3 .tier-card-head {{ color: #34d399; }}
    .tier-card-content {{ font-size: 13px; color: #e2e8f0; line-height: 1.5; }}
    
    /* Scene Block */
    .scene-block {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 24px 20px; margin-bottom: 30px; scroll-margin-top: 70px; }}
    .scene-header {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; padding-bottom: 14px; border-bottom: 1px solid var(--border-subtle); margin-bottom: 16px; flex-wrap: wrap; }}
    .scene-title-group {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
    .scene-num-badge {{ background: linear-gradient(135deg, var(--accent), #2563eb); color: #fff; font-size: 12px; font-weight: 800; padding: 4px 10px; border-radius: 6px; }}
    .scene-main-title {{ font-size: 17px; font-weight: 800; color: #fff; }}
    .scene-time-badge {{ background: rgba(255, 255, 255, 0.08); color: var(--text-secondary); font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; }}
    .scene-intent-box {{ background: rgba(0, 0, 0, 0.25); border-left: 3px solid var(--accent); padding: 8px 12px; border-radius: 0 6px 6px 0; font-size: 12px; color: var(--text-secondary); margin-bottom: 16px; }}
    .audio-box {{ background: linear-gradient(90deg, rgba(56, 189, 248, 0.08) 0%, rgba(24, 34, 52, 0.4) 100%); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: var(--radius-md); padding: 12px 16px; margin-bottom: 18px; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; }}
    .voice-content {{ display: flex; align-items: center; gap: 10px; flex: 1; }}
    .voice-icon {{ font-size: 18px; background: var(--cyan-glow); width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .voice-text {{ font-size: 13.5px; font-weight: 600; color: #fff; font-style: italic; }}
    
    /* 3 Beats Grid */
    .beats-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
    @media (max-width: 960px) {{ .beats-grid {{ grid-template-columns: 1fr; }} }}
    .beat-card {{ background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); overflow: hidden; display: flex; flex-direction: column; }}
    .beat-card:hover {{ border-color: var(--border-accent); }}
    .beat-img-container {{ position: relative; width: 100%; aspect-ratio: 9 / 16; background: #000; overflow: hidden; cursor: pointer; }}
    .beat-img-container img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s; }}
    .beat-img-container:hover img {{ transform: scale(1.03); }}
    .beat-badge-top {{ position: absolute; top: 8px; left: 8px; z-index: 2; font-size: 9.5px; font-weight: 800; padding: 3px 7px; border-radius: 4px; text-transform: uppercase; }}
    .badge-in {{ background: rgba(16, 185, 129, 0.9); color: #fff; }}
    .badge-main {{ background: rgba(245, 158, 11, 0.9); color: #000; }}
    .badge-out {{ background: rgba(56, 189, 248, 0.9); color: #000; }}
    .beat-time-tag {{ position: absolute; bottom: 8px; right: 8px; background: rgba(0, 0, 0, 0.75); color: #fff; font-family: 'JetBrains Mono', monospace; font-size: 9.5px; font-weight: 700; padding: 2px 6px; border-radius: 4px; }}
    .beat-content {{ padding: 14px; display: flex; flex-direction: column; gap: 10px; flex: 1; }}
    .beat-header {{ display: flex; justify-content: space-between; align-items: center; }}
    .beat-id-title {{ font-size: 13px; font-weight: 800; color: var(--text-primary); }}
    .specs-table {{ width: 100%; font-size: 11px; border-collapse: collapse; background: rgba(0, 0, 0, 0.2); border-radius: 6px; overflow: hidden; }}
    .specs-table tr {{ border-bottom: 1px solid rgba(255, 255, 255, 0.04); }}
    .specs-table tr:last-child {{ border-bottom: none; }}
    .specs-table td {{ padding: 5px 8px; }}
    .specs-table td.spec-name {{ color: var(--text-muted); font-weight: 600; width: 36%; }}
    .specs-table td.spec-val {{ color: var(--text-primary); font-weight: 500; }}
    .director-note-box {{ background: rgba(245, 158, 11, 0.06); border: 1px dashed rgba(245, 158, 11, 0.3); padding: 8px 10px; border-radius: 6px; font-size: 11px; color: #fde68a; line-height: 1.4; margin-top: auto; }}
    
    /* Timeline Filmstrip */
    .timeline-wrapper {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 22px 20px; margin-bottom: 28px; }}
    .filmstrip {{ display: flex; gap: 10px; overflow-x: auto; padding-bottom: 12px; }}
    .strip-frame {{ flex: 0 0 130px; background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 6px; overflow: hidden; cursor: pointer; transition: transform 0.2s; }}
    .strip-frame:hover {{ transform: translateY(-3px); border-color: var(--cyan); }}
    .strip-frame-img {{ width: 100%; aspect-ratio: 9 / 16; object-fit: cover; display: block; }}
    .strip-meta {{ padding: 5px 6px; font-size: 9.5px; text-align: center; }}
    .strip-title {{ font-weight: 700; color: #fff; }}
    .strip-ts {{ color: var(--cyan); font-family: 'JetBrains Mono', monospace; }}
    
    /* Lightbox Modal */
    .lightbox {{
      display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.88); z-index: 1000; align-items: center; justify-content: center; padding: 20px;
    }}
    .lightbox.active {{ display: flex; }}
    .lightbox-content {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
      max-width: 800px; width: 100%; max-height: 90vh; overflow: hidden; display: flex; gap: 20px; padding: 20px; position: relative;
    }}
    @media (max-width: 650px) {{ .lightbox-content {{ flex-direction: column; overflow-y: auto; }} }}
    .lightbox-img-box {{ flex: 1; max-width: 320px; aspect-ratio: 9 / 16; background: #000; border-radius: 8px; overflow: hidden; }}
    .lightbox-img-box img {{ width: 100%; height: 100%; object-fit: cover; }}
    .lightbox-details {{ flex: 1.2; display: flex; flex-direction: column; gap: 12px; }}
    .lightbox-close {{ position: absolute; top: 12px; right: 14px; background: none; border: none; font-size: 24px; color: #fff; cursor: pointer; }}
  </style>
</head>
<body>
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">Bảng Phân Cảnh AI</span>
      <div class="header-title">🎬 Kịch Bản 0{num}: {title} (30s)</div>
    </div>
    <div class="header-controls">
      <a href="index.html" class="hub-link">🏛️ Master Hub</a>
      <a href="#orig-msg" class="nav-btn">📩 Tin Nhắn Gốc</a>
      <a href="#scene-1" class="nav-btn">Cảnh 1</a>
      <a href="#scene-2" class="nav-btn">Cảnh 2</a>
      <a href="#scene-3" class="nav-btn">Cảnh 3</a>
      <a href="#scene-4" class="nav-btn">Cảnh 4</a>
      <a href="#scene-5" class="nav-btn">Cảnh 5</a>
      <a href="#filmstrip-view" class="nav-btn">🎞️ Dải Timeline</a>
      <button class="action-btn" onclick="window.print()">📄 In / PDF</button>
    </div>
  </header>

  <div class="container">
    <!-- ORIGINAL MESSAGE SECTION -->
    <section class="original-message-box" id="orig-msg">
      <div class="orig-header">
        <div class="orig-title">📩 Tin Nhắn & Kịch Bản Gốc Trích Xuất Online <span class="orig-badge">KỊCH BẢN 0{num}</span></div>
        <div style="font-size: 11px; color: var(--text-muted);">⏱️ Nguồn: <b>9_kich_ban_thuc_chien.html</b></div>
      </div>
      <div class="orig-content-grid">
        <div>
          <div style="font-size: 11px; color: var(--cyan); font-weight: 700; margin-bottom: 6px; text-transform: uppercase;">
            💬 Kịch bản thoại & Phân cảnh gốc:
          </div>
          <div class="raw-text-panel">{raw_script_formatted}</div>
        </div>
        <div>
          <div style="font-size: 11px; color: var(--cyan); font-weight: 700; margin-bottom: 6px; text-transform: uppercase;">
            🖼️ Ảnh bối cảnh tham chiếu (Cloudflare R2):
          </div>
          <div class="ref-gallery">
            <div class="ref-item">
              <div class="ref-thumb-box"><img src="{R2_MEDIA_BASE}/assets/reference/ref_01_classroom.jpg" alt="Bối Cảnh Lớp Học"></div>
              <div class="ref-caption"><strong>Bối Cảnh Lớp Học & Bàn Gỗ</strong><span>Bàn gỗ tự nhiên, ly cafe, sổ tay, ánh sáng xiên.</span></div>
            </div>
            <div class="ref-item">
              <div class="ref-thumb-box"><img src="{R2_MEDIA_BASE}/assets/reference/ref_02_character.jpg" alt="Nhân Vật Mặc Định"></div>
              <div class="ref-caption"><strong>Nhân Diện Mặc Định: Anh Việt</strong><span>Áo blazer đen/sơ mi tối giản, biểu cảm từng trải.</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- HERO SECTION -->
    <section class="hero">
      <div class="hero-tags">
        <span class="tag tag-accent">⚡ 9:16 Vertical Master</span>
        <span class="tag tag-amber">🎯 15 Storyboard Beats</span>
        <span class="tag tag-emerald">🔄 J-Cut -0.4s Sync</span>
        <span class="tag tag-cyan">🏷️ {cat}</span>
      </div>
      <h1>Bảng Phân Cảnh Storyboard: Kịch Bản 0{num} • {title}</h1>
      <p style="color: var(--text-secondary); font-size: 13px;">{desc} • 💡 {takeaway}</p>
      <div class="metrics-bar">
        <div><span class="metric-label">Tổng Thời Lượng</span><div class="metric-value">30 Giây</div></div>
        <div><span class="metric-label">Số Cảnh Chính</span><div class="metric-value">5 Cảnh</div></div>
        <div><span class="metric-label">Số Vi Phân Cảnh</span><div class="metric-value">15 Beats</div></div>
        <div><span class="metric-label">Nhịp Cắt Trung Bình</span><div class="metric-value">1.5s / Beat</div></div>
      </div>
    </section>

    <!-- 3 TIERS OF TRUTH -->
    <section class="tiers-box">
      <div class="tier-card t1">
        <div class="tier-card-head">❌ {tiers[0]['badge']}</div>
        <div class="tier-card-content">"{tiers[0]['content']}"</div>
      </div>
      <div class="tier-card t2">
        <div class="tier-card-head">⚠️ {tiers[1]['badge']}</div>
        <div class="tier-card-content">"{tiers[1]['content']}"</div>
      </div>
      <div class="tier-card t3">
        <div class="tier-card-head">✅ {tiers[2]['badge']}</div>
        <div class="tier-card-content">"{tiers[2]['content']}"</div>
      </div>
    </section>
"""

    # SCENES SECTION
    for sc in scenes:
        s_id = sc["scene_id"]
        html += f"""
    <!-- SCENE {s_id} -->
    <section class="scene-block" id="scene-{s_id}">
      <div class="scene-header">
        <div class="scene-title-group">
          <span class="scene-num-badge">CẢNH {s_id}</span>
          <h3 class="scene-main-title">{sc['title']}</h3>
          <span class="tag tag-cyan">{sc['main_shot_type']}</span>
        </div>
        <span class="scene-time-badge">⏱️ {sc['time_range']} ({sc['duration']})</span>
      </div>
      <div class="scene-intent-box"><strong>🎯 Ý Đồ Đạo Diễn:</strong> {sc['intent']}</div>
      <div class="audio-box">
        <div class="voice-content">
          <div class="voice-icon">🎙️</div>
          <div>
            <div style="font-size: 10.5px; color: var(--cyan); font-weight: 700; text-transform: uppercase;">Lời Thoại Kịch Bản:</div>
            <div class="voice-text">"{sc['voiceover']}"</div>
          </div>
        </div>
        <span class="tag tag-cyan">J-Cut -0.4s</span>
      </div>
      <div class="beats-grid">
"""
        for b_idx, b in enumerate(sc["beats"], 1):
            badge_class = "badge-in" if b_idx == 1 else ("badge-main" if b_idx == 2 else "badge-out")
            r2_media = f"https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/{slug}"
            img_url = f"{r2_media}/assets/frames/scene{s_id}_beat{b_idx}.jpg"
            html += f"""
        <div class="beat-card">
          <div class="beat-img-container" onclick="openLightbox('{img_url}', 'Khung Hình {b['id']}: {b['shot']}', '{b['note']}')">
            <span class="beat-badge-top {badge_class}">{b['label']}</span>
            <span class="beat-time-tag">{b['ts']}</span>
            <img src="{img_url}" alt="{b['id']}">
          </div>
          <div class="beat-content">
            <div class="beat-header">
              <span class="beat-id-title">Khung Hình {b['id']}</span>
              <span class="tag tag-cyan" style="font-size: 10px;">{b['shot']}</span>
            </div>
            <table class="specs-table">
              <tr><td class="spec-name">Góc Máy</td><td class="spec-val">{b['angle']}</td></tr>
              <tr><td class="spec-name">Động Tác</td><td class="spec-val">{b['motion']}</td></tr>
              <tr><td class="spec-name">Bố Cục</td><td class="spec-val">{b['comp']}</td></tr>
            </table>
            <div class="director-note-box"><strong>💡 Đạo Diễn:</strong> {b['note']}</div>
          </div>
        </div>
"""
        html += """      </div>\n    </section>\n"""

    # TIMELINE FILMSTRIP & LIGHTBOX
    html += f"""
    <!-- TIMELINE FILMSTRIP -->
    <section class="timeline-wrapper" id="filmstrip-view">
      <h2 style="font-size: 18px; font-weight: 800; margin-bottom: 12px; color: #fff;">🎞️ Dải Timeline Phân Cảnh (15 Khung Hình Liên Tiếp • 0s ➔ 30s)</h2>
      <div class="filmstrip">
"""
    for sc in scenes:
        for b_idx, b in enumerate(sc["beats"], 1):
            r2_media = f"https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/{slug}"
            img_url = f"{r2_media}/assets/frames/scene{sc['scene_id']}_beat{b_idx}.jpg"
            html += f"""
        <div class="strip-frame" onclick="openLightbox('{img_url}', 'Cảnh {b['id']} ({b['ts']})', '{b['note']}')">
          <img class="strip-frame-img" src="{img_url}" alt="{b['id']}">
          <div class="strip-meta"><div class="strip-title">Cảnh {b['id']}</div><div class="strip-ts">{b['ts']}</div></div>
        </div>
"""
    html += f"""
      </div>
    </section>
  </div>

  <!-- Lightbox Modal -->
  <div class="lightbox" id="lightboxModal" onclick="closeLightbox(event)">
    <div class="lightbox-content" onclick="event.stopPropagation()">
      <button class="lightbox-close" onclick="closeLightboxDirect()">&times;</button>
      <div class="lightbox-img-box">
        <img id="lightboxImg" src="" alt="Enlarged Frame">
      </div>
      <div class="lightbox-details">
        <span class="tag tag-cyan" id="lightboxTag">Frame Preview 9:16</span>
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
      if (e.target.id === 'lightboxModal') closeLightboxDirect();
    }}

    function closeLightboxDirect() {{
      document.getElementById('lightboxModal').classList.remove('active');
      document.body.style.overflow = 'auto';
    }}

    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') closeLightboxDirect();
    }});
  </script>
</body>
</html>
"""
    return html

def build_master_index(all_storyboards):
    total_sb = len(all_storyboards)
    total_scenes = total_sb * 5
    total_beats = total_sb * 15
    total_duration_sec = total_sb * 30
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
    .card-summary {{ font-size: 12.5px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 12px; }}
    .card-quote {{
      background: rgba(0, 0, 0, 0.25); border-left: 3px solid var(--cyan); padding: 6px 10px;
      border-radius: 0 4px 4px 0; font-size: 11.5px; color: #cbd5e1; font-style: italic; margin-top: auto;
    }}
    
    .card-bottom {{
      padding: 16px 22px; background: rgba(0, 0, 0, 0.2); display: flex; justify-content: space-between; align-items: center; gap: 12px;
    }}
    .card-metrics-mini {{ display: flex; gap: 14px; font-size: 11.5px; color: var(--text-muted); }}
    .card-metrics-mini span b {{ color: var(--text-primary); }}
    .view-btn {{
      background: linear-gradient(135deg, var(--cyan), #2563eb); color: #000; font-weight: 800;
      font-size: 12px; padding: 8px 18px; border-radius: var(--radius-sm); text-decoration: none;
      display: inline-flex; align-items: center; gap: 6px; transition: opacity 0.2s;
    }}
    .view-btn:hover {{ opacity: 0.9; }}
    
    /* Filmstrip Mini */
    .card-strip {{
      display: flex; gap: 6px; padding: 12px 22px; background: rgba(0, 0, 0, 0.35); overflow-x: auto; border-bottom: 1px solid var(--border-subtle);
    }}
    .card-strip-thumb {{
      flex: 0 0 54px; aspect-ratio: 9 / 16; background: #000; border-radius: 4px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    .card-strip-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
  </style>
</head>
<body>
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">Bảng Phân Cảnh Master</span>
      <div class="header-title">🎬 AI Storyboard Studio 9:16</div>
    </div>
    <div class="header-controls">
      <a href="https://fedu.vn/Bang-Phan-Canh/" class="header-link" target="_blank">🌐 Cổng fedu.vn</a>
      <a href="https://github.com/vietndj/Bang-Phan-Canh" class="header-link" target="_blank">🐙 GitHub Repo</a>
      <a href="https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/9_kich_ban_thuc_chien.html" class="header-link" target="_blank">📋 9 Kịch Bản Gốc</a>
    </div>
  </header>

  <div class="container">
    <!-- HERO -->
    <section class="hero">
      <div class="hero-badge">⚡ Kho Bảng Phân Cảnh Điện Ảnh 9:16 Chuẩn Quốc Tế</div>
      <h1>Bộ 9 Kịch Bản Thực Chiến 3 Tầng Sự Thật</h1>
      <p class="hero-desc">
        Hệ thống băm nhỏ kịch bản thoại thành 15 micro-beats đạo diễn chuẩn xác từng giây (In-point, Main Action, Out-point Lead).
        Nhân diện chuẩn Anh Việt, tối ưu chuyển thể cho định dạng video ngắn TikTok, Reels và YouTube Shorts.
      </p>
      <div class="stats-bar">
        <div class="stat-item"><div class="stat-label">Tổng Kịch Bản</div><div class="stat-val">{total_sb} Kịch Bản</div></div>
        <div class="stat-item"><div class="stat-label">Tổng Phân Cảnh</div><div class="stat-val">{total_scenes} Cảnh Quay</div></div>
        <div class="stat-item"><div class="stat-label">Vi Phân Cảnh (Beats)</div><div class="stat-val">{total_beats} Micro-Beats</div></div>
        <div class="stat-item"><div class="stat-label">Thời Lượng Chuẩn</div><div class="stat-val">30s / Video</div></div>
        <div class="stat-item"><div class="stat-label">Tỷ Lệ Khung Hình</div><div class="stat-val">9:16 Vertical</div></div>
      </div>
    </section>

    <!-- SEARCH & FILTER -->
    <div class="filter-bar">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" class="search-input" id="searchInput" placeholder="Tìm kiếm kịch bản, lời thoại, nỗi đau..." onkeyup="filterCards()">
      </div>
      <div class="filter-tags">
        <button class="filter-tag active" onclick="setFilter('all', this)">Tất cả ({total_sb})</button>
        <button class="filter-tag" onclick="setFilter('Bán Hàng', this)">Bán Hàng</button>
        <button class="filter-tag" onclick="setFilter('Văn Phòng', this)">Văn Phòng</button>
        <button class="filter-tag" onclick="setFilter('Tự Do', this)">Tự Do & Tư Vấn</button>
        <button class="filter-tag" onclick="setFilter('Kỹ Thuật', this)">Kỹ Thuật</button>
        <button class="filter-tag" onclick="setFilter('Đại Lý', this)">Đại Lý</button>
        <button class="filter-tag" onclick="setFilter('Chuyển Nghề', this)">Chuyển Nghề</button>
      </div>
    </div>

    <!-- CARDS GRID -->
    <div class="storyboards-grid" id="sbGrid">
"""
    for sb in all_storyboards:
        num = sb["num"]
        title = sb["title"]
        tag = sb["tag"]
        cat = sb["category"]
        color = sb["badge_color"]
        fname = sb["file_name"]
        hook = sb["scenes"][0]["voiceover"]
        cta = sb["scenes"][-1]["voiceover"]
        thumb = f"{R2_MEDIA_BASE}/assets/frames/scene1_beat1.jpg"
        
        html += f"""
      <div class="sb-card" data-category="{cat} {tag} {title} {hook}">
        <div class="card-top">
          <div class="card-thumb-wrap">
            <img src="{thumb}" alt="{title}">
            <span class="card-badge-tag">KB 0{num}</span>
          </div>
          <div class="card-info">
            <div class="card-meta-row">
              <span class="pill" style="background: {color}22; color: {color}; border: 1px solid {color}55;">{tag}</span>
              <span class="pill" style="background: rgba(255,255,255,0.06); color: var(--text-muted);">30 Giây • 15 Beats</span>
            </div>
            <h2 class="card-title">Kịch Bản 0{num}: {title}</h2>
            <p class="card-summary">{sb['context_desc']}</p>
            <div class="card-quote">🎙️ "{hook}"</div>
          </div>
        </div>
        
        <div class="card-strip">
"""
        for sc in sb["scenes"]:
            for b_idx in range(1, 4):
                img_url = f"{R2_MEDIA_BASE}/assets/frames/scene{sc['scene_id']}_beat{b_idx}.jpg"
                html += f"""          <div class="card-strip-thumb"><img src="{img_url}" alt="f"></div>\n"""
        
        html += f"""
        </div>
        
        <div class="card-bottom">
          <div class="card-metrics-mini">
            <span>🎯 Target: <b>{sb['target_audience']}</b></span>
          </div>
          <a href="{fname}" class="view-btn">🎬 Mở Bảng Phân Cảnh ➔</a>
        </div>
      </div>
"""
    html += """
    </div>
  </div>

  <script>
    function setFilter(cat, btn) {
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
    print("🚀 ĐANG TẠO BẢNG PHÂN CẢNH CHO CÁC KỊCH BẢN TỪ 4 TRONG 9_KICH_BAN_THUC_CHIEN.HTML")
    print("=" * 60)
    
    generated_files = []
    
    # 1. Render all HTML files (scripts 1 through 9)
    for sb in scripts_data:
        file_path = os.path.join(REPO_DIR, sb["file_name"])
        html_content = render_storyboard_html(sb)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ Đã tạo thành công: {sb['file_name']} (Kịch bản 0{sb['num']}: {sb['title']})")
        generated_files.append(sb["file_name"])
        
    # 2. Rebuild Master Index Hub
    master_index_html = build_master_index(scripts_data)
    index_path = os.path.join(REPO_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(master_index_html)
    print(f"✅ Đã cập nhật Master Hub: index.html với trọn bộ {len(scripts_data)} kịch bản")
    
    print("\n🎉 HOÀN THÀNH XUẤT BẢN TẤT CẢ CÁC BẢNG PHÂN CẢNH!")

if __name__ == "__main__":
    main()
