#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tự động sinh trang HTML Studio: nguyet.html và nguyệt.html
Trình bày cách làm, kết quả thực tế, mô phỏng hướng dẫn và Mega Prompt 1-click copy.
"""

import os
import shutil

REPO_DIR = "/Users/vietmac/Documents/CODE/offline02"
R2_BASE = "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/nguyet/assets"

MEGA_PROMPT = """Bạn là Giám Đốc Nghệ Thuật (Art Director) & Chuyên Gia Thiết Kế Thumbnail Video AI hàng đầu thế giới.

Nhiệm vụ của bạn là tạo ra các ảnh Poster / Thumbnail Video ngắn dọc (tỉ lệ 9:16) chuẩn nhận diện thương hiệu công nghệ cao cấp theo quy trình 2 bước tương tác:

═══════════════════════════════════════════════════════════════
BƯỚC 1: HỎI THÔNG TIN ĐẦU VÀO TỪ NGƯỜI DÙNG (CHƯA SINH ẢNH NGAY)
═══════════════════════════════════════════════════════════════
Khi tôi gửi prompt này, bạn HÃY TẠM DỪNG và phản hồi lại bằng một lời chào chuyên nghiệp kèm bảng câu hỏi thu thập 3 thông tin sau:

1. ẢNH LOGO & TÊN THƯƠNG HIỆU:
   - Hãy tải lên ảnh Logo PNG tròn (hoặc cho biết chữ cái/biểu tượng đại diện, ví dụ: 'VM', 'AI', 'NOVA').
   - Tên thương hiệu chính (Brand Title) & Câu Slogan phụ bên dưới.

2. NỘI DUNG TEXT TO (HOOK BANNER 2 DÒNG):
   - Dòng 1 (Từ khóa chính màu Vàng Neon): ví dụ "TẠO VIDEO BẰNG AI"
   - Dòng 2 (Nội dung bổ trợ màu Trắng Tinh): ví dụ "X10 TỐC ĐỘ DỰNG PHIM"

3. ẢNH DIỄN GIẢ / FRAME CHỤP TỪ VIDEO:
   - Hãy đính kèm bức ảnh chân dung hoặc ảnh cap màn hình từ video của bạn.

═══════════════════════════════════════════════════════════════
BƯỚC 2: TIẾN HÀNH THIẾT KẾ POSTER CÔNG NGHỆ CHUYÊN NGHIỆP
═══════════════════════════════════════════════════════════════
Ngay khi tôi cung cấp đủ 3 thông tin trên, bạn sẽ tự động thiết kế bức ảnh với quy chuẩn mỹ thuật cao cấp sau:

1. CHỦ THỂ (SUBJECT):
   - Tách sạch 100% nền phía sau người, giữ trọn chi tiết tóc, ngón tay và biểu cảm.
   - Thêm đường viền sticker màu trắng tinh khiết (White Sticker Outline) dày dặn, mịn đẹp bao quanh toàn bộ silhouette.
   - Thêm hiệu ứng đổ bóng mờ Cyber Drop Shadow màu xanh đen mờ ảo phía sau để tạo chiều sâu 3D.
   - Đặt người lùi xuống nửa dưới khung hình để tạo khoảng trống thoáng đãng phía trên.

2. NỀN CÔNG NGHỆ (CYBER TECH BACKGROUND):
   - Tone màu chủ đạo: Deep Obsidian Navy (#04060A đến #090D1A).
   - Hiệu ứng ánh sáng tỏa Radial Glow màu Cyan Neon & Sapphire Blue phía sau logo và sau lưng chủ thể.
   - Họa tiết Dot Matrix tinh xảo và các đường Line Framing công nghệ tinh tế ở 4 góc, tuyệt đối không lem nhem hay bệt màu.

3. HEADER THƯƠNG HIỆU (PHÍA TRÊN CÙNG):
   - Logo tròn với viền kép Cyan Neon phát sáng nhẹ đặt chính giữa trên cùng.
   - Dòng Tên Thương Hiệu in hoa nét cực đậm, màu Trắng sáng (#FFFFFF).
   - Dòng Slogan công nghệ màu Xanh Sky (#38BDF8) đặt ngay dưới tên thương hiệu.

4. HOOK BANNER 2 DÒNG (NGANG NGỰC):
   - Khung thẻ Card Cyber góc bo tròn với nền màu tối đặc (Solid Opaque Dark Slate), viền Cyan phát sáng tinh tế che kín phụ đề cũ.
   - Dòng 1: Chữ in hoa màu Vàng Neon (#FFDE00), font chữ cực dày và nổi bật.
   - Dòng 2: Chữ in hoa màu Trắng Tinh (#FFFFFF).

5. FOOTER:
   - Thanh thông tin mạng xã hội mờ dần ở đáy ảnh gồm avatar logo, tên kênh, audio tag và hashtag.

Hãy xuất ảnh poster 9:16 có độ phân giải cao nhất, màu sắc tương phản sắc nét và bố cục vững chắc."""

html_content = f"""<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quy Trình Tự Động Hóa Poster Video Chuẩn Thương Hiệu & Mega Prompt | VietMac AI Studio</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }},
          colors: {{
            cyber: {{
              950: '#04060a',
              900: '#070a13',
              850: '#0b0f1d',
              800: '#111728',
              700: '#1e293b',
              neon: '#00f0ff',
              gold: '#ffde00',
              blue: '#38bdf8',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      background-color: #04060a;
      color: #e2e8f0;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .glow-cyan {{
      box-shadow: 0 0 40px -10px rgba(0, 240, 255, 0.35);
    }}
    .glow-gold {{
      box-shadow: 0 0 35px -10px rgba(255, 222, 0, 0.4);
    }}
    .tech-border {{
      border: 1px solid rgba(0, 240, 255, 0.2);
    }}
    .glass-card {{
      background: rgba(11, 15, 29, 0.75);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .glass-header {{
      background: rgba(7, 10, 19, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(0, 240, 255, 0.15);
    }}
    pre code {{
      font-family: 'JetBrains Mono', monospace;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-cyan-500 selection:text-black">

  <!-- STICKY TOPBAR -->
  <header class="sticky top-0 z-50 glass-header px-4 lg:px-8 py-3.5 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-blue-600 flex items-center justify-center text-black font-bold text-lg shadow-lg shadow-cyan-500/20">
        AI
      </div>
      <div>
        <h1 class="text-sm lg:text-base font-extrabold tracking-wide text-white flex items-center gap-2">
          BRAND POSTER STUDIO <span class="px-2 py-0.5 text-[10px] uppercase font-bold bg-cyan-500/20 text-cyan-400 border border-cyan-500/40 rounded-full">v2.0 Pro</span>
        </h1>
        <p class="text-xs text-slate-400 hidden sm:block">Quy trình tự động hóa Thumbnail 9:16 & Mega Prompt Gemini Web</p>
      </div>
    </div>
    <div class="flex items-center gap-2.5">
      <a href="#mega-prompt" class="px-3.5 py-1.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-black font-bold text-xs sm:text-sm flex items-center gap-1.5 transition shadow-lg shadow-cyan-500/30">
        <i data-lucide="copy" class="w-4 h-4"></i> Copy Mega Prompt
      </a>
      <a href="https://vietndj.github.io/offline02/" class="px-3 py-1.5 rounded-lg glass-card hover:bg-slate-800 text-slate-300 text-xs sm:text-sm flex items-center gap-1.5 transition">
        <i data-lucide="arrow-left" class="w-4 h-4"></i> Kho Kịch Bản
      </a>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12">

    <!-- HERO SHOWCASE SECTION -->
    <section class="space-y-6">
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/80 border border-cyan-500/30 text-cyan-400 text-xs font-semibold">
          <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Kết Quả Thực Nghiệm & Tự Động Hóa 100%
        </div>
        <h2 class="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
          Chuyển Đổi Video Thô Thành <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-yellow-300">Poster Thương Hiệu 4K</span>
        </h2>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
          Bóc tách frame đắt giá từ video MP4, tách nền AI giữ trọn sợi tóc & ngón tay, tạo viền trắng sticker nổi khối 3D và ghép nền Cyber Studio chống lem nhem.
        </p>
      </div>

      <!-- 3-PHASE TRANSFORMATION CARDS -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4">
        
        <!-- Phase 1 -->
        <div class="glass-card rounded-2xl p-4 flex flex-col space-y-3 transition duration-300 hover:border-slate-600">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-1 text-xs font-bold bg-slate-800 text-slate-300 rounded-lg">BƯỚC 1</span>
            <span class="text-xs text-slate-400 font-mono">22.0s / 4K UHD</span>
          </div>
          <div class="relative aspect-[9/16] rounded-xl overflow-hidden bg-black/60 border border-slate-800 group">
            <img src="{R2_BASE}/frame_goc_22s.jpg" alt="Ảnh Gốc Video" class="w-full h-full object-cover transition duration-500 group-hover:scale-105" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
              <p class="text-xs font-medium text-slate-300">Frame cử chỉ tay mở & nhìn thẳng ống kính</p>
            </div>
          </div>
          <div class="text-center pt-1">
            <h3 class="font-bold text-white text-sm">1. Ảnh Gốc Cap Từ Video</h3>
            <p class="text-xs text-slate-400">Trích xuất tự động qua OpenCV</p>
          </div>
        </div>

        <!-- Phase 2 -->
        <div class="glass-card rounded-2xl p-4 flex flex-col space-y-3 transition duration-300 hover:border-cyan-500/40">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-1 text-xs font-bold bg-cyan-950 text-cyan-400 border border-cyan-500/40 rounded-lg">BƯỚC 2</span>
            <span class="text-xs text-cyan-400 font-mono">U2Net AI Matting</span>
          </div>
          <div class="relative aspect-[9/16] rounded-xl overflow-hidden bg-slate-950 border border-cyan-900/50 group">
            <div class="w-full h-full bg-[radial-gradient(#1e293b_1px,transparent_1px)] [background-size:16px_16px] flex items-center justify-center p-2">
              <img src="{R2_BASE}/cand_cutout_22.0s.png" alt="Tách Nền AI" class="w-full h-full object-contain filter drop-shadow-[0_0_15px_rgba(255,255,255,0.4)] transition duration-500 group-hover:scale-105" loading="lazy">
            </div>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-4">
              <p class="text-xs font-medium text-cyan-200">Tách nền mịn + Viền trắng sticker 32px</p>
            </div>
          </div>
          <div class="text-center pt-1">
            <h3 class="font-bold text-white text-sm">2. AI Tách Nền & Viền Trắng</h3>
            <p class="text-xs text-slate-400">Morphological Dilation + Drop Shadow</p>
          </div>
        </div>

        <!-- Phase 3 -->
        <div class="glass-card rounded-2xl p-4 flex flex-col space-y-3 glow-cyan border-cyan-500/40 transition duration-300">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-1 text-xs font-bold bg-gradient-to-r from-cyan-400 to-yellow-400 text-black rounded-lg font-mono">BƯỚC 3 • MASTER</span>
            <span class="text-xs text-yellow-400 font-mono">2160 x 3840 (4K)</span>
          </div>
          <div class="relative aspect-[9/16] rounded-xl overflow-hidden bg-black group border border-cyan-500/30">
            <img src="{R2_BASE}/vietmac_tech_poster_final.jpg" alt="Poster Hoàn Thiện" class="w-full h-full object-cover transition duration-500 group-hover:scale-105" loading="lazy">
            <div class="absolute top-3 right-3 bg-black/70 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] font-bold text-yellow-300 border border-yellow-500/40">
              CYBER STUDIO PRO
            </div>
          </div>
          <div class="text-center pt-1">
            <h3 class="font-bold text-white text-sm">3. Poster Thương Hiệu 4K</h3>
            <p class="text-xs text-slate-400">Nền Obsidian + Logo + Hook Banner 2 Dòng</p>
          </div>
        </div>

      </div>
    </section>

    <!-- INTERACTIVE SIMULATION SECTION -->
    <section class="glass-card rounded-3xl p-6 sm:p-8 space-y-6 tech-border">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-5">
        <div>
          <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Mô Phỏng Trực Quan 2 Bước</span>
          <h2 class="text-xl sm:text-2xl font-bold text-white flex items-center gap-2 mt-1">
            <i data-lucide="bot" class="w-6 h-6 text-cyan-400"></i> Cách Mega Prompt Hoạt Động Trên Gemini Web
          </h2>
        </div>
        <div class="flex items-center gap-2">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-950 border border-emerald-500/40 text-emerald-400 text-xs font-semibold">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> Sẵn sàng chạy
          </span>
        </div>
      </div>

      <!-- CHAT SIMULATOR TIMELINE -->
      <div class="space-y-4 font-sans text-sm">
        
        <!-- Msg 1: User sends mega prompt -->
        <div class="flex items-start gap-3 justify-end">
          <div class="bg-cyan-600/90 text-white rounded-2xl rounded-tr-sm p-4 max-w-xl shadow-lg">
            <div class="text-xs font-bold text-cyan-200 mb-1 flex items-center gap-1">
              <i data-lucide="user" class="w-3.5 h-3.5"></i> Bạn (User)
            </div>
            <p class="font-mono text-xs text-slate-100 bg-cyan-800/60 p-2.5 rounded-lg border border-cyan-400/30">
              [Dán Mega Prompt: "Bạn là Giám Đốc Nghệ Thuật & Chuyên Gia Thiết Kế Thumbnail Video AI..."]
            </p>
          </div>
        </div>

        <!-- Msg 2: Gemini responses Step 1 (Asking for inputs) -->
        <div class="flex items-start gap-3">
          <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-cyan-400 to-blue-500 flex items-center justify-center text-black font-extrabold text-xs shrink-0 shadow-md">
            G
          </div>
          <div class="glass-card bg-slate-900/90 rounded-2xl rounded-tl-sm p-4.5 max-w-2xl border border-cyan-500/30 space-y-3">
            <div class="text-xs font-bold text-cyan-400 flex items-center gap-1.5">
              <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Gemini AI Assistant • Bước 1: Thu Thập Dữ Liệu
            </div>
            <p class="text-slate-200 leading-relaxed">
              Chào bạn! Tôi đã sẵn sàng tạo ảnh thumbnail công nghệ cao cấp 9:16. Để bắt đầu, vui lòng cung cấp giúp tôi <strong>3 thông tin sau</strong>:
            </p>
            <div class="bg-slate-950/80 p-3.5 rounded-xl border border-slate-800 space-y-2 text-xs">
              <div class="flex items-center gap-2 text-slate-300">
                <span class="w-5 h-5 rounded-full bg-cyan-950 border border-cyan-500 text-cyan-400 flex items-center justify-center font-bold text-[10px]">1</span>
                <strong>Ảnh Logo / Tên thương hiệu:</strong> Gửi file logo PNG hoặc tên (VD: 'AI MASTER LAB')
              </div>
              <div class="flex items-center gap-2 text-slate-300">
                <span class="w-5 h-5 rounded-full bg-cyan-950 border border-cyan-500 text-cyan-400 flex items-center justify-center font-bold text-[10px]">2</span>
                <strong>Nội dung Text To (Hook 2 Dòng):</strong> Dòng 1 (Vàng Neon) & Dòng 2 (Trắng Tinh)
              </div>
              <div class="flex items-center gap-2 text-slate-300">
                <span class="w-5 h-5 rounded-full bg-cyan-950 border border-cyan-500 text-cyan-400 flex items-center justify-center font-bold text-[10px]">3</span>
                <strong>Ảnh Chân Dung / Frame video:</strong> Đính kèm ảnh người cần tách nền
              </div>
            </div>
          </div>
        </div>

        <!-- Msg 3: User answers with sample data -->
        <div class="flex items-start gap-3 justify-end">
          <div class="bg-cyan-600/90 text-white rounded-2xl rounded-tr-sm p-4 max-w-xl shadow-lg space-y-2">
            <div class="text-xs font-bold text-cyan-200 flex items-center gap-1">
              <i data-lucide="user" class="w-3.5 h-3.5"></i> Bạn (User) gửi dữ liệu mẫu
            </div>
            <div class="text-xs space-y-1 bg-cyan-800/60 p-2.5 rounded-lg border border-cyan-400/30">
              <p>📌 <strong>Logo:</strong> 'AI MASTER LAB' • Slogan: 'AUTOMATION & EDITING STUDIO'</p>
              <p>📌 <strong>Dòng 1:</strong> 'TẠO VIDEO BẰNG AI'</p>
              <p>📌 <strong>Dòng 2:</strong> 'X10 TỐC ĐỘ DỰNG PHIM'</p>
              <p>📌 <strong>Ảnh đính kèm:</strong> [frame_goc_22s.jpg]</p>
            </div>
          </div>
        </div>

        <!-- Msg 4: Gemini outputs final master poster -->
        <div class="flex items-start gap-3">
          <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-cyan-400 to-blue-500 flex items-center justify-center text-black font-extrabold text-xs shrink-0 shadow-md">
            G
          </div>
          <div class="glass-card bg-slate-900/90 rounded-2xl rounded-tl-sm p-4.5 max-w-2xl border border-yellow-500/30 space-y-3">
            <div class="text-xs font-bold text-yellow-400 flex items-center gap-1.5">
              <i data-lucide="check-circle-2" class="w-3.5 h-3.5"></i> Gemini AI Assistant • Bước 2: Xuất Bản Ảnh Poster 4K
            </div>
            <p class="text-slate-200 text-xs">
              Đã hoàn tất bóc tách người, phủ nền Cyber Obsidian, gắn Logo 'AI MASTER LAB' và chèn Thẻ Hook tương phản. Bấm vào ảnh để xem chi tiết:
            </p>
            <div class="max-w-xs rounded-xl overflow-hidden border border-cyan-500/50 shadow-2xl">
              <img src="{R2_BASE}/vietmac_tech_poster_final.jpg" alt="Poster Output" class="w-full object-cover" loading="lazy">
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- MEGA PROMPT COPY BOX SECTION -->
    <section id="mega-prompt" class="space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider">Bộ Công Cụ Sẵn Dùng</span>
          <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">Mega Prompt Thiết Kế Thumbnail Tương Tác</h2>
        </div>
        <button id="copyBtn" onclick="copyMegaPrompt()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-black font-bold text-sm flex items-center gap-2 shadow-lg shadow-cyan-500/25 transition active:scale-95">
          <i data-lucide="copy" class="w-4 h-4"></i> <span id="copyBtnText">Sao Chép Mega Prompt</span>
        </button>
      </div>

      <div class="relative rounded-2xl overflow-hidden glass-card border border-slate-700">
        <div class="flex items-center justify-between px-4 py-2.5 bg-slate-950/80 border-b border-slate-800 text-xs text-slate-400 font-mono">
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-red-500/80 inline-block"></span>
            <span class="w-3 h-3 rounded-full bg-yellow-500/80 inline-block"></span>
            <span class="w-3 h-3 rounded-full bg-green-500/80 inline-block"></span>
            <span class="ml-2 text-slate-300">gemini_web_mega_prompt.txt</span>
          </div>
          <span class="text-[11px] text-cyan-400">Interactive 2-Step Protocol</span>
        </div>
        <pre class="p-4 sm:p-6 text-xs sm:text-sm text-slate-200 font-mono overflow-x-auto whitespace-pre-wrap leading-relaxed max-h-96 scrollbar-thin scrollbar-thumb-slate-700"><code>{MEGA_PROMPT}</code></pre>
      </div>
    </section>

    <!-- 5-STEP WORKFLOW BREAKDOWN SECTION -->
    <section class="space-y-6">
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Kỹ Thuật Chuyên Sâu</span>
        <h2 class="text-2xl font-bold text-white">5 Mắt Xích Kỹ Thuật Đằng Sau Bức Ảnh Hoàn Hảo</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        
        <!-- Step 1 -->
        <div class="glass-card rounded-2xl p-5 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-950 border border-cyan-500/40 text-cyan-400 flex items-center justify-center font-bold text-base">
            01
          </div>
          <h3 class="font-bold text-white text-base">Trích Xuất Frame Vàng</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Sử dụng OpenCV quét toàn bộ mốc thời gian để chọn frame có cử chỉ 2 tay mở rộng, mắt nhìn thẳng tự tin và không bị nhòe chuyển động (Motion Blur).
          </p>
        </div>

        <!-- Step 2 -->
        <div class="glass-card rounded-2xl p-5 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-950 border border-cyan-500/40 text-cyan-400 flex items-center justify-center font-bold text-base">
            02
          </div>
          <h3 class="font-bold text-white text-base">AI Segmentation Sắc Nét</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Mô hình U2Net / BiRefNet bóc tách alpha mask chuẩn xác từng kẽ ngón tay, sợi tóc và bờ vai áo vest, loại bỏ hoàn toàn background phòng cũ.
          </p>
        </div>

        <!-- Step 3 -->
        <div class="glass-card rounded-2xl p-5 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-950 border border-cyan-500/40 text-cyan-400 flex items-center justify-center font-bold text-base">
            03
          </div>
          <h3 class="font-bold text-white text-base">Viền Trắng Sticker & 3D Shadow</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Dùng toán tử Morphological Dilation bán kính 32px tạo viền trắng sticker, kết hợp Gaussian Blur khử răng cưa và đổ bóng mờ Cyan tạo chiều sâu 3D.
          </p>
        </div>

        <!-- Step 4 -->
        <div class="glass-card rounded-2xl p-5 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-950 border border-cyan-500/40 text-cyan-400 flex items-center justify-center font-bold text-base">
            04
          </div>
          <h3 class="font-bold text-white text-base">Nền Cyber Obsidian 4 Tầng</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Cấu trúc nền đen Obsidian không bị lem nhem, ánh sáng tỏa Radial Glow màu Cyan sau đầu và họa tiết Dot Matrix công nghệ tương lai.
          </p>
        </div>

        <!-- Step 5 -->
        <div class="glass-card rounded-2xl p-5 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-950 border border-cyan-500/40 text-cyan-400 flex items-center justify-center font-bold text-base">
            05
          </div>
          <h3 class="font-bold text-white text-base">Thẻ Hook Che Phụ Đề Cũ</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            Thẻ Card đen đặc bo góc với 2 dòng chữ tương phản mạnh (Dòng 1 Vàng Neon + Dòng 2 Trắng Tinh) che kín phụ đề cũ, tăng tỉ lệ click (CTR).
          </p>
        </div>

        <!-- Step 6 -->
        <div class="glass-card rounded-2xl p-5 space-y-3 bg-gradient-to-br from-slate-900 to-cyan-950/40 border-cyan-500/30 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-yellow-950 border border-yellow-500/40 text-yellow-400 flex items-center justify-center font-bold text-base mb-3">
              <i data-lucide="code-2" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-white text-base">Script Python Tự Động</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Mã nguồn Python sẵn có chạy 1 lệnh để tự động tạo poster cho mọi video tiếp theo trong 3 giây.
            </p>
          </div>
          <div class="pt-2">
            <code class="text-[11px] bg-black/60 px-2 py-1 rounded text-cyan-300 font-mono block">python3 create_branded_poster.py</code>
          </div>
        </div>

      </div>
    </section>

    <!-- PLATFORM COMPARISON TABLE -->
    <section class="glass-card rounded-3xl p-6 sm:p-8 space-y-5">
      <div class="border-b border-slate-800 pb-4">
        <h2 class="text-xl font-bold text-white flex items-center gap-2">
          <i data-lucide="layers" class="w-5 h-5 text-cyan-400"></i> So Sánh 3 Phương Pháp Thực Hiện
        </h2>
        <p class="text-xs text-slate-400 mt-1">Lựa chọn công cụ phù hợp với quy trình làm việc của bạn</p>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs sm:text-sm text-slate-300">
          <thead class="bg-slate-950/80 text-cyan-400 font-mono uppercase text-xs border-b border-slate-800">
            <tr>
              <th class="p-3.5">Tiêu chí</th>
              <th class="p-3.5 text-yellow-300">Python Script (Khuyên dùng)</th>
              <th class="p-3.5">Gemini Web (Mega Prompt)</th>
              <th class="p-3.5">CapCut Mobile</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 font-sans">
            <tr>
              <td class="p-3.5 font-bold text-white">Độ chính xác pixel</td>
              <td class="p-3.5 text-yellow-400 font-bold">100% Tuyệt đối</td>
              <td class="p-3.5 text-slate-300">95% (AI Render)</td>
              <td class="p-3.5 text-slate-300">Thủ công căn chỉnh</td>
            </tr>
            <tr>
              <td class="p-3.5 font-bold text-white">Tốc độ xuất file</td>
              <td class="p-3.5 text-yellow-400 font-bold">3 giây (1 lệnh)</td>
              <td class="p-3.5 text-slate-300">10 - 20 giây</td>
              <td class="p-3.5 text-slate-300">2 - 3 phút</td>
            </tr>
            <tr>
              <td class="p-3.5 font-bold text-white">Độ phân giải đầu ra</td>
              <td class="p-3.5 text-yellow-400 font-bold">4K UHD (2160x3840)</td>
              <td class="p-3.5 text-slate-300">2K - 4K</td>
              <td class="p-3.5 text-slate-300">1080p - 2K</td>
            </tr>
            <tr>
              <td class="p-3.5 font-bold text-white">Thiết bị phù hợp</td>
              <td class="p-3.5 text-yellow-400 font-bold">Máy Mac / PC Server</td>
              <td class="p-3.5 text-slate-300">Mọi trình duyệt Web</td>
              <td class="p-3.5 text-slate-300">Điện thoại di động</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800/80 bg-slate-950 py-8 px-4 text-center text-xs text-slate-500 space-y-2">
    <p class="text-slate-400 font-medium">Hệ Thống Thiết Kế Thumbnail Video Chuẩn Thương Hiệu &bull; VietMac AI Studio & Fedu</p>
    <p>Đồng bộ tự động lên GitHub Pages & Cloudflare R2 CDN</p>
  </footer>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    lucide.createIcons();

    function copyMegaPrompt() {{
      const promptText = `{MEGA_PROMPT}`;
      navigator.clipboard.writeText(promptText).then(() => {{
        const btnText = document.getElementById('copyBtnText');
        const originalText = btnText.innerText;
        btnText.innerText = 'Đã Sao Chép Thành Công!';
        const btn = document.getElementById('copyBtn');
        btn.classList.remove('from-cyan-500', 'to-blue-600');
        btn.classList.add('from-emerald-500', 'to-green-600');
        
        setTimeout(() => {{
          btnText.innerText = originalText;
          btn.classList.remove('from-emerald-500', 'to-green-600');
          btn.classList.add('from-cyan-500', 'to-blue-600');
        }}, 2500);
      }}).catch(err => {{
        alert('Không thể sao chép tự động: ' + err);
      }});
    }}
  </script>
</body>
</html>
"""

# Save nguyet.html and nguyệt.html
nguyet_path = os.path.join(REPO_DIR, "nguyet.html")
nguyet_unicode_path = os.path.join(REPO_DIR, "nguyệt.html")

with open(nguyet_path, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(nguyet_unicode_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Đã tạo thành công: {nguyet_path}")
print(f"Đã tạo thành công: {nguyet_unicode_path}")
