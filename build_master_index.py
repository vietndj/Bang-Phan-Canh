#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tự động biên dịch Master Hub Quản Trị Bảng Phân Cảnh (index.html)
Hiển thị ĐẦY ĐỦ 100% tất cả các file HTML trong dự án với ẢNH ĐỘC LẬP TỪNG DỰ ÁN.
"""

import os
import json
from datetime import datetime

REPO_DIR = "/Users/vietmac/Documents/CODE/Bang-Phan-Canh"

# -------------------------------------------------------------
# 1. DANH SÁCH BẢNG PHÂN CẢNH 9:16 (VISUAL STORYBOARDS) - 100% ẢNH ĐỘC LẬP
# -------------------------------------------------------------
storyboards = [
    {
        "id": "kb_nguyet_store_hp",
        "slug": "kich_ban_nguyet_store_hai_phong",
        "file_name": "kich_ban_nguyet_store_hai_phong.html",
        "title": "Kịch Bản Thực Chiến: Nguyệt Store Hải Phòng (5 Video B-Roll Theo Beat)",
        "category": "Bán Lẻ Công Nghệ & Điện Thoại Cũ",
        "badge_color": "#06b6d4",
        "target_audience": "Cửa hàng điện thoại tại Hải Phòng, bán iPhone/iPad/Watch Like New",
        "duration": "18 - 22 Giây / Video",
        "scenes_count": 5,
        "beats_count": 16,
        "rhythm": "1.5s / Beat (Kick/Snare + ASMR)",
        "thumb_url": "assets/kb1_c1.jpg",
        "summary": "Bộ 5 kịch bản video bán lẻ công nghệ ít thoại, cắt theo nhịp beat nhạc và ASMR vật lý (Ốc zin, True Tone, 3uTools, Thu cũ đổi mới, Vạch khuyết điểm trừ 1 triệu, Đóng gói hỏa tốc Hải Phòng).",
        "hook_dialogue": "15 Pro Max Like New Có Zin Như Lời Đồn?",
        "cta_dialogue": "Bảo hành lỗi 1 đổi 1 tận nơi Hải Phòng • Nhận hàng check zin mới trả tiền.",
        "mini_frames": [
            "assets/kb1_c1.jpg",
            "assets/kb1_c2.jpg",
            "assets/kb2_c2.jpg",
            "assets/kb3_c2.jpg",
            "assets/kb4_c2.jpg"
        ],
        "created_at": "22/08/2026",
        "source": "Học Viên Nguyệt • Hải Phòng"
    },
    {
        "id": "kb01_master",
        "slug": "tu_dot_tien_den_tu_tin_xuat_hien",
        "file_name": "tu_dot_tien_den_tu_tin_xuat_hien.html",
        "title": "Kịch Bản Gốc: Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện",
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
        "source": "Kịch Bản Thực Chiến Demo Gốc"
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
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_01_ngoi_ca_phe_10h_toi/assets/frames/scene1_beat1.jpg",
        "summary": "Bóc trần thói quen 'cố tỏ ra bận rộn' để xoa dịu nỗi sợ tụt hậu. Cày đêm không phải vì đam mê mà là liều thuốc an thần cho sự bất an của chính mình.",
        "hook_dialogue": "10h tối, ngồi ở góc quán này không phải vì chăm chỉ...",
        "cta_dialogue": "Nhiều khi cố cày đêm không phải để giàu lên, mà chỉ là liều thuốc an thần cho sự bất an của chính mình.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_01_ngoi_ca_phe_10h_toi/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_01_ngoi_ca_phe_10h_toi/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_01_ngoi_ca_phe_10h_toi/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_01_ngoi_ca_phe_10h_toi/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_01_ngoi_ca_phe_10h_toi/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb01)"
    },
    {
        "id": "kb02_master",
        "slug": "tien_mat_bang_va_cua_hang_vang_khach",
        "file_name": "kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach.html",
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
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_03_chung_lai_sau_tuoi_30/assets/frames/scene1_beat1.jpg",
        "summary": "Khủng hoảng tuổi 30 của người làm văn phòng khi thu nhập đứng yên mà chi phí tăng. Nỗi sợ bị bỏ lại phía sau trước làn sóng công nghệ mới và quyết tâm học lại từ đầu.",
        "hook_dialogue": "Hơn 30 tuổi, ngồi trong căn phòng này cùng mọi người...",
        "cta_dialogue": "Bớt ngại đi, chịu khó học lại từ đầu còn hơn cứ ngồi yên nhìn công việc của mình đi xuống.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_03_chung_lai_sau_tuoi_30/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_03_chung_lai_sau_tuoi_30/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_03_chung_lai_sau_tuoi_30/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_03_chung_lai_sau_tuoi_30/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_03_chung_lai_sau_tuoi_30/assets/frames/scene5_beat1.jpg"
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
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_04_tien_quang_cao_an_het_tien_lai/assets/frames/scene1_beat1.jpg",
        "summary": "Bế tắc vì chi phí quảng cáo tăng phi mã nhưng không dám tắt ads. Lựa chọn dũng cảm: Thay vì đổ tiền nuôi nền tảng thì tự học cách xuất hiện để kéo khách tự nhiên.",
        "hook_dialogue": "Cứ 5 phút tôi lại mở màn hình điện thoại kiểm tra một lần...",
        "cta_dialogue": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_04_tien_quang_cao_an_het_tien_lai/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_04_tien_quang_cao_an_het_tien_lai/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_04_tien_quang_cao_an_het_tien_lai/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_04_tien_quang_cao_an_het_tien_lai/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_04_tien_quang_cao_an_het_tien_lai/assets/frames/scene5_beat1.jpg"
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
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_05_het_khach_tu_moi_quan_he_quen/assets/frames/scene1_beat1.jpg",
        "summary": "Nỗi ngại ngùng khi chào mời người quen ủng hộ đã đến giới hạn. Nhận ra giá trị của việc làm nội dung để người lạ tự tìm đến và đặt niềm tin.",
        "hook_dialogue": "Lướt danh bạ điện thoại từ trên xuống dưới mà không biết nhắn cho ai...",
        "cta_dialogue": "Phải tự học cách tiếp cận người lạ bằng nội dung tử tế thôi.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_05_het_khach_tu_moi_quan_he_quen/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_05_het_khach_tu_moi_quan_he_quen/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_05_het_khach_tu_moi_quan_he_quen/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_05_het_khach_tu_moi_quan_he_quen/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_05_het_khach_tu_moi_quan_he_quen/assets/frames/scene5_beat1.jpg"
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
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_06_tay_nghe_tot_nhung_van_vang_khach/assets/frames/scene1_beat1.jpg",
        "summary": "Nghịch lý 'hữu xạ tự nhiên hương' không còn đúng trong thời đại số. Giỏi nghề thôi chưa đủ, phải biết cách cho khách hàng thấy sự tâm huyết và kỹ lưỡng của mình.",
        "hook_dialogue": "Làm nghề mười mấy năm, đồ mình làm ra tự tin không thua ai...",
        "cta_dialogue": "Giỏi nghề mà giữ trong xưởng thì không ai biết, phải tự đưa nghề ra ánh sáng.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_06_tay_nghe_tot_nhung_van_vang_khach/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_06_tay_nghe_tot_nhung_van_vang_khach/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_06_tay_nghe_tot_nhung_van_vang_khach/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_06_tay_nghe_tot_nhung_van_vang_khach/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_06_tay_nghe_tot_nhung_van_vang_khach/assets/frames/scene5_beat1.jpg"
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
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc/assets/frames/scene1_beat1.jpg",
        "summary": "Không thể đua giá rẻ với các tổng kho và sàn thương mại điện tử. Con đường sống sót duy nhất là bán trải nghiệm, dịch vụ tận tâm và sự đồng hành của người bán.",
        "hook_dialogue": "Khách cầm điện thoại vào hỏi: 'Sao bên kia bán rẻ hơn anh mấy chục ngàn?'...",
        "cta_dialogue": "Không đua giá được thì phải bán bằng sự tận tụy và uy tín của chính mình.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc/assets/frames/scene5_beat1.jpg"
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
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_08_bat_dau_lai_tu_con_so_0/assets/frames/scene1_beat1.jpg",
        "summary": "Tâm thế làm lại từ đầu sau cú vấp ngã. Không còn ảo tưởng về vốn lớn, tập trung vào mô hình tinh gọn, chi phí thấp và tự làm chủ truyền thông.",
        "hook_dialogue": "Đóng cửa cửa hàng cũ, trong tay gần như về lại số 0...",
        "cta_dialogue": "Ngã ở đâu thì đứng lên ở đó, lần này làm chuẩn từ gốc không vội vàng.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_08_bat_dau_lai_tu_con_so_0/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_08_bat_dau_lai_tu_con_so_0/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_08_bat_dau_lai_tu_con_so_0/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_08_bat_dau_lai_tu_con_so_0/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_08_bat_dau_lai_tu_con_so_0/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb08)"
    },
    {
        "id": "kb09_series",
        "slug": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia",
        "file_name": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html",
        "title": "Kịch Bản 09: Hàng Làm Kỹ Nhưng Bị So Sánh Giá",
        "category": "Chất Lượng & Định Vị Cao Cấp",
        "badge_color": "#f97316",
        "target_audience": "Chủ xưởng sản xuất, người làm hàng thủ công / kỹ nghệ tâm huyết",
        "duration": "30 Giây",
        "scenes_count": 5,
        "beats_count": 15,
        "rhythm": "1.5s / Beat (J-Cut -0.4s)",
        "thumb_url": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia/assets/frames/scene1_beat1.jpg",
        "summary": "Nỗi đau hàng làm kỹ, nguyên liệu xịn nhưng bị khách ép giá với hàng chợ giá rẻ. Chiến lược quay lại quy trình chế tác công phu để chứng minh giá trị thực.",
        "hook_dialogue": "Nhập nguyên liệu xịn, làm từng chi tiết cẩn thận... nhưng khách chỉ hỏi 'Sao đắt thế?'...",
        "cta_dialogue": "Thay vì ngồi bực mình khi bị so sánh, tôi chọn quay lại từng công đoạn thật để khách tự nhìn thấy giá trị.",
        "mini_frames": [
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia/assets/frames/scene1_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia/assets/frames/scene2_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia/assets/frames/scene3_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia/assets/frames/scene4_beat1.jpg",
            "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia/assets/frames/scene5_beat1.jpg"
        ],
        "created_at": "21/08/2026",
        "source": "9 Kịch Bản Thực Chiến (#kb09)"
    }
]

# -------------------------------------------------------------
# 2. DANH SÁCH TÀI LIỆU KỊCH BẢN & TEXT DOCUMENTS
# -------------------------------------------------------------
documents = [
    {
        "id": "doc_9kb_raw",
        "file_name": "9_kich_ban_thuc_chien.html",
        "title": "9 Kịch Bản Thực Chiến 3 Tầng Sự Thật (Toàn Tập)",
        "badge_text": "KHO KỊCH BẢN GỐC",
        "badge_color": "#38bdf8",
        "target": "Chủ doanh nghiệp, Content Creator, Chuyên gia",
        "format": "Interactive HTML Table • 9 Kịch Bản • 3 Tầng Sự Thật",
        "summary": "Bộ tài liệu tổng hợp 9 kịch bản short-form 30s bóc tách 3 tầng tâm lý (Đãi bôi ➔ Cảm giác thật ➔ Ngượng miệng). Kèm lời thoại phân cảnh mẫu và bối cảnh quay thực tế.",
        "highlights": [
            "Bóc tách 3 tầng sự thật",
            "Trọn bộ 9 kịch bản mẫu 30s",
            "Bảng phân tích lời thoại chi tiết",
            "Ánh xạ bối cảnh quay thực tế"
        ],
        "created_at": "21/08/2026",
        "icon": "📑"
    },
    {
        "id": "doc_phong_nha",
        "file_name": "kich_ban_phong_nha.html",
        "title": "Bảng Kịch Bản Voice-Over Thực Chiến - Góc Phòng & Ban Công",
        "badge_text": "KỊCH BẢN VOICE-OVER",
        "badge_color": "#10b981",
        "target": "Người tự quay tại nhà, Bối cảnh ban công & Phòng làm việc",
        "format": "Phân cảnh Voice-Over & Visual Map",
        "summary": "Kịch bản mẫu khai thác không gian thực tế tại nhà (Góc phòng làm việc, bàn gỗ, ban công chung cư) kết hợp kỹ thuật thu âm giọng đọc và băm nhịp hình ảnh.",
        "highlights": [
            "Bối cảnh nhà ở & ban công",
            "Phân đoạn voice-over chi tiết",
            "Kỹ thuật thu âm thực chiến",
            "Góc máy tối giản 1 người quay"
        ],
        "created_at": "21/08/2026",
        "icon": "🎙️"
    }
]

total_storyboards = len(storyboards)
total_docs = len(documents)
total_all_files = total_storyboards + total_docs
total_scenes = sum(s["scenes_count"] for s in storyboards)
total_beats = sum(s["beats_count"] for s in storyboards)

# -------------------------------------------------------------
# 3. RENDER CARDS HTML
# -------------------------------------------------------------
cards_html = ""
for sb in storyboards:
    mini_strip = ""
    for mf in sb["mini_frames"]:
        mini_strip += f'<div class="strip-thumb"><img src="{mf}" alt="frame" loading="lazy"></div>\n'
        
    cards_html += f"""
    <article class="board-card" data-category="{sb['category']}">
      <div class="card-header">
        <div class="thumb-box">
          <img src="{sb['thumb_url']}" alt="{sb['title']}" loading="lazy">
          <span class="thumb-badge">{sb['duration']}</span>
        </div>
        <div class="card-header-info">
          <span class="category-pill" style="background: {sb['badge_color']}20; color: {sb['badge_color']}; border-color: {sb['badge_color']}40;">
            {sb['category']}
          </span>
          <h3 class="card-title"><a href="{sb['file_name']}">{sb['title']}</a></h3>
          <div class="card-target">🎯 <b>Đối tượng:</b> {sb['target_audience']}</div>
          <div class="card-chips">
            <span class="chip">⏱️ {sb['scenes_count']} Cảnh • {sb['beats_count']} Beats</span>
            <span class="chip">⚡ {sb['rhythm']}</span>
          </div>
        </div>
      </div>
      
      <div class="card-body">
        <p class="card-summary">{sb['summary']}</p>
        <div class="quote-box">
          <div class="quote-label">🎙️ Hook Mở Màn:</div>
          <div class="quote-text">"{sb['hook_dialogue']}"</div>
        </div>
        
        <div class="strip-box">
          <div class="strip-label">🎞️ 5 Phân Cảnh Trọng Tâm (3-Beat Rhythm):</div>
          <div class="strip-frames">
            {mini_strip}
          </div>
        </div>
      </div>
      
      <div class="card-footer">
        <div class="card-meta">
          <span>📅 {sb['created_at']}</span>
          <span>•</span>
          <span>📑 {sb['source']}</span>
        </div>
        <a href="{sb['file_name']}" class="open-btn">Xem Phân Cảnh Chi Tiết ➔</a>
      </div>
    </article>
"""

docs_html = ""
for doc in documents:
    hl_items = "".join([f"<li>✓ {hl}</li>" for hl in doc["highlights"]])
    docs_html += f"""
    <article class="doc-card">
      <div class="doc-header">
        <div class="doc-icon-badge">{doc['icon']}</div>
        <div class="doc-title-group">
          <span class="doc-badge" style="background: {doc['badge_color']}20; color: {doc['badge_color']}; border-color: {doc['badge_color']}50;">
            {doc['badge_text']}
          </span>
          <h3 class="doc-title"><a href="{doc['file_name']}">{doc['title']}</a></h3>
        </div>
      </div>
      
      <div class="doc-body">
        <div class="doc-meta-bar">
          <div>🎯 <b>Đối tượng:</b> {doc['target']}</div>
          <div>📄 <b>Định dạng:</b> {doc['format']}</div>
        </div>
        
        <p class="doc-summary">{doc['summary']}</p>
        
        <div class="doc-highlights-box">
          <div class="doc-hl-title">⚡ Nội Dung Nổi Bật:</div>
          <ul class="doc-hl-list">
            {hl_items}
          </ul>
        </div>
      </div>
      
      <div class="doc-footer">
        <span class="doc-date">📅 Cập nhật: {doc['created_at']}</span>
        <a href="{doc['file_name']}" class="doc-open-btn">
          Mở Tài Liệu Toàn Văn ➔
        </a>
      </div>
    </article>
"""

full_index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>Kho Quản Trị Bảng Phân Cảnh & Kịch Bản Thực Chiến | Storyboard Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #060911;
      --bg-surface: #0c121e;
      --bg-card: #111a2b;
      --bg-card-hover: #17243c;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.35);
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.15);
      --amber: #f59e0b;
      --emerald: #10b981;
      --rose: #f43f5e;
      --indigo: #818cf8;
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
    .container {{ max-width: 1380px; margin: 0 auto; padding: 0 20px; }}
    
    /* Top Header */
    .top-header {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(6, 9, 17, 0.94);
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
    
    /* Hero */
    .hero {{
      background: linear-gradient(180deg, #0f172a 0%, #090e1a 100%);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      margin: 28px 0 36px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    .hero-badge {{
      display: inline-flex; align-items: center; gap: 6px;
      background: var(--cyan-glow); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 14px; border-radius: 9999px; font-size: 12px; font-weight: 700; margin-bottom: 12px;
    }}
    .hero h1 {{
      font-size: 32px; font-weight: 800; color: #fff; margin-bottom: 12px; line-height: 1.3;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hero-desc {{ color: var(--text-secondary); font-size: 15px; max-width: 820px; margin: 0 auto 24px; }}
    
    .stats-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 14px;
      background: rgba(0, 0, 0, 0.4); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 16px 20px;
    }}
    .stat-item {{ text-align: center; }}
    .stat-num {{ font-size: 24px; font-weight: 800; color: var(--text-primary); font-family: 'JetBrains Mono', monospace; }}
    .stat-label {{ font-size: 11px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; margin-top: 2px; }}
    
    /* Section Headings */
    .section-header {{
      display: flex; justify-content: space-between; align-items: flex-end;
      margin-bottom: 20px; padding-bottom: 12px; border-bottom: 1px solid var(--border-subtle);
    }}
    .section-title {{ font-size: 20px; font-weight: 800; color: #fff; }}
    .section-sub {{ font-size: 13px; color: var(--text-muted); margin-top: 4px; }}
    
    /* Boards Grid */
    .boards-grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(440px, 1fr)); gap: 24px;
    }}
    @media (max-width: 900px) {{ .boards-grid {{ grid-template-columns: 1fr; }} }}
    
    .board-card {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
      padding: 20px; display: flex; flex-direction: column; transition: all 0.25s ease;
    }}
    .board-card:hover {{
      border-color: var(--border-accent); box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45); transform: translateY(-3px);
    }}
    
    .card-header {{ display: flex; gap: 16px; margin-bottom: 16px; }}
    .thumb-box {{
      flex: 0 0 110px; aspect-ratio: 9 / 16; border-radius: var(--radius-sm); overflow: hidden;
      background: #000; position: relative; border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .thumb-box img {{ width: 100%; height: 100%; object-fit: cover; }}
    .thumb-badge {{
      position: absolute; bottom: 6px; right: 6px; background: rgba(0, 0, 0, 0.8);
      font-size: 9px; font-weight: 700; padding: 2px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; color: #fff;
    }}
    
    .card-header-info {{ flex: 1; display: flex; flex-direction: column; }}
    .category-pill {{
      display: inline-block; font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 4px;
      border: 1px solid; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.5px; width: fit-content;
    }}
    .card-title {{ font-size: 16px; font-weight: 800; line-height: 1.35; margin-bottom: 6px; }}
    .card-title a {{ color: #fff; text-decoration: none; }}
    .card-title a:hover {{ color: var(--cyan); }}
    .card-target {{ font-size: 11.5px; color: var(--text-muted); margin-bottom: 8px; }}
    .card-chips {{ display: flex; gap: 6px; flex-wrap: wrap; margin-top: auto; }}
    .chip {{
      background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-secondary); font-size: 10.5px; font-weight: 600; padding: 2px 6px; border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
    }}
    
    .card-body {{ display: flex; flex-direction: column; flex: 1; gap: 12px; margin-bottom: 16px; }}
    .card-summary {{ font-size: 12.5px; color: #cbd5e1; line-height: 1.5; }}
    
    .quote-box {{
      background: rgba(0, 0, 0, 0.3); border-left: 3px solid var(--cyan); padding: 8px 12px; border-radius: 0 6px 6px 0;
    }}
    .quote-label {{ font-size: 10px; font-weight: 700; color: var(--cyan); text-transform: uppercase; margin-bottom: 2px; }}
    .quote-text {{ font-size: 12px; color: #fff; font-style: italic; font-weight: 600; }}
    
    .strip-box {{}}
    .strip-label {{ font-size: 10.5px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px; }}
    .strip-frames {{ display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px; }}
    .strip-thumb {{
      flex: 0 0 54px; aspect-ratio: 9 / 16; border-radius: 4px; overflow: hidden; background: #000;
      border: 1px solid rgba(255, 255, 255, 0.08); flex-shrink: 0;
    }}
    .strip-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
    
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
    
    /* Text Documents Cards */
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
        Đầy đủ 100% hình ảnh độc lập, chân thực cho từng dự án.
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
        <div class="section-sub">Bảng phân cảnh chi tiết 3 nhịp Micro-Beats, thông số góc máy, động tác, bố cục và hình ảnh độc lập cho từng kịch bản</div>
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

# Ghi đè index.html trong repo
with open(os.path.join(REPO_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(full_index_html)

print("✅ Đã tạo thành công Master Hub index.html với 100% hình ảnh độc lập cho từng dự án!")
