import os
import json
from datetime import datetime

storyboards = [
    {
        "id": "kb01",
        "slug": "tu_dot_tien_den_tu_tin_xuat_hien",
        "file_name": "tu_dot_tien_den_tu_tin_xuat_hien.html",
        "title": "Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện",
        "category": "Kinh Doanh & Bán Hàng",
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
        "source": "Chat Antigravity / Telegram Bot"
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
        "source": "9 Kịch Bản Thực Chiến (Link Online)"
    }
]

total_scenes = sum(s["scenes_count"] for s in storyboards)
total_beats = sum(s["beats_count"] for s in storyboards)
total_duration_sec = len(storyboards) * 30

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
      color: var(--text-secondary); font-size: 15px; max-width: 780px; margin: 0 auto 24px;
    }}
    
    /* Stats Bar */
    .stats-bar {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px;
      background: rgba(0, 0, 0, 0.3); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 16px 20px;
    }}
    .stat-item {{ text-align: center; }}
    .stat-label {{ font-size: 11px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; margin-bottom: 4px; }}
    .stat-val {{ font-size: 22px; font-weight: 800; color: var(--text-primary); }}
    
    /* Search & Filter Bar */
    .filter-bar {{
      display: flex; justify-content: space-between; align-items: center; gap: 16px; margin: 32px 0 20px; flex-wrap: wrap;
    }}
    .search-box {{
      position: relative; flex: 1; min-width: 260px; max-width: 400px;
    }}
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
      flex: 0 0 130px; height: 180px; border-radius: var(--radius-md); overflow: hidden; position: relative; background: #000;
    }}
    .card-thumb-wrap img {{ width: 100%; height: 100%; object-fit: cover; }}
    .card-thumb-badge {{
      position: absolute; top: 6px; left: 6px; background: rgba(0, 0, 0, 0.75); color: #fff;
      font-size: 9.5px; font-weight: 700; padding: 2px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace;
    }}
    
    .card-info {{ flex: 1; display: flex; flex-direction: column; justify-content: space-between; }}
    .card-category-badge {{
      display: inline-block; font-size: 10.5px; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-bottom: 6px;
      text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .card-title {{ font-size: 18px; font-weight: 800; color: #fff; margin-bottom: 6px; line-height: 1.3; }}
    .card-target {{ font-size: 11.5px; color: var(--text-muted); margin-bottom: 10px; }}
    .card-meta-chips {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 6px; }}
    .chip {{
      background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.08); color: var(--text-secondary);
      font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; font-family: 'JetBrains Mono', monospace;
    }}
    
    .card-body {{ padding: 18px 22px; flex: 1; display: flex; flex-direction: column; gap: 14px; }}
    .summary-text {{ font-size: 13px; color: #cbd5e1; line-height: 1.5; }}
    
    .hook-quote-box {{
      background: rgba(0, 0, 0, 0.25); border-left: 3px solid var(--cyan); padding: 8px 12px; border-radius: 0 6px 6px 0; font-size: 12px;
    }}
    .hook-quote-label {{ font-size: 10px; font-weight: 700; color: var(--cyan); text-transform: uppercase; margin-bottom: 2px; }}
    .hook-quote-text {{ color: #fff; font-style: italic; font-weight: 600; }}
    
    .mini-filmstrip-label {{ font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; }}
    .mini-filmstrip {{ display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px; }}
    .mini-frame-thumb {{ flex: 0 0 60px; height: 80px; border-radius: 4px; overflow: hidden; background: #000; border: 1px solid var(--border-subtle); }}
    .mini-frame-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
    
    .card-footer {{
      padding: 14px 22px; background: rgba(0, 0, 0, 0.2); border-top: 1px solid var(--border-subtle);
      display: flex; justify-content: space-between; align-items: center; gap: 10px; flex-wrap: wrap;
    }}
    .btn-view-primary {{
      background: linear-gradient(135deg, #0284c7, #2563eb); color: #fff; font-size: 12.5px; font-weight: 700;
      padding: 8px 18px; border-radius: var(--radius-sm); text-decoration: none; display: inline-flex; align-items: center; gap: 6px;
      transition: all 0.2s;
    }}
    .btn-view-primary:hover {{ background: linear-gradient(135deg, #38bdf8, #0284c7); color: #000; }}
    
    .btn-sub-link {{
      color: var(--text-secondary); font-size: 12px; font-weight: 600; text-decoration: none; padding: 6px 10px; border-radius: 4px;
      transition: color 0.2s;
    }}
    .btn-sub-link:hover {{ color: var(--cyan); }}
    
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
          <div class="stat-label">Lưu Trữ Media</div>
          <div class="stat-val" style="color: var(--cyan);">Cloudflare R2</div>
        </div>
      </div>
    </section>

    <!-- Search & Filter -->
    <div class="filter-bar">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm kịch bản, lời thoại, chủ đề..." onkeyup="filterCards()">
      </div>
      <div class="filter-tags">
        <span class="filter-tag active" onclick="filterCategory('all', this)">Tất cả ({len(storyboards)})</span>
        <span class="filter-tag" onclick="filterCategory('Kinh Doanh', this)">Kinh Doanh & Bán Hàng</span>
        <span class="filter-tag" onclick="filterCategory('Phát Triển', this)">Phát Triển Bản Thân</span>
      </div>
    </div>

    <!-- Storyboards Grid -->
    <div class="storyboards-grid" id="storyboardList">
"""

for sb in storyboards:
    html += f"""
      <article class="sb-card" data-category="{sb['category']}" data-title="{sb['title'].lower()}" data-summary="{sb['summary'].lower()}">
        <div class="card-top">
          <div class="card-thumb-wrap">
            <img src="{sb['thumb_url']}" alt="{sb['title']}">
            <span class="card-thumb-badge">{sb['duration']}</span>
          </div>
          <div class="card-info">
            <div>
              <span class="card-category-badge" style="background: {sb['badge_color']}20; color: {sb['badge_color']}; border: 1px solid {sb['badge_color']}40;">
                {sb['category']}
              </span>
              <h2 class="card-title">{sb['title']}</h2>
              <div class="card-target">🎯 <b>Đối tượng:</b> {sb['target_audience']}</div>
            </div>
            <div class="card-meta-chips">
              <span class="chip">⏱️ {sb['scenes_count']} Cảnh • {sb['beats_count']} Beats</span>
              <span class="chip">⚡ {sb['rhythm']}</span>
              <span class="chip">📅 {sb['created_at']}</span>
            </div>
          </div>
        </div>

        <div class="card-body">
          <p class="summary-text">{sb['summary']}</p>
          
          <div class="hook-quote-box">
            <div class="hook-quote-label">🎙️ Câu Mở Đầu (Hook):</div>
            <div class="hook-quote-text">"{sb['hook_dialogue']}"</div>
          </div>

          <div>
            <div class="mini-filmstrip-label" style="margin-bottom: 6px;">🎞️ Preview 5 Cảnh Chính:</div>
            <div class="mini-filmstrip">
"""
    for mf in sb['mini_frames']:
        html += f"""              <div class="mini-frame-thumb"><img src="{mf}" alt="frame"></div>\n"""
        
    html += f"""            </div>
          </div>
        </div>

        <div class="card-footer">
          <a href="{sb['file_name']}" class="btn-view-primary">
            📱 Xem Bảng Phân Cảnh Đầy Đủ ➔
          </a>
          <div style="display: flex; gap: 4px;">
            <a href="https://fedu.vn/Bang-Phan-Canh/{sb['file_name']}" class="btn-sub-link">🌐 Cổng fedu.vn</a>
          </div>
        </div>
      </article>
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
    function filterCards() {
      const q = document.getElementById('searchInput').value.toLowerCase();
      const cards = document.querySelectorAll('.sb-card');
      cards.forEach(card => {
        const title = card.getAttribute('data-title');
        const summary = card.getAttribute('data-summary');
        if (title.includes(q) || summary.includes(q)) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }

    function filterCategory(cat, el) {
      document.querySelectorAll('.filter-tag').forEach(t => t.classList.remove('active'));
      el.classList.add('active');
      
      const cards = document.querySelectorAll('.sb-card');
      cards.forEach(card => {
        const itemCat = card.getAttribute('data-category');
        if (cat === 'all' || itemCat.includes(cat)) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

index_path = "/Users/vietmac/Documents/CODE/Bang-Phan-Canh/index.html"
with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã tạo Master Hub index.html thành công!")
