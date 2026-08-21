import os
import json
from datetime import datetime

storyboards = [
    {
        "id": "kb01",
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
        "id": "kb02",
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
        "id": "kb03",
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
    }
]

total_scenes = sum(s["scenes_count"] for s in storyboards)
total_beats = sum(s["beats_count"] for s in storyboards)
total_duration_sec = len(storyboards) * 30

cards_html = ""
for s in storyboards:
    mini_html = "".join([f'<img src="{img}" alt="beat frame" loading="lazy">' for img in s["mini_frames"]])
    cards_html += f"""
      <article class="board-card">
        <div class="card-media">
          <img src="{s['thumb_url']}" alt="{s['title']}" class="card-thumb" loading="lazy">
          <div class="card-badge" style="background: {s['badge_color']}; color: #000;">{s['category']}</div>
          <div class="card-duration">⏱️ {s['duration']} • {s['scenes_count']} Cảnh</div>
        </div>
        
        <div class="card-body">
          <h2 class="card-title"><a href="{s['file_name']}">{s['title']}</a></h2>
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

html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kho Bảng Phân Cảnh Điện Ảnh 9:16 | Storyboard Hub</title>
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
      max-width: 780px; margin: 0 auto 24px auto; color: var(--text-secondary); font-size: 14px; line-height: 1.7;
    }}
    
    /* Stats Bar */
    .stats-grid {{
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;
      max-width: 900px; margin: 0 auto;
    }}
    @media (max-width: 768px) {{ .stats-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    .stat-item {{
      background: rgba(0, 0, 0, 0.35); border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm); padding: 12px 16px;
    }}
    .stat-num {{ font-size: 22px; font-weight: 800; color: var(--cyan); font-family: 'JetBrains Mono', monospace; }}
    .stat-label {{ font-size: 11.5px; color: var(--text-muted); font-weight: 600; text-transform: uppercase; margin-top: 2px; }}
    
    /* Grid of Storyboards */
    .section-header {{
      display: flex; justify-content: space-between; align-items: flex-end;
      margin: 40px 0 20px 0; padding-bottom: 12px; border-bottom: 1px solid var(--border-subtle);
    }}
    .section-title {{ font-size: 20px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 8px; }}
    .section-sub {{ font-size: 13px; color: var(--text-muted); }}
    
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
      width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;
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
  </style>
</head>
<body>

  <!-- Top Header -->
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">Studio Hub</span>
      <div class="header-title">🎬 Kho Quản Trị Bảng Phân Cảnh Điện Ảnh 9:16</div>
    </div>
    <div class="header-controls">
      <a href="https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/9_kich_ban_thuc_chien.html" target="_blank" class="header-link">📄 9 Kịch Bản Gốc</a>
      <a href="https://fedu.vn/scene.html" target="_blank" class="header-link">🌐 Đạo Diễn Scene Hub</a>
    </div>
  </header>

  <div class="container">
    <!-- Hero -->
    <section class="hero">
      <div class="hero-badge">⚡ Master Storyboard Repository</div>
      <h1>Kho Bảng Phân Cảnh Điện Ảnh 9:16</h1>
      <p class="hero-desc">
        Hệ thống Storyboard chuẩn Studio ứng dụng công thức phân rã <b>3 Micro-Beats</b> (Đầu cảnh • Cao trào • Mồi chuyển) cho từng phân cảnh 30 giây. 
        Đồng bộ hình ảnh trực tiếp qua Cloudflare R2 CDN và xuất bản trực tuyến trên GitHub Pages.
      </p>
      
      <div class="stats-grid">
        <div class="stat-item">
          <div class="stat-num">{len(storyboards)}</div>
          <div class="stat-label">Kịch Bản Đã Lên Bảng</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">{total_scenes}</div>
          <div class="stat-label">Phân Cảnh Quay</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">{total_beats}</div>
          <div class="stat-label">Micro-Beats Đạo Diễn</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">{total_duration_sec}s</div>
          <div class="stat-label">Tổng Thời Lượng</div>
        </div>
      </div>
    </section>

    <!-- Content Grid -->
    <div class="section-header">
      <div>
        <h2 class="section-title">🎬 Danh Sách Bảng Phân Cảnh Trực Tuyến</h2>
        <div class="section-sub">Tra cứu thông số góc máy, động tác máy, bố cục và lời thoại từng micro-beat</div>
      </div>
    </div>

    <div class="boards-grid">
      {cards_html}
    </div>
  </div>

</body>
</html>
"""

with open("/Users/vietmac/Documents/CODE/Bang-Phan-Canh/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã cập nhật thành công Master Hub index.html!")
