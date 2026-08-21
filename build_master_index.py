#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tự động biên dịch Master Hub Quản Trị Bảng Phân Cảnh (index.html)
Hiển thị ĐẦY ĐỦ 100% tất cả các file HTML trong dự án:
1. Bảng Phân Cảnh Điện Ảnh 9:16 (Visual Storyboards)
2. Kho Kịch Bản & Tài Liệu Tham Khảo (Text Documents - Không có Thumbnail)
"""

import os
import json
from datetime import datetime

REPO_DIR = "/Users/vietmac/Documents/CODE/Bang-Phan-Canh"

# -------------------------------------------------------------
# 1. DANH SÁCH BẢNG PHÂN CẢNH 9:16 (VISUAL STORYBOARDS)
# -------------------------------------------------------------
storyboards = [
    {
        "id": "kb01_master",
        "slug": "tu_dot_tien_den_tu_tin_xuat_hien",
        "file_name": "tu_dot_tien_den_tu_tin_xuat_hien.html",
        "title": "Kịch Bản 01: Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện",
        "category": "Kinh Doanh & Quảng Cáo Online",
        "badge_color": "#38bdf8",
        "target_audience": "Chủ shop, người bán hàng online phụ thuộc chạy Ads",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
        "summary": "Nỗi đau chi phí quảng cáo tăng gấp đôi, tiền nạp ăn hết lãi. Chuyển dịch tư duy từ 'đốt tiền mua Ads' sang tự quay video xuất hiện để xây dựng niềm tin thật với khách hàng.",
        "hook_dialogue": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
        "cta_dialogue": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "Kịch Bản Thực Chiến 01"
    },
    {
        "id": "kb02_master",
        "slug": "tien_mat_bang_va_cua_hang_vang_khach",
        "file_name": "tien_mat_bang_va_cua_hang_vang_khach.html",
        "title": "Kịch Bản 02: Tiền Mặt Bằng & Cửa Hàng Vắng Khách",
        "category": "Chủ Shop & Mở Tiệm Kinh Doanh",
        "badge_color": "#f43f5e",
        "target_audience": "Chủ shop offline, chủ tiệm gánh áp lực mặt bằng và nhân sự",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene1_beat1.jpg",
        "summary": "Áp lực sinh tồn khi tiền mặt bằng 20 triệu đến hạn, cửa hàng vắng khách. Tự làm thuê cho chính mình 16h/ngày và quyết tâm học lại mọi thứ để duy trì cửa hàng.",
        "hook_dialogue": "Sáng Chủ Nhật, tôi ngồi ở lớp này không phải vì rảnh rỗi...",
        "cta_dialogue": "Đến lúc này thì cái gì giúp mình duy trì được cửa hàng thì phải bắt tay vào học thôi.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb02)"
    },
    {
        "id": "kb01_series",
        "slug": "kich_ban_01_ngoi_ca_phe_10h_toi",
        "file_name": "kich_ban_01_ngoi_ca_phe_10h_toi.html",
        "title": "Kịch Bản 01: Ngồi Cà Phê 10h Tối",
        "category": "Tâm Lý & Áp Lực Kiệt Sức",
        "badge_color": "#818cf8",
        "target_audience": "Người trẻ làm nghề, freelancer cày đêm vì bất an",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
        "summary": "Bóc trần thói quen 'cố tỏ ra bận rộn' để xoa dịu nỗi sợ tụt hậu. Cày đêm không phải vì đam mê mà là liều thuốc an thần cho sự bất an của chính mình.",
        "hook_dialogue": "10h tối, ngồi ở góc quán này không phải vì chăm chỉ...",
        "cta_dialogue": "Nhiều khi cố cày đêm không phải để giàu lên, mà chỉ là liều thuốc an thần cho sự bất an của chính mình.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb01)"
    },
    {
        "id": "kb03_series",
        "slug": "kich_ban_03_chung_lai_sau_tuoi_30",
        "file_name": "kich_ban_03_chung_lai_sau_tuoi_30.html",
        "title": "Kịch Bản 03: Chững Lại Sau Tuổi 30",
        "category": "Phát Triển Bản Thân & Nghề Nghiệp",
        "badge_color": "#f59e0b",
        "target_audience": "Người làm văn phòng 30+, người sợ tụt hậu công nghệ",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat2.jpg",
        "summary": "Khủng hoảng tuổi 30 của người làm văn phòng khi thu nhập đứng yên mà chi phí tăng. Nỗi sợ bị bỏ lại phía sau trước làn sóng công nghệ mới và quyết tâm học lại từ đầu.",
        "hook_dialogue": "Hơn 30 tuổi, ngồi trong căn phòng này cùng mọi người...",
        "cta_dialogue": "Bớt ngại đi, chịu khó học lại từ đầu còn hơn cứ ngồi yên nhìn công việc của mình đi xuống.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat2.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat2.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat2.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat2.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat2.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb03)"
    },
    {
        "id": "kb04_series",
        "slug": "kich_ban_04_tien_quang_cao_an_het_tien_lai",
        "file_name": "kich_ban_04_tien_quang_cao_an_het_tien_lai.html",
        "title": "Kịch Bản 04: Tiền Quảng Cáo Ăn Hết Tiền Lãi",
        "category": "Bán Hàng Online & Chạy Ads",
        "badge_color": "#ec4899",
        "target_audience": "Người kinh doanh online phụ thuộc hoàn toàn vào Facebook/TikTok Ads",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
        "summary": "Bế tắc vì chi phí quảng cáo tăng phi mã nhưng không dám tắt ads. Lựa chọn dũng cảm: Thay vì đổ tiền nuôi nền tảng thì tự học cách xuất hiện để kéo khách tự nhiên.",
        "hook_dialogue": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
        "cta_dialogue": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb04)"
    },
    {
        "id": "kb05_series",
        "slug": "kich_ban_05_het_khach_tu_moi_quan_he_quen",
        "file_name": "kich_ban_05_het_khach_tu_moi_quan_he_quen.html",
        "title": "Kịch Bản 05: Hết Khách Từ Mối Quan Hệ Quen",
        "category": "Mối Quan Hệ & Bán Hàng",
        "badge_color": "#a855f7",
        "target_audience": "Người làm dịch vụ, tư vấn, bảo hiểm, bất động sản",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
        "summary": "Nỗi ngại ngùng khi chào mời người quen ủng hộ đã đến giới hạn. Nhận ra giá trị của việc làm nội dung để người lạ tự tìm đến và đặt niềm tin.",
        "hook_dialogue": "Lướt danh bạ điện thoại từ trên xuống dưới mà không biết nhắn cho ai...",
        "cta_dialogue": "Phải tự học cách tiếp cận người lạ bằng nội dung tử tế thôi.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb05)"
    },
    {
        "id": "kb06_series",
        "slug": "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach",
        "file_name": "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach.html",
        "title": "Kịch Bản 06: Tay Nghề Tốt Nhưng Vẫn Vắng Khách",
        "category": "Kỹ Năng Nghề & Xây Uy Tín",
        "badge_color": "#14b8a6",
        "target_audience": "Thợ thủ công, kỹ thuật viên, chuyên gia chuyên môn giỏi nhưng thiếu truyền thông",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
        "summary": "Nghịch lý 'hữu xạ tự nhiên hương' không còn đúng trong thời đại số. Giỏi nghề thôi chưa đủ, phải biết cách cho khách hàng thấy sự tâm huyết và kỹ lưỡng của mình.",
        "hook_dialogue": "Làm nghề mười mấy năm, đồ mình làm ra tự tin không thua ai...",
        "cta_dialogue": "Giỏi nghề mà giữ trong xưởng thì không ai biết, phải tự đưa nghề ra ánh sáng.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb06)"
    },
    {
        "id": "kb07_series",
        "slug": "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc",
        "file_name": "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc.html",
        "title": "Kịch Bản 07: Bị Cạnh Tranh Bởi Tổng Kho & Giá Gốc",
        "category": "Cạnh Tranh Giá & Xây Khách Quen",
        "badge_color": "#06b6d4",
        "target_audience": "Cửa hàng bán lẻ, đại lý phân phối truyền thống",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
        "summary": "Không thể đua giá rẻ với các tổng kho và sàn thương mại điện tử. Con đường sống sót duy nhất là bán trải nghiệm, dịch vụ tận tâm và sự đồng hành của người bán.",
        "hook_dialogue": "Khách cầm điện thoại vào hỏi: 'Sao bên kia bán rẻ hơn anh mấy chục ngàn?'...",
        "cta_dialogue": "Không đua giá được thì phải bán bằng sự tận tụy và uy tín của chính mình.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb07)"
    },
    {
        "id": "kb08_series",
        "slug": "kich_ban_08_bat_dau_lai_tu_con_so_0",
        "file_name": "kich_ban_08_bat_dau_lai_tu_con_so_0.html",
        "title": "Kịch Bản 08: Bắt Đầu Lại Từ Con Số 0",
        "category": "Khởi Nghiệp Lại & Vượt Khủng Hoảng",
        "badge_color": "#10b981",
        "target_audience": "Người từng thất bại, chuyển đổi mô hình kinh doanh mới",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg",
        "summary": "Tâm thế làm lại từ đầu sau cú vấp ngã. Không còn ảo tưởng về vốn lớn, tập trung vào mô hình tinh gọn, chi phí thấp và tự làm chủ truyền thông.",
        "hook_dialogue": "Đóng cửa cửa hàng cũ, trong tay gần như về lại số 0...",
        "cta_dialogue": "Ngã ở đâu thì đứng lên ở đó, lần này làm chuẩn từ gốc không vội vàng.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb08)"
    },
    {
        "id": "kb09_series",
        "slug": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia",
        "file_name": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html",
        "title": "Kịch Bản 09: Hàng Làm Kỹ Nhưng Bị So Sánh Giá",
        "category": "Chất Lượng vs Giá Rẻ",
        "badge_color": "#eab308",
        "target_audience": "Nhà sản xuất, thợ lành nghề, thương hiệu tập trung chất lượng",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat2.jpg",
        "summary": "Nỗi uất ức khi sản phẩm làm bằng cái tâm bị đem ra so kè với hàng chợ kém chất lượng. Giải pháp: Quay cận cảnh quy trình để người xem tự nhìn thấy sự khác biệt.",
        "hook_dialogue": "Nhập từng con ốc, chọn từng miếng gỗ tốt nhất nhưng khách chỉ hỏi: 'Sao đắt thế?'...",
        "cta_dialogue": "Không giải thích suông, quay toàn bộ quy trình lên cho khách hàng tự thẩm định.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb09)"
    }
]

# -------------------------------------------------------------
# 2. DANH SÁCH TÀI LIỆU KỊCH BẢN & VĂN BẢN (KHÔNG CÓ THUMBNAIL)
# -------------------------------------------------------------
text_documents = [
    {
        "id": "doc_9_kich_ban",
        "file_name": "9_kich_ban_thuc_chien.html",
        "title": "📑 9 Mẫu Kịch Bản 3 Tầng Sự Thật (Bản Tài Liệu Gốc - Lớp Học Offline)",
        "category": "Tài Liệu Kịch Bản & Voice-Over",
        "badge_color": "#38bdf8",
        "badge_text": "Tài Liệu Tổng Hợp",
        "icon": "📑",
        "target_audience": "Học viên, chủ doanh nghiệp, người sáng tạo nội dung thực chiến",
        "structure": "9 Kịch Bản Hoàn Chỉnh • Bảng Biểu Phân Cảnh • Lời Thoại • Bóc 3 Tầng Sự Thật",
        "summary": "Tài liệu master tổng hợp toàn bộ 9 kịch bản thực chiến được thiết kế theo cấu trúc 3 Tầng Sự Thật (Đãi bôi ➔ Cảm giác thật ➔ Ngượng miệng). Tích hợp thanh điều hướng nhanh, bảng thông số cỡ cảnh, thời gian và nút copy kịch bản tiện lợi.",
        "highlights": [
            "Bản đồ tư duy 3 Tầng Bóc Sự Thật",
            "Bảng phân cảnh chi tiết từng giây (0 - 30s)",
            "Đầy đủ 9 kịch bản từ Cafe Đêm đến Hàng Làm Kỹ",
            "Nút Copy 1-Click cho từng kịch bản"
        ],
        "updated_at": "21/08/2026"
    },
    {
        "id": "doc_phong_nha",
        "file_name": "kich_ban_phong_nha.html",
        "title": "🎙️ Kịch Bản Voice-Over Thực Chiến: Phong Nha (Góc Phòng & Ban Công)",
        "category": "Kịch Bản Review & Du Lịch",
        "badge_color": "#10b981",
        "badge_text": "Kịch Bản Voice-Over",
        "icon": "🎙️",
        "target_audience": "Người làm video du lịch, review trải nghiệm, phong cách kể chuyện chân thực",
        "structure": "Bảng Phân Đoạn Voice-Over • Thời Gian • Cỡ Cảnh • Lời Thoại",
        "summary": "Mẫu kịch bản Voice-Over phong cách tự nhiên, ghi lại cảm xúc và câu chuyện du lịch Phong Nha với bối cảnh thu âm/quay tại góc phòng và ban công thực tế.",
        "highlights": [
            "Cấu trúc Voice-Over phân đoạn từng 3 - 5s",
            "Chuyển đổi nhịp cảm xúc giữa không gian phòng & ban công",
            "Bảng thông số đạo diễn chi tiết"
        ],
        "updated_at": "21/08/2026"
    }
]

total_storyboards = len(storyboards)
total_scenes = sum(s["scenes_count"] for s in storyboards)
total_beats = sum(s["beats_count"] for s in storyboards)
total_docs = len(text_documents)
total_all_files = total_storyboards + total_docs

# Render Cards cho Storyboards 9:16
cards_html = ""
for s in storyboards:
    mini_html = "".join([f'<img src="{img}" alt="beat frame" loading="lazy">' for img in s["mini_frames"]])
    cards_html += f"""
      <article class="board-card" data-category="{s['category']}">
        <div class="card-media">
          <img src="{s['thumb_url']}" alt="{s['title']}" class="card-thumb" loading="lazy">
          <div class="card-badge" style="background: {s['badge_color']}; color: #000;">{s['category']}</div>
          <div class="card-duration">⏱️ {s['duration']} • {s['scenes_count']} Cảnh</div>
        </div>
        
        <div class="card-body">
          <h3 class="card-title"><a href="{s['file_name']}">{s['title']}</a></h3>
          <div class="card-target">🎯 Đối tượng: <b>{s['target_audience']}</b></div>
          <p class="card-summary">{s['summary']}</p>
          
          <div class="quote-box">
            <div class="quote-label">🎙️ Hook Mở Màn:</div>
            <div class="quote-text">"{s['hook_dialogue']}"</div>
          </div>
          
          <div class="filmstrip-preview">
            <div class="filmstrip-title">🎞️ 5 Phân Cảnh Trọng Tâm (3-Beat Rhythm):</div>
            <div class="filmstrip-imgs">
              {mini_html}
            </div>
          </div>
          
          <div class="card-footer">
            <div class="card-meta">
              <span>📅 {s['created_at']}</span>
              <span>•</span>
              <span>📱 {s['source']}</span>
            </div>
            <a href="{s['file_name']}" class="open-btn">Xem Phân Cảnh Chi Tiết →</a>
          </div>
        </div>
      </article>
    """

# Render Cards cho Text Documents (Không Có Thumbnail)
docs_html = ""
for d in text_documents:
    highlights_html = "".join([f'<li>✓ {hl}</li>' for hl in d['highlights']])
    docs_html += f"""
      <article class="doc-card" data-category="{d['category']}">
        <div class="doc-header">
          <div class="doc-icon-badge">{d['icon']}</div>
          <div class="doc-title-group">
            <div class="doc-badge" style="border-color: {d['badge_color']}; color: {d['badge_color']};">{d['badge_text']}</div>
            <h3 class="doc-title"><a href="{d['file_name']}">{d['title']}</a></h3>
          </div>
        </div>
        
        <div class="doc-body">
          <div class="doc-meta-bar">
            <span>🎯 <b>Đối tượng:</b> {d['target_audience']}</span>
            <span>📐 <b>Định dạng:</b> {d['structure']}</span>
          </div>
          
          <p class="doc-summary">{d['summary']}</p>
          
          <div class="doc-highlights-box">
            <div class="doc-hl-title">⚡ Điểm Nổi Bật & Cấu Trúc:</div>
            <ul class="doc-hl-list">
              {highlights_html}
            </ul>
          </div>
          
          <div class="doc-footer">
            <div class="doc-date">📅 Cập nhật: {d['updated_at']}</div>
            <a href="{d['file_name']}" class="doc-open-btn">Mở Tài Liệu Gốc ({d['file_name']}) →</a>
          </div>
        </div>
      </article>
    """

full_index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kho Quản Trị Bảng Phân Cảnh Điện Ảnh 9:16 & Kịch Bản Thực Chiến | Master Hub</title>
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
      --rose: #f43f5e;
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
    .container {{ max-width: 1360px; margin: 0 auto; padding: 0 20px; }}
    
    /* Top Header */
    .top-header {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(10, 14, 23, 0.94);
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
    .header-link:hover {{ background: var(--cyan); color: #000; border-color: var(--cyan); font-weight: 700; }}
    
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
      padding: 4px 14px; border-radius: 9999px; font-size: 11.5px; font-weight: 700; margin-bottom: 14px; text-transform: uppercase;
    }}
    .hero h1 {{
      font-size: 30px; font-weight: 800; color: #fff; margin-bottom: 12px; line-height: 1.3;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hero-desc {{
      max-width: 820px; margin: 0 auto 24px auto; color: var(--text-secondary); font-size: 14px; line-height: 1.7;
    }}
    
    /* Stats Bar */
    .stats-grid {{
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;
      max-width: 960px; margin: 0 auto;
    }}
    @media (max-width: 768px) {{ .stats-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    .stat-item {{
      background: rgba(0, 0, 0, 0.35); border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm); padding: 14px 16px;
    }}
    .stat-num {{ font-size: 24px; font-weight: 800; color: var(--cyan); font-family: 'JetBrains Mono', monospace; }}
    .stat-label {{ font-size: 11.5px; color: var(--text-muted); font-weight: 600; text-transform: uppercase; margin-top: 2px; }}
    
    /* Filter Bar */
    .filter-bar {{
      display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;
      background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
      padding: 12px 18px; margin-bottom: 30px;
    }}
    .filter-tabs {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .filter-tab {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); color: var(--text-secondary);
      font-size: 12px; font-weight: 600; padding: 6px 14px; border-radius: var(--radius-sm); cursor: pointer; transition: all 0.2s;
    }}
    .filter-tab:hover, .filter-tab.active {{
      background: var(--cyan); color: #000; border-color: var(--cyan); font-weight: 700;
    }}
    .search-box {{
      background: #090e17; border: 1px solid var(--border-subtle); border-radius: var(--radius-sm);
      padding: 6px 12px; color: #fff; font-size: 12.5px; outline: none; min-width: 240px;
    }}
    .search-box:focus {{ border-color: var(--cyan); }}
    
    /* Section Headers */
    .section-header {{
      display: flex; justify-content: space-between; align-items: flex-end;
      margin: 40px 0 20px 0; padding-bottom: 12px; border-bottom: 1px solid var(--border-subtle);
    }}
    .section-title {{ font-size: 20px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 8px; }}
    .section-sub {{ font-size: 13px; color: var(--text-muted); }}
    
    /* Storyboard Grid */
    .boards-grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 24px;
    }}
    @media (max-width: 850px) {{ .boards-grid {{ grid-template-columns: 1fr; }} }}
    
    .board-card {{
      background: var(--bg-surface); border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg); overflow: hidden;
      display: flex; flex-direction: column; transition: all 0.25s ease;
    }}
    .board-card:hover {{
      transform: translateY(-4px); border-color: var(--border-accent);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
    }}
    
    .card-media {{
      position: relative; height: 260px; background: #000; overflow: hidden;
    }}
    .card-thumb {{
      width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.4s ease;
    }}
    .board-card:hover .card-thumb {{ transform: scale(1.04); }}
    
    .card-badge {{
      position: absolute; top: 12px; left: 12px;
      font-size: 10.5px; font-weight: 800; padding: 4px 10px; border-radius: 6px;
      text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .card-duration {{
      position: absolute; bottom: 12px; right: 12px;
      background: rgba(0, 0, 0, 0.8); color: var(--cyan);
      font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px;
      backdrop-filter: blur(4px); font-family: 'JetBrains Mono', monospace;
    }}
    
    .card-body {{ padding: 22px; display: flex; flex-direction: column; flex: 1; }}
    .card-title {{ font-size: 17px; font-weight: 800; line-height: 1.4; margin-bottom: 8px; }}
    .card-title a {{ color: #fff; text-decoration: none; transition: color 0.2s; }}
    .card-title a:hover {{ color: var(--cyan); }}
    
    .card-target {{ font-size: 12px; color: var(--text-muted); margin-bottom: 12px; }}
    .card-target b {{ color: var(--text-secondary); }}
    
    .card-summary {{ font-size: 13px; color: var(--text-secondary); line-height: 1.6; margin-bottom: 16px; flex: 1; }}
    
    .quote-box {{
      background: #090e17; border-left: 3px solid var(--cyan); border-radius: 4px;
      padding: 10px 12px; margin-bottom: 16px;
    }}
    .quote-label {{ font-size: 10px; font-weight: 800; color: var(--cyan); text-transform: uppercase; margin-bottom: 2px; }}
    .quote-text {{ font-size: 12px; color: #cbd5e1; font-style: italic; }}
    
    .filmstrip-preview {{ margin-bottom: 20px; }}
    .filmstrip-title {{ font-size: 11px; font-weight: 700; color: var(--text-muted); margin-bottom: 6px; }}
    .filmstrip-imgs {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; }}
    .filmstrip-imgs img {{
      width: 100%; aspect-ratio: 9/16; object-fit: cover; border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.1); background: #000;
    }}
    
    .card-footer {{
      display: flex; justify-content: space-between; align-items: center;
      padding-top: 16px; border-top: 1px solid var(--border-subtle); gap: 12px;
    }}
    .card-meta {{ font-size: 11.5px; color: var(--text-muted); display: flex; gap: 6px; }}
    .open-btn {{
      background: linear-gradient(135deg, #0284c7, #2563eb); color: #fff;
      font-size: 12px; font-weight: 700; padding: 7px 14px; border-radius: var(--radius-sm);
      text-decoration: none; transition: all 0.2s; white-space: nowrap;
    }}
    .open-btn:hover {{
      transform: translateY(-1px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }}
    
    /* Text Documents Cards (No Thumbnails) */
    .docs-grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(460px, 1fr)); gap: 24px;
    }}
    @media (max-width: 850px) {{ .docs-grid {{ grid-template-columns: 1fr; }} }}
    
    .doc-card {{
      background: linear-gradient(180deg, #131d2e 0%, #0d1522 100%);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: var(--radius-lg); padding: 24px;
      display: flex; flex-direction: column; transition: all 0.25s ease;
    }}
    .doc-card:hover {{
      border-color: var(--cyan); box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45); transform: translateY(-3px);
    }}
    .doc-header {{ display: flex; align-items: flex-start; gap: 14px; margin-bottom: 16px; }}
    .doc-icon-badge {{
      width: 48px; height: 48px; border-radius: 12px;
      background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.3);
      display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0;
    }}
    .doc-title-group {{ flex: 1; }}
    .doc-badge {{
      display: inline-block; font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 4px;
      border: 1px solid; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.5px;
    }}
    .doc-title {{ font-size: 16px; font-weight: 800; line-height: 1.4; }}
    .doc-title a {{ color: #fff; text-decoration: none; }}
    .doc-title a:hover {{ color: var(--cyan); }}
    
    .doc-body {{ display: flex; flex-direction: column; flex: 1; gap: 12px; }}
    .doc-meta-bar {{
      display: flex; flex-direction: column; gap: 4px; font-size: 12px; color: var(--text-muted);
      background: rgba(0, 0, 0, 0.25); padding: 8px 12px; border-radius: 6px; border-left: 3px solid var(--cyan);
    }}
    .doc-meta-bar b {{ color: var(--text-secondary); }}
    .doc-summary {{ font-size: 13px; color: var(--text-secondary); line-height: 1.6; }}
    
    .doc-highlights-box {{
      background: rgba(0, 0, 0, 0.3); border: 1px dashed rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 12px 14px;
    }}
    .doc-hl-title {{ font-size: 11px; font-weight: 700; color: var(--cyan); margin-bottom: 6px; text-transform: uppercase; }}
    .doc-hl-list {{ list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }}
    @media (max-width: 600px) {{ .doc-hl-list {{ grid-template-columns: 1fr; }} }}
    .doc-hl-list li {{ font-size: 11.5px; color: #cbd5e1; }}
    
    .doc-footer {{
      display: flex; justify-content: space-between; align-items: center;
      margin-top: auto; padding-top: 16px; border-top: 1px solid var(--border-subtle); gap: 12px; flex-wrap: wrap;
    }}
    .doc-date {{ font-size: 11.5px; color: var(--text-muted); }}
    .doc-open-btn {{
      background: linear-gradient(135deg, #0284c7, #2563eb); color: #fff;
      font-size: 12px; font-weight: 700; padding: 8px 16px; border-radius: var(--radius-sm);
      text-decoration: none; transition: all 0.2s; display: inline-flex; align-items: center; gap: 6px;
    }}
    .doc-open-btn:hover {{ box-shadow: 0 4px 14px rgba(37, 99, 235, 0.5); transform: translateY(-1px); }}
    
    /* Footer */
    footer {{
      text-align: center; color: var(--text-muted); font-size: 13px; margin-top: 60px; padding-top: 24px;
      border-top: 1px solid var(--border-subtle);
    }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">Studio Hub</span>
      <div class="header-title">🎬 Kho Quản Trị Bảng Phân Cảnh & Kịch Bản Thực Chiến</div>
    </div>
    <div class="header-controls">
      <a href="9_kich_ban_thuc_chien.html" class="header-link">📑 9 Kịch Bản Gốc</a>
      <a href="kich_ban_phong_nha.html" class="header-link">🎙️ Kịch Bản Phong Nha</a>
      <a href="https://fedu.vn/scene.html" target="_blank" class="header-link">🌐 Scene Hub</a>
    </div>
  </header>

  <div class="container">
    <!-- Hero -->
    <section class="hero">
      <div class="hero-badge">⚡ Master Storyboard & Script Repository</div>
      <h1>Kho Bảng Phân Cảnh & Kịch Bản Thực Chiến</h1>
      <p class="hero-desc">
        Hệ thống Storyboard Studio chuẩn điện ảnh 9:16 ứng dụng công thức băm nhỏ <b>3 Micro-Beats</b> (Đầu cảnh • Cao trào • Mồi chuyển) cho từng cảnh quay 30 giây.
        Đầy đủ các bản thiết kế visual storyboard và toàn bộ tài liệu kịch bản gốc.
      </p>
      
      <div class="stats-grid">
        <div class="stat-item">
          <div class="stat-num">{total_all_files}</div>
          <div class="stat-label">Tổng Số File HTML</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">{total_storyboards}</div>
          <div class="stat-label">Bảng Phân Cảnh 9:16</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">{total_scenes}</div>
          <div class="stat-label">Phân Cảnh Quay</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">{total_docs}</div>
          <div class="stat-label">Tài Liệu Kịch Bản Gốc</div>
        </div>
      </div>
    </section>

    <!-- SECTION 1: VISUAL STORYBOARDS 9:16 -->
    <div class="section-header" id="storyboards-sec">
      <div>
        <h2 class="section-title">🎬 Bảng Phân Cảnh Điện Ảnh 9:16 ({total_storyboards} Kịch Bản)</h2>
        <div class="section-sub">Bảng phân cảnh chi tiết 3 nhịp Micro-Beats, thông số góc máy, động tác, bố cục và lời thoại</div>
      </div>
    </div>

    <div class="boards-grid">
      {cards_html}
    </div>

    <!-- SECTION 2: TEXT DOCUMENTS & RAW SCRIPTS -->
    <div class="section-header" id="docs-sec" style="margin-top: 60px;">
      <div>
        <h2 class="section-title">📑 Kho Kịch Bản Văn Bản & Tài Liệu Gốc ({total_docs} Tài Liệu)</h2>
        <div class="section-sub">Tài liệu kịch bản 3 tầng sự thật, bản đồ tư duy, kịch bản voice-over phân đoạn</div>
      </div>
    </div>

    <div class="docs-grid">
      {docs_html}
    </div>

    <footer>
      <p>🎬 Hệ Thống Bảng Phân Cảnh Điện Ảnh AI &bull; vietndj.github.io/Bang-Phan-Canh &bull; Cloudflare R2 CDN</p>
    </footer>

  </div>

</body>
</html>
"""

# Ghi đè build_master_index.py trong repo
with open(os.path.join(REPO_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(full_index_html)

print("✅ Đã tạo thành công Master Hub index.html hiển thị đầy đủ TẤT CẢ các file HTML!")
