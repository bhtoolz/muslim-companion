# Python builder for Muslim Companion index.html
import os
import shutil

html_content = r'''<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <meta name="google" content="notranslate">
  <title>Muslim Companion (Rafiq Al-Muslim) — Phase 1 MVP</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- Premium Islamic Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <!-- Premium Islamic & Modern Typography (5 Arabic + 4 UI Fonts) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&family=Amiri+Quran&family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=Lexend:wght@400;500;600;700&family=Noto+Naskh+Arabic:wght@400;500;600;700&family=Outfit:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Scheherazade+New:wght@400;600;700&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            emerald: {
              850: '#0B3E2F',
              900: '#072C21',
              950: '#041B14',
            },
            gold: {
              400: '#DFBE7A',
              500: '#C5A059',
              600: '#A9843F',
            },
            parchment: '#FAF8F5',
            midnight: '#0A1612',
          },
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            arabic: ['Amiri', 'serif'],
            'arabic-ui': ['Cairo', 'sans-serif'],
            quran: ['"Amiri Quran"', '"Scheherazade New"', 'serif'],
          }
        }
      }
    }
  </script>

  <style>
    /* Smooth Touch and Scroll Styling */
    * {
      -webkit-tap-highlight-color: transparent;
      box-sizing: border-box;
    }
    /* Dynamic Typography CSS Variables */
    :root {
      --font-quran: 'Scheherazade New', 'Amiri Quran', 'Amiri', serif;
      --font-arabic-general: 'Amiri', 'Scheherazade New', 'Cairo', serif;
      --font-ui: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    }
    body {
      background-color: #030806;
      color: #E2E8F0;
      font-family: var(--font-ui);
    }
    .font-arabic {
      font-family: var(--font-arabic-general);
      line-height: 1.6;
      text-rendering: optimizeLegibility;
    }
    .font-arabic-ui {
      font-family: 'Cairo', var(--font-ui);
    }
    .font-quran-text {
      font-family: var(--font-quran);
      font-weight: 600;
      line-height: 2.35;
      letter-spacing: 0.15px;
      word-spacing: 0.12em;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
    }
    /* Specific Font Classes for Live Previews */
    .font-scheherazade { font-family: 'Scheherazade New', serif; }
    .font-amiri-quran { font-family: 'Amiri Quran', 'Amiri', serif; }
    .font-noto-naskh { font-family: 'Noto Naskh Arabic', serif; }
    .font-cairo { font-family: 'Cairo', sans-serif; }
    .font-almarai { font-family: 'Almarai', sans-serif; }
    .font-plus-jakarta { font-family: 'Plus Jakarta Sans', sans-serif; }
    .font-inter { font-family: 'Inter', sans-serif; }
    .font-outfit { font-family: 'Outfit', sans-serif; }
    .font-lexend { font-family: 'Lexend', sans-serif; }
    .emerald-gradient {
      background: linear-gradient(135deg, #0B3E2F 0%, #072C21 100%);
    }
    .gold-gradient {
      background: linear-gradient(135deg, #DFBE7A 0%, #C5A059 100%);
    }
    ::-webkit-scrollbar {
      width: 4px;
      height: 4px;
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(197, 160, 89, 0.3);
      border-radius: 4px;
    }
    .ayah-marker {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #C5A059;
      font-family: 'Amiri', serif;
      font-size: 1.15em;
      margin: 0 4px;
      user-select: none;
    }
  </style>
</head>
<body class="h-full flex flex-col items-center justify-start py-4 px-2 sm:px-6 overflow-x-hidden">

  <!-- Desktop Presentation Layout: Left Phone Screen, Right Vertically Centered Content -->
  <div class="w-full max-w-5xl flex flex-col lg:flex-row items-center justify-center gap-8 lg:gap-14 my-auto py-4">
    
    <!-- LEFT COLUMN: Content (Vertically Centered With Phone) -->
    <div class="flex-1 max-w-md w-full space-y-4 text-left my-auto self-center">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-950/90 border border-emerald-700/50 text-emerald-300 text-xs font-semibold tracking-wide shadow-sm">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        FLUTTERFLOW READY • PHASE 1 MVP
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
        Muslim Companion <br>
        <span class="text-gold-400 font-arabic text-3xl font-normal">رفيق المسلم</span>
      </h1>
      <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
        Production-ready mobile architecture for iOS & Android. Dual-mode GPS/city timetable, spherical trigonometry Qibla compass, Uthmani Quran reader, authentic Hisn al-Muslim Adhkar, tactile Tasbeeh, and daily Sahih Hadith.
      </p>

      <!-- Architecture Badges -->
      <div class="grid grid-cols-2 gap-2.5 text-xs pt-1">
        <div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800">
          <p class="text-slate-400 font-medium text-[11px]">Framework</p>
          <p class="text-white font-bold mt-0.5">FlutterFlow & Dart</p>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800">
          <p class="text-slate-400 font-medium text-[11px]">Sensor Math</p>
          <p class="text-white font-bold mt-0.5">Spherical Qibla Trig</p>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800">
          <p class="text-slate-400 font-medium text-[11px]">Database Cost</p>
          <p class="text-white font-bold mt-0.5">$0 Offline Bundled</p>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800">
          <p class="text-slate-400 font-medium text-[11px]">Handoff Format</p>
          <p class="text-white font-bold mt-0.5">Custom Widgets/Actions</p>
        </div>
      </div>

      <!-- Quick Interactive Presentation Controls -->
      <div class="pt-2 flex flex-wrap items-center gap-2.5">
        <button id="langToggleBtn" onclick="toggleLang()" class="px-4 py-2 rounded-lg bg-emerald-800 hover:bg-emerald-700 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm active:scale-95">
          <i data-lucide="globe" class="w-3.5 h-3.5"></i> <span id="langBtnText">Switch to Arabic (RTL)</span>
        </button>
        <button id="themeToggleBtn" onclick="toggleTheme()" class="px-4 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 active:scale-95">
          <i data-lucide="moon" class="w-3.5 h-3.5"></i> <span id="themeBtnText">Dark / Light</span>
        </button>

      </div>
    </div>


    <!-- RIGHT COLUMN: Interactive Phone Device Frame -->
    <div class="flex flex-col items-center gap-2.5 flex-shrink-0">
      
      <!-- OS Platform Switcher Pill (iOS vs Android) -->
      <div class="inline-flex items-center p-1 rounded-full bg-slate-900 border border-slate-800 shadow-xl text-xs font-semibold">
        <button id="osIosBtn" onclick="setOS('ios')" class="px-4 py-1.5 rounded-full bg-blue-600 text-white font-bold transition-all duration-200 flex items-center gap-1.5 shadow-sm">
          <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 170 170"><path d="M150.37 130.25c-2.45 5.66-5.35 10.87-8.71 15.66-4.58 6.53-8.33 11.05-11.22 13.56-4.48 4.12-9.28 6.23-14.42 6.35-3.69 0-8.14-1.05-13.32-3.18-5.19-2.12-9.97-3.17-14.34-3.17-4.58 0-9.49 1.05-14.75 3.17-5.26 2.13-9.5 3.24-12.74 3.35-4.35.13-9.16-1.9-14.42-6.08-3.7-3.04-7.58-7.7-11.64-13.99-6.3-9.77-11.14-20.94-14.52-33.51-3.38-12.57-5.07-24.16-5.07-34.78 0-14.28 3.59-25.96 10.77-35.04 7.18-9.08 16.31-13.73 27.4-13.95 5.23 0 10.63 1.25 16.2 3.75 5.58 2.5 9.38 3.82 11.41 3.96 1.74-.27 5.76-1.68 12.06-4.23 6.3-2.55 11.75-3.69 16.36-3.43 14.5.98 25.4 6.32 32.7 16.03-12.83 7.82-19.14 18.39-18.92 31.7.22 10.54 4.3 19.34 12.24 26.4 4.13 3.69 8.8 6.41 14.01 8.15-2.83 8.25-6.52 16.66-11.08 25.23zM119.22 31.84c0-7.28 2.66-14.12 7.99-20.52 5.33-6.4 11.85-10.43 19.57-12.09.22 1.09.33 2.18.33 3.26 0 7.39-2.77 14.34-8.32 20.85-5.55 6.51-12.16 10.37-19.82 11.58-.11-1.09-.16-2.12-.16-3.08z"/></svg>
          iPhone (iOS)
        </button>
        <button id="osAndroidBtn" onclick="setOS('android')" class="px-4 py-1.5 rounded-full text-slate-400 hover:text-white font-medium transition-all duration-200 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M17.523 15.3414c-.5511 0-.9993-.4486-.9993-.9997s.4482-.9993.9993-.9993c.551 0 .9993.4482.9993.9993.0001.5511-.4483.9997-.9993.9997m-11.046 0c-.5511 0-.9993-.4486-.9993-.9997s.4482-.9993.9993-.9993c.5511 0 .9993.4482.9993.9993 0 .5511-.4482.9997-.9993.9997m11.4045-6.02l1.9973-3.4592a.416.416 0 00-.1521-.5676.416.416 0 00-.5676.1521l-2.0223 3.503C15.5902 8.414 13.8533 8.0833 12 8.0833c-1.8533 0-3.5902.3307-5.1368.8664L4.8409 5.4467a.4161.4161 0 00-.5677-.1521.4157.4157 0 00-.1521.5676l1.9973 3.4592C2.6889 11.1867.3432 14.6589 0 18.761h24c-.3432-4.1021-2.6889-7.5743-6.1185-9.4396"/></svg>
          Android
        </button>
      </div>

      <!-- Phone Device Chassis -->
      <div id="deviceContainer" class="relative w-[360px] h-[710px] bg-black rounded-[46px] p-2.5 shadow-2xl border-4 border-slate-700 transition-all duration-300">
        
        <!-- iOS Dynamic Island -->
        <div id="iosDynamicIsland" class="absolute top-5 left-1/2 -translate-x-1/2 w-24 h-4 bg-black rounded-full z-50 flex items-center justify-center transition-all duration-200">
          <div class="w-2 h-2 rounded-full bg-slate-900 border border-slate-800 mr-1.5"></div>
        </div>

        <!-- Android Punch-hole Camera -->
        <div id="androidCameraDot" class="hidden absolute top-4 left-1/2 -translate-x-1/2 w-3.5 h-3.5 bg-black rounded-full z-50 border border-slate-900 shadow-inner">
          <div class="w-1.5 h-1.5 rounded-full bg-slate-950 m-auto mt-0.5"></div>
        </div>

        <!-- Phone Screen Frame -->
        <div id="deviceScreen" class="w-full h-full bg-[#FAF8F5] text-slate-800 rounded-[38px] overflow-hidden flex flex-col relative transition-all duration-200">
          
          <!-- Native Status Bar -->
          <div id="statusBarContainer" class="pt-3 px-5 pb-1 flex items-center justify-between text-[11px] font-bold text-slate-600 dark:text-slate-400 z-40 select-none">
            <span id="statusBarClock">09:41</span>
            <!-- iOS Icons -->
            <div id="statusBarIosIcons" class="flex items-center gap-1.5">
              <i data-lucide="signal" class="w-3.5 h-3.5"></i>
              <i data-lucide="wifi" class="w-3.5 h-3.5"></i>
              <i data-lucide="battery" class="w-4 h-4"></i>
            </div>
            <!-- Android Icons -->
            <div id="statusBarAndroidIcons" class="hidden flex items-center gap-1.5 text-[10px]">
              <span class="font-mono text-[9px] px-1 py-0.2 bg-slate-200 dark:bg-slate-700 rounded font-bold">5G</span>
              <i data-lucide="wifi" class="w-3.5 h-3.5"></i>
              <div class="flex items-center gap-0.5">
                <span class="text-[9px]">98%</span>
                <i data-lucide="battery-charging" class="w-3.5 h-3.5"></i>
              </div>
            </div>
          </div>

          <!-- Sleek Native Notification Toast Banner -->
          <div id="adhanToast" class="hidden absolute top-10 left-3 right-3 z-50 bg-slate-900/95 dark:bg-slate-800/95 text-white p-3 rounded-2xl border border-gold-500/50 shadow-2xl backdrop-blur-md flex items-center gap-3 transition-all transform duration-300 -translate-y-4 opacity-0 pointer-events-auto">
            <div class="w-9 h-9 rounded-full bg-emerald-800 text-gold-400 flex items-center justify-center flex-shrink-0 shadow-inner">
              <i data-lucide="bell-ring" class="w-4 h-4"></i>
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-xs font-bold text-gold-400 flex items-center justify-between">
                <span id="toastHeaderTitle">Prayer Notification</span>
                <span class="text-[10px] text-slate-400 font-mono font-normal">Now</span>
              </p>
              <p id="toastMessageText" class="text-[11px] text-slate-200 truncate">Time for Dhuhr Prayer • Hayya 'alas-Salah</p>
            </div>
            <button onclick="dismissAdhanToast()" class="text-slate-400 hover:text-white text-xs font-bold px-1.5 py-1">✕</button>
          </div>

          <!-- City Selection Sheet / Modal -->
          <div id="citySelectorModal" class="hidden absolute inset-0 z-50 bg-black/60 backdrop-blur-xs flex flex-col justify-end transition-opacity duration-200">
            <div class="bg-white dark:bg-slate-900 rounded-t-3xl p-4 space-y-3 max-h-[82%] flex flex-col shadow-2xl border-t border-slate-200 dark:border-slate-800">
              <div class="flex items-center justify-between pb-1 border-b border-slate-100 dark:border-slate-800">
                <div class="flex items-center gap-2">
                  <i data-lucide="map-pin" class="w-4 h-4 text-emerald-600"></i>
                  <h3 id="modalTitle" class="text-sm font-bold text-slate-900 dark:text-white">Select Location</h3>
                </div>
                <button onclick="closeCityModal()" class="w-6 h-6 rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-xs font-bold text-slate-500 hover:text-slate-900 dark:hover:text-white">✕</button>
              </div>

              <!-- Live GPS Auto-Detect Button -->
              <button onclick="detectLocationGPS()" id="btnAutoGPS" class="w-full py-2.5 px-3 rounded-xl bg-emerald-850 hover:bg-emerald-900 text-white text-xs font-bold flex items-center justify-center gap-2 shadow-sm transition active:scale-98">
                <i data-lucide="crosshair" class="w-3.5 h-3.5 text-gold-400 animate-spin-slow"></i>
                <span id="btnGpsText">Detect GPS Location</span>
              </button>

              <!-- Search Filter Input -->
              <div class="relative">
                <input id="citySearchInput" oninput="filterCities(this.value)" type="text" placeholder="Search cities..." class="w-full pl-8 pr-3 py-1.5 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 focus:outline-none focus:border-emerald-600">
                <i data-lucide="search" class="w-3.5 h-3.5 absolute left-2.5 top-2 text-slate-400"></i>
              </div>

              <!-- Cities List Scrollable -->
              <div id="citiesListContainer" class="overflow-y-auto space-y-1.5 max-h-60 pr-1">
                <!-- Rendered dynamically by JS -->
              </div>
            </div>
          </div>

                    <!-- Searchable 114 Surah Index Modal (Market-Standard Drawer) -->
          <div id="surahIndexModal" class="hidden absolute inset-0 z-50 bg-[#FAF8F5] dark:bg-[#0A1612] flex flex-col pt-11 px-3.5 pb-4 transition-all duration-300 shadow-2xl">
            <!-- Modal Header (Comprehensive Islamic Directory) -->
            <div class="flex items-center justify-between pb-2 border-b border-slate-200 dark:border-slate-800">
              <div class="flex items-center gap-2">
                <div class="w-7 h-7 rounded-lg bg-emerald-800 text-gold-400 flex items-center justify-center flex-shrink-0">
                  <i data-lucide="book-open" class="w-3.5 h-3.5"></i>
                </div>
                <div>
                  <h3 class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                    Quran & Duas Directory <span class="font-arabic text-sm text-gold-500 font-normal">فهرس السور والأدعية</span>
                  </h3>
                  <p class="text-[10px] text-slate-400">114 Surahs, Daily Duas & Special Verses</p>
                </div>
              </div>
              <button onclick="closeSurahIndexModal()" class="w-7 h-7 rounded-full bg-slate-200/80 dark:bg-slate-800 flex items-center justify-center text-slate-500 hover:text-slate-800 dark:hover:text-white transition active:scale-90">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>

            <!-- Primary Category Tabs (Surahs vs Duas vs Special Verses) -->
            <div class="grid grid-cols-3 gap-1.5 mt-2 bg-slate-200/80 dark:bg-slate-800 p-1 rounded-xl text-[10px] font-bold">
              <button onclick="switchDirectoryTab('surahs')" id="dirTab-surahs" class="py-1 rounded-lg bg-emerald-800 text-white transition flex items-center justify-center gap-1">
                <i data-lucide="book" class="w-3 h-3"></i> Surahs (114)
              </button>
              <button onclick="switchDirectoryTab('duas')" id="dirTab-duas" class="py-1 rounded-lg text-slate-600 dark:text-slate-300 hover:text-white transition flex items-center justify-center gap-1">
                <i data-lucide="heart" class="w-3 h-3"></i> Duas & Adhkar
              </button>
              <button onclick="switchDirectoryTab('special')" id="dirTab-special" class="py-1 rounded-lg text-slate-600 dark:text-slate-300 hover:text-white transition flex items-center justify-center gap-1">
                <i data-lucide="book-marked" class="w-3 h-3"></i> Special Verses
              </button>
            </div>

            <!-- Instant Search Input -->
            <div class="relative mt-2">
              <input type="text" id="surahSearchInput" oninput="filterDirectoryList(this.value)" placeholder="Search Surahs, Duas, Verses..." class="w-full pl-8 pr-3 py-1.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs text-slate-800 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-gold-500">
              <i data-lucide="search" class="w-3.5 h-3.5 absolute left-2.5 top-2 text-slate-400"></i>
            </div>

            <!-- Filter Chips (Visible for Surahs Tab) -->
            <div id="surahFilterSubChips" class="flex items-center gap-1.5 mt-1.5 pb-1 text-[10px] font-semibold">
              <button onclick="setSurahFilter('all')" id="surahFilterAll" class="px-2.5 py-0.5 rounded-full bg-emerald-800 text-white font-bold transition">All (114)</button>
              <button onclick="setSurahFilter('meccan')" id="surahFilterMeccan" class="px-2.5 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 transition">Meccan (86)</button>
              <button onclick="setSurahFilter('medinan')" id="surahFilterMedinan" class="px-2.5 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 transition">Medinan (28)</button>
            </div>

            <!-- Scrollable 114 Surahs List -->
            <div id="surahIndexCardsContainer" class="flex-1 overflow-y-auto space-y-1 mt-1.5 pr-0.5 pb-6">
              <!-- Rendered dynamically -->
            </div>
          </div>

                              <!-- Saved Ayahs / Bookmarks Drawer Modal -->
          <div id="bookmarksModal" class="hidden absolute inset-0 z-50 bg-[#FAF8F5] dark:bg-[#0A1612] flex flex-col pt-11 px-3.5 pb-4 transition-all duration-300 shadow-2xl">
            <!-- Modal Header -->
            <div class="flex items-center justify-between pb-2.5 border-b border-slate-200 dark:border-slate-800">
              <div class="flex items-center gap-2">
                <div class="w-7 h-7 rounded-lg bg-gold-500/20 text-gold-600 dark:text-gold-400 flex items-center justify-center flex-shrink-0">
                  <i data-lucide="bookmark" class="w-4 h-4 fill-current"></i>
                </div>
                <div>
                  <h3 class="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                    Saved Ayahs <span class="font-arabic text-sm text-gold-500 font-normal">الآيات المحفوظة</span>
                  </h3>
                  <p class="text-[10px] text-slate-400" id="bookmarksCountSub">0 verses bookmarked</p>
                </div>
              </div>
              <button onclick="closeBookmarksModal()" class="w-7 h-7 rounded-full bg-slate-200/80 dark:bg-slate-800 flex items-center justify-center text-slate-500 hover:text-slate-800 dark:hover:text-white transition active:scale-90">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>

            <!-- Bookmarks List Container -->
            <div id="bookmarksCardsContainer" class="flex-1 overflow-y-auto space-y-2 pt-2.5 pb-6 pr-0.5">
              <!-- Rendered dynamically -->
            </div>
          </div>

          <!-- Comprehensive App Settings & Audio Preferences Modal -->
          <div id="settingsModal" class="hidden absolute inset-0 z-50 bg-[#FAF8F5] dark:bg-[#0A1612] flex flex-col pt-11 px-3.5 pb-4 transition-all duration-300 shadow-2xl">
            <!-- Modal Header -->
            <div class="flex items-center justify-between pb-2 border-b border-slate-200 dark:border-slate-800">
              <div class="flex items-center gap-2">
                <div class="w-7 h-7 rounded-lg bg-emerald-850 text-gold-400 flex items-center justify-center flex-shrink-0">
                  <i data-lucide="sliders" class="w-4 h-4"></i>
                </div>
                <div>
                  <h3 class="text-xs font-bold text-slate-900 dark:text-white">Settings</h3>
                </div>
              </div>
              <button onclick="closeSettingsModal()" class="w-7 h-7 rounded-full bg-slate-200/80 dark:bg-slate-800 flex items-center justify-center text-slate-500 hover:text-slate-800 dark:hover:text-white transition active:scale-90">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>

            <!-- Settings Section Navigation Pills -->
            <div class="flex gap-1.5 overflow-x-auto py-1.5 text-[11px] font-semibold no-scrollbar border-b border-slate-100 dark:border-slate-800/80">
              <button onclick="switchSettingsTab('reciters')" id="tabBtnSettingsReciters" class="px-3 py-1 rounded-full bg-emerald-800 text-white font-bold flex-shrink-0 flex items-center gap-1">
                <i data-lucide="headphones" class="w-3 h-3"></i> Reciters
              </button>
              <button onclick="switchSettingsTab('adhans')" id="tabBtnSettingsAdhans" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0 flex items-center gap-1">
                <i data-lucide="bell" class="w-3 h-3"></i> Adhans
              </button>
              <button onclick="switchSettingsTab('calculation')" id="tabBtnSettingsCalculation" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0 flex items-center gap-1">
                <i data-lucide="compass" class="w-3 h-3"></i> Fiqh
              </button>
              <button onclick="switchSettingsTab('display')" id="tabBtnSettingsDisplay" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0 flex items-center gap-1">
                <i data-lucide="type" class="w-3 h-3"></i> Display
              </button>
            </div>

            <!-- Scrollable Content Area -->
            <div class="flex-1 overflow-y-auto space-y-3.5 pt-2 pb-6 pr-0.5 text-xs text-slate-700 dark:text-slate-300">
              
              <!-- SECTION 1: QURAN RECITERS -->
              <div id="settingsSectionReciters" class="space-y-1.5">
                <div class="flex items-center justify-between pb-0.5">
                  <h4 class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                    <i data-lucide="headphones" class="w-3.5 h-3.5 text-gold-500"></i> Reciter
                  </h4>
                  <span class="text-[10px] text-emerald-700 dark:text-emerald-400 font-semibold" id="activeReciterBadge">Alafasy</span>
                </div>
                <div id="recitersListContainer" class="space-y-1 pt-0.5">
                  <!-- Rendered dynamically by renderRecitersSettings() -->
                </div>
              </div>

              <!-- SECTION 2: ADHAN & NOTIFICATION TONES -->
              <div id="settingsSectionAdhans" class="hidden space-y-1.5">
                <div class="flex items-center justify-between pb-0.5">
                  <h4 class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                    <i data-lucide="bell" class="w-3.5 h-3.5 text-gold-500"></i> Adhan Tone
                  </h4>
                  <span class="text-[10px] text-emerald-700 dark:text-emerald-400 font-semibold" id="activeAdhanBadge">Makkah</span>
                </div>
                <div id="adhansListContainer" class="space-y-1 pt-0.5">
                  <!-- Rendered dynamically by renderAdhansSettings() -->
                </div>
              </div>

              <!-- SECTION 3: CALCULATION & ASR JURISTIC METHOD -->
              <!-- SECTION 3: CALCULATION & ASR JURISTIC METHOD -->
              <div id="settingsSectionCalculation" class="hidden space-y-3">
                <!-- Asr Madhab -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                      <i data-lucide="sun" class="w-3.5 h-3.5 text-gold-500"></i> Asr Method
                    </span>
                    <span class="text-[10px] font-bold text-emerald-700 dark:text-emerald-400" id="currentMadhabLabel">Hanafi</span>
                  </div>
                  <p class="text-[10px] text-slate-400">Hanafi (later Asr) or Standard (Shafi'i, Maliki, Hanbali)</p>
                  <div class="grid grid-cols-2 gap-2 pt-0.5">
                    <button onclick="setJuristicMethod('hanafi')" id="btnMadhabHanafi" class="py-2 px-2.5 rounded-lg border text-xs font-bold flex items-center justify-center gap-1.5 transition active:scale-95 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200">
                      <span>Hanafi</span> <span class="font-arabic font-normal text-slate-400 text-[10px]">(حنفي)</span>
                    </button>
                    <button onclick="setJuristicMethod('standard')" id="btnMadhabStandard" class="py-2 px-2.5 rounded-lg border text-xs font-bold flex items-center justify-center gap-1.5 transition active:scale-95 bg-white dark:bg-slate-700 border-slate-200 dark:border-slate-600 text-slate-700 dark:text-slate-300">
                      <span>Standard</span> <span class="font-arabic font-normal text-slate-400 text-[10px]">(شافعي)</span>
                    </button>
                  </div>
                </div>

                <!-- Hijri Date Manual Adjustment -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                      <i data-lucide="moon" class="w-3.5 h-3.5 text-gold-500"></i> Hijri Date Adjustment
                    </span>
                    <span class="whitespace-nowrap text-[10px] font-bold text-gold-600 dark:text-gold-400" id="currentHijriOffsetLabel">0 Days</span>
                  </div>
                  <p class="text-[10px] text-slate-400">Adjust ±1 or 2 days for local moon sighting</p>
                  <div class="flex items-center justify-between gap-1 pt-0.5 text-[11px] font-bold">
                    <button onclick="setHijriOffset(-2)" id="btnHijriM2" class="flex-1 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300">-2</button>
                    <button onclick="setHijriOffset(-1)" id="btnHijriM1" class="flex-1 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300">-1</button>
                    <button onclick="setHijriOffset(0)" id="btnHijri0" class="flex-1 py-1.5 rounded-lg border border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200">0</button>
                    <button onclick="setHijriOffset(1)" id="btnHijriP1" class="flex-1 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300">+1</button>
                    <button onclick="setHijriOffset(2)" id="btnHijriP2" class="flex-1 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300">+2</button>
                  </div>
                </div>

                <!-- Calculation Fiqh Authority -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2">
                  <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                    <i data-lucide="book" class="w-3.5 h-3.5 text-gold-500"></i> Calculation Authority
                  </span>
                  <div class="p-2 rounded-lg bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-800 text-[11px] font-semibold text-emerald-800 dark:text-emerald-300 flex items-center justify-between">
                    <span>Univ. of Islamic Sciences, Karachi</span>
                    <span class="px-1.5 py-0.5 rounded text-[9px] bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-400 font-bold">Auto</span>
                  </div>
                </div>
              </div>

              <!-- SECTION 4: DISPLAY & TYPOGRAPHY -->
              <div id="settingsSectionDisplay" class="hidden space-y-3">
                <!-- Quran Arabic Font Size Slider with Reset Button -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                      <i data-lucide="type" class="w-3.5 h-3.5 text-gold-500"></i> Arabic Font Size
                    </span>
                    <div class="flex items-center gap-2">
                      <span class="text-xs font-bold text-emerald-700 dark:text-emerald-400" id="lblSettingsFontSize">24px</span>
                      <button onclick="resetArabicFontSize()" title="Reset to default font size (24px)" class="text-[10px] font-bold px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-750 text-slate-500 hover:text-emerald-700 dark:text-slate-400 dark:hover:text-emerald-300 transition active:scale-95 border border-slate-200/60 dark:border-slate-700/60">
                        Reset
                      </button>
                    </div>
                  </div>
                  <input type="range" min="18" max="36" value="24" id="settingsFontSizeSlider" oninput="onSettingsFontSizeChange(this.value)" class="w-full accent-emerald-700 dark:accent-gold-500 cursor-pointer">
                  <!-- Live Sample Preview -->
                  <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-slate-900 text-right border border-slate-100 dark:border-slate-800">
                    <p id="fontPreviewSample" class="notranslate font-quran-text text-emerald-950 dark:text-white font-semibold" translate="no" lang="ar" dir="rtl" style="font-size: 24px; line-height: 2.35;">
                      بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
                    </p>
                  </div>
                </div>

                <!-- Premium Arabic Script Selector (5 Famous Authentic Typefaces) -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                      <i data-lucide="feather" class="w-3.5 h-3.5 text-gold-500"></i> Arabic Script <span class="font-arabic text-gold-600 dark:text-gold-400 font-normal text-xs">خط المصحف</span>
                    </span>
                    <span id="activeArabicFontBadge" class="text-[9px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 border border-emerald-300/40">Scheherazade</span>
                  </div>
                  <div class="space-y-1.5 pt-0.5" id="arabicFontOptionsContainer">
                    <!-- 1. Scheherazade New -->
                    <button onclick="setArabicFont('scheherazade')" id="fontBtn-scheherazade" class="w-full p-2 rounded-xl border text-left flex items-center justify-between transition active:scale-98 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 shadow-2xs">
                      <div>
                        <p class="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                          <span>Scheherazade New</span>
                          <span class="text-[9px] px-1.5 py-0.2 rounded bg-gold-500/20 text-gold-700 dark:text-gold-400 font-semibold">Recommended</span>
                        </p>
                        <p class="text-[10px] text-slate-400">Traditional Quranic Naskh</p>
                      </div>
                      <span class="font-scheherazade text-base text-emerald-950 dark:text-emerald-200 font-bold" dir="rtl">ٱلْحَمْدُ لِلَّهِ</span>
                    </button>

                    <!-- 2. Amiri Quran -->
                    <button onclick="setArabicFont('amiri-quran')" id="fontBtn-amiri-quran" class="w-full p-2 rounded-xl border text-left flex items-center justify-between transition active:scale-98 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700">
                      <div>
                        <p class="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                          <span>Amiri Quran</span>
                          <span class="text-[9px] px-1.5 py-0.2 rounded bg-slate-200 dark:bg-slate-750 text-slate-600 dark:text-slate-300 font-medium">Bulaq</span>
                        </p>
                        <p class="text-[10px] text-slate-400">Authentic 1924 Cairo Mushaf</p>
                      </div>
                      <span class="font-amiri-quran text-base text-emerald-950 dark:text-emerald-200 font-bold" dir="rtl">ٱلْحَمْدُ لِلَّهِ</span>
                    </button>

                    <!-- 3. Noto Naskh Arabic -->
                    <button onclick="setArabicFont('noto-naskh')" id="fontBtn-noto-naskh" class="w-full p-2 rounded-xl border text-left flex items-center justify-between transition active:scale-98 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700">
                      <div>
                        <p class="text-xs font-bold text-slate-900 dark:text-white">Noto Naskh Arabic</p>
                        <p class="text-[10px] text-slate-400">Madinah Standard Typography</p>
                      </div>
                      <span class="font-noto-naskh text-base text-emerald-950 dark:text-emerald-200 font-bold" dir="rtl">ٱلْحَمْدُ لِلَّهِ</span>
                    </button>

                    <!-- 4. Cairo -->
                    <button onclick="setArabicFont('cairo')" id="fontBtn-cairo" class="w-full p-2 rounded-xl border text-left flex items-center justify-between transition active:scale-98 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700">
                      <div>
                        <p class="text-xs font-bold text-slate-900 dark:text-white">Cairo</p>
                        <p class="text-[10px] text-slate-400">Modern Geometric Kufi</p>
                      </div>
                      <span class="font-cairo text-sm text-emerald-950 dark:text-emerald-200 font-bold" dir="rtl">ٱلْحَمْدُ لِلَّهِ</span>
                    </button>

                    <!-- 5. Almarai -->
                    <button onclick="setArabicFont('almarai')" id="fontBtn-almarai" class="w-full p-2 rounded-xl border text-left flex items-center justify-between transition active:scale-98 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700">
                      <div>
                        <p class="text-xs font-bold text-slate-900 dark:text-white">Almarai</p>
                        <p class="text-[10px] text-slate-400">Contemporary Clean Sans</p>
                      </div>
                      <span class="font-almarai text-sm text-emerald-950 dark:text-emerald-200 font-bold" dir="rtl">ٱلْحَمْدُ لِلَّهِ</span>
                    </button>
                  </div>
                </div>

                <!-- App Interface UI Font (4 Famous Acclaimed Typefaces) -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                      <i data-lucide="palette" class="w-3.5 h-3.5 text-gold-500"></i> App Interface Font
                    </span>
                    <span id="activeUIFontBadge" class="text-[9px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 border border-emerald-300/40">Plus Jakarta</span>
                  </div>
                  <div class="grid grid-cols-2 gap-2 pt-0.5" id="uiFontOptionsContainer">
                    <!-- 1. Plus Jakarta Sans -->
                    <button onclick="setUIFont('plus-jakarta')" id="uiFontBtn-plus-jakarta" class="p-2.5 rounded-xl border text-left transition active:scale-95 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 shadow-2xs">
                      <p class="text-xs font-bold text-slate-900 dark:text-white font-plus-jakarta">Plus Jakarta</p>
                      <p class="text-[9px] text-slate-400">Modern Geometric</p>
                      <p class="text-[11px] font-semibold text-emerald-700 dark:text-emerald-300 mt-1 font-plus-jakarta">Aa 123</p>
                    </button>

                    <!-- 2. Inter -->
                    <button onclick="setUIFont('inter')" id="uiFontBtn-inter" class="p-2.5 rounded-xl border text-left transition active:scale-95 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700">
                      <p class="text-xs font-bold text-slate-900 dark:text-white font-inter">Inter</p>
                      <p class="text-[9px] text-slate-400">Interface Standard</p>
                      <p class="text-[11px] font-semibold text-slate-700 dark:text-slate-300 mt-1 font-inter">Aa 123</p>
                    </button>

                    <!-- 3. Outfit -->
                    <button onclick="setUIFont('outfit')" id="uiFontBtn-outfit" class="p-2.5 rounded-xl border text-left transition active:scale-95 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700">
                      <p class="text-xs font-bold text-slate-900 dark:text-white font-outfit">Outfit</p>
                      <p class="text-[9px] text-slate-400">Luxury Display</p>
                      <p class="text-[11px] font-semibold text-slate-700 dark:text-slate-300 mt-1 font-outfit">Aa 123</p>
                    </button>

                    <!-- 4. Lexend -->
                    <button onclick="setUIFont('lexend')" id="uiFontBtn-lexend" class="p-2.5 rounded-xl border text-left transition active:scale-95 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700">
                      <p class="text-xs font-bold text-slate-900 dark:text-white font-lexend">Lexend</p>
                      <p class="text-[9px] text-slate-400">Reading Fluency</p>
                      <p class="text-[11px] font-semibold text-slate-700 dark:text-slate-300 mt-1 font-lexend">Aa 123</p>
                    </button>
                  </div>
                </div>

                <!-- Toggles (Clean, Professional & Short Microcopy) -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2.5">
                  <!-- Translation Toggle -->
                  <div class="flex items-center justify-between">
                    <div>
                      <h5 class="text-xs font-bold text-slate-800 dark:text-white">English Translation</h5>
                      <p class="text-[10px] text-slate-400">Sahih International</p>
                    </div>
                    <label class="relative inline-flex items-center cursor-pointer">
                      <input type="checkbox" id="chkShowTranslation" checked onchange="toggleTranslationSetting(this.checked)" class="sr-only peer">
                      <div class="w-9 h-5 bg-slate-300 peer-focus:outline-none rounded-full peer dark:bg-slate-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-700"></div>
                    </label>
                  </div>

                  <!-- Transliteration Toggle -->
                  <div class="flex items-center justify-between border-t border-slate-100 dark:border-slate-700/60 pt-2">
                    <div>
                      <h5 class="text-xs font-bold text-slate-800 dark:text-white">Roman Transliteration</h5>
                      <p class="text-[10px] text-slate-400">Phonetic reading</p>
                    </div>
                    <label class="relative inline-flex items-center cursor-pointer">
                      <input type="checkbox" id="chkShowTranslit" checked onchange="toggleTranslitSetting(this.checked)" class="sr-only peer">
                      <div class="w-9 h-5 bg-slate-300 peer-focus:outline-none rounded-full peer dark:bg-slate-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-700"></div>
                    </label>
                  </div>

                  <!-- Haptic Touch Feedback Toggle -->
                  <div class="flex items-center justify-between border-t border-slate-100 dark:border-slate-700/60 pt-2">
                    <div>
                      <h5 class="text-xs font-bold text-slate-800 dark:text-white">Haptic Vibration</h5>
                      <p class="text-[10px] text-slate-400">Vibrate on tap</p>
                    </div>
                    <label class="relative inline-flex items-center cursor-pointer">
                      <input type="checkbox" id="chkHaptics" checked onchange="toggleHapticsSetting(this.checked)" class="sr-only peer">
                      <div class="w-9 h-5 bg-slate-300 peer-focus:outline-none rounded-full peer dark:bg-slate-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-700"></div>
                    </label>
                  </div>
                </div>

                <!-- Multiple Tasbeeh Sounds Selector (Instant Acoustic Preview on Click) -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                      <i data-lucide="music" class="w-3.5 h-3.5 text-emerald-600"></i> Tasbeeh Tap Sound
                    </span>
                    <span id="currentSoundLabelBadge" class="text-[9px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 border border-emerald-300/40">Wood Bead</span>
                  </div>
                  <div class="grid grid-cols-4 gap-1.5 pt-0.5" id="tasbeehSoundOptionsContainer">
                    <button onclick="setTasbeehSound('wood')" id="sndBtn-wood" class="p-1.5 rounded-lg border text-center transition active:scale-95 bg-emerald-50 dark:bg-emerald-950 border-emerald-500 text-emerald-800 dark:text-emerald-300 font-bold text-[10px]">
                      🪵 Wood
                    </button>
                    <button onclick="setTasbeehSound('click')" id="sndBtn-click" class="p-1.5 rounded-lg border text-center transition active:scale-95 bg-slate-50 dark:bg-slate-900 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 text-[10px]">
                      🔘 Click
                    </button>
                    <button onclick="setTasbeehSound('water')" id="sndBtn-water" class="p-1.5 rounded-lg border text-center transition active:scale-95 bg-slate-50 dark:bg-slate-900 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 text-[10px]">
                      💧 Water
                    </button>
                    <button onclick="setTasbeehSound('digital')" id="sndBtn-digital" class="p-1.5 rounded-lg border text-center transition active:scale-95 bg-slate-50 dark:bg-slate-900 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 text-[10px]">
                      📟 Digital
                    </button>
                  </div>
                </div>

                <!-- Theme Selection -->
                <div class="p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2 mb-6">
                  <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                    <i data-lucide="palette" class="w-3.5 h-3.5 text-gold-500"></i> Theme
                  </span>
                  <div class="grid grid-cols-2 gap-2 pt-1">
                    <button onclick="setThemeMode('light')" class="py-2 rounded-lg border border-slate-200 bg-white text-slate-800 text-xs font-bold hover:bg-slate-50 transition">
                      ☀️ Light Parchment
                    </button>
                    <button onclick="setThemeMode('dark')" class="py-2 rounded-lg border border-slate-700 bg-slate-900 text-gold-300 text-xs font-bold hover:bg-slate-800 transition">
                      🌙 Emerald Dark
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 1. ISLAMIC HIJRI CALENDAR & FASTING MODAL -->
          <div id="islamicCalendarModal" class="hidden absolute inset-0 z-50 bg-[#FAF8F5] dark:bg-[#0A1612] flex flex-col pt-11 px-3.5 pb-4 transition-all duration-300 shadow-2xl">
            <!-- Modal Header -->
            <div class="flex items-center justify-between pb-2.5 border-b border-slate-200 dark:border-slate-800">
              <div class="flex items-center gap-2">
                <div class="w-7 h-7 rounded-lg bg-emerald-850 text-gold-400 flex items-center justify-center flex-shrink-0">
                  <i data-lucide="calendar" class="w-4 h-4"></i>
                </div>
                <div>
                  <h3 class="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                    Hijri Calendar <span class="font-arabic text-xs text-gold-500 font-normal">التقويم الهجري</span>
                  </h3>
                </div>
              </div>
              <button onclick="closeCalendarModal()" class="w-7 h-7 rounded-full bg-slate-200/80 dark:bg-slate-800 flex items-center justify-center text-slate-500 hover:text-slate-800 dark:hover:text-white transition active:scale-90">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto space-y-3 pt-2 pb-6 pr-0.5">

              <!-- Month Navigation & Full Calendar Card -->
              <div class="p-3 rounded-2xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 shadow-xs">
                <!-- Month Switcher Header -->
                <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-100 dark:border-slate-750">
                  <button onclick="navigateHijriMonth(-1)" title="Previous Month" class="w-7 h-7 rounded-lg bg-slate-100 dark:bg-slate-750 flex items-center justify-center text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 active:scale-90 transition">
                    <i data-lucide="chevron-left" class="w-4 h-4"></i>
                  </button>
                  <div class="text-center cursor-pointer select-none" onclick="jumpToCurrentHijriMonth()" title="Click to jump to Today">
                    <h4 id="calMonthTitle" class="text-xs font-extrabold text-slate-900 dark:text-white flex items-center justify-center gap-1.5">
                      Shawwal 1447 <span class="font-arabic text-emerald-600 dark:text-emerald-400 font-normal text-xs">شَوَّال</span>
                    </h4>
                    <p id="calMonthSubtitle" class="text-[9px] text-slate-400">Mar 20 – Apr 18, 2026</p>
                  </div>
                  <button onclick="navigateHijriMonth(1)" title="Next Month" class="w-7 h-7 rounded-lg bg-slate-100 dark:bg-slate-750 flex items-center justify-center text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 active:scale-90 transition">
                    <i data-lucide="chevron-right" class="w-4 h-4"></i>
                  </button>
                </div>

                <!-- 7 Weekday Headers -->
                <div class="grid grid-cols-7 gap-1 text-center py-1 text-[9px] font-bold text-slate-400 uppercase tracking-wider">
                  <span>Sun</span>
                  <span>Mon</span>
                  <span>Tue</span>
                  <span>Wed</span>
                  <span>Thu</span>
                  <span>Fri</span>
                  <span>Sat</span>
                </div>

                <!-- 7-Column Hijri Days Grid -->
                <div id="hijriMonthGrid" class="grid grid-cols-7 gap-1 pt-1.5">
                  <!-- Rendered dynamically -->
                </div>

                <!-- Calendar Legend -->
                <div class="flex items-center justify-center gap-3 pt-2 text-[9px] text-slate-400 border-t border-slate-100 dark:border-slate-750 mt-2.5">
                  <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-emerald-700"></span> Today</span>
                  <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> Mon/Thu Fast</span>
                  <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span> White Days</span>
                </div>
              </div>

              <!-- Selected Day Details & Fasting Card -->
              <div id="selectedDateDetailCard" class="p-3 rounded-2xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 shadow-xs space-y-2.5">
                <div class="flex items-center justify-between">
                  <div>
                    <h5 id="selDateHijri" class="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                      18 Shawwal 1447 <span class="text-[10px] font-normal text-slate-400">• Mon, Apr 6</span>
                    </h5>
                    <div id="selDateTags" class="flex flex-wrap items-center gap-1 mt-0.5">
                      <span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300">Today</span>
                      <span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300">Monday Sunnah Fast</span>
                    </div>
                  </div>
                  <button id="btnToggleDateFast" onclick="toggleSelectedDateFast()" class="px-2.5 py-1.5 rounded-xl bg-emerald-850 hover:bg-emerald-800 text-gold-400 text-[10px] font-bold flex items-center gap-1 shadow-xs transition active:scale-95 flex-shrink-0">
                    <i data-lucide="check" class="w-3.5 h-3.5"></i>
                    <span id="btnFastLabel">Log Fast</span>
                  </button>
                </div>

                <!-- Suhoor / Iftar Row -->
                <div class="grid grid-cols-2 gap-2 pt-0.5">
                  <div class="p-2 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200/60 dark:border-slate-800 flex items-center justify-between">
                    <div>
                      <p class="text-[9px] text-slate-400 font-semibold uppercase tracking-wider">Suhoor</p>
                      <p id="calSuhoorTime" class="text-xs font-extrabold text-emerald-700 dark:text-emerald-400 mt-0.5">05:22 AM</p>
                    </div>
                    <i data-lucide="sunrise" class="w-4 h-4 text-emerald-600/70"></i>
                  </div>
                  <div class="p-2 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200/60 dark:border-slate-800 flex items-center justify-between">
                    <div>
                      <p class="text-[9px] text-slate-400 font-semibold uppercase tracking-wider">Iftar</p>
                      <p id="calIftarTime" class="text-xs font-extrabold text-amber-600 dark:text-amber-400 mt-0.5">05:49 PM</p>
                    </div>
                    <i data-lucide="sunset" class="w-4 h-4 text-amber-500/80"></i>
                  </div>
                </div>
              </div>

              <!-- Islamic Events (Clean, no AI slop stars, single-line pills) -->
              <div class="p-3 rounded-2xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 shadow-xs space-y-2">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
                    <i data-lucide="calendar-days" class="w-3.5 h-3.5 text-emerald-600"></i> Islamic Events
                  </span>
                  <span class="text-[9px] font-bold text-slate-400">1447–1448 AH</span>
                </div>
                <div class="space-y-1.5 text-xs pt-0.5" id="islamicEventsContainer">
                  <!-- Rendered dynamically -->
                </div>
              </div>

              <!-- Event Notifications Toggle -->
              <div class="p-2.5 rounded-2xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <div class="w-7 h-7 rounded-lg bg-slate-100 dark:bg-slate-750 text-slate-600 dark:text-slate-300 flex items-center justify-center flex-shrink-0">
                    <i data-lucide="bell" class="w-3.5 h-3.5"></i>
                  </div>
                  <div>
                    <h5 class="text-xs font-bold text-slate-800 dark:text-slate-100">Event Notifications</h5>
                    <p class="text-[9px] text-slate-400">Reminders for Sunnah fasts and major dates</p>
                  </div>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" id="chkIslamicEventAlerts" checked onchange="toggleEventNotifications(this.checked)" class="sr-only peer">
                  <div class="w-9 h-5 bg-slate-300 peer-focus:outline-none rounded-full peer dark:bg-slate-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-700"></div>
                </label>
              </div>

            </div>
          </div>

          <!-- 2. 99 NAMES OF ALLAH (ASMA-UL-HUSNA) MODAL -->
          <div id="namesOfAllahModal" class="hidden absolute inset-0 z-50 bg-[#FAF8F5] dark:bg-[#0A1612] flex flex-col pt-11 px-3.5 pb-4 transition-all duration-300 shadow-2xl">
            <!-- Modal Header -->
            <div class="flex items-center justify-between pb-2 border-b border-slate-200 dark:border-slate-800">
              <div class="flex items-center gap-2">
                <div id="namesModalIcon" class="w-7 h-7 rounded-lg bg-gold-500/15 border border-gold-500/30 text-gold-700 dark:text-gold-400 flex items-center justify-center flex-shrink-0 font-bold font-arabic text-xs">
                  الله
                </div>
                <div>
                  <h3 id="namesModalTitle" class="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                    99 Names of Allah <span class="font-arabic text-sm text-gold-500 font-normal">أسماء الله الحسنى</span>
                  </h3>
                  <p id="namesModalSubtitle" class="text-[10px] text-slate-400">"To Allah belong the best names, so call upon Him by them" (7:180)</p>
                </div>
              </div>
              <button onclick="closeNamesOfAllahModal()" class="w-7 h-7 rounded-full bg-slate-200/80 dark:bg-slate-800 flex items-center justify-center text-slate-500 hover:text-slate-800 dark:hover:text-white transition active:scale-90">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>

            <!-- Segmented Switcher (Allah vs Prophet ﷺ) -->
            <div class="grid grid-cols-2 gap-1 mt-2 p-1 rounded-xl bg-slate-200/70 dark:bg-slate-800 text-xs font-bold">
              <button id="tabBtnNamesAllah" onclick="switchNamesTab('allah')" class="py-1.5 rounded-lg bg-emerald-800 text-white font-bold transition flex items-center justify-center gap-1 shadow-xs">
                <span>Allah (99)</span> <span class="font-arabic font-normal text-gold-300">أسماء الله</span>
              </button>
              <button id="tabBtnNamesProphet" onclick="switchNamesTab('prophet')" class="py-1.5 rounded-lg text-slate-600 dark:text-slate-300 font-semibold transition flex items-center justify-center gap-1 hover:text-slate-900 dark:hover:text-white">
                <span>Prophet ﷺ (99)</span> <span class="font-arabic font-normal text-emerald-400">أسماء النبي</span>
              </button>
            </div>

            <!-- Instant Search Input -->
            <div class="relative mt-2">
              <input type="text" id="namesSearchInput" oninput="filterActiveNames(this.value)" placeholder="Search names by number, English, or Arabic..." class="w-full pl-8 pr-3 py-1.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs text-slate-800 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-gold-500">
              <i data-lucide="search" class="w-3.5 h-3.5 absolute left-2.5 top-2 text-slate-400"></i>
            </div>

            <!-- Scrollable Names Container -->
            <div id="namesCardsContainer" class="flex-1 overflow-y-auto space-y-1.5 mt-2 pr-0.5 pb-6">
              <!-- Rendered dynamically -->
            </div>
          </div>

          <!-- 3. FLUTTERFLOW BLUEPRINT & DART CODE DRAWER MODAL -->
          <div id="flutterflowModal" class="hidden absolute inset-0 z-50 bg-[#FAF8F5] dark:bg-[#0A1612] flex flex-col pt-11 px-3.5 pb-4 transition-all duration-300 shadow-2xl">
            <!-- Modal Header -->
            <div class="flex items-center justify-between pb-2.5 border-b border-slate-200 dark:border-slate-800">
              <div class="flex items-center gap-2">
                <div class="w-7 h-7 rounded-lg bg-emerald-850 text-gold-400 flex items-center justify-center flex-shrink-0">
                  <i data-lucide="code-2" class="w-4 h-4"></i>
                </div>
                <div>
                  <h3 class="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                    FlutterFlow Code Blueprints <span class="text-gold-500 text-[10px] font-mono font-bold">100% Ready</span>
                  </h3>
                  <p class="text-[10px] text-slate-400">Custom Actions, Widgets & SQLite Schemas</p>
                </div>
              </div>
              <button onclick="closeFlutterflowModal()" class="w-7 h-7 rounded-full bg-slate-200/80 dark:bg-slate-800 flex items-center justify-center text-slate-500 hover:text-slate-800 dark:hover:text-white transition active:scale-90">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>

            <!-- Tab Switcher -->
            <div class="flex gap-1 overflow-x-auto py-2 text-[10px] font-bold no-scrollbar border-b border-slate-200 dark:border-slate-800">
              <button onclick="switchFFTab('prayer_action')" id="ffTabBtn-prayer_action" class="px-2.5 py-1 rounded-full bg-emerald-800 text-white flex-shrink-0">Prayer Times Action</button>
              <button onclick="switchFFTab('qibla_action')" id="ffTabBtn-qibla_action" class="px-2.5 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">Qibla Trig Action</button>
              <button onclick="switchFFTab('compass_widget')" id="ffTabBtn-compass_widget" class="px-2.5 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">Compass Widget</button>
              <button onclick="switchFFTab('database_schema')" id="ffTabBtn-database_schema" class="px-2.5 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">SQLite Schema</button>
            </div>

            <!-- Code Display & Copy Box -->
            <div class="flex-1 overflow-y-auto pt-2 space-y-2 pr-0.5 pb-6">
              <div class="flex items-center justify-between px-1">
                <span id="ffSnippetTitle" class="text-xs font-bold text-slate-800 dark:text-slate-200">PrayerTimesAction.dart</span>
                <button onclick="copyCurrentFFSnippet()" class="px-2.5 py-1 rounded-lg bg-gold-500 text-slate-950 font-bold text-xs flex items-center gap-1 shadow-xs hover:bg-gold-400 active:scale-95 transition">
                  <i data-lucide="copy" class="w-3 h-3"></i> Copy Code
                </button>
              </div>
              <pre class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-emerald-400 font-mono text-[10px] leading-relaxed overflow-x-auto select-all"><code id="ffSnippetCode"></code></pre>
            </div>
          </div>

          <!-- Scrollable Main Content Area -->
          <div id="appBody" class="flex-1 overflow-y-auto px-3.5 pt-1 pb-16 space-y-3">

            <!-- TAB 1: PRAYERS (DEFAULT) -->
            <div id="tab-prayers" class="tab-content space-y-3">
              
              <!-- Native Header: Uniform Location & Action Island -->
              <div class="flex items-center justify-between pt-1 px-0.5">
                <!-- Location Pill with Chevron -->
                <button onclick="openCityModal()" title="Change Location" class="flex items-center gap-1.5 h-8 px-3 rounded-full bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/70 text-slate-800 dark:text-slate-100 text-xs font-bold hover:border-emerald-500/50 shadow-xs transition active:scale-95">
                  <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400"></i>
                  <span id="cityNameLabel">Karachi</span>
                  <i data-lucide="chevron-down" class="w-3 h-3 text-slate-400"></i>
                </button>

                <!-- Hijri Date Pill & Utility Actions (Consistent Height & Aesthetic) -->
                <div class="flex items-center gap-1.5">
                  <button onclick="openCalendarModal()" title="Hijri Calendar" class="flex items-center gap-1 h-8 px-2.5 rounded-full bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/70 text-[11px] font-bold text-slate-700 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400 shadow-xs transition active:scale-95">
                    <i data-lucide="calendar" class="w-3.5 h-3.5 text-gold-500"></i>
                    <span id="hijriDateLabel">18 Shawwal</span>
                  </button>
                  <button onclick="playAdhanPreview()" id="topAdhanBellBtn" title="Play Adhan Notification" class="w-8 h-8 rounded-full bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/70 flex items-center justify-center text-slate-600 dark:text-slate-300 hover:text-gold-500 active:scale-90 transition shadow-xs">
                    <i data-lucide="bell" class="w-3.5 h-3.5"></i>
                  </button>
                  <button onclick="openSettingsModal()" title="Settings" class="w-8 h-8 rounded-full bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/70 flex items-center justify-center text-slate-600 dark:text-slate-300 hover:text-emerald-600 active:scale-90 transition shadow-xs">
                    <i data-lucide="settings" class="w-3.5 h-3.5"></i>
                  </button>
                </div>
              </div>

              <!-- Hero Countdown Card with Visual Prayer Window Elapsed Bar -->
              <div class="emerald-gradient text-white rounded-2xl p-4 shadow-md relative overflow-hidden border border-emerald-700/40">
                <div class="absolute -right-8 -bottom-8 w-32 h-32 rounded-full bg-emerald-600/15 pointer-events-none"></div>
                
                <div class="flex items-center justify-between">
                  <span id="lblNextPrayerBadge" class="px-2.5 py-0.5 rounded-full bg-gold-500/20 text-gold-400 text-[9px] font-extrabold uppercase tracking-widest border border-gold-500/30">
                    Upcoming
                  </span>
                  <span id="heroPrayerTime" class="text-xs font-semibold text-slate-200">12:21 PM</span>
                </div>

                <div class="mt-2.5 flex items-baseline justify-between">
                  <div>
                    <h2 id="heroPrayerName" class="text-2xl font-extrabold tracking-tight">Dhuhr</h2>
                    <p id="lblCountdownSub" class="text-slate-300 text-[11px] mt-0.5">Countdown</p>
                  </div>
                  <div id="countdownTimer" class="text-2xl font-mono font-bold text-gold-400 tracking-wider">
                    02:14:32
                  </div>
                </div>

                <!-- Prayer Interval Elapsed Progress Bar -->
                <div class="w-full bg-emerald-950/70 rounded-full h-1 mt-3 overflow-hidden">
                  <div id="prayerWindowProgress" class="bg-gold-400 h-full rounded-full transition-all duration-500" style="width: 48%;"></div>
                </div>
              </div>

              <!-- Daily Salah Tracker (Interactive Prayer Log & Streak) -->
              <div class="p-2.5 rounded-2xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 shadow-xs space-y-2">
                <div class="flex items-center justify-between text-[11px]">
                  <div class="flex items-center gap-1.5 font-bold text-slate-800 dark:text-white text-xs">
                    <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600"></i>
                    <span id="lblDailySalahTitle">Salah Log</span>
                  </div>
                  <div class="flex items-center gap-1.5">
                    <span id="salahTrackerProgressText" class="text-[10px] font-bold text-emerald-700 dark:text-emerald-400">0/5</span>
                    <button onclick="markAllPrayersToday()" id="btnMarkAllSalah" title="Mark All Completed" class="text-[9px] font-bold px-2 py-0.5 rounded-full bg-emerald-700 hover:bg-emerald-800 text-white shadow-xs transition active:scale-95">
                      All
                    </button>
                    <button onclick="resetDailySalahTracker()" title="Reset Today" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 p-0.5 rounded transition">
                      <i data-lucide="rotate-ccw" class="w-3 h-3"></i>
                    </button>
                  </div>
                </div>
                <!-- 5 Prayer Status Circles -->
                <div class="grid grid-cols-5 gap-1.5 text-center pt-0.5" id="salahTrackerCirclesContainer">
                  <!-- Rendered dynamically by renderSalahTracker() -->
                </div>
              </div>

              <!-- Daily Prayer Timetable -->
              <div class="space-y-1.5">
                <div class="px-1">
                  <span id="lblTimetableTitle" class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Timetable</span>
                </div>

                <div id="prayerCardsList" class="space-y-1.5">
                  <!-- Generated by JS with individual alarm bell toggles -->
                </div>
              </div>

              <!-- Daily Hadith Card with Next & Copy Controls -->
              <div class="bg-white dark:bg-slate-800/90 rounded-2xl p-3.5 border border-slate-200/80 dark:border-slate-700/80 shadow-xs space-y-2">
                <div class="flex items-center justify-between">
                  <span id="lblDailyHadithTitle" class="text-[10px] font-bold text-emerald-800 dark:text-emerald-400 uppercase tracking-wider flex items-center gap-1">
                    <i data-lucide="book-marked" class="w-3 h-3 text-gold-500"></i> Daily Hadith
                  </span>
                  <div class="flex items-center gap-1.5">
                    <button onclick="copyCurrentHadith()" title="Copy Hadith" class="text-slate-400 hover:text-emerald-700 text-[10px] font-semibold flex items-center gap-0.5 px-1.5 py-0.5 rounded hover:bg-slate-100 dark:hover:bg-slate-700 transition">
                      <i data-lucide="copy" class="w-3 h-3"></i> Copy
                    </button>
                    <button onclick="shareCurrentHadith()" title="Share Hadith to WhatsApp" class="text-emerald-700 dark:text-emerald-400 hover:underline text-[10px] font-bold flex items-center gap-0.5 px-1.5 py-0.5 rounded hover:bg-slate-100 dark:hover:bg-slate-700 transition">
                      <i data-lucide="share-2" class="w-3 h-3"></i> Share
                    </button>
                    <button onclick="cycleNextHadith()" title="Next Hadith" class="text-emerald-700 dark:text-emerald-400 hover:underline text-[10px] font-bold flex items-center gap-0.5 px-1.5 py-0.5 rounded hover:bg-slate-100 dark:hover:bg-slate-700 transition">
                      <i data-lucide="refresh-cw" class="w-3 h-3"></i> Next
                    </button>
                  </div>
                </div>
                <p id="hadithMatnAr" class="notranslate font-arabic text-right text-[19px] text-emerald-950 dark:text-emerald-100 font-bold leading-[2.2]" translate="no" lang="ar" dir="rtl">
                  إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى
                </p>
                <p id="hadithMatnEn" class="text-[14px] text-slate-700 dark:text-slate-200 leading-relaxed font-normal">
                  "Actions are judged by intentions, and every person will be rewarded according to their intention."
                </p>
                <div class="pt-1 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between text-[10px] text-slate-400">
                  <span id="hadithNarratorText">Umar ibn Al-Khattab (RA)</span>
                  <span id="hadithSourceText" class="font-semibold text-emerald-700 dark:text-emerald-400">Sahih al-Bukhari 1</span>
                </div>
              </div>

              <!-- 99 Names of Allah & Prophet Muhammad ﷺ (Unified 2-Column Responsive Card) -->
              <div class="bg-white dark:bg-slate-800/90 rounded-2xl p-3 border border-slate-200/80 dark:border-slate-700/80 shadow-xs space-y-2">
                <div class="flex items-center justify-between pb-0.5">
                  <div class="flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-gold-500"></span>
                    <h4 class="text-xs font-bold text-slate-900 dark:text-white">99 Divine & Noble Names</h4>
                  </div>
                  <span class="text-[10px] text-slate-400 font-arabic">الأسماء الحسنى الشريفة</span>
                </div>
                <div class="grid grid-cols-2 gap-2">
                  <!-- Allah (99) -->
                  <div onclick="openNamesModal('allah')" class="cursor-pointer p-2.5 rounded-xl bg-gold-500/10 dark:bg-gold-500/15 border border-gold-500/30 hover:border-gold-500 text-left flex items-center gap-2 transition active:scale-95 group shadow-2xs">
                    <div class="w-8 h-8 rounded-lg bg-gold-500/20 text-gold-700 dark:text-gold-400 flex items-center justify-center font-bold text-xs font-arabic flex-shrink-0">
                      الله
                    </div>
                    <div class="min-w-0 flex-1">
                      <p class="text-xs font-bold text-slate-900 dark:text-white truncate">Allah (99)</p>
                      <p class="text-[9px] text-gold-600 dark:text-gold-400 font-arabic truncate whitespace-nowrap">أسماء الله الحسنى</p>
                    </div>
                  </div>
                  <!-- Prophet Muhammad (99) -->
                  <div onclick="openNamesModal('prophet')" class="cursor-pointer p-2.5 rounded-xl bg-emerald-500/10 dark:bg-emerald-500/15 border border-emerald-500/30 hover:border-emerald-500 text-left flex items-center gap-2 transition active:scale-95 group shadow-2xs">
                    <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-700 dark:text-emerald-400 flex items-center justify-center font-bold text-xs font-arabic flex-shrink-0">
                      محمد
                    </div>
                    <div class="min-w-0 flex-1">
                      <p class="text-xs font-bold text-slate-900 dark:text-white truncate">Prophet ﷺ (99)</p>
                      <p class="text-[9px] text-emerald-600 dark:text-emerald-400 font-arabic truncate whitespace-nowrap">أسماء النبي</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- TAB 2: QIBLA (SPHERICAL TRIG SENSOR ENGINE) -->
            <div id="tab-qibla" class="tab-content hidden space-y-3 text-center pt-1">
              <div>
                <h2 id="lblQiblaTitle" class="text-base font-bold text-slate-900 dark:text-white">Qibla</h2>
                <p class="text-xs text-slate-500">
                  <span id="qiblaBearingValueText" class="font-bold text-emerald-700 dark:text-emerald-400">265° W</span> 
                  • <span id="qiblaDistanceValueText">2,810 km</span>
                </p>
              </div>

              <!-- Compass Dial Frame -->
              <div class="relative w-60 h-60 mx-auto flex items-center justify-center">
                
                <!-- Outer Ring (Glows gold/emerald when aligned) -->
                <div id="compassOuterRing" class="w-60 h-60 rounded-full border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 flex items-center justify-center shadow-lg transition-all duration-300">
                  
                  <!-- Rotating Compass Dial -->
                  <div id="compassDial" class="w-52 h-52 rounded-full border border-dashed border-slate-300 dark:border-slate-600 relative transition-transform duration-150 ease-out flex items-center justify-center">
                    
                    <span class="absolute top-2 text-xs font-bold text-red-500">N</span>
                    <span class="absolute bottom-2 text-xs font-bold text-slate-400">S</span>
                    <span class="absolute right-2 text-xs font-bold text-slate-400">E</span>
                    <span class="absolute left-2 text-xs font-bold text-slate-400">W</span>

                    <!-- Kaaba Target Needle -->
                    <div id="kaabaNeedleContainer" class="absolute inset-0 flex flex-col items-center pointer-events-none transition-transform duration-200">
                      <div class="mt-2 flex flex-col items-center">
                        <div class="w-7 h-7 rounded-full bg-emerald-900 text-gold-400 flex items-center justify-center shadow-md border border-gold-500/70">
                          <i data-lucide="navigation" class="w-3.5 h-3.5 fill-current"></i>
                        </div>
                        <span class="text-[8px] font-extrabold text-gold-500 uppercase mt-0.5">Kaaba</span>
                      </div>
                    </div>
                  </div>

                  <!-- Center Hub (Precision Circular Glass Pivot) -->
                  <div class="absolute w-20 h-20 rounded-full bg-white/95 dark:bg-slate-900/95 border-2 border-slate-200/90 dark:border-slate-700/90 shadow-md flex flex-col items-center justify-center z-10 backdrop-blur-xs">
                    <span id="compassDegrees" class="text-xl font-extrabold text-slate-900 dark:text-white font-mono tracking-tight leading-none">0°</span>
                    <span id="compassStatus" class="text-[8px] font-black tracking-widest text-slate-400 uppercase mt-0.5">TURN</span>
                  </div>
                </div>
              </div>

              <!-- Live Phone Sensor & Simulation Controls -->
              <div class="px-4 space-y-2">
                <div class="flex items-center justify-between">
                  <button onclick="togglePhoneCompassSensor()" id="phoneCompassBtn" class="px-3 py-1.5 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs font-bold flex items-center gap-1.5 transition active:scale-95 border border-slate-300 dark:border-slate-700">
                    <i data-lucide="compass" class="w-3.5 h-3.5 text-emerald-600"></i>
                    <span id="phoneCompassBtnText">Live Compass Sensor</span>
                  </button>
                  <button onclick="detectLocationGPS()" class="px-2.5 py-1.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 text-xs font-bold flex items-center gap-1 border border-emerald-300/50">
                    <i data-lucide="map-pin" class="w-3 h-3"></i> GPS
                  </button>
                </div>

                <div class="space-y-1">
                  <div class="flex items-center justify-between text-[11px] font-semibold text-slate-400">
                    <span>Manual Rotation Slider</span>
                    <span id="qiblaTargetLabel" class="text-emerald-600 dark:text-emerald-400 font-bold">Align at 265°</span>
                  </div>
                  <input id="headingSlider" type="range" min="0" max="360" value="0" oninput="updateCompass(this.value, true)" class="w-full accent-emerald-700 cursor-pointer">
                  <div class="flex justify-between text-[10px] text-slate-400">
                    <span>0° (North)</span>
                    <span>180° (South)</span>
                    <span>360°</span>
                  </div>
                </div>
              </div>

              <div id="alignmentBannerCard" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-500">
                <span id="alignmentBanner">Rotate compass to match target bearing</span>
              </div>
            </div>

            <!-- TAB 3: QURAN (UTHMANI READER & TRANSLITERATION) -->
            <div id="tab-quran" class="tab-content hidden space-y-3 pt-1">
              
              <!-- Surah Selector & Reader Controls Bar -->
              <div class="flex items-center justify-between">
                <div>
                  <h2 id="lblQuranTitle" class="text-base font-extrabold tracking-tight text-slate-900 dark:text-white">Quran</h2>
                </div>

                <!-- Font Size, Bookmarks & Transliteration Controls -->
                <div class="flex items-center gap-1 bg-slate-200 dark:bg-slate-800 p-0.5 rounded-lg text-xs font-bold">
                  <button onclick="changeFontSize(-2)" title="Decrease Font" class="w-6 h-6 flex items-center justify-center rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 font-bold text-xs hover:bg-slate-100 transition active:scale-95">-</button>
                  <button onclick="changeFontSize(2)" title="Increase Font" class="w-6 h-6 flex items-center justify-center rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 font-bold text-xs hover:bg-slate-100 transition active:scale-95">+</button>
                  <button onclick="toggleTransliteration()" id="translitBtn" title="Toggle English Transliteration" class="w-6 h-6 flex items-center justify-center rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 text-[10px] font-bold hover:bg-slate-100 transition active:scale-95">
                    Aa
                  </button>
                  <button onclick="openBookmarksModal()" id="topBookmarksBtn" title="Saved Bookmarks" class="h-6 px-1.5 rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 flex items-center gap-0.5 hover:text-gold-500 transition active:scale-95">
                    <i data-lucide="bookmark" class="w-3 h-3 text-gold-500 fill-current"></i>
                    <span id="topBookmarksCount" class="text-[10px] font-bold">0</span>
                  </button>
                  <button onclick="toggleAudioRecitation()" id="reciteAudioBtn" class="h-6 px-2 rounded bg-emerald-800 text-white flex items-center gap-1 font-bold text-xs active:scale-95 transition shadow-xs">
                    <i data-lucide="volume-2" class="w-3 h-3"></i> Recite
                  </button>
                </div>
              </div>

              <!-- Sleek Top Search Bar (Spacious, Clean & Responsive) -->
              <div onclick="openSurahIndexModal()" class="cursor-pointer relative flex items-center bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 rounded-xl px-3 py-2 text-xs hover:border-gold-500/60 transition shadow-xs group">
                <i data-lucide="search" class="w-3.5 h-3.5 text-slate-400 group-hover:text-gold-500 mr-2 flex-shrink-0 transition"></i>
                <span class="text-slate-400 dark:text-slate-400 text-xs truncate">Search Surahs, Duas & Verses...</span>
              </div>

              <!-- Quick Horizontal Surahs Scroll Bar -->
              <div class="flex gap-1.5 overflow-x-auto pb-0.5 text-xs no-scrollbar items-center" id="surahPillsBar">
                <!-- Rendered dynamically -->
              </div>

              <!-- Clean & Spacious Surah Banner Card -->
              <div onclick="openSurahIndexModal()" title="Click to browse all 114 Surahs" class="emerald-gradient text-white rounded-2xl p-4 text-center relative overflow-hidden border border-emerald-700/50 shadow-sm cursor-pointer group hover:border-gold-500/50 transition">
                <div class="flex items-center justify-between text-[11px] text-gold-300 uppercase font-semibold">
                  <span id="surahMetaType">MECCAN</span>
                  <span id="surahMetaVerses">7 VERSES</span>
                </div>
                <h3 id="surahHeaderTitleAr" class="notranslate font-arabic text-3xl font-bold py-1.5 text-gold-400 select-none" translate="no" lang="ar" dir="rtl">سُورَةُ الفَاتِحَة</h3>
                <p id="surahHeaderTitleEn" class="text-xs font-semibold text-white tracking-wide">1. Al-Fatihah <span class="text-emerald-200/80 font-normal">• The Opening</span></p>
                
                <div class="mt-3 pt-2.5 border-t border-emerald-800/80">
                  <p class="notranslate font-quran-text text-lg text-gold-300 leading-normal" translate="no" lang="ar" dir="rtl">
                    بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
                  </p>
                </div>
              </div>

              <!-- Verses Container -->
              <div id="quranVersesList" class="space-y-2.5 pb-3">
                <!-- Rendered dynamically by JS with Amiri Quran font -->
              </div>
            </div>

            <!-- TAB 4: ADHKAR (INTERACTIVE COUNTERS & SESSION PROGRESS) -->
            <div id="tab-adhkar" class="tab-content hidden space-y-2.5 pt-1">
              <div class="flex items-center justify-between">
                <div>
                  <h2 id="lblAdhkarTitle" class="text-base font-bold text-slate-900 dark:text-white">Adhkar</h2>
                  <p class="text-[10px] text-slate-400">Hisn al-Muslim</p>
                </div>
              </div>

              <!-- Category Filter Chips -->
              <div class="flex items-center gap-1.5 overflow-x-auto pb-0.5 text-xs no-scrollbar">
                <button id="adhkarMornBtn" onclick="setAdhkarMode('morning')" class="px-3 py-1 rounded-full bg-emerald-800 text-white font-bold shadow-xs flex-shrink-0 transition">Morning</button>
                <button id="adhkarEveBtn" onclick="setAdhkarMode('evening')" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-semibold flex-shrink-0 transition">Evening</button>
                <button id="adhkarAfterBtn" onclick="setAdhkarMode('after_prayer')" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-semibold flex-shrink-0 transition">After Salah</button>
                <button id="adhkarDailyBtn" onclick="setAdhkarMode('daily')" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-semibold flex-shrink-0 transition">Daily Duas</button>
                <button id="adhkarQuranicBtn" onclick="setAdhkarMode('quranic')" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-semibold flex-shrink-0 transition">Quranic Duas</button>
                <button id="adhkarSleepBtn" onclick="setAdhkarMode('sleep')" class="px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-semibold flex-shrink-0 transition">Sleep</button>
              </div>

              <!-- Real-Time Adhkar Search with Floating Suggestions Dropdown -->
              <div class="relative" id="adhkarSearchContainer">
                <input type="text" id="adhkarSearchInput" oninput="handleAdhkarLiveSearch(this.value)" onfocus="handleAdhkarLiveSearch(this.value)" placeholder="Search adhkar & duas..." class="w-full pl-8 pr-7 py-1.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs text-slate-800 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-emerald-600 transition shadow-2xs">
                <i data-lucide="search" class="w-3.5 h-3.5 absolute left-2.5 top-2 text-slate-400"></i>
                <button id="adhkarSearchClearBtn" onclick="clearAdhkarSearch()" class="hidden absolute right-2.5 top-1.5 text-slate-400 hover:text-slate-600 dark:hover:text-white p-0.5 transition">
                  <i data-lucide="x" class="w-3.5 h-3.5"></i>
                </button>
                
                <!-- Floating Live Suggestions Dropdown -->
                <div id="adhkarSuggestionsDropdown" class="hidden absolute left-0 right-0 top-full mt-1.5 z-40 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700/80 rounded-2xl shadow-xl max-h-56 overflow-y-auto p-1.5 space-y-1">
                  <!-- Injected dynamically on keystroke -->
                </div>
              </div>

              <!-- Overall Adhkar Progress Tracker & Reset -->
              <div class="p-2.5 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 flex items-center justify-between text-xs shadow-xs">
                <div class="flex items-center gap-1.5">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600"></i>
                  <span id="lblProgressWord" class="text-slate-500 text-[11px]">Completed:</span>
                  <span id="adhkarProgressText" class="font-bold text-emerald-700 dark:text-emerald-400">0 of 5 (0%)</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-20 h-1.5 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                    <div id="adhkarProgressBar" class="h-full bg-emerald-600 transition-all duration-300" style="width: 0%;"></div>
                  </div>
                  <button onclick="resetAdhkarSession()" title="Reset Session" class="text-slate-400 hover:text-red-500 text-[10px] font-semibold">
                    <i data-lucide="rotate-ccw" class="w-3 h-3"></i>
                  </button>
                </div>
              </div>

              <div id="adhkarItemsList" class="space-y-2">
                <!-- Rendered via JS with interactive counts and references -->
              </div>
            </div>

            <!-- TAB 5: TASBEEH (TACTILE AUDIO COUNTER WITH REAL SVG PROGRESS RING) -->
            <div id="tab-tasbeeh" class="tab-content hidden space-y-3 pt-1 text-center">
              <div class="flex items-center justify-between px-1">
                <div>
                  <h2 id="lblTasbeehTitle" class="text-base font-bold text-slate-900 dark:text-white text-left">Tasbeeh</h2>
                  <p id="lblTasbeehSub" class="text-[10px] text-slate-400 text-left">Dhikr Counter</p>
                </div>
                <div class="flex items-center gap-1.5">
                  <button onclick="cycleTasbeehSound()" id="soundProfileBtn" title="Change Tasbeeh Tap Sound" class="px-2 py-1 text-[10px] font-bold rounded-lg bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-300/50 text-emerald-800 dark:text-emerald-300 flex items-center gap-1 active:scale-95 transition">
                    <span id="soundProfileName">🪵 Wood</span>
                  </button>
                  <button onclick="toggleTasbeehSound()" id="soundToggleBtn" title="Toggle Tap Sound (ON/OFF)" class="w-7 h-7 rounded-lg bg-slate-200/90 dark:bg-slate-800 flex items-center justify-center text-slate-700 dark:text-slate-300 active:scale-95 transition shadow-xs border border-slate-300/40 dark:border-slate-700/60">
                    <i data-lucide="volume-2" class="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400"></i>
                  </button>
                </div>
              </div>

              <!-- Dhikr Selector Pills (6 Presets) -->
              <div class="flex gap-1.5 overflow-x-auto pb-1 text-xs">
                <button onclick="setTasbeehDhikr(0)" id="dhikr-pill-0" class="px-3 py-1.5 rounded-full font-bold bg-emerald-800 text-white flex-shrink-0">SubhanAllah</button>
                <button onclick="setTasbeehDhikr(1)" id="dhikr-pill-1" class="px-3 py-1.5 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">Alhamdulillah</button>
                <button onclick="setTasbeehDhikr(2)" id="dhikr-pill-2" class="px-3 py-1.5 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">Allahu Akbar</button>
                <button onclick="setTasbeehDhikr(3)" id="dhikr-pill-3" class="px-3 py-1.5 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">Astaghfirullah</button>
                <button onclick="setTasbeehDhikr(4)" id="dhikr-pill-4" class="px-3 py-1.5 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">La Ilaha Illallah</button>
                <button onclick="setTasbeehDhikr(5)" id="dhikr-pill-5" class="px-3 py-1.5 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">Salawat</button>
              </div>

              <!-- Current Arabic Phrase in Crystal Clear Calligraphy -->
              <div class="py-1">
                <h3 id="currentDhikrAr" class="notranslate font-arabic text-2xl font-bold text-emerald-950 dark:text-emerald-300" translate="no" lang="ar" dir="rtl">سُبْحَانَ اللَّهِ</h3>
              </div>

              <!-- Giant Interactive Tap Dial with Dynamic SVG Progress Arc -->
              <div class="relative w-56 h-56 mx-auto flex items-center justify-center">
                <!-- Circular SVG Progress Ring -->
                <svg class="absolute inset-0 w-full h-full -rotate-90 pointer-events-none" viewBox="0 0 224 224">
                  <!-- Background Track -->
                  <circle cx="112" cy="112" r="96" stroke="currentColor" stroke-width="6" fill="none" class="text-slate-200 dark:text-slate-800" />
                  <!-- Dynamic Golden Progress Arc -->
                  <circle id="tasbeehProgressArc" cx="112" cy="112" r="96" stroke="#C5A059" stroke-width="7" stroke-linecap="round" fill="none" stroke-dasharray="603" stroke-dashoffset="603" class="transition-all duration-150" />
                </svg>

                <button onclick="incrementTasbeeh()" class="w-48 h-48 rounded-full bg-white dark:bg-slate-800 shadow-xl flex flex-col items-center justify-center active:scale-95 transition-transform duration-75 border border-slate-100 dark:border-slate-700">
                  <span id="tasbeehCount" class="text-5xl font-extrabold text-slate-900 dark:text-white font-sans tracking-tight">0</span>
                  <span id="tasbeehTargetLabel" class="text-[10px] font-bold uppercase tracking-widest text-slate-400 mt-1">Target 33</span>
                  <span id="tasbeehLapsLabel" class="text-[10px] font-semibold text-emerald-700 dark:text-emerald-400 mt-0.5">Lap 1</span>
                </button>
              </div>

              <!-- Target Controls Bar & Daily Session Counter -->
              <div class="space-y-1.5 pt-1">
                <div class="flex items-center justify-center gap-2">
                  <button onclick="setTasbeehTarget(33)" id="target-btn-33" class="px-3 py-1 text-xs font-bold rounded-lg border border-emerald-600 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300">33</button>
                  <button onclick="setTasbeehTarget(99)" id="target-btn-99" class="px-3 py-1 text-xs font-bold rounded-lg border border-slate-300 dark:border-slate-700">99</button>
                  <button onclick="setTasbeehTarget(100)" id="target-btn-100" class="px-3 py-1 text-xs font-bold rounded-lg border border-slate-300 dark:border-slate-700">100</button>
                  <button onclick="setTasbeehTarget(0)" id="target-btn-0" class="px-2.5 py-1 text-xs font-bold rounded-lg border border-slate-300 dark:border-slate-700">∞</button>
                  <button onclick="resetTasbeeh()" class="px-3 py-1 text-xs font-bold rounded-lg bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300">Reset</button>
                </div>
                <p class="text-[11px] text-slate-400">
                  Total beads counted today: <span id="tasbeehTotalDaily" class="font-bold text-emerald-700 dark:text-emerald-400">0</span>
                </p>
              </div>
            </div>

          </div>

          <!-- Floating Bottom Mini Audio Player (YouTube Music / Spotify Style) -->
          <div id="miniAudioPlayer" class="hidden absolute bottom-[68px] left-3 right-3 bg-slate-900/95 dark:bg-slate-950/95 backdrop-blur-md rounded-2xl border border-gold-500/40 shadow-2xl z-40 overflow-hidden transition-all duration-300">
            <!-- Top Ultra-thin 2px Solid Gold Progress Line -->
            <div class="w-full bg-white/10 h-0.5 relative">
              <div id="miniPlayerProgress" class="h-full bg-gold-500 w-0 transition-all duration-150 shadow-[0_0_8px_rgba(230,179,37,0.8)]"></div>
            </div>
            
            <div class="px-3 py-2 flex items-center justify-between gap-2.5">
              <!-- Left: Disc Artwork & Details (Click to jump to Ayah) -->
              <div onclick="jumpToCurrentRecitingAyah()" class="flex items-center gap-2.5 min-w-0 flex-1 cursor-pointer">
                <div class="w-9 h-9 rounded-xl bg-emerald-950 border border-gold-500/40 flex items-center justify-center flex-shrink-0 relative overflow-hidden shadow-inner">
                  <img src="assets/reciter_artwork.png" onerror="this.src='preview/reciter_artwork.png'" class="w-full h-full object-cover" alt="Reciter">
                  <div class="absolute inset-0 bg-gold-500/10 animate-pulse"></div>
                </div>
                <div class="min-w-0">
                  <div class="flex items-center gap-1.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                    <h4 id="miniPlayerTitle" class="text-xs font-bold text-white truncate">Ayah 1 • Surah Al-Fatihah</h4>
                  </div>
                  <p id="miniPlayerSubtitle" class="text-[10px] text-gold-400/90 truncate">Sheikh Mishary Rashid Alafasy</p>
                </div>
              </div>

              <!-- Right: Media Player Action Controls -->
              <div class="flex items-center gap-1 flex-shrink-0">
                <button onclick="playPreviousAyahAudio()" title="Previous Ayah" class="p-1.5 text-slate-300 hover:text-white transition active:scale-95">
                  <i data-lucide="skip-back" class="w-4 h-4"></i>
                </button>
                <button onclick="toggleMiniPlayerPlayPause()" id="miniPlayerPlayBtn" title="Play / Pause" class="w-8 h-8 rounded-full bg-gold-500 hover:bg-gold-400 text-slate-950 flex items-center justify-center transition shadow-md shadow-gold-500/20 active:scale-95">
                  <i data-lucide="pause" class="w-4 h-4 fill-current"></i>
                </button>
                <button onclick="playNextAyahAudio()" title="Next Ayah" class="p-1.5 text-slate-300 hover:text-white transition active:scale-95">
                  <i data-lucide="skip-forward" class="w-4 h-4"></i>
                </button>
                <button onclick="stopAyahAudio(); hideMiniPlayer();" title="Close" class="p-1 text-slate-400 hover:text-red-400 transition ml-0.5">
                  <i data-lucide="x" class="w-3.5 h-3.5"></i>
                </button>
              </div>
            </div>
          </div>

          <!-- Bottom Navigation Bar (Strict 1-Word Clean Islamic Navigation) -->
          <div class="absolute bottom-0 left-0 right-0 h-16 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-t border-slate-200/80 dark:border-slate-800 px-2 flex items-center justify-around z-40 select-none">
            <button onclick="switchTab('prayers')" id="nav-prayers" class="flex flex-col items-center gap-1 text-emerald-800 dark:text-emerald-400 font-bold transition">
              <svg class="w-5 h-5 fill-none stroke-current" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              <span id="tabNavTextPrayers" class="text-[10px]">Prayers</span>
            </button>
            <button onclick="switchTab('qibla')" id="nav-qibla" class="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-600 transition">
              <svg class="w-5 h-5 fill-none stroke-current" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
              <span id="tabNavTextQibla" class="text-[10px]">Qibla</span>
            </button>
            <button onclick="switchTab('quran')" id="nav-quran" class="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-600 transition">
              <svg class="w-5 h-5 fill-none stroke-current" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
              <span id="tabNavTextQuran" class="text-[10px]">Quran</span>
            </button>
            <button onclick="switchTab('adhkar')" id="nav-adhkar" class="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-600 transition">
              <!-- Vector Dua / Supplication Hands SVG -->
              <svg class="w-5 h-5 fill-none stroke-current" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M7 11V6a2 2 0 0 1 4 0v5"/>
                <path d="M13 11V6a2 2 0 0 1 4 0v5"/>
                <path d="M3 13a4 4 0 0 0 4 4h10a4 4 0 0 0 4-4v-2a2 2 0 0 0-2-2h-1"/>
                <path d="M4 11.5a2 2 0 0 1 2-2h1"/>
              </svg>
              <span id="tabNavTextAdhkar" class="text-[10px]">Adhkar</span>
            </button>
            <button onclick="switchTab('tasbeeh')" id="nav-tasbeeh" class="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-600 transition">
              <!-- Vector Misbaha / Tasbeeh Bead Ring SVG -->
              <svg class="w-5 h-5 fill-none stroke-current" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="10" r="7"/>
                <path d="M12 17v4"/>
                <circle cx="12" cy="21.5" r="1" fill="currentColor"/>
                <path d="M12 3V2"/>
              </svg>
              <span id="tabNavTextTasbeeh" class="text-[10px]">Tasbeeh</span>
            </button>
          </div>

          <!-- Device Home Indicator Bar -->
          <div class="absolute bottom-1 left-0 right-0 flex justify-center pointer-events-none z-50">
            <div id="iosHomeBar" class="w-28 h-1 bg-slate-400/60 dark:bg-slate-500/60 rounded-full"></div>
            <div id="androidNavLine" class="hidden w-16 h-1 bg-slate-400/60 dark:bg-slate-500/60 rounded-full"></div>
          </div>

        </div>
      </div>
    </div>

  </div>

  <script>
    // State Architecture
    let currentOS = 'ios';
    let isArabic = false;
    let isDark = false;
    let currentCityIndex = 0;
    let quranFontSize = 25; // Default px
    let showTransliteration = true;
    let isTasbeehSoundOn = true;
    let bookmarkedVerses = {};
    let prayerAlerts = { Fajr: true, Sunrise: true, Dhuhr: true, Asr: true, Maghrib: true, Isha: true };

    // Web Audio Synthesizer (Realistic acoustic clicks, wood beads & chimes)
    let audioCtx = null;
    let currentTasbeehSound = localStorage.getItem("muslim_comp_tasbeeh_sound") || "wood";

    function setTasbeehSound(soundType) {
      currentTasbeehSound = soundType;
      localStorage.setItem("muslim_comp_tasbeeh_sound", soundType);
      
      // Auto-enable sound when a user explicitly selects a sound in Settings
      isTasbeehSoundOn = true;
      const soundBtn = document.getElementById("soundToggleBtn");
      if (soundBtn) {
        soundBtn.innerHTML = `<i data-lucide="volume-2" class="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400"></i>`;
        soundBtn.className = "w-7 h-7 rounded-lg flex items-center justify-center active:scale-95 transition shadow-xs bg-slate-200/90 dark:bg-slate-800 border border-slate-300/40 dark:border-slate-700/60";
      }

      // Live sound preview - force play even if previously muted
      playTasbeehTickSound(soundType, true);
      renderTasbeehSoundSelectors();
      lucide.createIcons();
      showToast("Tap Sound Selected", `${soundType.toUpperCase()} sound enabled`);
    }

    function cycleTasbeehSound() {
      const sounds = ['wood', 'click', 'water', 'digital'];
      const idx = sounds.indexOf(currentTasbeehSound);
      const nextSound = sounds[(idx + 1) % sounds.length];
      setTasbeehSound(nextSound);
    }

    function renderTasbeehSoundSelectors() {
      const sounds = ['wood', 'click', 'water', 'digital'];
      const soundLabels = { wood: 'Wood Bead', click: 'Soft Click', water: 'Water Drop', digital: 'Digital' };
      const badge = document.getElementById("currentSoundLabelBadge");
      if (badge) badge.innerText = soundLabels[currentTasbeehSound] || 'Wood Bead';
      
      const soundEmojis = { wood: '🪵 Wood', click: '🔘 Click', water: '💧 Water', digital: '📟 Digital' };
      const profName = document.getElementById("soundProfileName");
      if (profName) profName.innerText = soundEmojis[currentTasbeehSound] || '🪵 Wood';

      sounds.forEach(s => {
        const btn = document.getElementById(`sndBtn-${s}`);
        if (btn) {
          if (s === currentTasbeehSound) {
            btn.className = "p-1.5 rounded-lg border text-center transition active:scale-95 bg-emerald-50 dark:bg-emerald-950 border-emerald-500 text-emerald-800 dark:text-emerald-300 font-bold text-[10px]";
          } else {
            btn.className = "p-1.5 rounded-lg border text-center transition active:scale-95 bg-slate-50 dark:bg-slate-900 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 text-[10px]";
          }
        }
      });
    }

    function playTasbeehTickSound(soundType = null, forcePlay = false) {
      if (!isTasbeehSoundOn && !forcePlay) return;
      const sound = soundType || currentTasbeehSound;
      if (sound === 'silent') return;

      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
        const t = audioCtx.currentTime;
        
        if (sound === 'wood') {
          // Acoustic Wooden Bead Clack (richer resonance)
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(580, t);
          osc.frequency.exponentialRampToValueAtTime(140, t + 0.045);
          gain.gain.setValueAtTime(0.38, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.05);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(t);
          osc.stop(t + 0.055);
        } else if (sound === 'click') {
          // Crisp Tactile Mechanical Click
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(1300, t);
          osc.frequency.exponentialRampToValueAtTime(320, t + 0.028);
          gain.gain.setValueAtTime(0.32, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.032);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(t);
          osc.stop(t + 0.035);
        } else if (sound === 'water') {
          // Gentle Spiritual Water Drop
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(960, t);
          osc.frequency.exponentialRampToValueAtTime(1550, t + 0.035);
          osc.frequency.exponentialRampToValueAtTime(680, t + 0.075);
          gain.gain.setValueAtTime(0.30, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.085);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(t);
          osc.stop(t + 0.095);
        } else if (sound === 'digital') {
          // Clean Modern Beep
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(920, t);
          gain.gain.setValueAtTime(0.24, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.035);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(t);
          osc.stop(t + 0.04);
        }
      } catch (e) {}
    }

    function playClickSound() {
      playTasbeehTickSound();
    }

    function playChimeSound() {
      if (!isTasbeehSoundOn) return;
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(523.25, audioCtx.currentTime); // C5
        osc.frequency.setValueAtTime(659.25, audioCtx.currentTime + 0.1); // E5
        osc.frequency.setValueAtTime(783.99, audioCtx.currentTime + 0.2); // G5
        gain.gain.setValueAtTime(0.25, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.55);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.6);
      } catch (e) {}
    }

    function showToast(title, message) {
      const toast = document.getElementById("adhanToast");
      document.getElementById("toastHeaderTitle").innerText = title;
      document.getElementById("toastMessageText").innerText = message;
      toast.classList.remove("hidden", "-translate-y-4", "opacity-0");
      toast.classList.add("translate-y-0", "opacity-100");
      lucide.createIcons();

      if (window.toastTimer) clearTimeout(window.toastTimer);
      window.toastTimer = setTimeout(() => {
        dismissAdhanToast();
      }, 4000);
    }

    function dismissAdhanToast() {
      const toast = document.getElementById("adhanToast");
      if (!toast) return;
      toast.classList.add("-translate-y-4", "opacity-0");
      setTimeout(() => toast.classList.add("hidden"), 300);
    }

    function playAdhanPreview() {
      playChimeSound();
      const nextP = document.getElementById("heroPrayerName").innerText;
      showToast("Prayer Notification", `Time for ${nextP} Prayer • Hayya 'alas-Salah`);
    }

    // Comprehensive World Cities with Coordinates & Real Timetable Data
    const cities = [
      { name: "Makkah", country: "Saudi Arabia", lat: 21.4225, lng: 39.8262, method: "Auto (Umm al-Qura)", fajr: "04:58", sunrise: "06:18", dhuhr: "12:21", asr: "15:43", maghrib: "18:24", isha: "19:54" },
      { name: "Madinah", country: "Saudi Arabia", lat: 24.4672, lng: 39.6111, method: "Auto (Umm al-Qura)", fajr: "05:02", sunrise: "06:22", dhuhr: "12:22", asr: "15:44", maghrib: "18:22", isha: "19:52" },
      { name: "Jerusalem", country: "Palestine", lat: 31.7683, lng: 35.2137, method: "Muslim World League", fajr: "04:42", sunrise: "06:05", dhuhr: "11:38", asr: "14:48", maghrib: "17:11", isha: "18:35" },
      { name: "Cairo", country: "Egypt", lat: 30.0444, lng: 31.2357, method: "Egyptian General Auth.", fajr: "04:48", sunrise: "06:14", dhuhr: "11:43", asr: "14:46", maghrib: "17:12", isha: "18:32" },
      { name: "Istanbul", country: "Turkey", lat: 41.0082, lng: 28.9784, method: "Diyanet İşleri", fajr: "05:58", sunrise: "07:29", dhuhr: "12:56", asr: "15:47", maghrib: "18:13", isha: "19:38" },
      { name: "Dubai", country: "UAE", lat: 25.2048, lng: 55.2708, method: "Gulf / Dubai Method", fajr: "05:08", sunrise: "06:26", dhuhr: "12:12", asr: "15:31", maghrib: "17:58", isha: "19:28" },
      { name: "Karachi", country: "Pakistan", lat: 24.8607, lng: 67.0011, method: "Univ. Islamic Sciences", fajr: "05:22", sunrise: "06:40", dhuhr: "12:15", asr: "15:28", maghrib: "17:49", isha: "19:07" },
      { name: "London", country: "United Kingdom", lat: 51.5074, lng: -0.1278, method: "Unified UK Timetable", fajr: "05:12", sunrise: "07:05", dhuhr: "11:58", asr: "14:14", maghrib: "16:48", isha: "18:32" },
      { name: "New York", country: "USA", lat: 40.7128, lng: -74.0060, method: "ISNA Method", fajr: "05:35", sunrise: "06:44", dhuhr: "11:47", asr: "14:32", maghrib: "16:51", isha: "18:01" },
      { name: "Toronto", country: "Canada", lat: 43.6532, lng: -79.3832, method: "ISNA Method", fajr: "05:46", sunrise: "07:01", dhuhr: "12:12", asr: "14:52", maghrib: "17:23", isha: "18:38" }
    ];

    const prayerNames = [
      { id: "Fajr", name: "Fajr", ar: "الفجر" },
      { id: "Sunrise", name: "Sunrise", ar: "الشروق" },
      { id: "Dhuhr", name: "Dhuhr", ar: "الظهر" },
      { id: "Asr", name: "Asr", ar: "العصر" },
      { id: "Maghrib", name: "Maghrib", ar: "المغرب" },
      { id: "Isha", name: "Isha", ar: "العشاء" },
    ];

    // Mathematical Spherical Trigonometry for Qibla Bearing & Distance
    function calculateQiblaBearing(lat, lng) {
      if (Math.abs(lat - 21.422487) < 0.05 && Math.abs(lng - 39.826206) < 0.05) return 0;
      const kaabaLat = 21.422487 * (Math.PI / 180);
      const kaabaLng = 39.826206 * (Math.PI / 180);
      const phi1 = lat * (Math.PI / 180);
      const deltaLambda = kaabaLng - (lng * (Math.PI / 180));
      const y = Math.sin(deltaLambda);
      const x = Math.cos(phi1) * Math.tan(kaabaLat) - Math.sin(phi1) * Math.cos(deltaLambda);
      const bearingRad = Math.atan2(y, x);
      const bearingDeg = (bearingRad * (180 / Math.PI) + 360) % 360;
      return Math.round(bearingDeg);
    }

    function calculateKaabaDistance(lat, lng) {
      const R = 6371; // km
      const dLat = (21.422487 - lat) * (Math.PI / 180);
      const dLon = (39.826206 - lng) * (Math.PI / 180);
      const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
                Math.cos(lat * Math.PI / 180) * Math.cos(21.422487 * Math.PI / 180) *
                Math.sin(dLon/2) * Math.sin(dLon/2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
      return Math.round(R * c);
    }

    function getBearingDirectionAbbr(deg) {
      const dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'];
      const idx = Math.round((deg % 360) / 22.5) % 16;
      return dirs[idx];
    }

    // Modal City Selector Controls
    function openCityModal() {
      playClickSound();
      renderCitiesList();
      const modal = document.getElementById("citySelectorModal");
      modal.classList.remove("hidden");
      lucide.createIcons();
    }

    function closeCityModal() {
      playClickSound();
      document.getElementById("citySelectorModal").classList.add("hidden");
    }

    function renderCitiesList(filter = "") {
      const container = document.getElementById("citiesListContainer");
      container.innerHTML = "";
      const q = filter.trim().toLowerCase();

      cities.forEach((c, idx) => {
        if (q && !c.name.toLowerCase().includes(q) && !c.country.toLowerCase().includes(q)) return;
        const isSelected = idx === currentCityIndex;
        const bearing = calculateQiblaBearing(c.lat, c.lng);
        const dist = calculateKaabaDistance(c.lat, c.lng);

        const item = document.createElement("button");
        item.onclick = () => selectCity(idx);
        item.className = `w-full text-left p-2.5 rounded-xl border flex items-center justify-between transition ${
          isSelected 
            ? 'bg-emerald-50 dark:bg-emerald-950/50 border-emerald-500 font-bold' 
            : 'bg-white dark:bg-slate-800 border-slate-100 dark:border-slate-700/60 hover:bg-slate-50'
        }`;

        item.innerHTML = `
          <div>
            <p class="text-xs text-slate-900 dark:text-white font-bold flex items-center gap-1.5">
              <span>${c.name}</span>
              <span class="text-[10px] text-slate-400 font-normal">(${c.country})</span>
            </p>
            <p class="text-[10px] text-slate-500 mt-0.5">Qibla: ${bearing}° ${getBearingDirectionAbbr(bearing)} • ${dist.toLocaleString()} km</p>
          </div>
          ${isSelected ? '<span class="text-xs text-emerald-600 font-bold">✓ Selected</span>' : '<span class="text-xs text-slate-400">Select</span>'}
        `;
        container.appendChild(item);
      });
    }

    function filterCities(val) {
      renderCitiesList(val);
    }

    function selectCity(idx) {
      currentCityIndex = idx;
      closeCityModal();
      applyActiveCity();
      showToast("City Updated", `Switched to ${cities[idx].name}, ${cities[idx].country}`);
    }

    // Precise Astronomical Solar Prayer Times Engine (Offline worldwide GPS support)
    function calculateSolarPrayerTimes(lat, lng, date = null, tzOffsetHours = null) {
      if (!date) date = new Date();
      if (tzOffsetHours === null) tzOffsetHours = -date.getTimezoneOffset() / 60;

      const y = date.getFullYear();
      let m = date.getMonth() + 1;
      const d = date.getDate();
      let adjY = y;
      let adjM = m;
      if (m <= 2) { adjY -= 1; adjM += 12; }
      const A = Math.floor(adjY / 100);
      const B = 2 - A + Math.floor(A / 4);
      const jd = Math.floor(365.25 * (adjY + 4716)) + Math.floor(30.6001 * (adjM + 1)) + d + B - 1524.5;

      const D = jd - 2451545.0;
      const g = (357.529 + 0.98560028 * D) % 360;
      const q = (280.459 + 0.98564736 * D) % 360;
      const L = (q + 1.915 * Math.sin(g * Math.PI / 180) + 0.020 * Math.sin(2 * g * Math.PI / 180)) % 360;
      const e = 23.439 - 0.00000036 * D;

      const sin_d = Math.sin(e * Math.PI / 180) * Math.sin(L * Math.PI / 180);
      const delta = Math.asin(sin_d) * 180 / Math.PI;

      let RA = Math.atan2(Math.cos(e * Math.PI / 180) * Math.sin(L * Math.PI / 180), Math.cos(L * Math.PI / 180)) * 180 / Math.PI / 15.0;
      RA = (RA + 24) % 24;
      let EqT = (q / 15.0) - RA;
      if (EqT > 12) EqT -= 24;
      if (EqT < -12) EqT += 24;

      const dhuhr_h = 12 + tzOffsetHours - (lng / 15.0) - EqT;

      function hourAngle(alpha) {
        const cos_ha = (Math.sin(alpha * Math.PI / 180) - Math.sin(lat * Math.PI / 180) * Math.sin(delta * Math.PI / 180)) /
                       (Math.cos(lat * Math.PI / 180) * Math.cos(delta * Math.PI / 180));
        if (cos_ha > 1.0 || cos_ha < -1.0) return null;
        return (Math.acos(cos_ha) * 180 / Math.PI) / 15.0;
      }

      const ha_sun = hourAngle(-0.833) || 6.0;
      const sunrise_h = dhuhr_h - ha_sun;
      const maghrib_h = dhuhr_h + ha_sun;

      const ha_fajr = hourAngle(-18.0) || 1.5;
      const fajr_h = dhuhr_h - ha_fajr;

      const ha_isha = hourAngle(-17.5) || 1.5;
      const isha_h = dhuhr_h + ha_isha;

      const phi = lat * Math.PI / 180;
      const del_r = delta * Math.PI / 180;
      const asr_alt = Math.atan(1.0 / (1.0 + Math.tan(Math.abs(phi - del_r)))) * 180 / Math.PI;
      const ha_asr = hourAngle(asr_alt) || 3.2;
      const asr_h = dhuhr_h + ha_asr;

      function fmt(h) {
        h = (h + 24) % 24;
        let hours = Math.floor(h);
        let mins = Math.round((h - hours) * 60);
        if (mins >= 60) { hours = (hours + 1) % 24; mins = 0; }
        return `${String(hours).padStart(2, '0')}:${String(mins).padStart(2, '0')}`;
      }

      return {
        fajr: fmt(fajr_h),
        sunrise: fmt(sunrise_h),
        dhuhr: fmt(dhuhr_h + 0.02),
        asr: fmt(asr_h),
        maghrib: fmt(maghrib_h + 0.03),
        isha: fmt(isha_h)
      };
    }

    // Live GPS Auto-Detection with Real Astronomical Calculation
    function detectLocationGPS() {
      playClickSound();
      const btn = document.getElementById("btnAutoGPS");
      const btnText = document.getElementById("btnGpsText");
      if (btnText) btnText.innerText = "Querying Device GPS Sensor...";

      if (!navigator.geolocation) {
        showToast("GPS Error", "Geolocation is not supported by your browser");
        if (btnText) btnText.innerText = "Detect My Live GPS Location";
        return;
      }

      navigator.geolocation.getCurrentPosition(
        (position) => {
          const lat = position.coords.latitude;
          const lng = position.coords.longitude;
          const tzOffset = -new Date().getTimezoneOffset() / 60;
          const solarTimes = calculateSolarPrayerTimes(lat, lng, new Date(), tzOffset);

          // Find nearest known metropolitan city for friendly naming
          let nearestCity = null;
          let minDistance = 999999;
          cities.forEach(c => {
            if (c.name.startsWith("Current GPS")) return;
            const dist = Math.hypot(lat - c.lat, lng - c.lng);
            if (dist < minDistance) {
              minDistance = dist;
              nearestCity = c;
            }
          });

          const locationLabel = (nearestCity && minDistance < 1.8)
            ? `GPS: ${nearestCity.name}`
            : "Current GPS Location";

          const gpsBearing = calculateQiblaBearing(lat, lng);
          const gpsDist = calculateKaabaDistance(lat, lng);

          const gpsCity = {
            name: locationLabel,
            country: `${lat.toFixed(2)}°, ${lng.toFixed(2)}°`,
            lat: lat,
            lng: lng,
            method: "Astronomical Solar GPS",
            fajr: solarTimes.fajr,
            sunrise: solarTimes.sunrise,
            dhuhr: solarTimes.dhuhr,
            asr: solarTimes.asr,
            maghrib: solarTimes.maghrib,
            isha: solarTimes.isha
          };

          if (cities[0].name.startsWith("Current GPS") || cities[0].name.startsWith("GPS:")) {
            cities[0] = gpsCity;
          } else {
            cities.unshift(gpsCity);
          }
          currentCityIndex = 0;
          closeCityModal();
          applyActiveCity();
          if (btnText) btnText.innerText = "Detect My Live GPS Location";
          showToast("GPS Locked", `${locationLabel} • Qibla: ${gpsBearing}° • ${gpsDist.toLocaleString()} km`);
        },
        (error) => {
          if (btnText) btnText.innerText = "Detect My Live GPS Location";
          showToast("Location Access", "GPS permission denied. Using selected city.");
        },
        { timeout: 7000 }
      );
    }

    function applyActiveCity() {
      const city = cities[currentCityIndex];
      document.getElementById("cityNameLabel").innerText = city.name;
      const methodEl = document.getElementById("cityCalcMethodLabel"); if (methodEl) methodEl.innerText = city.method;

      // Update Qibla math
      const bearing = calculateQiblaBearing(city.lat, city.lng);
      const dist = calculateKaabaDistance(city.lat, city.lng);
      document.getElementById("qiblaBearingValueText").innerText = `${bearing}° ${getBearingDirectionAbbr(bearing)}`;
      document.getElementById("qiblaDistanceValueText").innerText = dist === 0 ? "At Kaaba" : `${dist.toLocaleString()} km to Kaaba`;
      document.getElementById("qiblaTargetLabel").innerText = `Align at ${bearing}°`;

      // Update Kaaba needle target orientation on the dial
      const needle = document.getElementById("kaabaNeedleContainer");
      if (needle) needle.style.transform = `rotate(${bearing}deg)`;

      calculateCityNextPrayer();
      renderPrayerCards();
      updateCompass(document.getElementById("headingSlider").value);
      saveState();
      lucide.createIcons();
    }

    // Toggle Prayer Notification Bell
    function togglePrayerAlert(prayerId) {
      playClickSound();
      prayerAlerts[prayerId] = !prayerAlerts[prayerId];
      renderPrayerCards();
      saveState();
      const status = prayerAlerts[prayerId] ? "enabled" : "muted";
      showToast("Alert Preferences", `${prayerId} prayer notification ${status}`);
    }

    let currentActivePrayerId = 'Fajr';
    const prayerNameAr = {
      Fajr: "الفجر",
      Sunrise: "الشروق",
      Dhuhr: "الظهر",
      Asr: "العصر",
      Maghrib: "المغرب",
      Isha: "العشاء"
    };

    // Render Prayer Cards with Per-Prayer Alert Bell
    function renderPrayerCards() {
      const city = cities[currentCityIndex];
      const container = document.getElementById("prayerCardsList");
      container.innerHTML = "";

      prayerNames.forEach(p => {
        const time = city[p.id.toLowerCase()];
        const isNext = p.id === currentActivePrayerId;
        const isAlertOn = prayerAlerts[p.id] !== false;

        const card = document.createElement("div");
        card.className = `flex items-center justify-between p-2.5 rounded-xl border transition ${
          isNext 
            ? "bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-700/60 font-bold" 
            : "bg-white dark:bg-slate-800 border-slate-100 dark:border-slate-700/60"
        }`;

        card.innerHTML = `
          <div class="flex items-center gap-2.5">
            <span class="w-2 h-2 rounded-full ${isNext ? 'bg-emerald-600 animate-ping' : 'bg-slate-300 dark:bg-slate-600'}"></span>
            <div>
              <span class="text-xs ${isNext ? 'text-emerald-900 dark:text-emerald-300 font-extrabold' : 'text-slate-700 dark:text-slate-300 font-semibold'}">
                ${isArabic ? p.ar : p.name}
              </span>
              ${isNext ? `<span class="ml-1 rtl:mr-1 text-[8px] uppercase px-1.5 py-0.2 rounded bg-emerald-600 text-white font-bold">${isArabic ? 'القادمة' : 'Upcoming'}</span>` : ''}
            </div>
          </div>
          <div class="flex items-center gap-3">
            <span class="text-xs font-mono font-bold ${isNext ? 'text-emerald-800 dark:text-emerald-400' : 'text-slate-500'}" dir="ltr">
              ${time}
            </span>
            <button onclick="togglePrayerAlert('${p.id}')" title="Toggle Alert" class="p-1 rounded hover:bg-slate-100 dark:hover:bg-slate-700 text-xs transition">
              <i data-lucide="${isAlertOn ? 'bell' : 'bell-off'}" class="w-3.5 h-3.5 ${isAlertOn ? 'text-gold-500' : 'text-slate-400'}"></i>
            </button>
          </div>
        `;
        container.appendChild(card);
      });
      lucide.createIcons();
    }

    // Dynamic Next Prayer & Countdown Engine
    let countdownInterval = null;
    let currentRemainingSeconds = 8072;
    let totalPrayerWindowSeconds = 12000;

    function calculateCityNextPrayer() {
      const city = cities[currentCityIndex];
      const now = new Date();
      const prayerOrder = ['fajr', 'sunrise', 'dhuhr', 'asr', 'maghrib', 'isha'];
      let foundNext = false;
      let nextName = 'Fajr';
      let nextTimeStr = city.fajr;
      let prevTimeStr = city.isha;
      let diffSeconds = 0;

      for (let i = 0; i < prayerOrder.length; i++) {
        const p = prayerOrder[i];
        if (p === 'sunrise') continue;
        const [h, m] = city[p].split(':').map(Number);
        const pDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), h, m, 0);
        const diff = Math.floor((pDate - now) / 1000);
        if (diff > 0) {
          nextName = p.charAt(0).toUpperCase() + p.slice(1);
          nextTimeStr = city[p];
          prevTimeStr = i > 0 ? city[prayerOrder[i - 1]] : city.isha;
          diffSeconds = diff;
          foundNext = true;
          break;
        }
      }

      if (!foundNext) {
        nextName = 'Fajr';
        nextTimeStr = city.fajr;
        prevTimeStr = city.isha;
        const [h, m] = city.fajr.split(':').map(Number);
        const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, h, m, 0);
        diffSeconds = Math.max(3600, Math.floor((tomorrow - now) / 1000));
      }

      currentActivePrayerId = nextName;
      document.getElementById("heroPrayerName").innerText = isArabic ? (prayerNameAr[nextName] || nextName) : nextName;
      const [h, m] = nextTimeStr.split(':').map(Number);
      const ampm = h >= 12 ? 'PM' : 'AM';
      const h12 = h % 12 || 12;
      document.getElementById("heroPrayerTime").innerHTML = `<span dir="ltr">${h12}:${String(m).padStart(2, '0')} ${ampm}</span>`;
      
      currentRemainingSeconds = diffSeconds;
      totalPrayerWindowSeconds = Math.max(diffSeconds, 10800); // approx 3h window
      updatePrayerProgressBar();
    }

    function updatePrayerProgressBar() {
      const elapsed = Math.max(0, totalPrayerWindowSeconds - currentRemainingSeconds);
      const pct = Math.min(100, Math.max(5, Math.round((elapsed / totalPrayerWindowSeconds) * 100)));
      const bar = document.getElementById("prayerWindowProgress");
      if (bar) bar.style.width = `${pct}%`;
    }

    function startCountdown() {
      calculateCityNextPrayer();
      if (countdownInterval) clearInterval(countdownInterval);
      countdownInterval = setInterval(() => {
        if (currentRemainingSeconds > 0) {
          currentRemainingSeconds--;
          updatePrayerProgressBar();
        }
        const h = String(Math.floor(currentRemainingSeconds / 3600)).padStart(2, '0');
        const m = String(Math.floor((currentRemainingSeconds % 3600) / 60)).padStart(2, '0');
        const s = String(currentRemainingSeconds % 60).padStart(2, '0');
        const el = document.getElementById("countdownTimer");
        if (el) el.innerHTML = `<span dir="ltr" class="inline-block font-mono">${h}:${m}:${s}</span>`;
      }, 1000);
    }

    // Daily Hadith Collection with Reliable References & Next/Copy features
    const hadithCollection = [
      {
        matnAr: "إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى",
        matnEn: "Actions are judged by intentions, and every person will be rewarded according to their intention.",
        narrator: "Umar ibn Al-Khattab (RA)",
        source: "Sahih al-Bukhari 1",
        topic: "Sincerity"
      },
      {
        matnAr: "الطُّهُورُ شَطْرُ الإِيمَانِ",
        matnEn: "Purity is half of faith, and Alhamdulillah fills the scale.",
        narrator: "Abu Malik Al-Ash'ari (RA)",
        source: "Sahih Muslim 223",
        topic: "Purity"
      },
      {
        matnAr: "لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ",
        matnEn: "None of you truly believes until he loves for his brother what he loves for himself.",
        narrator: "Anas ibn Malik (RA)",
        source: "Sahih al-Bukhari 13",
        topic: "Brotherhood"
      },
      {
        matnAr: "خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ",
        matnEn: "The best among you are those who learn the Quran and teach it to others.",
        narrator: "Uthman ibn Affan (RA)",
        source: "Sahih al-Bukhari 5027",
        topic: "Quran"
      },
      {
        matnAr: "مَنْ سَلَكَ طَرِيقًا يَلْتَمِسُ فِيهِ عِلْمًا سَهَّلَ اللَّهُ لَهُ بِهِ طَرِيقًا إِلَى الْجَنَّةِ",
        matnEn: "Whoever travels a path in search of knowledge, Allah will make easy for him a path to Paradise.",
        narrator: "Abu Hurairah (RA)",
        source: "Sahih Muslim 2699",
        topic: "Knowledge"
      },
      {
        matnAr: "تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ لَكَ صَدَقَةٌ",
        matnEn: "Your smiling in the face of your brother is charity for you.",
        narrator: "Abu Dharr (RA)",
        source: "Jami` at-Tirmidhi 1956",
        topic: "Kindness"
      }
    ];
    let currentHadithIdx = 0;

    function renderHadith() {
      const h = hadithCollection[currentHadithIdx];
      document.getElementById("hadithMatnAr").innerText = h.matnAr;
      document.getElementById("hadithMatnEn").innerText = `"${h.matnEn}"`;
      document.getElementById("hadithNarratorText").innerText = h.narrator;
      document.getElementById("hadithSourceText").innerText = h.source;
    }

    function cycleNextHadith() {
      playClickSound();
      currentHadithIdx = (currentHadithIdx + 1) % hadithCollection.length;
      renderHadith();
    }

    function copyCurrentHadith() {
      playClickSound();
      const h = hadithCollection[currentHadithIdx];
      const text = `${h.matnAr}\n"${h.matnEn}"\n— ${h.narrator} (${h.source})`;
      navigator.clipboard.writeText(text).then(() => {
        showToast("Hadith Copied", "Copied narration & reference to clipboard");
      }).catch(() => {
        showToast("Hadith Copied", `${h.source} ready to share`);
      });
    }

    // Qibla Compass Sensor Engine
    let userHeading = 0;
    let hasTriggeredAlignmentHaptic = false;
    let lastHapticTime = 0;

    function updateCompass(val, isUserEvent = false) {
      userHeading = parseInt(val);
      const city = cities[currentCityIndex];
      const qiblaTarget = calculateQiblaBearing(city.lat, city.lng);

      const dial = document.getElementById("compassDial");
      const degText = document.getElementById("compassDegrees");
      const statusText = document.getElementById("compassStatus");
      const outerRing = document.getElementById("compassOuterRing");
      const banner = document.getElementById("alignmentBanner");
      const bannerCard = document.getElementById("alignmentBannerCard");

      degText.innerText = `${userHeading}°`;
      dial.style.transform = `rotate(${-userHeading}deg)`;

      // Shortest circular difference (0° to 180°)
      const rawDiff = Math.abs(userHeading - qiblaTarget);
      const diff = Math.min(rawDiff, 360 - rawDiff);
      const isAligned = diff <= 3;

      if (isAligned) {
        statusText.innerText = isArabic ? "متطابق" : "ALIGNED";
        statusText.className = "text-[8px] font-black tracking-widest text-emerald-600 dark:text-emerald-400 uppercase mt-0.5 animate-pulse";
        outerRing.classList.add("ring-4", "ring-gold-400", "border-gold-500");
        bannerCard.className = "p-2 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-400 text-xs font-bold text-emerald-800 dark:text-emerald-300";
        banner.innerHTML = isArabic 
          ? `✓ متجه نحو الكعبة المشرفة تماماً (${qiblaTarget}°)` 
          : `✓ Perfectly Aligned with Kaaba (${qiblaTarget}°)`;
        
        // Single debounced haptic trigger when entering alignment
        const now = Date.now();
        if (isUserEvent && !hasTriggeredAlignmentHaptic && (now - lastHapticTime > 900)) {
          hasTriggeredAlignmentHaptic = true;
          lastHapticTime = now;
          try { if (navigator.vibrate) navigator.vibrate([40, 50, 40]); } catch (e) {}
          playClickSound();
        }
      } else {
        if (diff > 5) {
          hasTriggeredAlignmentHaptic = false; // Reset trigger when moving out of alignment
        }
        statusText.innerText = diff < 20 ? (isArabic ? "قريب" : "CLOSE") : (isArabic ? "استدر" : "TURN");
        statusText.className = "text-[8px] font-black tracking-widest text-slate-400 uppercase mt-0.5";
        outerRing.classList.remove("ring-4", "ring-gold-400", "border-gold-500");
        bannerCard.className = "p-2 rounded-xl bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-500";
        banner.innerText = isArabic 
          ? `قم بتدوير الهاتف إلى ${qiblaTarget}° للمحاذاة (${diff}° متبقي)` 
          : `Rotate phone to ${qiblaTarget}° to align (${diff}° off)`;
      }
    }

    // Physical Device Orientation handled exclusively through togglePhoneCompassSensor()
    // Duplicate unremovable listener removed to avoid sensor collision & battery drain

    // Rich Quran Surahs with Transliteration & Saheeh International Translation
    const surahsData = {
      fatihah: {
        number: 1,
        name: "Al-Fatihah",
        translation: "The Opening",
        titleAr: "سُورَةُ الفَاتِحَة",
        titleEn: "1. Al-Fatihah • The Opening",
        type: "Meccan",
        versesCount: 7,
        verses: [
          { id: 1, ar: "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ", tr: "Bismillaahir-Rahmaanir-Raheem", en: "In the name of Allah, the Entirely Merciful, the Especially Merciful." },
          { id: 2, ar: "ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ", tr: "Alhamdu lillaahi Rabbil-'aalameen", en: "[All] praise is [due] to Allah, Lord of the worlds." },
          { id: 3, ar: "ٱلرَّحْمَٰنِ ٱلرَّحِيمِ", tr: "Ar-Rahmaanir-Raheem", en: "The Entirely Merciful, the Especially Merciful." },
          { id: 4, ar: "مَٰلِكِ يَوْمِ ٱلدِّينِ", tr: "Maaliki Yawmid-Deen", en: "Sovereign of the Day of Recompense." },
          { id: 5, ar: "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ", tr: "Iyyaaka na'budu wa lyyaaka nasta'een", en: "It is You we worship and You we ask for help." },
          { id: 6, ar: "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ", tr: "Ihdinas-Siraatal-Mustaqeem", en: "Guide us to the straight path." },
          { id: 7, ar: "صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ", tr: "Siraatal-lazeena an'amta 'alayhim ghayril-maghdoobi 'alayhim wa lad-daalleen", en: "The path of those upon whom You have bestowed favor, not of those who have evoked anger or are astray." }
        ]
      },
      kursi: {
        number: 2,
        name: "Ayat al-Kursi",
        translation: "The Throne Verse",
        titleAr: "آيَةُ الكُرْسِيِّ",
        titleEn: "Ayat al-Kursi • The Throne Verse",
        type: "Medinan",
        versesCount: 1,
        verses: [
          { 
            id: 255, 
            ar: "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ ۚ لَهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ ۗ مَنْ ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلَّا بِإِذْنِهِ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَيْءٍ مِنْ عِلْمِهِ إِلَّا بِمَا شَاءَ ۚ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ ۖ وَلَا يَئُودُهُ حِفْظُهُمَا ۚ وَهُوَ الْعَلِيُّ الْعَظِيمُ", 
            tr: "Allahu laaa ilaaha illaa Huwal Hayyul Qayyuum; laa ta'khuzuhuu sinatunw wa laa nawm; lahuu maa fissamaawaati wa maa fil ard; man zal lazee yashfa'u 'indahuuu illaa bi-iznih; ya'lamu maa bayna aydeehim wa maa khalfahum; wa laa yuheetoona bishay'im min 'ilmiheee illaa bimaa shaaa'; wasi'a Kursiyyuhus samaawaati wal arda wa laa ya'ooduhuu hifzuhumaa; wa Huwal 'Aliyyul 'Azeem", 
            en: "Allah - there is no deity except Him, the Ever-Living, the Sustainer of all existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great." 
          }
        ]
      },
      ikhlas: {
        number: 112,
        name: "Al-Ikhlas",
        translation: "The Sincerity",
        titleAr: "سُورَةُ الإِخْلَاص",
        titleEn: "112. Al-Ikhlas • The Sincerity",
        type: "Meccan",
        versesCount: 4,
        verses: [
          { id: 1, ar: "قُلْ هُوَ ٱللَّهُ أَحَدٌ", tr: "Qul Huwal-laahu Ahad", en: "Say, \"He is Allah, [who is] One,\"" },
          { id: 2, ar: "ٱللَّهُ ٱلصَّمَدُ", tr: "Allaahus-Samad", en: "Allah, the Eternal Refuge." },
          { id: 3, ar: "لَمْ يَلِدْ وَلَمْ يُولَدْ", tr: "Lam yalid wa lam yoolad", en: "He neither begets nor is born," },
          { id: 4, ar: "وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ", tr: "Wa lam yakul-lahu kufuwan ahad", en: "Nor is there to Him any equivalent." }
        ]
      },
      falaq: {
        number: 113,
        name: "Al-Falaq",
        translation: "The Daybreak",
        titleAr: "سُورَةُ الفَلَق",
        titleEn: "113. Al-Falaq • The Daybreak",
        type: "Meccan",
        versesCount: 5,
        verses: [
          { id: 1, ar: "قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ", tr: "Qul a'oozu bi-Rabbil-Falaq", en: "Say, \"I seek refuge in the Lord of daybreak\"" },
          { id: 2, ar: "مِن شَرِّ مَا خَلَقَ", tr: "Min sharri maa khalaq", en: "From the evil of that which He created" },
          { id: 3, ar: "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ", tr: "Wa min sharri ghaasiqin izaa waqab", en: "And from the evil of darkness when it settles" },
          { id: 4, ar: "وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ", tr: "Wa min sharrin-naffaasaati fil-'uqad", en: "And from the evil of the blowers in knots" },
          { id: 5, ar: "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ", tr: "Wa min sharri haasidin izaa hasad", en: "And from the evil of an envier when he envies." }
        ]
      },
      nas: {
        number: 114,
        name: "An-Nas",
        translation: "Mankind",
        titleAr: "سُورَةُ النَّاس",
        titleEn: "114. An-Nas • Mankind",
        type: "Meccan",
        versesCount: 6,
        verses: [
          { id: 1, ar: "قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ", tr: "Qul a'oozu bi-Rabbin-Naas", en: "Say, \"I seek refuge in the Lord of mankind,\"" },
          { id: 2, ar: "مَلِكِ ٱلنَّاسِ", tr: "Malikin-Naas", en: "The Sovereign of mankind," },
          { id: 3, ar: "إِلَٰهِ ٱلنَّاسِ", tr: "Ilaahin-Naas", en: "The God of mankind," },
          { id: 4, ar: "مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ", tr: "Min sharril-waswaasil-khannaas", en: "From the evil of the retreating whisperer -" },
          { id: 5, ar: "ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ", tr: "Allazee yuwaswisu fee sudoorin-naas", en: "Who whispers into the breasts of mankind -" },
          { id: 6, ar: "مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ", tr: "Minal-jinnati wan-naas", en: "From among the jinn and mankind." }
        ]
      },
      mulk: {
        number: 67,
        name: "Al-Mulk",
        translation: "The Sovereignty",
        titleAr: "سُورَةُ المُلْك",
        titleEn: "67. Al-Mulk • The Sovereignty",
        type: "Meccan",
        versesCount: 3,
        verses: [
          { id: 1, ar: "تَبَٰرَكَ ٱلَّذِى بِيَدِهِ ٱلْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ", tr: "Tabaarakal-lazee biyadihil-mulku wa Huwa 'alaa kulli shay'in Qadeer", en: "Blessed is He in whose hand is dominion, and He is over all things competent -" },
          { id: 2, ar: "ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ", tr: "Allazee khalaqal-mawta wal-hayaata liyabluwakum ayyukum ahsanu 'amalaa", en: "Who created death and life to test you as to which is best in deed." },
          { id: 3, ar: "ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا ۖ مَّا تَرَىٰ فِى خَلْقِ ٱلرَّحْمَٰنِ مِن تَفَٰوُتٍۢ", tr: "Allazee khalaqa sab'a samaawaatin tibaaqan", en: "Who created seven heavens in layers. You do not see in the creation of the Most Merciful any inconsistency." }
        ]
      },
      qadr: {
        number: 97,
        titleAr: "سُورَةُ القَدْرِ",
        titleEn: "The Night of Decree",
        type: "Meccan",
        versesCount: 5,
        verses: [
          { id: 1, ar: "إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةِ ٱلْقَدْرِ", tr: "Innaaa anzalnaahu fee laylatil-qadr", en: "Indeed, We sent the Qur'an down during the Night of Decree." },
          { id: 2, ar: "وَمَآ أَدْرَىٰكَ مَا لَيْلَةُ ٱلْقَدْرِ", tr: "Wa maaa adraaka maa laylatul-qadr", en: "And what can make you know what is the Night of Decree?" },
          { id: 3, ar: "لَيْلَةُ ٱلْقَدْرِ خَيْرٌۭ مِّنْ أَلْفِ شَهْرٍۢ", tr: "Laylatul-qadri khayrum-min alfi shahr", en: "The Night of Decree is better than a thousand months." },
          { id: 4, ar: "تَنَزَّلُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ فِيهَا بِإِذْنِ رَبِّهِم مِّن كُلِّ أَمْرٍۢ", tr: "Tanazzalul-malaaa'ikatu war-roohu feehaa bi-izni Rabbihim min kulli amr", en: "The angels and the Spirit descend therein by permission of their Lord for every matter." },
          { id: 5, ar: "سَلَٰمٌ هِىَ حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ", tr: "Salaamun hiya hattaa matla'il-fajr", en: "Peace it is until the emergence of dawn." }
        ]
      },
      asr: {
        number: 103,
        titleAr: "سُورَةُ العَصْرِ",
        titleEn: "The Declining Day",
        type: "Meccan",
        versesCount: 3,
        verses: [
          { id: 1, ar: "وَٱلْعَصْرِ", tr: "Wal-'asr", en: "By time," },
          { id: 2, ar: "إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ", tr: "Innal-insaana lafee khusr", en: "Indeed, mankind is in loss," },
          { id: 3, ar: "إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ", tr: "Illal-lazeena aamanoo wa 'amilus-saalihaati wa tawaasaw bil-haqqi wa tawaasaw bis-sabr", en: "Except for those who have believed and done righteous deeds and advised each other to truth and patience." }
        ]
      },
      fil: {
        number: 105,
        titleAr: "سُورَةُ الفِيلِ",
        titleEn: "The Elephant",
        type: "Meccan",
        versesCount: 5,
        verses: [
          { id: 1, ar: "أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ", tr: "Alam tara kayfa fa'ala Rabbuka bi-as-haabil-feel", en: "Have you not considered how your Lord dealt with the companions of the elephant?" },
          { id: 2, ar: "أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ", tr: "Alam yaj'al kaydahum fee tadleel", en: "Did He not make their plan into misguidance?" },
          { id: 3, ar: "وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ", tr: "Wa arsala 'alayhim tayran abaabeel", en: "And He sent against them birds in flocks," },
          { id: 4, ar: "تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ", tr: "Tarmeehim bi-hijaaratim-min sijjeel", en: "Striking them with stones of hard clay," },
          { id: 5, ar: "فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ", tr: "Faja'alahum ka'asfim-ma'kool", en: "And He made them like eaten straw." }
        ]
      },
      quraysh: {
        number: 106,
        titleAr: "سُورَةُ قُرَيْشٍ",
        titleEn: "Quraysh",
        type: "Meccan",
        versesCount: 4,
        verses: [
          { id: 1, ar: "لِإِيلَٰفِ قُرَيْشٍ", tr: "Li-eelaafi Quraysh", en: "For the accustomed security of the Quraysh -" },
          { id: 2, ar: "إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ", tr: "Eelaafihim rihlatash-shitaaa'i was-sayf", en: "Their accustomed security [in] the caravan of winter and summer -" },
          { id: 3, ar: "فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ", tr: "Falya'budoo Rabba haazal-Bayt", en: "Let them worship the Lord of this House," },
          { id: 4, ar: "ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ", tr: "Allazeee at'amahum min joo'inw-wa aamanahum min khawf", en: "Who has fed them, [saving them] from hunger and made them safe, from fear." }
        ]
      },
      maun: {
        number: 107,
        titleAr: "سُورَةُ المَاعُونِ",
        titleEn: "The Small Kindnesses",
        type: "Meccan",
        versesCount: 7,
        verses: [
          { id: 1, ar: "أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ", tr: "Ara'aytal-lazee yukazzibu bid-deen", en: "Have you seen the one who denies the Recompense?" },
          { id: 2, ar: "فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ", tr: "Fazalikal-lazee yadu''ul-yateem", en: "For that is the one who drives away the orphan," },
          { id: 3, ar: "وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ", tr: "Wa laa yahuddu 'alaa ta'aamil-miskeen", en: "And does not encourage the feeding of the poor." },
          { id: 4, ar: "فَوَيْلٌۭ لِّلْمُصَلِّينَ", tr: "Fawaylul-lilmussalleen", en: "So woe to those who pray," },
          { id: 5, ar: "ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ", tr: "Allazeena hum 'an salaatihim saahoon", en: "[But] who are heedless of their prayer -" },
          { id: 6, ar: "ٱلَّذِينَ هُمْ يُرَآءُونَ", tr: "Allazeena hum yuraaa'oon", en: "Those who make a show [of their deeds]" },
          { id: 7, ar: "وَيَمْنَعُونَ ٱلْمَاعُونَ", tr: "Wa yamna'oonal-maa'oon", en: "And withhold simple assistance." }
        ]
      },
      kawthar: {
        number: 108,
        titleAr: "سُورَةُ الكَوْثَرِ",
        titleEn: "The Abundance",
        type: "Meccan",
        versesCount: 3,
        verses: [
          { id: 1, ar: "إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ", tr: "Innaaa a'tainaakal-kawthar", en: "Indeed, We have granted you, [O Muhammad], al-Kawthar." },
          { id: 2, ar: "فَصَلِّ لِرَبِّكَ وَٱنْحَرْ", tr: "Fasalli li-Rabbika wanhar", en: "So pray to your Lord and sacrifice [to Him alone]." },
          { id: 3, ar: "إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ", tr: "Inna shaani'aka huwal-abtar", en: "Indeed, your enemy is the one cut off." }
        ]
      },
      kafirun: {
        number: 109,
        titleAr: "سُورَةُ الكَافِرُونَ",
        titleEn: "The Disbelievers",
        type: "Meccan",
        versesCount: 6,
        verses: [
          { id: 1, ar: "قُلْ يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ", tr: "Qul yaaa-ayyuhal-kaafiroon", en: "Say, 'O disbelievers,'" },
          { id: 2, ar: "لَآ أَعْبُدُ مَا تَعْبُدُونَ", tr: "Laaa a'budu maa ta'budoon", en: "'I do not worship what you worship.'" },
          { id: 3, ar: "وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ", tr: "Wa laaa antum 'aabidoona maaa a'bud", en: "'Nor are you worshippers of what I worship.'" },
          { id: 4, ar: "وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ", tr: "Wa laaa ana 'aabidum-maa 'abattum", en: "'Nor will I be a worshipper of what you worship.'" },
          { id: 5, ar: "وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ", tr: "Wa laaa antum 'aabidoona maaa a'bud", en: "'Nor will you be worshippers of what I worship.'" },
          { id: 6, ar: "لَكُمْ دِينُكُمْ وَلِىَ دِينِ", tr: "Lakum deenukum wa liya deen", en: "'For you is your religion, and for me is my religion.'" }
        ]
      },
      nasr: {
        number: 110,
        titleAr: "سُورَةُ النَّصْرِ",
        titleEn: "The Divine Support",
        type: "Medinan",
        versesCount: 3,
        verses: [
          { id: 1, ar: "إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ", tr: "Izaa jaaa'a nasrul-laahi wal-fath", en: "When the victory of Allah has come and the conquest," },
          { id: 2, ar: "وَرَأَيْتَ ٱلنَّاسَ يَدْخُلُونَ فِى دِينِ ٱللَّهِ أَفْوَاجًا", tr: "Wa ra'aitan-naasa yadkhuloona fee deenil-laahi afwaajaa", en: "And you see the people entering into the religion of Allah in multitudes," },
          { id: 3, ar: "فَسَبِّحْ بِحَمْدِ رَبِّكَ وَٱسْتَغْفِرْهُ ۚ إِنَّهُۥ كَانَ تَوَّابًۢا", tr: "Fasabbih bihamdi Rabbika wastaghfirh; innahoo kaana tawwaabaa", en: "Then exalt with praise of your Lord and ask forgiveness of Him. Indeed, He is ever Accepting of repentance." }
        ]
      }
    };
    let currentSurahKey = 'fatihah';

    
    function renderSurahPills() {
      const container = document.getElementById("surahPillsBar");
      if (!container) return;

      const currentNum = surahsData[currentSurahKey] ? surahsData[currentSurahKey].number : 1;
      
      const savedCount = Object.keys(bookmarkedVerses).filter(k => bookmarkedVerses[k]).length;
      let html = `
        <button onclick="openSurahIndexModal()" class="px-3 py-1 rounded-full font-bold bg-gold-500 hover:bg-gold-400 text-slate-950 flex items-center gap-1 shadow-xs flex-shrink-0 active:scale-95 transition sticky left-0 z-10">
          <i data-lucide="book-open" class="w-3 h-3 fill-current"></i> ${isArabic ? "الكل" : "All"}
        </button>
        <button onclick="openBookmarksModal()" title="Saved Bookmarks" class="px-2.5 py-1 rounded-full font-bold bg-gold-500/15 border border-gold-500/30 text-gold-700 dark:text-gold-400 flex items-center gap-1 shadow-xs flex-shrink-0 active:scale-95 transition">
          <i data-lucide="bookmark" class="w-3 h-3 fill-current"></i> <span id="pillBookmarksCount">${savedCount}</span>
        </button>
      `;

      if (currentSurahKey === 'kursi') {
        html += `
          <button onclick="loadSurah('kursi')" id="surah-pill-kursi" class="px-3 py-1 rounded-full font-bold bg-emerald-800 text-white shadow-xs flex-shrink-0 transition">
            Ayat al-Kursi
          </button>
        `;
      }

      all114Surahs.forEach(s => {
        const isCurrent = (currentSurahKey !== 'kursi' && currentNum === s.number);
        const preKey = surahNumToKey[s.number];
        const clickFn = preKey ? `loadSurah('${preKey}')` : `selectSurahFromIndex(${s.number})`;
        const pillId = preKey ? `surah-pill-${preKey}` : `surah-pill-num-${s.number}`;
        const cls = isCurrent 
          ? "font-bold bg-emerald-800 text-white shadow-xs" 
          : "bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-300 dark:hover:bg-slate-700";
        
        html += `<button onclick="${clickFn}" id="${pillId}" class="px-3 py-1 rounded-full font-medium flex-shrink-0 transition ${cls}">${s.number}. ${s.titleEn}</button>`;
      });

      container.innerHTML = html;
      lucide.createIcons();

      // Auto scroll active pill to center
      setTimeout(() => {
        const activePill = container.querySelector(".bg-emerald-800");
        if (activePill) {
          activePill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        }
      }, 50);
    }

    function loadSurah(surahKey) {
      stopFullSurahRecitation();
      currentSurahKey = surahKey;
      const s = surahsData[surahKey];
      if (!s) return;
      
      const typeEl = document.getElementById("surahMetaType");
      const versesEl = document.getElementById("surahMetaVerses");
      const titleArEl = document.getElementById("surahHeaderTitleAr");
      const titleEnEl = document.getElementById("surahHeaderTitleEn");

      if (typeEl) typeEl.innerText = s.type.toUpperCase();
      if (versesEl) versesEl.innerText = `${s.versesCount} VERSES`;
      if (titleArEl) titleArEl.innerText = s.titleAr;

      if (titleEnEl) {
        if (s.name && s.translation) {
          titleEnEl.innerHTML = `${s.number ? s.number + '. ' : ''}${s.name} <span class="text-emerald-200/80 font-normal">• ${s.translation}</span>`;
        } else if (s.titleEn && s.titleEn.includes(' • ')) {
          const parts = s.titleEn.split(' • ');
          titleEnEl.innerHTML = `${parts[0]} <span class="text-emerald-200/80 font-normal">• ${parts[1]}</span>`;
        } else {
          titleEnEl.innerText = s.titleEn || "";
        }
      }

      renderSurahPills();
      renderQuranVerses();
    }

    function renderQuranVerses() {
      const s = surahsData[currentSurahKey];
      const container = document.getElementById("quranVersesList");
      container.innerHTML = "";

      s.verses.forEach((v, index) => {
        const isBookmarked = bookmarkedVerses[`${currentSurahKey}_${v.id}`];
        const isPlayingThis = activePlayingIndex === index;
        const card = document.createElement("div");
        card.id = `ayah-card-${index}`;
        card.className = "ayah-card p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-1.5 transition-all duration-300";
        
        card.innerHTML = `
          <div class="flex items-center justify-between pb-1 border-b border-slate-100 dark:border-slate-700/60">
            <span class="w-5 h-5 rounded-full bg-gold-500/15 text-gold-600 dark:text-gold-400 text-[10px] font-bold flex items-center justify-center font-sans border border-gold-500/30">
              ${v.id}
            </span>
            <div class="flex items-center gap-1.5">
              <button onclick="copySingleAyah('${currentSurahKey}', ${v.id}, ${index})" title="Copy & Share Ayah" class="p-1 rounded hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-400 hover:text-emerald-600 transition">
                <i data-lucide="share-2" class="w-3.5 h-3.5"></i>
              </button>
              <button onclick="toggleBookmark('${currentSurahKey}', ${v.id})" title="Bookmark" class="p-1 rounded hover:bg-slate-100 dark:hover:bg-slate-700 transition">
                <i data-lucide="bookmark" class="w-3.5 h-3.5 ${isBookmarked ? 'text-gold-500 fill-current' : 'text-slate-400'}"></i>
              </button>
              <button onclick="playSingleAyahAudio(${index})" id="ayah-play-btn-${index}" title="Play Audio Recitation" class="p-1 rounded hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-400 hover:text-emerald-700">
                <i data-lucide="${isPlayingThis ? 'pause' : 'play'}" class="w-3.5 h-3.5 ${isPlayingThis ? 'text-gold-500 fill-current' : ''}"></i>
              </button>
            </div>
          </div>
          <p class="notranslate font-quran-text text-right text-emerald-950 dark:text-white font-normal select-text" translate="no" lang="ar" dir="rtl" style="font-size: ${quranFontSize}px; line-height: 2.35;">
            ${v.ar} <span class="ayah-marker notranslate" translate="no">﴿${toArabicDigits(v.id)}﴾</span>
          </p>
          ${showTransliteration && v.tr ? `<p class="text-left text-[13px] text-emerald-800/90 dark:text-emerald-400/90 font-sans italic leading-normal pt-1 select-text">${v.tr}</p>` : ''}
          ${showEnglishTranslation && v.en ? `<p class="text-left text-[14px] text-slate-700 dark:text-slate-200 font-sans leading-relaxed pt-1 select-text font-normal">${v.en}</p>` : ''}
        `;
        container.appendChild(card);
      });

      // End of Surah Milestone & Next/Prev Navigation
      const surahNum = (s && s.number) ? s.number : 1;
      const prevSurah = all114Surahs.find(x => x.number === surahNum - 1);
      const nextSurah = all114Surahs.find(x => x.number === surahNum + 1);

      const endCard = document.createElement("div");
      endCard.className = "mt-3 p-4 rounded-2xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 text-center space-y-2.5 shadow-xs";
      endCard.innerHTML = `
        <div class="flex items-center justify-center gap-2">
          <div class="h-px w-10 bg-gold-500/30"></div>
          <span class="notranslate font-arabic text-base text-gold-600 dark:text-gold-400 font-bold" translate="no" lang="ar" dir="rtl">
            صَدَقَ اللّٰهُ الْعَظِيمُ
          </span>
          <div class="h-px w-10 bg-gold-500/30"></div>
        </div>
        <div>
          <p class="text-xs font-bold text-slate-800 dark:text-white">End of ${s.titleEn}</p>
          <p class="text-[10px] text-slate-400">${s.versesCount} Verses • Completed</p>
        </div>
        <div class="flex items-center justify-center gap-2 pt-1 text-xs">
          ${prevSurah ? `
            <button onclick="goToSurahByNum(${prevSurah.number})" class="px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-500 text-slate-600 dark:text-slate-300 text-[11px] font-semibold flex items-center gap-1 active:scale-95 transition">
              <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i> ${prevSurah.titleEn}
            </button>
          ` : ''}
          <button onclick="scrollAppBodyToTop()" class="px-2.5 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-500 text-slate-400 text-[11px] font-semibold flex items-center gap-1 active:scale-95 transition" title="Scroll to Top">
            <i data-lucide="arrow-up" class="w-3.5 h-3.5"></i> Top
          </button>
          ${nextSurah ? `
            <button onclick="goToSurahByNum(${nextSurah.number})" class="px-3.5 py-1.5 rounded-xl bg-emerald-800 hover:bg-emerald-700 text-white text-[11px] font-bold flex items-center gap-1 active:scale-95 transition shadow-xs">
              ${nextSurah.titleEn} <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
            </button>
          ` : `
            <button onclick="goToSurahByNum(1)" class="px-3.5 py-1.5 rounded-xl bg-emerald-800 hover:bg-emerald-700 text-white text-[11px] font-bold flex items-center gap-1 active:scale-95 transition shadow-xs">
              Al-Fatihah <i data-lucide="rotate-ccw" class="w-3 h-3"></i>
            </button>
          `}
        </div>
      `;
      container.appendChild(endCard);

      lucide.createIcons();
    }

    function scrollAppBodyToTop() {
      playClickSound();
      const appBody = document.getElementById("appBody");
      if (appBody) appBody.scrollTo({ top: 0, behavior: "smooth" });
    }

    function goToSurahByNum(num) {
      playClickSound();
      selectSurahFromIndex(num);
      scrollAppBodyToTop();
    }

    function toArabicDigits(num) {
      const arabicNumerals = ['٠','١','٢','٣','٤','٥','٦','٧','٨','٩'];
      return String(num).split('').map(d => arabicNumerals[parseInt(d)] || d).join('');
    }

    function changeFontSize(delta) {
      playClickSound();
      quranFontSize = Math.max(18, Math.min(36, quranFontSize + delta));
      renderQuranVerses();
      saveState();
    }

    function toggleTransliteration() {
      playClickSound();
      showTransliteration = !showTransliteration;
      const btn = document.getElementById("translitBtn");
      if (showTransliteration) {
        btn.className = "px-2 py-0.5 rounded bg-emerald-800 text-white text-[10px]";
      } else {
        btn.className = "px-2 py-0.5 rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 text-[10px]";
      }
      renderQuranVerses();
      saveState();
    }

    function updateBookmarksCountBadges() {
      const count = Object.keys(bookmarkedVerses).filter(k => bookmarkedVerses[k]).length;
      const topBadge = document.getElementById("topBookmarksCount");
      if (topBadge) topBadge.innerText = count;
      const searchBadge = document.getElementById("searchBarBookmarksCount");
      if (searchBadge) searchBadge.innerText = `Saved (${count})`;
      const pillBadge = document.getElementById("pillBookmarksCount");
      if (pillBadge) pillBadge.innerText = count;
      const modalSub = document.getElementById("bookmarksCountSub");
      if (modalSub) modalSub.innerText = `${count} verses bookmarked`;
    }

    function toggleBookmark(surahKey, verseId) {
      playClickSound();
      const k = `${surahKey}_${verseId}`;
      const sTitle = surahsData[surahKey] ? surahsData[surahKey].titleEn : 'Quran';
      if (bookmarkedVerses[k]) {
        delete bookmarkedVerses[k];
        showToast("Bookmark Removed", `Ayah ${verseId} removed from saved`);
      } else {
        bookmarkedVerses[k] = true;
        showToast("Ayah Bookmarked", `Saved! Tap 'Saved' in the top bar to view`);
      }
      updateBookmarksCountBadges();
      renderQuranVerses();
      saveState();
    }

    // Real Audio Recitation Engine (Mishary Rashid Alafasy via EveryAyah CDN)
    let currentAyahAudio = null;
    let isRecitingFullSurah = false;
    let activePlayingIndex = null;

    function playSingleAyahAudio(index) {
      const s = surahsData[currentSurahKey];
      const v = s.verses[index];

      if (activePlayingIndex === index && currentAyahAudio && !currentAyahAudio.paused) {
        stopAyahAudio();
        return;
      }

      stopAyahAudio();
      playAyahAudio(s.number, v.id, index);
    }

    
    // -------------------------------------------------------------
    // AUDIO PREFERENCES & SETTINGS ENGINE
    // -------------------------------------------------------------
    
    // 6 World-Renowned Quran Reciters (EveryAyah CDN verified HTTP 200)
    const recitersList = {
      alafasy: {
        id: 'alafasy',
        name: 'Mishary Alafasy',
        nameAr: 'مشاري العفاسي',
        folder: 'Alafasy_128kbps',
        badge: 'Default',
        country: 'Kuwait'
      },
      sudais: {
        id: 'sudais',
        name: 'Abdul Rahman Al-Sudais',
        nameAr: 'عبد الرحمن السديس',
        folder: 'Abdurrahmaan_As-Sudais_192kbps',
        badge: 'Makkah',
        country: 'Makkah'
      },
      ghamdi: {
        id: 'ghamdi',
        name: 'Saad Al-Ghamdi',
        nameAr: 'سعد الغامدي',
        folder: 'Ghamadi_40kbps',
        badge: 'Murattal',
        country: 'Saudi Arabia'
      },
      maher: {
        id: 'maher',
        name: 'Maher Al-Muaiqly',
        nameAr: 'ماهر المعيقلي',
        folder: 'Maher_AlMuaiqly_64kbps',
        badge: 'Makkah',
        country: 'Makkah'
      },
      shatri: {
        id: 'shatri',
        name: 'Abu Bakr Al-Shatri',
        nameAr: 'أبو بكر الشاطري',
        folder: 'Abu_Bakr_Ash-Shaatree_128kbps',
        badge: 'Tajweed',
        country: 'Yemen'
      },
      abdulbasit: {
        id: 'abdulbasit',
        name: 'Abdul Basit Samad',
        nameAr: 'عبد الباسط',
        folder: 'Abdul_Basit_Murattal_192kbps',
        badge: 'Classic',
        country: 'Egypt'
      }
    };

    let currentReciterKey = 'alafasy';
    let sampleReciterAudio = null;
    let playingSampleReciterKey = null;

    // 7 Authentic Adhan & Notification Tones (jsDelivr CDN verified HTTP 200)
    const adhanBaseCdn = "https://cdn.jsdelivr.net/gh/Kiwifu/adhan-mp3@main/";
    const adhanTonesList = {
      makkah: {
        id: 'makkah',
        title: 'Makkah',
        titleAr: 'الحرم المكي',
        muezzin: 'Ali Mulla',
        file: 'Ali_Ibn_Ahmad_Mala_1_-_Al_Haram_Al_Maki_(علي_بن_أحمد_ملا_-_الحرم_المكي).mp3',
        tag: 'Kaaba'
      },
      madinah: {
        id: 'madinah',
        title: 'Madinah',
        titleAr: 'الحرم المدني',
        muezzin: 'Al-Haram',
        file: 'Adhan_Al_Haram_Al_Madani_-_Al_Madinah_1_(أذان_الحرم_المدني_-_المدينة_المنورة).mp3',
        tag: "Prophet's Mosque"
      },
      madinah_fajr: {
        id: 'madinah_fajr',
        title: 'Madinah Fajr',
        titleAr: 'فجر المدينة',
        muezzin: 'Al-Haram',
        file: 'Adhan_Fajr_Al_Haram_Al_Madani_(أذان_الفجر_الحرم_المدني).mp3',
        tag: 'Fajr'
      },
      alafasy: {
        id: 'alafasy',
        title: 'Mishary Alafasy',
        titleAr: 'مشاري العفاسي',
        muezzin: 'Alafasy',
        file: 'Mishary_Al_Afasy_-_HQ_(مشاري_العفاسي).mp3',
        tag: 'Studio'
      },
      alaqsa: {
        id: 'alaqsa',
        title: 'Al-Aqsa',
        titleAr: 'المسجد الأقصى',
        muezzin: 'Jerusalem',
        file: 'Adhan_Al_Aqsa_-_Jerusalem_(أذان_المسجد_الأقصى_-_القدس).mp3',
        tag: 'Al-Quds'
      },
      abdulbasit: {
        id: 'abdulbasit',
        title: 'Cairo',
        titleAr: 'مصر',
        muezzin: 'Abdul Basit',
        file: 'Abdulbasit_Abdusamad_1_-_Egypt_(عبد_الباسط_عبد_الصمد_-_مصر).mp3',
        tag: 'Classic'
      },
      soft_chime: {
        id: 'soft_chime',
        title: 'Soft Chime',
        titleAr: 'تنبيه هادئ',
        muezzin: 'Gentle Tone',
        file: '',
        tag: 'Quiet'
      }
    };

    let currentAdhanKey = 'makkah';
    let currentAdhanAudio = null;
    let playingAdhanKey = null;

    // Fiqh & Calculation Settings
    let currentJuristicMethod = 'hanafi'; // 'hanafi' or 'standard'
    let currentHijriOffset = 0; // -2 to +2 days
    let showEnglishTranslation = true;
    let hapticsEnabled = true;

    // Open & Close Settings Modal
    function openSettingsModal(defaultTab = 'reciters') {
      playClickSound();
      const modal = document.getElementById("settingsModal");
      if (!modal) return;
      modal.classList.remove("hidden");
      switchSettingsTab(defaultTab);
      renderRecitersSettings();
      renderAdhansSettings();
      updateSettingsUIFromState();
      lucide.createIcons();
    }

    function closeSettingsModal() {
      playClickSound();
      stopSampleReciter();
      stopAdhanTonePreview();
      const modal = document.getElementById("settingsModal");
      if (modal) modal.classList.add("hidden");
    }

    function switchSettingsTab(tab) {
      playClickSound();
      const tabs = ['reciters', 'adhans', 'calculation', 'display'];
      tabs.forEach(t => {
        const btn = document.getElementById(`tabBtnSettings${t.charAt(0).toUpperCase() + t.slice(1)}`);
        const sec = document.getElementById(`settingsSection${t.charAt(0).toUpperCase() + t.slice(1)}`);
        if (btn && sec) {
          if (t === tab) {
            btn.className = "px-3 py-1 rounded-full bg-emerald-800 text-white font-bold flex-shrink-0 flex items-center gap-1 transition shadow-xs";
            sec.classList.remove("hidden");
          } else {
            btn.className = "px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0 flex items-center gap-1 transition";
            sec.classList.add("hidden");
          }
        }
      });
      lucide.createIcons();
    }

    // Render Reciters Cards
    function renderRecitersSettings() {
      const container = document.getElementById("recitersListContainer");
      if (!container) return;
      container.innerHTML = "";

      Object.values(recitersList).forEach(r => {
        const isSelected = r.id === currentReciterKey;
        const isPlayingSample = playingSampleReciterKey === r.id;

        const card = document.createElement("div");
        card.className = `p-2.5 rounded-xl border transition flex items-center justify-between gap-2 cursor-pointer ${
          isSelected 
            ? "bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 dark:border-emerald-600 shadow-xs" 
            : "bg-white dark:bg-slate-800/90 hover:bg-slate-50 dark:hover:bg-slate-700/60 border-slate-200/80 dark:border-slate-700/80"
        }`;
        card.onclick = (e) => {
          if (e.target.closest('.sample-btn')) return;
          selectReciter(r.id);
        };

        card.innerHTML = `
          <div class="flex items-center gap-2.5 min-w-0">
            <div class="w-8 h-8 rounded-full ${isSelected ? 'bg-gold-500 text-slate-950 font-bold' : 'bg-slate-100 dark:bg-slate-700 text-slate-500'} flex items-center justify-center flex-shrink-0 text-xs">
              ${isSelected ? '✓' : '<i data-lucide="mic" class="w-3.5 h-3.5"></i>'}
            </div>
            <div class="min-w-0">
              <h5 class="text-xs font-bold text-slate-900 dark:text-white truncate">
                ${r.name}
              </h5>
              <p class="text-[10px] text-slate-400 truncate">${r.badge} • <span class="font-arabic font-normal text-gold-500">${r.nameAr}</span></p>
            </div>
          </div>
          <button onclick="toggleReciterSample('${r.id}')" title="Preview Voice" class="sample-btn p-1.5 rounded-lg border flex-shrink-0 transition active:scale-90 ${
            isPlayingSample 
              ? 'bg-gold-500 border-gold-500 text-slate-950 shadow-xs' 
              : 'border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300'
          }">
            <i data-lucide="${isPlayingSample ? 'pause' : 'volume-2'}" class="w-3.5 h-3.5 ${isPlayingSample ? 'animate-pulse' : ''}"></i>
          </button>
        `;
        container.appendChild(card);
      });


      lucide.createIcons();
    }

    function scrollAppBodyToTop() {
      playClickSound();
      const appBody = document.getElementById("appBody");
      if (appBody) appBody.scrollTo({ top: 0, behavior: "smooth" });
    }

    function goToSurahByNum(num) {
      playClickSound();
      selectSurahFromIndex(num);
      scrollAppBodyToTop();
    }

    function selectReciter(reciterId) {
      if (!recitersList[reciterId]) return;
      playClickSound();
      currentReciterKey = reciterId;
      try {
        localStorage.setItem("muslim_comp_reciter", reciterId);
      } catch (e) {}

      const badge = document.getElementById("activeReciterBadge");
      if (badge) badge.innerText = recitersList[reciterId].name.replace('Sheikh ', '');

      renderRecitersSettings();
      showToast("Reciter Updated", `Set to ${recitersList[reciterId].name}`);

      // If active ayah audio is playing, restart with new reciter
      if (currentAyahAudio && !currentAyahAudio.paused && activePlayingIndex !== -1) {
        const s = surahsData[currentSurahKey];
        if (s && s.verses && s.verses[activePlayingIndex]) {
          playAyahAudio(s.number, s.verses[activePlayingIndex].id, activePlayingIndex);
        }
      }
    }

    function toggleReciterSample(reciterId) {
      if (playingSampleReciterKey === reciterId && sampleReciterAudio && !sampleReciterAudio.paused) {
        stopSampleReciter();
        renderRecitersSettings();
        return;
      }
      stopSampleReciter();
      stopAdhanTonePreview();

      const r = recitersList[reciterId];
      if (!r) return;

      playingSampleReciterKey = reciterId;
      renderRecitersSettings();

      // Sample Surah 1 Ayah 1
      const sampleUrl = `https://everyayah.com/data/${r.folder}/001001.mp3`;
      sampleReciterAudio = new Audio(sampleUrl);
      sampleReciterAudio.onended = () => {
        stopSampleReciter();
        renderRecitersSettings();
      };
      sampleReciterAudio.onerror = () => {
        stopSampleReciter();
        renderRecitersSettings();
      };
      sampleReciterAudio.play().catch(() => {});
    }

    function stopSampleReciter() {
      if (sampleReciterAudio) {
        sampleReciterAudio.pause();
        sampleReciterAudio = null;
      }
      playingSampleReciterKey = null;
    }

    // Render Adhans Cards
    function renderAdhansSettings() {
      const container = document.getElementById("adhansListContainer");
      if (!container) return;
      container.innerHTML = "";

      Object.values(adhanTonesList).forEach(a => {
        const isSelected = a.id === currentAdhanKey;
        const isPlayingThis = playingAdhanKey === a.id;

        const card = document.createElement("div");
        card.className = `p-2.5 rounded-xl border transition flex items-center justify-between gap-2 cursor-pointer ${
          isSelected 
            ? "bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 dark:border-emerald-600 shadow-xs" 
            : "bg-white dark:bg-slate-800/90 hover:bg-slate-50 dark:hover:bg-slate-700/60 border-slate-200/80 dark:border-slate-700/80"
        }`;
        card.onclick = (e) => {
          if (e.target.closest('.sample-btn')) return;
          selectAdhanTone(a.id);
        };

        card.innerHTML = `
          <div class="flex items-center gap-2.5 min-w-0">
            <div class="w-8 h-8 rounded-full ${isSelected ? 'bg-gold-500 text-slate-950 font-bold' : 'bg-slate-100 dark:bg-slate-700 text-slate-500'} flex items-center justify-center flex-shrink-0 text-xs">
              ${isSelected ? '✓' : '<i data-lucide="bell" class="w-3.5 h-3.5"></i>'}
            </div>
            <div class="min-w-0">
              <h5 class="text-xs font-bold text-slate-900 dark:text-white truncate flex items-center gap-1.5">
                ${a.title}
              </h5>
              <p class="text-[10px] text-slate-400 truncate">${a.muezzin} • <span class="font-arabic font-normal text-gold-500">${a.titleAr}</span></p>
            </div>
          </div>
          <button onclick="toggleAdhanTonePreview('${a.id}')" title="Preview Adhan" class="sample-btn p-1.5 rounded-lg border flex-shrink-0 transition active:scale-90 ${
            isPlayingThis 
              ? 'bg-gold-500 border-gold-500 text-slate-950 shadow-xs' 
              : 'border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300'
          }">
            <i data-lucide="${isPlayingThis ? 'square' : 'play'}" class="w-3.5 h-3.5 ${isPlayingThis ? 'fill-current animate-pulse' : ''}"></i>
          </button>
        `;
        container.appendChild(card);
      });


      lucide.createIcons();
    }

    function scrollAppBodyToTop() {
      playClickSound();
      const appBody = document.getElementById("appBody");
      if (appBody) appBody.scrollTo({ top: 0, behavior: "smooth" });
    }

    function goToSurahByNum(num) {
      playClickSound();
      selectSurahFromIndex(num);
      scrollAppBodyToTop();
    }

    function selectAdhanTone(toneId) {
      if (!adhanTonesList[toneId]) return;
      playClickSound();
      currentAdhanKey = toneId;
      try {
        localStorage.setItem("muslim_comp_adhan", toneId);
      } catch (e) {}

      const badge = document.getElementById("activeAdhanBadge");
      if (badge) badge.innerText = adhanTonesList[toneId].title.split(' ')[0];

      renderAdhansSettings();
      showToast("Adhan Tone Saved", `Default tone set to ${adhanTonesList[toneId].title}`);
    }

    function toggleAdhanTonePreview(toneId) {
      if (playingAdhanKey === toneId && currentAdhanAudio && !currentAdhanAudio.paused) {
        stopAdhanTonePreview();
        renderAdhansSettings();
        return;
      }
      stopSampleReciter();
      stopAdhanTonePreview();

      const a = adhanTonesList[toneId];
      if (!a) return;

      playingAdhanKey = toneId;
      renderAdhansSettings();

      if (a.id === 'soft_chime' || !a.file) {
        playChimeSound();
        setTimeout(() => playChimeSound(), 400);
        setTimeout(() => {
          stopAdhanTonePreview();
          renderAdhansSettings();
        }, 1500);
        return;
      }

      const toneUrl = adhanBaseCdn + encodeURIComponent(a.file);
      currentAdhanAudio = new Audio(toneUrl);
      currentAdhanAudio.onended = () => {
        stopAdhanTonePreview();
        renderAdhansSettings();
      };
      currentAdhanAudio.onerror = () => {
        stopAdhanTonePreview();
        renderAdhansSettings();
      };
      currentAdhanAudio.play().catch(() => {});
    }

    function stopAdhanTonePreview() {
      if (currentAdhanAudio) {
        currentAdhanAudio.pause();
        currentAdhanAudio = null;
      }
      playingAdhanKey = null;
    }

    // Top Bell Click Handler (Plays chosen Adhan or stops it)
    function playAdhanPreview() {
      if (currentAdhanAudio && !currentAdhanAudio.paused) {
        stopAdhanTonePreview();
        const bell = document.getElementById("topAdhanBellBtn");
        if (bell) bell.classList.remove("text-gold-500", "bg-gold-500/20");
        showToast("Adhan Stopped", "Playback muted");
        return;
      }

      const bell = document.getElementById("topAdhanBellBtn");
      if (bell) bell.classList.add("text-gold-500", "bg-gold-500/20");

      const a = adhanTonesList[currentAdhanKey] || adhanTonesList['makkah'];
      const nextP = document.getElementById("heroPrayerName") ? document.getElementById("heroPrayerName").innerText : "Prayer";
      showToast(`Adhan • ${a.title}`, `Calling to ${nextP} Prayer — Hayya 'alas-Salah`);

      toggleAdhanTonePreview(a.id);
    }

    // Fiqh & Asr Madhab Calculation
    function setJuristicMethod(method) {
      playClickSound();
      currentJuristicMethod = method;
      try {
        localStorage.setItem("muslim_comp_madhab", method);
      } catch (e) {}

      updateSettingsUIFromState();
      applyActiveCity();
      showToast("Madhab Updated", `Asr prayer calculated via ${method === 'hanafi' ? 'Hanafi' : 'Standard'} method`);
    }

    // Hijri Date Adjustment
    function setHijriOffset(days) {
      playClickSound();
      currentHijriOffset = parseInt(days, 10);
      try {
        localStorage.setItem("muslim_comp_hijri_offset", String(currentHijriOffset));
      } catch (e) {}

      updateSettingsUIFromState();
      updateHijriDateDisplay();
      showToast("Hijri Date Adjusted", `${days >= 0 ? '+' : ''}${days} days from regional astronomical sighting`);
    }

    function updateHijriDateDisplay() {
      const baseDay = 18 + currentHijriOffset;
      const str = `${baseDay} Shawwal`;
      const lbl1 = document.getElementById("hijriDateLabel");
      const lbl2 = document.getElementById("statusBarClock"); // or other headers
      if (lbl1) lbl1.innerText = str;
    }

    // Display & Quran Font Settings
    function onSettingsFontSizeChange(val) {
      quranFontSize = parseInt(val, 10);
      const lbl = document.getElementById("lblSettingsFontSize");
      if (lbl) lbl.innerText = `${quranFontSize}px`;

      const sample = document.getElementById("fontPreviewSample");
      if (sample) sample.style.fontSize = `${quranFontSize}px`;

      renderQuranVerses();
      saveState();
    }

    function resetArabicFontSize() {
      playClickSound();
      quranFontSize = 24;
      const slider = document.getElementById("settingsFontSizeSlider");
      if (slider) slider.value = 24;
      onSettingsFontSizeChange(24);
      showToast("Font Size", "Reset to default (24px)");
    }

    function toggleTranslationSetting(checked) {
      showEnglishTranslation = checked;
      try {
        localStorage.setItem("muslim_comp_show_trans", checked ? "1" : "0");
      } catch(e) {}
      renderQuranVerses();
    }

    function toggleTranslitSetting(checked) {
      showTransliteration = checked;
      try {
        localStorage.setItem("muslim_comp_show_translit", checked ? "1" : "0");
      } catch(e) {}
      renderQuranVerses();
    }

    function toggleHapticsSetting(checked) {
      hapticsEnabled = checked;
      try {
        localStorage.setItem("muslim_comp_haptics", checked ? "1" : "0");
      } catch(e) {}
      if (checked && navigator.vibrate) navigator.vibrate(40);
    }

    function setThemeMode(mode) {
      playClickSound();
      if (mode === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      try {
        localStorage.setItem('muslim_comp_theme', mode);
      } catch(e) {}
    }

    // Update settings UI states from loaded state
        // Premium Typography Engine (Arabic & English Font Pickers)
    const arabicFontsMap = {
      'scheherazade': {
        name: 'Scheherazade',
        quranFamily: "'Scheherazade New', 'Amiri Quran', 'Amiri', serif",
        generalFamily: "'Scheherazade New', 'Amiri', serif"
      },
      'amiri-quran': {
        name: 'Amiri Quran',
        quranFamily: "'Amiri Quran', 'Amiri', serif",
        generalFamily: "'Amiri', serif"
      },
      'noto-naskh': {
        name: 'Noto Naskh',
        quranFamily: "'Noto Naskh Arabic', 'Amiri', serif",
        generalFamily: "'Noto Naskh Arabic', serif"
      },
      'cairo': {
        name: 'Cairo',
        quranFamily: "'Cairo', sans-serif",
        generalFamily: "'Cairo', sans-serif"
      },
      'almarai': {
        name: 'Almarai',
        quranFamily: "'Almarai', sans-serif",
        generalFamily: "'Almarai', sans-serif"
      }
    };

    const uiFontsMap = {
      'plus-jakarta': {
        name: 'Plus Jakarta',
        family: "'Plus Jakarta Sans', system-ui, -apple-system, sans-serif"
      },
      'inter': {
        name: 'Inter',
        family: "'Inter', system-ui, -apple-system, sans-serif"
      },
      'outfit': {
        name: 'Outfit',
        family: "'Outfit', system-ui, -apple-system, sans-serif"
      },
      'lexend': {
        name: 'Lexend',
        family: "'Lexend', system-ui, -apple-system, sans-serif"
      }
    };

    let activeArabicFontKey = localStorage.getItem("muslim_comp_arabic_font") || "scheherazade";
    let activeUIFontKey = localStorage.getItem("muslim_comp_ui_font") || "plus-jakarta";

    function applyTypographySettings() {
      const arConf = arabicFontsMap[activeArabicFontKey] || arabicFontsMap['scheherazade'];
      const uiConf = uiFontsMap[activeUIFontKey] || uiFontsMap['plus-jakarta'];

      document.documentElement.style.setProperty('--font-quran', arConf.quranFamily);
      document.documentElement.style.setProperty('--font-arabic-general', arConf.generalFamily);
      document.documentElement.style.setProperty('--font-ui', uiConf.family);

      // Update badges in Settings
      const arBadge = document.getElementById("activeArabicFontBadge");
      if (arBadge) arBadge.innerText = arConf.name;
      const uiBadge = document.getElementById("activeUIFontBadge");
      if (uiBadge) uiBadge.innerText = uiConf.name;

      // Update Arabic Font Buttons styling
      Object.keys(arabicFontsMap).forEach(k => {
        const btn = document.getElementById(`fontBtn-${k}`);
        if (btn) {
          if (k === activeArabicFontKey) {
            btn.className = "w-full p-2 rounded-xl border text-left flex items-center justify-between transition active:scale-98 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 shadow-2xs";
          } else {
            btn.className = "w-full p-2 rounded-xl border text-left flex items-center justify-between transition active:scale-98 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600";
          }
        }
      });

      // Update UI Font Buttons styling
      Object.keys(uiFontsMap).forEach(k => {
        const btn = document.getElementById(`uiFontBtn-${k}`);
        if (btn) {
          if (k === activeUIFontKey) {
            btn.className = "p-2.5 rounded-xl border text-left transition active:scale-95 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 shadow-2xs";
          } else {
            btn.className = "p-2.5 rounded-xl border text-left transition active:scale-95 bg-slate-50 dark:bg-slate-900/60 border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600";
          }
        }
      });
    }

    function setArabicFont(key) {
      playClickSound();
      if (!arabicFontsMap[key]) return;
      activeArabicFontKey = key;
      try {
        localStorage.setItem("muslim_comp_arabic_font", key);
      } catch(e) {}
      applyTypographySettings();
      renderQuranVerses();
      showToast("Arabic Font", `${arabicFontsMap[key].name} applied`);
    }

    function setUIFont(key) {
      playClickSound();
      if (!uiFontsMap[key]) return;
      activeUIFontKey = key;
      try {
        localStorage.setItem("muslim_comp_ui_font", key);
      } catch(e) {}
      applyTypographySettings();
      showToast("UI Font", `${uiFontsMap[key].name} applied`);
    }

    function updateSettingsUIFromState() {
      applyTypographySettings();
      // Reciter badge
      const rBadge = document.getElementById("activeReciterBadge");
      if (rBadge && recitersList[currentReciterKey]) {
        rBadge.innerText = recitersList[currentReciterKey].name.replace('Sheikh ', '');
      }

      // Adhan badge
      const aBadge = document.getElementById("activeAdhanBadge");
      if (aBadge && adhanTonesList[currentAdhanKey]) {
        aBadge.innerText = adhanTonesList[currentAdhanKey].title.split(' ')[0];
      }

      // Madhab buttons
      const bH = document.getElementById("btnMadhabHanafi");
      const bS = document.getElementById("btnMadhabStandard");
      const lblM = document.getElementById("currentMadhabLabel");
      if (lblM) lblM.innerText = currentJuristicMethod === 'hanafi' ? 'Hanafi' : 'Standard';
      if (bH && bS) {
        if (currentJuristicMethod === 'hanafi') {
          bH.className = "py-2 px-2.5 rounded-lg border text-xs font-bold flex items-center justify-center gap-1.5 transition active:scale-95 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200";
          bS.className = "py-2 px-2.5 rounded-lg border text-xs font-bold flex items-center justify-center gap-1.5 transition active:scale-95 bg-white dark:bg-slate-700 border-slate-200 dark:border-slate-600 text-slate-700 dark:text-slate-300";
        } else {
          bS.className = "py-2 px-2.5 rounded-lg border text-xs font-bold flex items-center justify-center gap-1.5 transition active:scale-95 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200";
          bH.className = "py-2 px-2.5 rounded-lg border text-xs font-bold flex items-center justify-center gap-1.5 transition active:scale-95 bg-white dark:bg-slate-700 border-slate-200 dark:border-slate-600 text-slate-700 dark:text-slate-300";
        }
      }

      // Hijri offset buttons
      const hOffsets = [-2, -1, 0, 1, 2];
      const hIds = ['btnHijriM2', 'btnHijriM1', 'btnHijri0', 'btnHijriP1', 'btnHijriP2'];
      hOffsets.forEach((val, idx) => {
        const btn = document.getElementById(hIds[idx]);
        if (btn) {
          if (val === currentHijriOffset) {
            btn.className = "flex-1 py-1.5 rounded-lg border border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 font-bold";
          } else {
            btn.className = "flex-1 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 font-bold";
          }
        }
      });
      const lblH = document.getElementById("currentHijriOffsetLabel");
      if (lblH) lblH.innerText = currentHijriOffset === 0 ? "0 Days" : `${currentHijriOffset > 0 ? '+' : ''}${currentHijriOffset} Days`;

      // Font size slider & label
      const slider = document.getElementById("settingsFontSizeSlider");
      if (slider) slider.value = quranFontSize;
      const lblF = document.getElementById("lblSettingsFontSize");
      if (lblF) lblF.innerText = `${quranFontSize}px`;
      const sample = document.getElementById("fontPreviewSample");
      if (sample) sample.style.fontSize = `${quranFontSize}px`;

      // Checkboxes
      const chkTrans = document.getElementById("chkShowTranslation");
      if (chkTrans) chkTrans.checked = showEnglishTranslation;
      const chkTrl = document.getElementById("chkShowTranslit");
      if (chkTrl) chkTrl.checked = showTransliteration;
      const chkHap = document.getElementById("chkHaptics");
      if (chkHap) chkHap.checked = hapticsEnabled;
    }

    // Load persisted settings
    function loadSavedAppSettings() {
      try {
        const r = localStorage.getItem("muslim_comp_reciter");
        if (r && recitersList[r]) currentReciterKey = r;

        const a = localStorage.getItem("muslim_comp_adhan");
        if (a && adhanTonesList[a]) currentAdhanKey = a;

        const m = localStorage.getItem("muslim_comp_madhab");
        if (m) currentJuristicMethod = m;

        const h = localStorage.getItem("muslim_comp_hijri_offset");
        if (h !== null) currentHijriOffset = parseInt(h, 10) || 0;

        const st = localStorage.getItem("muslim_comp_show_trans");
        if (st !== null) showEnglishTranslation = (st === "1");

        const strl = localStorage.getItem("muslim_comp_show_translit");
        if (strl !== null) showTransliteration = (strl === "1");

        const hap = localStorage.getItem("muslim_comp_haptics");
        if (hap !== null) hapticsEnabled = (hap === "1");

        updateHijriDateDisplay();
      } catch (e) {}
    }

    function playAyahAudio(surahNum, verseId, index, onComplete = null) {
      stopAyahAudio();

      activePlayingIndex = index;
      highlightActiveAyah(index);
      updatePlayIcons(index, true);

      const s = surahsData[currentSurahKey];
      const sStr = String(surahNum).padStart(3, '0');
      const aStr = String(verseId).padStart(3, '0');
      const reciter = recitersList[currentReciterKey] || recitersList['alafasy'];
      const audioUrl = `https://everyayah.com/data/${reciter.folder}/${sStr}${aStr}.mp3`;

      currentAyahAudio = new Audio(audioUrl);

      // Track progress & notify Android system lockscreen & in-app mini player
      currentAyahAudio.ontimeupdate = () => {
        if (currentAyahAudio && currentAyahAudio.duration && !isNaN(currentAyahAudio.duration)) {
          const pct = Math.min(100, Math.max(0, (currentAyahAudio.currentTime / currentAyahAudio.duration) * 100));
          const prog = document.getElementById("miniPlayerProgress");
          if (prog) prog.style.width = pct + "%";

          // YouTube Music style live scrub position in Android notification drawer
          if ('mediaSession' in navigator && 'setPositionState' in navigator.mediaSession) {
            try {
              navigator.mediaSession.setPositionState({
                duration: currentAyahAudio.duration,
                playbackRate: currentAyahAudio.playbackRate || 1.0,
                position: currentAyahAudio.currentTime || 0
              });
            } catch (e) {}
          }
        }
      };

      currentAyahAudio.play().then(() => {
        showMiniPlayer(s.titleEn, verseId);

        // Real Android / Mobile MediaSession Notification in Status Bar & Lock Screen (YouTube Music Style)
        if ('mediaSession' in navigator) {
          navigator.mediaSession.metadata = new MediaMetadata({
            title: `Ayah ${verseId} • Surah ${s.titleEn}`,
            artist: recitersList[currentReciterKey] ? recitersList[currentReciterKey].name : 'Sheikh Mishary Rashid Alafasy',
            album: `The Noble Qur'an (${s.titleAr})`,
            artwork: [
              { src: 'assets/reciter_artwork.png', sizes: '512x512', type: 'image/png' },
              { src: 'preview/reciter_artwork.png', sizes: '512x512', type: 'image/png' },
              { src: 'https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=512&q=80', sizes: '512x512', type: 'image/jpeg' }
            ]
          });
          navigator.mediaSession.playbackState = 'playing';

          navigator.mediaSession.setActionHandler('play', () => {
            if (currentAyahAudio) {
              currentAyahAudio.play();
              navigator.mediaSession.playbackState = 'playing';
              updatePlayIcons(activePlayingIndex, true);
              updateMiniPlayerPlayBtn(true);
            }
          });
          navigator.mediaSession.setActionHandler('pause', () => {
            if (currentAyahAudio) {
              currentAyahAudio.pause();
              navigator.mediaSession.playbackState = 'paused';
              updatePlayIcons(activePlayingIndex, false);
              updateMiniPlayerPlayBtn(false);
            }
          });
          navigator.mediaSession.setActionHandler('previoustrack', () => {
            playPreviousAyahAudio();
          });
          navigator.mediaSession.setActionHandler('nexttrack', () => {
            playNextAyahAudio();
          });
          navigator.mediaSession.setActionHandler('seekto', (details) => {
            if (currentAyahAudio && details.seekTime) {
              currentAyahAudio.currentTime = details.seekTime;
            }
          });
          navigator.mediaSession.setActionHandler('seekbackward', (details) => {
            if (currentAyahAudio) {
              currentAyahAudio.currentTime = Math.max(0, currentAyahAudio.currentTime - (details.seekOffset || 5));
            }
          });
          navigator.mediaSession.setActionHandler('seekforward', (details) => {
            if (currentAyahAudio) {
              currentAyahAudio.currentTime = Math.min(currentAyahAudio.duration, currentAyahAudio.currentTime + (details.seekOffset || 5));
            }
          });
          navigator.mediaSession.setActionHandler('stop', () => {
            stopAyahAudio();
            hideMiniPlayer();
          });
        }
      }).catch(err => {
        playChimeSound();
        if (onComplete) onComplete();
      });

      currentAyahAudio.onended = () => {
        updatePlayIcons(index, false);
        activePlayingIndex = null;
        if (onComplete) {
          onComplete();
        } else {
          hideMiniPlayer();
          document.querySelectorAll('.ayah-card').forEach(c => {
            c.classList.remove("ring-2", "ring-gold-500", "bg-gold-500/10", "dark:bg-gold-500/15");
          });
          if ('mediaSession' in navigator) {
            navigator.mediaSession.playbackState = 'none';
          }
        }
      };

      currentAyahAudio.onerror = () => {
        updatePlayIcons(index, false);
        activePlayingIndex = null;
        hideMiniPlayer();
        if (onComplete) onComplete();
      };
    }

    function showMiniPlayer(surahTitle, verseId) {
      const player = document.getElementById("miniAudioPlayer");
      if (!player) return;
      player.classList.remove("hidden");
      const titleEl = document.getElementById("miniPlayerTitle");
      if (titleEl) titleEl.innerText = `Ayah ${verseId} • Surah ${surahTitle}`;
      const subEl = document.getElementById("miniPlayerSubtitle");
      if (subEl && recitersList[currentReciterKey]) {
        subEl.innerText = recitersList[currentReciterKey].name;
      }
      updateMiniPlayerPlayBtn(true);
      lucide.createIcons();
    }

    function hideMiniPlayer() {
      const player = document.getElementById("miniAudioPlayer");
      if (player) player.classList.add("hidden");
      const prog = document.getElementById("miniPlayerProgress");
      if (prog) prog.style.width = "0%";
    }

    function updateMiniPlayerPlayBtn(isPlaying) {
      const btn = document.getElementById("miniPlayerPlayBtn");
      if (btn) {
        btn.innerHTML = `<i data-lucide="${isPlaying ? 'pause' : 'play'}" class="w-4 h-4 fill-current"></i>`;
        lucide.createIcons();
      }
    }

    function toggleMiniPlayerPlayPause() {
      if (!currentAyahAudio) {
        if (activePlayingIndex !== null) {
          playSingleAyahAudio(activePlayingIndex);
        } else {
          playSingleAyahAudio(0);
        }
        return;
      }
      if (currentAyahAudio.paused) {
        currentAyahAudio.play();
        updatePlayIcons(activePlayingIndex, true);
        updateMiniPlayerPlayBtn(true);
        if ('mediaSession' in navigator) navigator.mediaSession.playbackState = 'playing';
      } else {
        currentAyahAudio.pause();
        updatePlayIcons(activePlayingIndex, false);
        updateMiniPlayerPlayBtn(false);
        if ('mediaSession' in navigator) navigator.mediaSession.playbackState = 'paused';
      }
    }

    function playPreviousAyahAudio() {
      if (activePlayingIndex !== null && activePlayingIndex > 0) {
        playSingleAyahAudio(activePlayingIndex - 1);
      }
    }

    function playNextAyahAudio() {
      const s = surahsData[currentSurahKey];
      if (activePlayingIndex !== null && activePlayingIndex + 1 < s.verses.length) {
        playSingleAyahAudio(activePlayingIndex + 1);
      }
    }

    function jumpToCurrentRecitingAyah() {
      switchTab('quran');
      if (activePlayingIndex !== null) {
        highlightActiveAyah(activePlayingIndex);
      }
    }

    function updatePlayIcons(playingIdx, isPlaying) {
      document.querySelectorAll('[id^="ayah-play-btn-"]').forEach((btn, idx) => {
        if (idx === playingIdx && isPlaying) {
          btn.innerHTML = `<i data-lucide="pause" class="w-3.5 h-3.5 text-gold-500 fill-current animate-pulse"></i>`;
        } else {
          btn.innerHTML = `<i data-lucide="play" class="w-3.5 h-3.5"></i>`;
        }
      });
      lucide.createIcons();
    }

    function stopAyahAudio() {
      if (currentAyahAudio) {
        currentAyahAudio.pause();
        currentAyahAudio = null;
      }
      activePlayingIndex = null;
      updatePlayIcons(-1, false);
      updateMiniPlayerPlayBtn(false);
      if ('mediaSession' in navigator) {
        navigator.mediaSession.playbackState = 'paused';
      }
    }

    function toggleAudioRecitation() {
      playClickSound();
      const btn = document.getElementById("reciteAudioBtn");
      const s = surahsData[currentSurahKey];

      if (isRecitingFullSurah) {
        stopFullSurahRecitation();
      } else {
        isRecitingFullSurah = true;
        btn.innerHTML = `<i data-lucide="pause" class="w-3 h-3 animate-pulse"></i> Pause`;
        btn.classList.add("bg-gold-600");
        playNextSequentialVerse(0);
      }
      lucide.createIcons();
    }

    function playNextSequentialVerse(idx) {
      const s = surahsData[currentSurahKey];
      if (!isRecitingFullSurah || idx >= s.verses.length) {
        stopFullSurahRecitation();
        return;
      }
      const v = s.verses[idx];
      playAyahAudio(s.number, v.id, idx, () => {
        if (isRecitingFullSurah) {
          playNextSequentialVerse(idx + 1);
        }
      });
    }

    function stopFullSurahRecitation() {
      isRecitingFullSurah = false;
      stopAyahAudio();
      const btn = document.getElementById("reciteAudioBtn");
      if (btn) {
        btn.innerHTML = `<i data-lucide="volume-2" class="w-3 h-3"></i> Recite`;
        btn.classList.remove("bg-gold-600");
      }
      document.querySelectorAll('.ayah-card').forEach(c => {
        c.classList.remove("ring-2", "ring-gold-500", "bg-gold-500/10", "dark:bg-gold-500/15");
      });
      if ('mediaSession' in navigator) {
        navigator.mediaSession.playbackState = 'none';
      }
      lucide.createIcons();
    }

    function highlightActiveAyah(idx) {
      document.querySelectorAll('.ayah-card').forEach((c, i) => {
        if (i === idx) {
          c.classList.add("ring-2", "ring-gold-500", "bg-gold-500/10", "dark:bg-gold-500/15");
          c.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
          c.classList.remove("ring-2", "ring-gold-500", "bg-gold-500/10", "dark:bg-gold-500/15");
        }
      });
    }

    // Authentic Hisn al-Muslim Adhkar
    const adhkarData = {
      morning: [
        { id: 1, ar: "أَصْبَحْنَا وَأَصْبَحَ الْمُلْكُ لِلَّهِ، وَالْحَمْدُ لِلَّهِ، لَا إِلَٰهَ إِلَّا اللَّهُ", tr: "Asbahna wa-asbahal-mulku lillah, wal-hamdu lillah, la ilaha illallah", en: "We have reached the morning and sovereignty belongs to Allah, and all praise is for Allah.", ref: "Sahih Muslim 2723", target: 1, current: 1, done: false },
        { id: 2, ar: "اللَّهُمَّ بِكَ أَصْبَحْنَا، وَبِكَ أَمْسَيْنَا، وَبِكَ نَحْيَا، وَبِكَ نَمُوتُ", tr: "Allahumma bika asbahna, wa bika amsayna, wa bika nahya, wa bika namoot", en: "O Allah, by You we enter the morning and the evening, by You we live and by You we die.", ref: "Sunan Abu Dawud 5068", target: 1, current: 1, done: false },
        { id: 3, ar: "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ: عَدَدَ خَلْقِهِ، وَرِضَا نَفْسِهِ، وَزِنَةَ عَرْشِهِ", tr: "SubhanAllahi wa bihamdihi: 'adada khalqihi, wa rida nafsihi, wa zinata 'arshihi", en: "Glory and praise be to Allah, by the number of His creation, His pleasure, and weight of His Throne.", ref: "Sahih Muslim 2726", target: 3, current: 3, done: false },
        { id: 4, ar: "بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ", tr: "Bismillaahil-lazee la yadurru ma'asmihi shay'un fil-ardi wa la fis-samaa'", en: "In the Name of Allah with Whose Name nothing can cause harm in earth or heaven.", ref: "Sunan Ibn Majah 3869", target: 3, current: 3, done: false },
        { id: 5, ar: "رَضِيتُ بِاللَّهِ رَبًّا، وَبِالْإِسْلَامِ دِينًا، وَبِمُحَمَّدٍ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ نَبِيًّا", tr: "Radheetu billahi Rabba, wa bil-Islami deena, wa bi-Muhammadin Nabiyya", en: "I am pleased with Allah as my Lord, Islam as my religion, and Muhammad (pbuh) as my Prophet.", ref: "Sunan Abu Dawud 5072", target: 3, current: 3, done: false }
      ],
      evening: [
        { id: 6, ar: "أَمْسَيْنَا وَأَمْسَى الْمُلْكُ لِلَّهِ، وَالْحَمْدُ لِلَّهِ، لَا إِلَٰهَ إِلَّا اللَّهُ", tr: "Amsayna wa-amsal-mulku lillah, wal-hamdu lillah", en: "We have reached the evening and sovereignty belongs to Allah, and all praise is for Allah.", ref: "Sahih Muslim 2723", target: 1, current: 1, done: false },
        { id: 7, ar: "اللَّهُمَّ بِكَ أَمْسَيْنَا، وَبِكَ أَصْبَحْنَا، وَبِكَ نَحْيَا، وَبِكَ نَمُوتُ", tr: "Allahumma bika amsayna, wa bika asbahna, wa bika nahya, wa bika namoot", en: "O Allah, by You we enter the evening, by You we live and die, and unto You is our return.", ref: "Sunan Abu Dawud 5068", target: 1, current: 1, done: false },
        { id: 8, ar: "أَعُوذُ بِكَلِمَاتِ اللَّهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ", tr: "A'oozu bi-kalimaatil-laahit-taammaati min sharri maa khalaq", en: "I seek refuge in the perfect words of Allah from the evil of what He created.", ref: "Sahih Muslim 2709", target: 3, current: 3, done: false },
        { id: 9, ar: "بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ", tr: "Bismillaahil-lazee la yadurru ma'asmihi shay'un fil-ardi wa la fis-samaa'", en: "In the Name of Allah with Whose Name nothing can cause harm in earth or heaven.", ref: "Sunan Ibn Majah 3869", target: 3, current: 3, done: false }
      ],
      after_prayer: [
        { id: 1, ar: "أَسْتَغْفِرُ اللَّهَ (٣x)، اللَّهُمَّ أَنْتَ السَّلَامُ وَمِنْكَ السَّلَامُ، تَبَارَكْتَ يَا ذَا الْجَلَالِ وَالإِكْرَامِ", tr: "Astaghfirullah (3x), Allahumma antas-Salamu wa minkas-Salam, tabarakta ya dhal-Jalali wal-Ikram", en: "I ask Allah for forgiveness (3x). O Allah, You are Peace and from You comes peace. Blessed are You, O Owner of majesty and honor.", ref: "Sahih Muslim 591", target: 1, current: 1, done: false },
        { id: 2, ar: "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ", tr: "Allahu la ilaha illa huwal-Hayyul-Qayyum, la ta'khudhuhu sinatun wa la nawm", en: "Allah - there is no deity except Him, the Ever-Living, the Sustainer of all existence. Neither drowsiness overtakes Him nor sleep.", ref: "Sunan an-Nasa'i (Ayat al-Kursi)", target: 1, current: 1, done: false },
        { id: 3, ar: "سُبْحَانَ اللَّهِ (٣٣x)، الْحَمْدُ لِلَّهِ (٣٣x)، اللَّهُ أَكْبَرُ (٣٣x)", tr: "SubhanAllah (33x), Alhamdulillah (33x), Allahu Akbar (33x)", en: "Glory be to Allah (33 times), Praise be to Allah (33 times), Allah is the Greatest (33 times).", ref: "Sahih al-Bukhari 843", target: 3, current: 3, done: false },
        { id: 4, ar: "لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ، وَهُوَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ", tr: "La ilaha illallahu wahdahu la shareeka lah, lahul-mulku wa lahul-hamd, wa huwa 'ala kulli shay'in qadeer", en: "None has the right to be worshipped but Allah alone, Who has no partner. His is the dominion and His is the praise, and He can do all things.", ref: "Sahih Muslim 597", target: 1, current: 1, done: false }
      ],
      sleep: [
        { id: 1, ar: "بِاسْمِكَ رَبِّي وَضَعْتُ جَنْبِي، وَبِكَ أَرْفَعُهُ، فَإِنْ أَمْسَكْتَ نَفْسِي فَارْحَمْهَا", tr: "Bismika Rabbi wada'tu janbi, wa bika arfa'uh, fa in amsakta nafsi farhamha", en: "In Your name my Lord, I lie down and in Your name I rise up. If You should take my soul, have mercy upon it.", ref: "Sahih al-Bukhari 6320", target: 1, current: 1, done: false },
        { id: 2, ar: "اللَّهُمَّ قِنِي عَذَابَكَ يَوْمَ تَبْعَثُ عِبَادَكَ", tr: "Allahumma qini 'adhabaka yawma tab'athu 'ibadak", en: "O Allah, protect me from Your punishment on the Day You resurrect Your servants.", ref: "Sunan Abu Dawud 5045", target: 3, current: 3, done: false },
        { id: 3, ar: "الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنَا وَسَقَانَا، وَكَفَانَا وَآوَانَا، فَكَمْ مِمَّنْ لَا كَافِيَ لَهُ وَلَا مُؤْوِيَ", tr: "Alhamdu lillahil-ladhi at'amana wa saqana, wa kafana wa awana", en: "Praise is to Allah Who has provided us with food and with drink, sufficed us and gave us an abode.", ref: "Sahih Muslim 2715", target: 1, current: 1, done: false }
      ],
      daily: [
        { id: 1, ar: "بِسْمِ اللَّهِ وَعَلَى بَرَكَةِ اللَّهِ", tr: "Bismillahi wa 'ala barakatillah", en: "In the name of Allah and with the blessings of Allah. (Before eating)", ref: "Mustadrak al-Hakim", target: 1, current: 1, done: false },
        { id: 2, ar: "الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنَا وَسَقَانَا وَجَعَلَنَا مُسْلِمِينَ", tr: "Alhamdu lillahil-ladhi at'amana wa saqana wa ja'alana muslimeen", en: "Praise is to Allah who has fed us, gave us drink, and made us Muslims. (After eating)", ref: "Sunan Abu Dawud 3850", target: 1, current: 1, done: false },
        { id: 3, ar: "بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ", tr: "Bismillahi, tawakkaltu 'alallahi, wa la hawla wa la quwwata illa billah", en: "In the name of Allah, I place my trust in Allah. There is no power or strength except with Allah. (Leaving home)", ref: "Sunan Abu Dawud 5095", target: 1, current: 1, done: false },
        { id: 4, ar: "بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى رَبِّنَا تَوَكَّلْنَا", tr: "Bismillahi walajna, wa bismillahi kharajna, wa 'ala Rabbina tawakkalna", en: "In the name of Allah we enter, and in the name of Allah we leave, and upon our Lord we rely. (Entering home)", ref: "Sunan Abu Dawud 5096", target: 1, current: 1, done: false },
        { id: 5, ar: "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ وَإِنَّا إِلَىٰ رَبِّنَا لَمُنْقَلِبُونَ", tr: "Subhanal-ladhee sakh-khara lana hadha wa ma kunna lahu muqrineen, wa inna ila Rabbina lamunqaliboon", en: "Glory unto Him who has subjected this to us, though we were not capable of it, and surely to our Lord we return. (Travel / Safar)", ref: "Surah Az-Zukhruf 13-14", target: 1, current: 1, done: false },
        { id: 6, ar: "اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ", tr: "Allahummaftah lee abwaba rahmatik", en: "O Allah, open for me the gates of Your mercy. (Entering masjid)", ref: "Sahih Muslim 713", target: 1, current: 1, done: false },
        { id: 7, ar: "اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ", tr: "Allahumma inni as'aluka min fadlik", en: "O Allah, I ask You of Your bounty. (Leaving masjid)", ref: "Sahih Muslim 713", target: 1, current: 1, done: false },
        { id: 8, ar: "الْحَمْدُ لِلَّهِ الَّذِي كَسَانِي هَٰذَا الثَّوْبَ وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ", tr: "Alhamdu lillahil-ladhee kasanee hadhath-thawba wa razaqaneehi min ghayri hawlin minnee wa la quwwah", en: "Praise be to Allah Who has clothed me with this garment and provided it for me without power or might from me. (Wearing clothes)", ref: "Sunan Abu Dawud 4023", target: 1, current: 1, done: false },
        { id: 9, ar: "اللَّهُمَّ أَنْتَ حَسَّنْتَ خَلْقِي فَحَسِّنْ خُلُقِي", tr: "Allahumma anta hassanta khalqi fa-hassin khuluqi", en: "O Allah, just as You made my external appearance good, make my inner character good. (Looking into mirror)", ref: "Musnad Ahmad 24392", target: 1, current: 1, done: false },
        { id: 10, ar: "الْحَمْدُ لِلَّهِ • يَرْحَمُكَ اللَّهُ • يَهْدِيكُمُ اللَّهُ وَيُصْلِحُ بَالَكُمْ", tr: "Alhamdulillah • Yarhamukallah • Yahdeekumullah wa yuslih baalakum", en: "Praise be to Allah (sneezing) • May Allah have mercy on you • May Allah guide you and rectify your condition.", ref: "Sahih al-Bukhari 6224", target: 1, current: 1, done: false },
        { id: 11, ar: "لَا بَأْسَ طَهُورٌ إِنْ شَاءَ اللَّهُ", tr: "La ba'sa tahoorun in sha Allah", en: "Do not worry, it is a purification if Allah wills. (Visiting the sick)", ref: "Sahih al-Bukhari 3616", target: 1, current: 1, done: false },
        { id: 12, ar: "رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا", tr: "Rabbi irhamhuma kama rabbayani sagheera", en: "My Lord, have mercy upon my parents as they brought me up when I was small. (For parents)", ref: "Surah Al-Isra 17:24", target: 1, current: 1, done: false }
      ],
      quranic: [
        { id: 1, ar: "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ", tr: "Rabbana atina fid-dunya hasanatan wa fil-akhirati hasanatan wa qina 'adhaban-nar", en: "Our Lord, give us in this world that which is good and in the Hereafter that which is good, and save us from the torment of the Fire.", ref: "Surah Al-Baqarah 2:201", target: 1, current: 1, done: false },
        { id: 2, ar: "رَبِّ زِدْنِي عِلْمًا", tr: "Rabbi zidni 'ilma", en: "My Lord, increase me in knowledge.", ref: "Surah Ta-Ha 20:114", target: 3, current: 3, done: false },
        { id: 3, ar: "رَبَّنَا أَفْرِغْ عَلَيْنَا صَبْرًا وَثَبِّتْ أَقْدَامَنَا وَانْصُرْنَا عَلَى الْقَوْمِ الْكَافِرِينَ", tr: "Rabbana afrigh 'alayna sabran wa thabbit aqdamana wansurna 'alal-qawmil-kafireen", en: "Our Lord, pour down upon us patience, plant our feet firmly, and help us against the disbelieving people.", ref: "Surah Al-Baqarah 2:250", target: 1, current: 1, done: false },
        { id: 4, ar: "رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِنْ لَدُنْكَ رَحْمَةً ۚ إِنَّكَ أَنْتَ الْوَهَّابُ", tr: "Rabbana la tuzigh quloobana ba'da idh hadaytana wa hab lana min ladunka rahmah, innaka Antal-Wahhab", en: "Our Lord, let not our hearts deviate after You have guided us and grant us from Yourself mercy. Indeed, You are the Bestower.", ref: "Surah Ali 'Imran 3:8", target: 1, current: 1, done: false },
        { id: 5, ar: "رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي وَاحْلُلْ عُقْدَةً مِنْ لِسَانِي يَفْقَهُوا قَوْلِي", tr: "Rabbish-rah li sadri, wa yassir li amri, wahlul 'uqdatan min lisani, yafqahoo qawli", en: "My Lord, expand for me my breast, ease for me my task, and untie the knot from my tongue that they may understand my speech.", ref: "Surah Ta-Ha 20:25-28", target: 1, current: 1, done: false },
        { id: 6, ar: "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ، وَالْعَجْزِ وَالْكَسَلِ، وَالْجُبْنِ وَالْبُخْلِ، وَضَلَعِ الدَّيْنِ وَغَلَبَةِ الرِّجَالِ", tr: "Allahumma inni a'oodhu bika minal-hammi wal-hazani, wal-'ajzi wal-kasali, wal-jubni wal-bukhli, wa dala'id-dayni wa ghalabatir-rijal", en: "O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, cowardice and stinginess, and the burden of debt and oppression of men.", ref: "Sahih al-Bukhari 2893", target: 1, current: 1, done: false },
        { id: 7, ar: "اللَّهُمَّ أَنْتَ رَبِّي لَا إِلَٰهَ إِلَّا أَنْتَ، خَلَقْتَنِي وَأَنَا عَبْدُكَ، وَأَنَا عَلَىٰ عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، أَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَأَبُوءُ لَكَ بِذَنْبِي فَاغْفِرْ لِي فَإِنَّهُ لَا يَغْفِرُ الذُّنُوبَ إِلَّا أَنْتَ", tr: "Allahumma anta Rabbi la ilaha illa anta, khalaqtani wa ana 'abduka, wa ana 'ala 'ahdika wa wa'dika mastata'tu, a'oodhu bika min sharri ma sana'tu, aboo'u laka bini'matika 'alayya, wa aboo'u laka bidhanbee faghfir lee fa innahu la yaghfirudh-dhunooba illa anta", en: "Sayyidul Istighfar (Supreme Supplication for Forgiveness): O Allah, You are my Lord, none has the right to be worshipped but You...", ref: "Sahih al-Bukhari 6306", target: 1, current: 1, done: false }
      ]
    };
    let currentAdhkarMode = 'morning';

    function setAdhkarMode(mode) {
      playClickSound();
      currentAdhkarMode = mode;
      const btnMap = {
        morning: 'adhkarMornBtn',
        evening: 'adhkarEveBtn',
        after_prayer: 'adhkarAfterBtn',
        daily: 'adhkarDailyBtn',
        quranic: 'adhkarQuranicBtn',
        sleep: 'adhkarSleepBtn'
      };

      Object.keys(btnMap).forEach(m => {
        const btn = document.getElementById(btnMap[m]);
        if (btn) {
          if (m === mode) {
            btn.className = "px-3 py-1 rounded-full bg-emerald-800 text-white font-bold shadow-xs flex-shrink-0 transition";
          } else {
            btn.className = "px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-semibold flex-shrink-0 transition";
          }
        }
      });
      renderAdhkar();
    }

    function renderAdhkar() {
      const list = adhkarData[currentAdhkarMode];
      const container = document.getElementById("adhkarItemsList");
      container.innerHTML = "";

      let completedCount = 0;
      list.forEach((item, index) => {
        if (item.done) completedCount++;
        const card = document.createElement("div");
        card.id = `adhkar-card-${item.id}`;
        card.className = `p-3 rounded-xl border transition-all ${item.done ? 'bg-emerald-50/60 dark:bg-emerald-950/30 border-emerald-300 dark:border-emerald-700/60' : 'bg-white dark:bg-slate-800 border-slate-100 dark:border-slate-700/60'}`;
        card.innerHTML = `
          <div class="space-y-1.5">
            <div class="flex items-start justify-between gap-2.5">
              <span class="text-[10px] font-semibold text-slate-400">${item.ref}</span>
              <button onclick="decrementAdhkar(${index})" class="px-2.5 py-1 rounded-lg flex-shrink-0 flex items-center gap-1 font-bold text-xs transition active:scale-90 border ${item.done ? 'bg-emerald-700 border-emerald-700 text-white shadow-xs' : 'bg-gold-500/10 border-gold-500/30 text-gold-600 dark:text-gold-400'}">
                ${item.done ? '✓ Completed' : `${item.current}x`}
              </button>
            </div>
            <p class="notranslate font-arabic text-right text-[19px] font-bold text-emerald-950 dark:text-emerald-100 leading-[2.2]" translate="no" lang="ar" dir="rtl">${item.ar}</p>
            ${showTransliteration && item.tr ? `<p class="text-left text-[13px] text-emerald-800/90 dark:text-emerald-400/90 font-sans italic leading-normal pt-0.5">${item.tr}</p>` : ''}
            <p class="text-left text-[14px] text-slate-700 dark:text-slate-200 leading-relaxed font-normal pt-0.5">${item.en}</p>
          </div>
        `;
        container.appendChild(card);
      });

      const total = list.length;
      const pct = Math.round((completedCount / total) * 100);
      const textEl = document.getElementById("adhkarProgressText");
      const barEl = document.getElementById("adhkarProgressBar");
      if (textEl) textEl.innerText = `${completedCount} of ${total} (${pct}%)`;
      if (barEl) barEl.style.width = `${pct}%`;

      if (completedCount === total && total > 0) {
        showToast("Session Finished", "Alhamdulillah! All daily adhkar in this collection completed.");
      }

      lucide.createIcons();
    }

    function decrementAdhkar(idx) {
      playClickSound();
      const item = adhkarData[currentAdhkarMode][idx];
      if (item.current > 1) {
        item.current--;
      } else {
        item.done = !item.done;
        if (!item.done) item.current = item.target;
        else playChimeSound();
      }
      renderAdhkar();
      saveState();
    }

    function resetAdhkarSession() {
      playClickSound();
      adhkarData[currentAdhkarMode].forEach(item => {
        item.current = item.target;
        item.done = false;
      });
      renderAdhkar();
      saveState();
      showToast("Adhkar Reset", "Session counts reset to beginning");
    }

    // Tactile Digital Tasbeeh with 6 Presets & Targets
    let tasbeehCount = 0;
    let tasbeehTarget = 33;
    let tasbeehLaps = 1;
    let tasbeehDailyTotal = 0;
    let selectedDhikrIdx = 0;
    const tasbeehPhrases = [
      { en: "SubhanAllah", ar: "سُبْحَانَ اللَّهِ", target: 33 },
      { en: "Alhamdulillah", ar: "الْحَمْدُ لِلَّهِ", target: 33 },
      { en: "Allahu Akbar", ar: "اللَّهُ أَكْبَرُ", target: 34 },
      { en: "Astaghfirullah", ar: "أَسْتَغْفِرُ اللَّهَ", target: 100 },
      { en: "La Ilaha Illallah", ar: "لَا إِلَٰهَ إِلَّا اللَّهُ", target: 100 },
      { en: "Salawat", ar: "اللَّهُمَّ صَلِّ عَلَىٰ مُحَمَّدٍ", target: 100 }
    ];

    function updateTasbeehRing() {
      const progress = tasbeehTarget > 0 ? (tasbeehCount / tasbeehTarget) : 0;
      const offset = 603 - (603 * Math.min(progress, 1.0));
      const arc = document.getElementById("tasbeehProgressArc");
      if (arc) arc.style.strokeDashoffset = offset;
    }

    function incrementTasbeeh() {
      playClickSound();
      tasbeehCount++;
      tasbeehDailyTotal++;
      
      if (tasbeehTarget > 0 && tasbeehCount >= tasbeehTarget) {
        tasbeehCount = 0;
        tasbeehLaps++;
        playChimeSound();
        if (navigator.vibrate) navigator.vibrate([40, 60, 40]);
      }
      
      document.getElementById("tasbeehCount").innerText = tasbeehCount;
      document.getElementById("tasbeehLapsLabel").innerText = `Lap ${tasbeehLaps}`;
      document.getElementById("tasbeehTotalDaily").innerText = tasbeehDailyTotal;
      updateTasbeehRing();
      saveState();
    }

    function resetTasbeeh() {
      playClickSound();
      tasbeehCount = 0;
      tasbeehLaps = 1;
      document.getElementById("tasbeehCount").innerText = 0;
      document.getElementById("tasbeehLapsLabel").innerText = "Lap 1";
      updateTasbeehRing();
      saveState();
    }

    function setTasbeehTarget(val) {
      playClickSound();
      tasbeehTarget = val;
      tasbeehCount = 0;
      document.getElementById("tasbeehCount").innerText = 0;
      document.getElementById("tasbeehTargetLabel").innerText = val === 0 ? "Continuous ∞" : `Target ${val}`;
      
      [33, 99, 100, 0].forEach(t => {
        const btn = document.getElementById(`target-btn-${t}`);
        if (!btn) return;
        if (t === val) {
          btn.className = "px-3 py-1 text-xs font-bold rounded-lg border border-emerald-600 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300";
        } else {
          btn.className = "px-3 py-1 text-xs font-bold rounded-lg border border-slate-300 dark:border-slate-700";
        }
      });

      updateTasbeehRing();
      saveState();
    }

    function toggleTasbeehSound() {
      playClickSound();
      isTasbeehSoundOn = !isTasbeehSoundOn;
      const btn = document.getElementById("soundToggleBtn");
      if (btn) {
        btn.innerHTML = `<i data-lucide="${isTasbeehSoundOn ? 'volume-2' : 'volume-x'}" class="w-3.5 h-3.5 ${isTasbeehSoundOn ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-400'}"></i>`;
        btn.className = `w-7 h-7 rounded-lg flex items-center justify-center active:scale-95 transition shadow-xs ${
          isTasbeehSoundOn 
            ? 'bg-slate-200/90 dark:bg-slate-800 border border-slate-300/40 dark:border-slate-700/60' 
            : 'bg-rose-50 dark:bg-rose-950/50 border border-rose-300/60 dark:border-rose-900/60'
        }`;
      }
      showToast("Tasbeeh Audio", isTasbeehSoundOn ? `Sound ON (${currentTasbeehSound.toUpperCase()})` : "Muted (Haptic only)");
      saveState();
      lucide.createIcons();
    }

    function setTasbeehDhikr(idx) {
      playClickSound();
      selectedDhikrIdx = idx;
      tasbeehCount = 0;
      document.getElementById("tasbeehCount").innerText = 0;
      document.getElementById("currentDhikrAr").innerText = tasbeehPhrases[idx].ar;
      setTasbeehTarget(tasbeehPhrases[idx].target);

      [0, 1, 2, 3, 4, 5].forEach(i => {
        const pill = document.getElementById(`dhikr-pill-${i}`);
        if (!pill) return;
        if (i === idx) {
          pill.className = "px-3 py-1.5 rounded-full font-bold bg-emerald-800 text-white flex-shrink-0";
        } else {
          pill.className = "px-3 py-1.5 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0";
        }
      });
      updateTasbeehRing();
      saveState();
    }

    // Switch Tab
    function switchTab(tabId) {
      playClickSound();
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.getElementById(`tab-${tabId}`).classList.remove('hidden');

      const tabs = ['prayers', 'qibla', 'quran', 'adhkar', 'tasbeeh'];
      tabs.forEach(t => {
        const btn = document.getElementById(`nav-${t}`);
        if (t === tabId) {
          btn.className = "flex flex-col items-center gap-1 text-emerald-800 dark:text-emerald-400 font-bold transition";
        } else {
          btn.className = "flex flex-col items-center gap-1 text-slate-400 hover:text-slate-600 transition";
        }
      });
      lucide.createIcons();
    }

    // Language toggle (Complete English & Arabic Translations)
    const translations = {
      en: {
        prayers: "Prayers",
        qibla: "Qibla",
        quran: "Quran",
        adhkar: "Adhkar",
        tasbeeh: "Tasbeeh",
        timetable: "Timetable",
        nextPrayer: "Upcoming",
        countdown: "Countdown",
        dailyHadith: "Daily Hadith",
        bearing: "Bearing:",
        qiblaTitle: "Qibla",
        quranTitle: "Quran",
        adhkarTitle: "Adhkar",
        tasbeehTitle: "Tasbeeh",
        tasbeehSub: "Dhikr Counter",
        langBtn: "Switch to Arabic (RTL)"
      },
      ar: {
        prayers: "الصلاة",
        qibla: "القبلة",
        quran: "القرآن",
        adhkar: "الأذكار",
        tasbeeh: "التسبيح",
        timetable: "مواقيت الصلاة",
        nextPrayer: "الصلاة القادمة",
        countdown: "الوقت المتبقي",
        dailyHadith: "حديث اليوم",
        bearing: "اتجاه القبلة:",
        qiblaTitle: "اتجاه القبلة الشريفة",
        quranTitle: "القرآن الكريم",
        adhkarTitle: "أذكار اليوم والليلة",
        tasbeehTitle: "المسبحة الإلكترونية",
        tasbeehSub: "تسبيح رقمي مع تنبيه صوتي عند الإتمام",
        langBtn: "Switch to English (LTR)"
      }
    };

    function toggleLang() {
      isArabic = !isArabic;
      const screen = document.getElementById("deviceScreen");
      const btnText = document.getElementById("langBtnText");
      const dict = isArabic ? translations.ar : translations.en;

      if (isArabic) {
        screen.setAttribute("dir", "rtl");
        screen.classList.add("font-arabic-ui");
      } else {
        screen.setAttribute("dir", "ltr");
        screen.classList.remove("font-arabic-ui");
      }

      btnText.innerText = dict.langBtn;
      document.getElementById("tabNavTextPrayers").innerText = dict.prayers;
      document.getElementById("tabNavTextQibla").innerText = dict.qibla;
      document.getElementById("tabNavTextQuran").innerText = dict.quran;
      document.getElementById("tabNavTextAdhkar").innerText = dict.adhkar;
      document.getElementById("tabNavTextTasbeeh").innerText = dict.tasbeeh;
      document.getElementById("lblTimetableTitle").innerText = dict.timetable;
      document.getElementById("lblNextPrayerBadge").innerText = dict.nextPrayer;
      document.getElementById("lblCountdownSub").innerText = dict.countdown;
      document.getElementById("lblDailyHadithTitle").innerHTML = `<i data-lucide="book-marked" class="w-3 h-3 text-gold-500"></i> ${dict.dailyHadith}`;
      document.getElementById("lblQiblaTitle").innerText = dict.qiblaTitle;
      document.getElementById("lblQuranTitle").innerText = dict.quranTitle;
      document.getElementById("lblAdhkarTitle").innerText = dict.adhkarTitle;
      document.getElementById("lblTasbeehTitle").innerText = dict.tasbeehTitle;
      document.getElementById("lblTasbeehSub").innerText = dict.tasbeehSub;

      // Translate Hero Next Prayer
      const heroEl = document.getElementById("heroPrayerName");
      if (heroEl) heroEl.innerText = isArabic ? (prayerNameAr[currentActivePrayerId] || currentActivePrayerId) : currentActivePrayerId;

      // Translate Daily Salah Log Header
      const salahTitle = document.getElementById("lblDailySalahTitle");
      if (salahTitle) salahTitle.innerText = isArabic ? "متابعة الصلوات" : "Salah Log";
      // Streak badge removed for minimal clean UI
      const markAllEl = document.getElementById("btnMarkAllSalah");
      if (markAllEl) markAllEl.innerText = isArabic ? "تحديد الكل" : "Mark All";

      // Translate Adhkar Chips
      const mChip = document.getElementById("adhkarMornBtn"); if (mChip) mChip.innerText = isArabic ? "أذكار الصباح" : "Morning";
      const eChip = document.getElementById("adhkarEveBtn"); if (eChip) eChip.innerText = isArabic ? "أذكار المساء" : "Evening";
      const aChip = document.getElementById("adhkarAfterBtn"); if (aChip) aChip.innerText = isArabic ? "بعد الصلاة" : "After Salah";
      const dChip = document.getElementById("adhkarDailyBtn"); if (dChip) dChip.innerText = isArabic ? "أدعية يومية" : "Daily Duas";
      const qChip = document.getElementById("adhkarQuranicBtn"); if (qChip) qChip.innerText = isArabic ? "أدعية قرآنية" : "Quranic Duas";
      const sChip = document.getElementById("adhkarSleepBtn"); if (sChip) sChip.innerText = isArabic ? "أذكار النوم" : "Sleep";

      // Translate Tasbeeh Counters
      const tgtLabel = document.getElementById("tasbeehTargetLabel");
      if (tgtLabel) tgtLabel.innerText = isArabic ? "الهدف ٣٣" : "Target 33";
      const lapsLabel = document.getElementById("tasbeehLapsLabel");
      if (lapsLabel) lapsLabel.innerText = isArabic ? "الدورة ١" : "Lap 1";
      const rstBtn = document.getElementById("btnResetTasbeeh");
      if (rstBtn) rstBtn.innerText = isArabic ? "إعادة ضبط" : "Reset";

      // Quran Header Title
      const qTitle = document.getElementById("lblQuranTitle");
      if (qTitle) qTitle.innerText = isArabic ? "القرآن الكريم" : "Quran";

      renderPrayerCards();
      renderSalahTracker();
      renderSurahPills();
      updateCompass(document.getElementById("headingSlider") ? document.getElementById("headingSlider").value : 0);
      saveState();
      lucide.createIcons();
    }

    // Theme toggle
    function toggleTheme() {
      isDark = !isDark;
      const screen = document.getElementById("deviceScreen");
      if (isDark) {
        screen.classList.add("dark", "bg-[#0A1612]");
        screen.classList.remove("bg-[#FAF8F5]");
      } else {
        screen.classList.remove("dark", "bg-[#0A1612]");
        screen.classList.add("bg-[#FAF8F5]");
      }
      saveState();
    }

    // OS Switcher (iOS vs Android)
    function setOS(os) {
      currentOS = os;
      const iosBtn = document.getElementById("osIosBtn");
      const androidBtn = document.getElementById("osAndroidBtn");
      const container = document.getElementById("deviceContainer");
      const screen = document.getElementById("deviceScreen");
      const dynamicIsland = document.getElementById("iosDynamicIsland");
      const cameraDot = document.getElementById("androidCameraDot");
      const iosIcons = document.getElementById("statusBarIosIcons");
      const androidIcons = document.getElementById("statusBarAndroidIcons");
      const clock = document.getElementById("statusBarClock");
      const iosBar = document.getElementById("iosHomeBar");
      const androidBar = document.getElementById("androidNavLine");

      if (os === 'ios') {
        iosBtn.className = "px-4 py-1.5 rounded-full bg-blue-600 text-white font-bold transition-all duration-200 flex items-center gap-1.5 shadow-sm";
        androidBtn.className = "px-4 py-1.5 rounded-full text-slate-400 hover:text-white font-medium transition-all duration-200 flex items-center gap-1.5";
        
        container.className = "relative w-[360px] h-[710px] bg-black rounded-[46px] p-2.5 shadow-2xl border-4 border-slate-700 transition-all duration-300";
        screen.className = screen.className.replace(/rounded-\[[^\]]+\]/, "rounded-[38px]");
        
        dynamicIsland.classList.remove("hidden");
        cameraDot.classList.add("hidden");
        
        iosIcons.classList.remove("hidden");
        androidIcons.classList.add("hidden");
        clock.innerText = "09:41";

        iosBar.classList.remove("hidden");
        androidBar.classList.add("hidden");
      } else {
        androidBtn.className = "px-4 py-1.5 rounded-full bg-emerald-600 text-white font-bold transition-all duration-200 flex items-center gap-1.5 shadow-sm";
        iosBtn.className = "px-4 py-1.5 rounded-full text-slate-400 hover:text-white font-medium transition-all duration-200 flex items-center gap-1.5";
        
        container.className = "relative w-[355px] h-[710px] bg-slate-900 rounded-[34px] p-2 shadow-2xl border-2 border-slate-600 transition-all duration-300";
        screen.className = screen.className.replace(/rounded-\[[^\]]+\]/, "rounded-[26px]");
        
        dynamicIsland.classList.add("hidden");
        cameraDot.classList.remove("hidden");
        
        iosIcons.classList.add("hidden");
        androidIcons.classList.remove("hidden");
        clock.innerText = "9:41 AM";

        iosBar.classList.add("hidden");
        androidBar.classList.remove("hidden");
      }
      saveState();
      lucide.createIcons();
    }

    // State Persistence (Professional Date-Aware Session Storage)
    function saveState() {
      try {
        const todayStr = new Date().toISOString().slice(0, 10);
        const adhkarProgress = {
          morning: adhkarData.morning.map(i => ({ id: i.id, current: i.current, done: i.done })),
          evening: adhkarData.evening.map(i => ({ id: i.id, current: i.current, done: i.done }))
        };

        const state = {
          lastActiveDate: todayStr,
          currentCityIndex,
          tasbeehCount,
          tasbeehLaps,
          tasbeehTarget,
          tasbeehDailyTotal,
          selectedDhikrIdx,
          isTasbeehSoundOn,
          quranFontSize,
          showTransliteration,
          bookmarkedVerses,
          prayerAlerts,
          adhkarProgress,
          isDark,
          isArabic,
          currentOS
        };
        localStorage.setItem("muslim_companion_v2_state", JSON.stringify(state));
      } catch (e) {}
    }

    function loadSavedState() {
      try {
        const raw = localStorage.getItem("muslim_companion_v2_state");
        if (!raw) return;
        const s = JSON.parse(raw);
        const todayStr = new Date().toISOString().slice(0, 10);
        const isSameDay = s.lastActiveDate === todayStr;

        // Permanent Settings (Never reset)
        if (s.currentCityIndex !== undefined) currentCityIndex = Math.min(s.currentCityIndex, cities.length - 1);
        if (s.tasbeehTarget !== undefined) tasbeehTarget = s.tasbeehTarget;
        if (s.selectedDhikrIdx !== undefined) selectedDhikrIdx = s.selectedDhikrIdx;
        if (s.isTasbeehSoundOn !== undefined) isTasbeehSoundOn = s.isTasbeehSoundOn;
        if (s.quranFontSize !== undefined) quranFontSize = s.quranFontSize;
        if (s.showTransliteration !== undefined) showTransliteration = s.showTransliteration;
        if (s.bookmarkedVerses !== undefined) bookmarkedVerses = s.bookmarkedVerses;
        if (s.prayerAlerts !== undefined) prayerAlerts = s.prayerAlerts;
        if (s.isDark) toggleTheme();
        if (s.isArabic) toggleLang();

        // Daily Progress (Preserved if same day, fresh reset if new day tomorrow)
        if (isSameDay) {
          if (s.tasbeehCount !== undefined) tasbeehCount = s.tasbeehCount;
          if (s.tasbeehLaps !== undefined) tasbeehLaps = s.tasbeehLaps;
          if (s.tasbeehDailyTotal !== undefined) tasbeehDailyTotal = s.tasbeehDailyTotal;

          if (s.adhkarProgress) {
            ['morning', 'evening'].forEach(mode => {
              if (s.adhkarProgress[mode]) {
                s.adhkarProgress[mode].forEach(savedItem => {
                  const target = adhkarData[mode].find(i => i.id === savedItem.id);
                  if (target) {
                    target.current = savedItem.current;
                    target.done = savedItem.done;
                  }
                });
              }
            });
          }
        } else {
          // New day: Start fresh 0 for daily Adhkar & daily beads, keep lifetime settings!
          tasbeehCount = 0;
          tasbeehLaps = 1;
        }
      } catch (e) {}
    }

    function autoDetectUserTimezone() {
      try {
        const raw = localStorage.getItem("muslim_companion_v2_state");
        if (raw) {
          const s = JSON.parse(raw);
          if (s.currentCityIndex !== undefined) return; // User already chose a specific city manually
        }
        
        const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
        let matchedIdx = -1;
        
        if (tz.includes("Karachi") || tz.includes("Pakistan") || tz.includes("Islamabad") || tz.includes("Lahore") || tz.includes("Asia/Karachi")) {
          matchedIdx = cities.findIndex(c => c.name.includes("Karachi"));
        } else if (tz.includes("London") || tz.includes("Europe/London") || tz.includes("Dublin") || tz.includes("Lisbon")) {
          matchedIdx = cities.findIndex(c => c.name.includes("London"));
        } else if (tz.includes("New_York") || tz.includes("Eastern") || tz.includes("Detroit") || tz.includes("Indiana")) {
          matchedIdx = cities.findIndex(c => c.name.includes("New York"));
        } else if (tz.includes("Dubai") || tz.includes("Muscat") || tz.includes("Abu_Dhabi") || tz.includes("Asia/Dubai")) {
          matchedIdx = cities.findIndex(c => c.name.includes("Dubai"));
        } else if (tz.includes("Cairo") || tz.includes("Africa/Cairo")) {
          matchedIdx = cities.findIndex(c => c.name.includes("Cairo"));
        } else if (tz.includes("Istanbul") || tz.includes("Europe/Istanbul")) {
          matchedIdx = cities.findIndex(c => c.name.includes("Istanbul"));
        } else if (tz.includes("Riyadh") || tz.includes("Asia/Riyadh") || tz.includes("Kuwait") || tz.includes("Qatar")) {
          matchedIdx = cities.findIndex(c => c.name.includes("Makkah"));
        } else if (tz.includes("Toronto") || tz.includes("Montreal") || tz.includes("America/Toronto")) {
          matchedIdx = cities.findIndex(c => c.name.includes("Toronto"));
        } else if (tz.includes("Jerusalem") || tz.includes("Gaza") || tz.includes("Hebron")) {
          matchedIdx = cities.findIndex(c => c.name.includes("Jerusalem"));
        }

        if (matchedIdx !== -1) {
          currentCityIndex = matchedIdx;
        }
      } catch (e) {}
    }

    
    // Complete 114 Surahs Directory with verified Uthmani calligraphy & metadata
    const all114Surahs = [{"number": 1, "titleAr": "سُورَةُ ٱلْفَاتِحَةِ", "titleEn": "Al-Faatiha", "meaningEn": "The Opening", "versesCount": 7, "type": "Meccan"}, {"number": 2, "titleAr": "سُورَةُ البَقَرَةِ", "titleEn": "Al-Baqara", "meaningEn": "The Cow", "versesCount": 286, "type": "Medinan"}, {"number": 3, "titleAr": "سُورَةُ آلِ عِمۡرَانَ", "titleEn": "Aal-i-Imraan", "meaningEn": "The Family of Imraan", "versesCount": 200, "type": "Medinan"}, {"number": 4, "titleAr": "سُورَةُ النِّسَاءِ", "titleEn": "An-Nisaa", "meaningEn": "The Women", "versesCount": 176, "type": "Medinan"}, {"number": 5, "titleAr": "سُورَةُ المَائـِدَةِ", "titleEn": "Al-Maaida", "meaningEn": "The Table", "versesCount": 120, "type": "Medinan"}, {"number": 6, "titleAr": "سُورَةُ الأَنۡعَامِ", "titleEn": "Al-An'aam", "meaningEn": "The Cattle", "versesCount": 165, "type": "Meccan"}, {"number": 7, "titleAr": "سُورَةُ الأَعۡرَافِ", "titleEn": "Al-A'raaf", "meaningEn": "The Heights", "versesCount": 206, "type": "Meccan"}, {"number": 8, "titleAr": "سُورَةُ الأَنفَالِ", "titleEn": "Al-Anfaal", "meaningEn": "The Spoils of War", "versesCount": 75, "type": "Medinan"}, {"number": 9, "titleAr": "سُورَةُ التَّوۡبَةِ", "titleEn": "At-Tawba", "meaningEn": "The Repentance", "versesCount": 129, "type": "Medinan"}, {"number": 10, "titleAr": "سُورَةُ يُونُسَ", "titleEn": "Yunus", "meaningEn": "Jonas", "versesCount": 109, "type": "Meccan"}, {"number": 11, "titleAr": "سُورَةُ هُودٍ", "titleEn": "Hud", "meaningEn": "Hud", "versesCount": 123, "type": "Meccan"}, {"number": 12, "titleAr": "سُورَةُ يُوسُفَ", "titleEn": "Yusuf", "meaningEn": "Joseph", "versesCount": 111, "type": "Meccan"}, {"number": 13, "titleAr": "سُورَةُ الرَّعۡدِ", "titleEn": "Ar-Ra'd", "meaningEn": "The Thunder", "versesCount": 43, "type": "Medinan"}, {"number": 14, "titleAr": "سُورَةُ إِبۡرَاهِيمَ", "titleEn": "Ibrahim", "meaningEn": "Abraham", "versesCount": 52, "type": "Meccan"}, {"number": 15, "titleAr": "سُورَةُ الحِجۡرِ", "titleEn": "Al-Hijr", "meaningEn": "The Rock", "versesCount": 99, "type": "Meccan"}, {"number": 16, "titleAr": "سُورَةُ النَّحۡلِ", "titleEn": "An-Nahl", "meaningEn": "The Bee", "versesCount": 128, "type": "Meccan"}, {"number": 17, "titleAr": "سُورَةُ الإِسۡرَاءِ", "titleEn": "Al-Israa", "meaningEn": "The Night Journey", "versesCount": 111, "type": "Meccan"}, {"number": 18, "titleAr": "سُورَةُ الكَهۡفِ", "titleEn": "Al-Kahf", "meaningEn": "The Cave", "versesCount": 110, "type": "Meccan"}, {"number": 19, "titleAr": "سُورَةُ مَرۡيَمَ", "titleEn": "Maryam", "meaningEn": "Mary", "versesCount": 98, "type": "Meccan"}, {"number": 20, "titleAr": "سُورَةُ طه", "titleEn": "Taa-Haa", "meaningEn": "Taa-Haa", "versesCount": 135, "type": "Meccan"}, {"number": 21, "titleAr": "سُورَةُ الأَنبِيَاءِ", "titleEn": "Al-Anbiyaa", "meaningEn": "The Prophets", "versesCount": 112, "type": "Meccan"}, {"number": 22, "titleAr": "سُورَةُ الحَجِّ", "titleEn": "Al-Hajj", "meaningEn": "The Pilgrimage", "versesCount": 78, "type": "Medinan"}, {"number": 23, "titleAr": "سُورَةُ المُؤۡمِنُونَ", "titleEn": "Al-Muminoon", "meaningEn": "The Believers", "versesCount": 118, "type": "Meccan"}, {"number": 24, "titleAr": "سُورَةُ النُّورِ", "titleEn": "An-Noor", "meaningEn": "The Light", "versesCount": 64, "type": "Medinan"}, {"number": 25, "titleAr": "سُورَةُ الفُرۡقَانِ", "titleEn": "Al-Furqaan", "meaningEn": "The Criterion", "versesCount": 77, "type": "Meccan"}, {"number": 26, "titleAr": "سُورَةُ الشُّعَرَاءِ", "titleEn": "Ash-Shu'araa", "meaningEn": "The Poets", "versesCount": 227, "type": "Meccan"}, {"number": 27, "titleAr": "سُورَةُ النَّمۡلِ", "titleEn": "An-Naml", "meaningEn": "The Ant", "versesCount": 93, "type": "Meccan"}, {"number": 28, "titleAr": "سُورَةُ القَصَصِ", "titleEn": "Al-Qasas", "meaningEn": "The Stories", "versesCount": 88, "type": "Meccan"}, {"number": 29, "titleAr": "سُورَةُ العَنكَبُوتِ", "titleEn": "Al-Ankaboot", "meaningEn": "The Spider", "versesCount": 69, "type": "Meccan"}, {"number": 30, "titleAr": "سُورَةُ الرُّومِ", "titleEn": "Ar-Room", "meaningEn": "The Romans", "versesCount": 60, "type": "Meccan"}, {"number": 31, "titleAr": "سُورَةُ لُقۡمَانَ", "titleEn": "Luqman", "meaningEn": "Luqman", "versesCount": 34, "type": "Meccan"}, {"number": 32, "titleAr": "سُورَةُ السَّجۡدَةِ", "titleEn": "As-Sajda", "meaningEn": "The Prostration", "versesCount": 30, "type": "Meccan"}, {"number": 33, "titleAr": "سُورَةُ الأَحۡزَابِ", "titleEn": "Al-Ahzaab", "meaningEn": "The Clans", "versesCount": 73, "type": "Medinan"}, {"number": 34, "titleAr": "سُورَةُ سَبَإٍ", "titleEn": "Saba", "meaningEn": "Sheba", "versesCount": 54, "type": "Meccan"}, {"number": 35, "titleAr": "سُورَةُ فَاطِرٍ", "titleEn": "Faatir", "meaningEn": "The Originator", "versesCount": 45, "type": "Meccan"}, {"number": 36, "titleAr": "سُورَةُ يسٓ", "titleEn": "Yaseen", "meaningEn": "Yaseen", "versesCount": 83, "type": "Meccan"}, {"number": 37, "titleAr": "سُورَةُ الصَّافَّاتِ", "titleEn": "As-Saaffaat", "meaningEn": "Those drawn up in Ranks", "versesCount": 182, "type": "Meccan"}, {"number": 38, "titleAr": "سُورَةُ صٓ", "titleEn": "Saad", "meaningEn": "The letter Saad", "versesCount": 88, "type": "Meccan"}, {"number": 39, "titleAr": "سُورَةُ الزُّمَرِ", "titleEn": "Az-Zumar", "meaningEn": "The Groups", "versesCount": 75, "type": "Meccan"}, {"number": 40, "titleAr": "سُورَةُ غَافِرٍ", "titleEn": "Ghafir", "meaningEn": "The Forgiver", "versesCount": 85, "type": "Meccan"}, {"number": 41, "titleAr": "سُورَةُ فُصِّلَتۡ", "titleEn": "Fussilat", "meaningEn": "Explained in detail", "versesCount": 54, "type": "Meccan"}, {"number": 42, "titleAr": "سُورَةُ الشُّورَىٰ", "titleEn": "Ash-Shura", "meaningEn": "Consultation", "versesCount": 53, "type": "Meccan"}, {"number": 43, "titleAr": "سُورَةُ الزُّخۡرُفِ", "titleEn": "Az-Zukhruf", "meaningEn": "Ornaments of gold", "versesCount": 89, "type": "Meccan"}, {"number": 44, "titleAr": "سُورَةُ الدُّخَانِ", "titleEn": "Ad-Dukhaan", "meaningEn": "The Smoke", "versesCount": 59, "type": "Meccan"}, {"number": 45, "titleAr": "سُورَةُ الجَاثِيَةِ", "titleEn": "Al-Jaathiya", "meaningEn": "Crouching", "versesCount": 37, "type": "Meccan"}, {"number": 46, "titleAr": "سُورَةُ الأَحۡقَافِ", "titleEn": "Al-Ahqaf", "meaningEn": "The Dunes", "versesCount": 35, "type": "Meccan"}, {"number": 47, "titleAr": "سُورَةُ مُحَمَّدٍ", "titleEn": "Muhammad", "meaningEn": "Muhammad", "versesCount": 38, "type": "Medinan"}, {"number": 48, "titleAr": "سُورَةُ الفَتۡحِ", "titleEn": "Al-Fath", "meaningEn": "The Victory", "versesCount": 29, "type": "Medinan"}, {"number": 49, "titleAr": "سُورَةُ الحُجُرَاتِ", "titleEn": "Al-Hujuraat", "meaningEn": "The Inner Apartments", "versesCount": 18, "type": "Medinan"}, {"number": 50, "titleAr": "سُورَةُ قٓ", "titleEn": "Qaaf", "meaningEn": "The letter Qaaf", "versesCount": 45, "type": "Meccan"}, {"number": 51, "titleAr": "سُورَةُ الذَّارِيَاتِ", "titleEn": "Adh-Dhaariyat", "meaningEn": "The Winnowing Winds", "versesCount": 60, "type": "Meccan"}, {"number": 52, "titleAr": "سُورَةُ الطُّورِ", "titleEn": "At-Tur", "meaningEn": "The Mount", "versesCount": 49, "type": "Meccan"}, {"number": 53, "titleAr": "سُورَةُ النَّجۡمِ", "titleEn": "An-Najm", "meaningEn": "The Star", "versesCount": 62, "type": "Meccan"}, {"number": 54, "titleAr": "سُورَةُ القَمَرِ", "titleEn": "Al-Qamar", "meaningEn": "The Moon", "versesCount": 55, "type": "Meccan"}, {"number": 55, "titleAr": "سُورَةُ الرَّحۡمَٰن", "titleEn": "Ar-Rahmaan", "meaningEn": "The Beneficent", "versesCount": 78, "type": "Medinan"}, {"number": 56, "titleAr": "سُورَةُ الوَاقِعَةِ", "titleEn": "Al-Waaqia", "meaningEn": "The Inevitable", "versesCount": 96, "type": "Meccan"}, {"number": 57, "titleAr": "سُورَةُ الحَدِيدِ", "titleEn": "Al-Hadid", "meaningEn": "The Iron", "versesCount": 29, "type": "Medinan"}, {"number": 58, "titleAr": "سُورَةُ المُجَادلَةِ", "titleEn": "Al-Mujaadila", "meaningEn": "The Pleading Woman", "versesCount": 22, "type": "Medinan"}, {"number": 59, "titleAr": "سُورَةُ الحَشۡرِ", "titleEn": "Al-Hashr", "meaningEn": "The Exile", "versesCount": 24, "type": "Medinan"}, {"number": 60, "titleAr": "سُورَةُ المُمۡتَحنَةِ", "titleEn": "Al-Mumtahana", "meaningEn": "She that is to be examined", "versesCount": 13, "type": "Medinan"}, {"number": 61, "titleAr": "سُورَةُ الصَّفِّ", "titleEn": "As-Saff", "meaningEn": "The Ranks", "versesCount": 14, "type": "Medinan"}, {"number": 62, "titleAr": "سُورَةُ الجُمُعَةِ", "titleEn": "Al-Jumu'a", "meaningEn": "Friday", "versesCount": 11, "type": "Medinan"}, {"number": 63, "titleAr": "سُورَةُ المُنَافِقُونَ", "titleEn": "Al-Munaafiqoon", "meaningEn": "The Hypocrites", "versesCount": 11, "type": "Medinan"}, {"number": 64, "titleAr": "سُورَةُ التَّغَابُنِ", "titleEn": "At-Taghaabun", "meaningEn": "Mutual Disillusion", "versesCount": 18, "type": "Medinan"}, {"number": 65, "titleAr": "سُورَةُ الطَّلَاقِ", "titleEn": "At-Talaaq", "meaningEn": "Divorce", "versesCount": 12, "type": "Medinan"}, {"number": 66, "titleAr": "سُورَةُ التَّحۡرِيمِ", "titleEn": "At-Tahrim", "meaningEn": "The Prohibition", "versesCount": 12, "type": "Medinan"}, {"number": 67, "titleAr": "سُورَةُ المُلۡكِ", "titleEn": "Al-Mulk", "meaningEn": "The Sovereignty", "versesCount": 30, "type": "Meccan"}, {"number": 68, "titleAr": "سُورَةُ القَلَمِ", "titleEn": "Al-Qalam", "meaningEn": "The Pen", "versesCount": 52, "type": "Meccan"}, {"number": 69, "titleAr": "سُورَةُ الحَاقَّةِ", "titleEn": "Al-Haaqqa", "meaningEn": "The Reality", "versesCount": 52, "type": "Meccan"}, {"number": 70, "titleAr": "سُورَةُ المَعَارِجِ", "titleEn": "Al-Ma'aarij", "meaningEn": "The Ascending Stairways", "versesCount": 44, "type": "Meccan"}, {"number": 71, "titleAr": "سُورَةُ نُوحٍ", "titleEn": "Nooh", "meaningEn": "Noah", "versesCount": 28, "type": "Meccan"}, {"number": 72, "titleAr": "سُورَةُ الجِنِّ", "titleEn": "Al-Jinn", "meaningEn": "The Jinn", "versesCount": 28, "type": "Meccan"}, {"number": 73, "titleAr": "سُورَةُ المُزَّمِّلِ", "titleEn": "Al-Muzzammil", "meaningEn": "The Enshrouded One", "versesCount": 20, "type": "Meccan"}, {"number": 74, "titleAr": "سُورَةُ المُدَّثِّرِ", "titleEn": "Al-Muddaththir", "meaningEn": "The Cloaked One", "versesCount": 56, "type": "Meccan"}, {"number": 75, "titleAr": "سُورَةُ القِيَامَةِ", "titleEn": "Al-Qiyaama", "meaningEn": "The Resurrection", "versesCount": 40, "type": "Meccan"}, {"number": 76, "titleAr": "سُورَةُ الإِنسَانِ", "titleEn": "Al-Insaan", "meaningEn": "Man", "versesCount": 31, "type": "Medinan"}, {"number": 77, "titleAr": "سُورَةُ المُرۡسَلَاتِ", "titleEn": "Al-Mursalaat", "meaningEn": "The Emissaries", "versesCount": 50, "type": "Meccan"}, {"number": 78, "titleAr": "سُورَةُ النَّبَإِ", "titleEn": "An-Naba", "meaningEn": "The Announcement", "versesCount": 40, "type": "Meccan"}, {"number": 79, "titleAr": "سُورَةُ النَّازِعَاتِ", "titleEn": "An-Naazi'aat", "meaningEn": "Those who drag forth", "versesCount": 46, "type": "Meccan"}, {"number": 80, "titleAr": "سُورَةُ عَبَسَ", "titleEn": "Abasa", "meaningEn": "He frowned", "versesCount": 42, "type": "Meccan"}, {"number": 81, "titleAr": "سُورَةُ التَّكۡوِيرِ", "titleEn": "At-Takwir", "meaningEn": "The Overthrowing", "versesCount": 29, "type": "Meccan"}, {"number": 82, "titleAr": "سُورَةُ الانفِطَارِ", "titleEn": "Al-Infitaar", "meaningEn": "The Cleaving", "versesCount": 19, "type": "Meccan"}, {"number": 83, "titleAr": "سُورَةُ المُطَفِّفِينَ", "titleEn": "Al-Mutaffifin", "meaningEn": "Defrauding", "versesCount": 36, "type": "Meccan"}, {"number": 84, "titleAr": "سُورَةُ الانشِقَاقِ", "titleEn": "Al-Inshiqaaq", "meaningEn": "The Splitting Open", "versesCount": 25, "type": "Meccan"}, {"number": 85, "titleAr": "سُورَةُ البُرُوجِ", "titleEn": "Al-Burooj", "meaningEn": "The Constellations", "versesCount": 22, "type": "Meccan"}, {"number": 86, "titleAr": "سُورَةُ الطَّارِقِ", "titleEn": "At-Taariq", "meaningEn": "The Morning Star", "versesCount": 17, "type": "Meccan"}, {"number": 87, "titleAr": "سُورَةُ الأَعۡلَىٰ", "titleEn": "Al-A'laa", "meaningEn": "The Most High", "versesCount": 19, "type": "Meccan"}, {"number": 88, "titleAr": "سُورَةُ الغَاشِيَةِ", "titleEn": "Al-Ghaashiya", "meaningEn": "The Overwhelming", "versesCount": 26, "type": "Meccan"}, {"number": 89, "titleAr": "سُورَةُ الفَجۡرِ", "titleEn": "Al-Fajr", "meaningEn": "The Dawn", "versesCount": 30, "type": "Meccan"}, {"number": 90, "titleAr": "سُورَةُ البَلَدِ", "titleEn": "Al-Balad", "meaningEn": "The City", "versesCount": 20, "type": "Meccan"}, {"number": 91, "titleAr": "سُورَةُ الشَّمۡسِ", "titleEn": "Ash-Shams", "meaningEn": "The Sun", "versesCount": 15, "type": "Meccan"}, {"number": 92, "titleAr": "سُورَةُ اللَّيۡلِ", "titleEn": "Al-Lail", "meaningEn": "The Night", "versesCount": 21, "type": "Meccan"}, {"number": 93, "titleAr": "سُورَةُ الضُّحَىٰ", "titleEn": "Ad-Dhuhaa", "meaningEn": "The Morning Hours", "versesCount": 11, "type": "Meccan"}, {"number": 94, "titleAr": "سُورَةُ الشَّرۡحِ", "titleEn": "Ash-Sharh", "meaningEn": "The Consolation", "versesCount": 8, "type": "Meccan"}, {"number": 95, "titleAr": "سُورَةُ التِّينِ", "titleEn": "At-Tin", "meaningEn": "The Fig", "versesCount": 8, "type": "Meccan"}, {"number": 96, "titleAr": "سُورَةُ العَلَقِ", "titleEn": "Al-Alaq", "meaningEn": "The Clot", "versesCount": 19, "type": "Meccan"}, {"number": 97, "titleAr": "سُورَةُ القَدۡرِ", "titleEn": "Al-Qadr", "meaningEn": "The Power, Fate", "versesCount": 5, "type": "Meccan"}, {"number": 98, "titleAr": "سُورَةُ البَيِّنَةِ", "titleEn": "Al-Bayyina", "meaningEn": "The Evidence", "versesCount": 8, "type": "Medinan"}, {"number": 99, "titleAr": "سُورَةُ الزَّلۡزَلَةِ", "titleEn": "Az-Zalzala", "meaningEn": "The Earthquake", "versesCount": 8, "type": "Medinan"}, {"number": 100, "titleAr": "سُورَةُ العَادِيَاتِ", "titleEn": "Al-Aadiyaat", "meaningEn": "The Chargers", "versesCount": 11, "type": "Meccan"}, {"number": 101, "titleAr": "سُورَةُ القَارِعَةِ", "titleEn": "Al-Qaari'a", "meaningEn": "The Calamity", "versesCount": 11, "type": "Meccan"}, {"number": 102, "titleAr": "سُورَةُ التَّكَاثُرِ", "titleEn": "At-Takaathur", "meaningEn": "Competition", "versesCount": 8, "type": "Meccan"}, {"number": 103, "titleAr": "سُورَةُ العَصۡرِ", "titleEn": "Al-Asr", "meaningEn": "The Declining Day, Epoch", "versesCount": 3, "type": "Meccan"}, {"number": 104, "titleAr": "سُورَةُ الهُمَزَةِ", "titleEn": "Al-Humaza", "meaningEn": "The Traducer", "versesCount": 9, "type": "Meccan"}, {"number": 105, "titleAr": "سُورَةُ الفِيلِ", "titleEn": "Al-Fil", "meaningEn": "The Elephant", "versesCount": 5, "type": "Meccan"}, {"number": 106, "titleAr": "سُورَةُ قُرَيۡشٍ", "titleEn": "Quraish", "meaningEn": "Quraysh", "versesCount": 4, "type": "Meccan"}, {"number": 107, "titleAr": "سُورَةُ المَاعُونِ", "titleEn": "Al-Maa'un", "meaningEn": "Almsgiving", "versesCount": 7, "type": "Meccan"}, {"number": 108, "titleAr": "سُورَةُ الكَوۡثَرِ", "titleEn": "Al-Kawthar", "meaningEn": "Abundance", "versesCount": 3, "type": "Meccan"}, {"number": 109, "titleAr": "سُورَةُ الكَافِرُونَ", "titleEn": "Al-Kaafiroon", "meaningEn": "The Disbelievers", "versesCount": 6, "type": "Meccan"}, {"number": 110, "titleAr": "سُورَةُ النَّصۡرِ", "titleEn": "An-Nasr", "meaningEn": "Divine Support", "versesCount": 3, "type": "Medinan"}, {"number": 111, "titleAr": "سُورَةُ المَسَدِ", "titleEn": "Al-Masad", "meaningEn": "The Palm Fibre", "versesCount": 5, "type": "Meccan"}, {"number": 112, "titleAr": "سُورَةُ الإِخۡلَاصِ", "titleEn": "Al-Ikhlaas", "meaningEn": "Sincerity", "versesCount": 4, "type": "Meccan"}, {"number": 113, "titleAr": "سُورَةُ الفَلَقِ", "titleEn": "Al-Falaq", "meaningEn": "The Dawn", "versesCount": 5, "type": "Meccan"}, {"number": 114, "titleAr": "سُورَةُ النَّاسِ", "titleEn": "An-Naas", "meaningEn": "Mankind", "versesCount": 6, "type": "Meccan"}];
    let currentSurahFilter = 'all';

    function openSurahIndexModal() {
      playClickSound();
      const modal = document.getElementById("surahIndexModal");
      if (!modal) return;
      modal.classList.remove("hidden");
      renderSurahIndexList();
      const input = document.getElementById("surahSearchInput");
      if (input) {
        input.value = "";
        setTimeout(() => input.focus(), 100);
      }
      lucide.createIcons();
    }

    function closeSurahIndexModal() {
      playClickSound();
      const modal = document.getElementById("surahIndexModal");
      if (modal) modal.classList.add("hidden");
    }

    function setSurahFilter(filter) {
      playClickSound();
      currentSurahFilter = filter;
      const allBtn = document.getElementById("surahFilterAll");
      const mecBtn = document.getElementById("surahFilterMeccan");
      const medBtn = document.getElementById("surahFilterMedinan");
      
      [allBtn, mecBtn, medBtn].forEach(b => {
        if (b) {
          b.className = "px-2.5 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 transition";
        }
      });

      if (filter === 'all' && allBtn) allBtn.className = "px-2.5 py-0.5 rounded-full bg-emerald-800 text-white font-bold transition";
      if (filter === 'meccan' && mecBtn) mecBtn.className = "px-2.5 py-0.5 rounded-full bg-emerald-800 text-white font-bold transition";
      if (filter === 'medinan' && medBtn) medBtn.className = "px-2.5 py-0.5 rounded-full bg-emerald-800 text-white font-bold transition";
      
      const q = document.getElementById("surahSearchInput") ? document.getElementById("surahSearchInput").value : "";
      filterSurahsList(q);
    }

    let currentDirectoryTab = 'surahs';

    function switchDirectoryTab(tab) {
      playClickSound();
      currentDirectoryTab = tab;
      const tabs = ['surahs', 'duas', 'special'];
      tabs.forEach(t => {
        const btn = document.getElementById(`dirTab-${t}`);
        if (btn) {
          btn.className = (t === tab)
            ? "py-1 rounded-lg bg-emerald-800 text-white transition flex items-center justify-center gap-1 font-bold shadow-xs"
            : "py-1 rounded-lg text-slate-600 dark:text-slate-300 hover:text-white transition flex items-center justify-center gap-1 font-semibold";
        }
      });

      const subChips = document.getElementById("surahFilterSubChips");
      if (subChips) {
        subChips.style.display = (tab === 'surahs') ? 'flex' : 'none';
      }

      const q = document.getElementById("surahSearchInput") ? document.getElementById("surahSearchInput").value : "";
      renderDirectoryList(q);
      lucide.createIcons();
    }

    function filterDirectoryList(query) {
      renderDirectoryList(query);
    }

    function renderDirectoryList(query = "") {
      const container = document.getElementById("surahIndexCardsContainer");
      if (!container) return;
      container.innerHTML = "";
      const q = query.trim().toLowerCase();

      if (currentDirectoryTab === 'surahs') {
        renderSurahIndexList(query);
        return;
      }

      if (currentDirectoryTab === 'duas') {
        const allDuas = [];
        if (typeof adhkarData !== 'undefined') {
          if (adhkarData.daily) adhkarData.daily.forEach(d => allDuas.push({ ...d, mode: 'daily', typeBadge: 'Daily Sunnah' }));
          if (adhkarData.quranic) adhkarData.quranic.forEach(d => allDuas.push({ ...d, mode: 'quranic', typeBadge: 'Quranic Rabbana' }));
          if (adhkarData.morning) adhkarData.morning.forEach(d => allDuas.push({ ...d, mode: 'morning', typeBadge: 'Morning Adhkar' }));
          if (adhkarData.evening) adhkarData.evening.forEach(d => allDuas.push({ ...d, mode: 'evening', typeBadge: 'Evening Adhkar' }));
        }

        const filteredDuas = allDuas.filter(d => {
          if (!q) return true;
          return (d.tr && d.tr.toLowerCase().includes(q)) ||
                 (d.en && d.en.toLowerCase().includes(q)) ||
                 (d.ref && d.ref.toLowerCase().includes(q)) ||
                 (d.ar && d.ar.includes(q));
        });

        if (filteredDuas.length === 0) {
          container.innerHTML = `<div class="p-6 text-center text-xs text-slate-400">No Duas found matching "${query}"</div>`;
          return;
        }

        filteredDuas.forEach(d => {
          const card = document.createElement("div");
          card.className = "p-2.5 rounded-xl border border-slate-200/80 dark:border-slate-700/70 bg-white dark:bg-slate-800/90 hover:border-emerald-500/50 transition cursor-pointer active:scale-[0.99] space-y-1.5";
          card.onclick = () => {
            closeSurahIndexModal();
            switchTab('adhkar');
            setAdhkarMode(d.mode || 'daily');
            showToast("Dua Selected", d.tr || "Hisn al-Muslim");
          };

          card.innerHTML = `
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-1.5 min-w-0 flex-1 pr-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-600 flex-shrink-0"></span>
                <h4 class="text-xs font-bold text-slate-900 dark:text-white truncate">${d.tr || d.ref}</h4>
              </div>
              <span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-50 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 border border-emerald-300/40 flex-shrink-0">
                ${d.typeBadge}
              </span>
            </div>
            <p class="notranslate font-arabic text-sm text-right text-emerald-950 dark:text-emerald-200 leading-relaxed font-bold" dir="rtl">${d.ar}</p>
            <p class="text-[11px] text-slate-600 dark:text-slate-300 line-clamp-2">${d.en}</p>
            <div class="flex items-center justify-between pt-1 border-t border-slate-100 dark:border-slate-700/60 text-[9px] text-slate-400">
              <span>${d.ref || 'Hisn al-Muslim'}</span>
              <span class="text-emerald-700 dark:text-emerald-400 font-bold flex items-center gap-0.5">Read in Adhkar →</span>
            </div>
          `;
          container.appendChild(card);
        });
        return;
      }

      if (currentDirectoryTab === 'special') {
        const specialVerses = [
          { key: 'kursi', title: 'Ayat al-Kursi (آية الكرسي)', ref: 'Surah 2:255', desc: 'The Throne Verse • Greatest verse in the Quran for protection', tag: 'Protection' },
          { key: 'fatihah', title: 'Surah Al-Faatiha (الفاتحة)', ref: 'Surah 1:1-7', desc: 'The Opening • Mother of the Book • Read in every Salah', tag: 'Daily Salah' },
          { key: 'ikhlas', title: 'Surah Al-Ikhlas (الإخلاص)', ref: 'Surah 112:1-4', desc: 'The Sincerity • Equals one-third of the Holy Quran', tag: 'Tawheed' },
          { key: 'falaq', title: 'Surah Al-Falaq (الفلق)', ref: 'Surah 113:1-5', desc: 'The Daybreak • Protection from envy and evil', tag: 'Mu’awwidhat' },
          { key: 'nas', title: 'Surah An-Naas (الناس)', ref: 'Surah 114:1-6', desc: 'Mankind • Refuge from whispers of Shaytan', tag: 'Mu’awwidhat' },
          { key: 'kahf', title: 'Surah Al-Kahf (الكهف)', ref: 'Surah 18', desc: 'The Cave • Sunnah reading every Friday for luminous light', tag: 'Friday Sunnah' },
          { key: 'yasin', title: 'Surah Yasin (يس)', ref: 'Surah 36', desc: 'The Heart of the Quran', tag: 'Virtue' },
          { key: 'mulk', title: 'Surah Al-Mulk (الملك)', ref: 'Surah 67', desc: 'The Sovereignty • Intercedes in the grave for its reader', tag: 'Nightly Protection' }
        ];

        const filteredSpecial = specialVerses.filter(v => {
          if (!q) return true;
          return v.title.toLowerCase().includes(q) || v.ref.toLowerCase().includes(q) || v.desc.toLowerCase().includes(q);
        });

        filteredSpecial.forEach(v => {
          const card = document.createElement("div");
          card.className = "p-2.5 rounded-xl border border-slate-200/80 dark:border-slate-700/70 bg-white dark:bg-slate-800/90 hover:border-gold-500/50 transition cursor-pointer active:scale-[0.99] flex items-center justify-between";
          card.onclick = () => {
            closeSurahIndexModal();
            if (v.key === 'kursi' || v.key === 'fatihah' || v.key === 'ikhlas' || v.key === 'falaq' || v.key === 'nas') {
              loadSurah(v.key);
            } else {
              showToast("Surah Selected", `Opening ${v.title}`);
            }
          };

          card.innerHTML = `
            <div class="min-w-0 flex-1 pr-2">
              <div class="flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-gold-500"></span>
                <h4 class="text-xs font-bold text-slate-900 dark:text-white truncate">${v.title}</h4>
              </div>
              <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5 line-clamp-1">${v.desc}</p>
              <p class="text-[9px] text-gold-600 dark:text-gold-400 font-semibold mt-0.5">${v.ref}</p>
            </div>
            <span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-gold-50 dark:bg-amber-950/60 text-gold-700 dark:text-gold-400 border border-gold-300/40 flex-shrink-0">
              ${v.tag}
            </span>
          `;
          container.appendChild(card);
        });
        return;
      }
    }


    function cleanArText(t) {
      return (t || "").replace(/[\u064B-\u065F\u0670\u0653]/g, "").replace(/[أإآ]/g, "ا");
    }

    function cleanEnText(t) {
      return (t || "").toLowerCase()
        .replace(/aa/g, "a")
        .replace(/ee/g, "i")
        .replace(/oo/g, "u")
        .replace(/h$/g, "")
        .replace(/[-'\s]/g, "");
    }

    function renderSurahIndexList(query = "") {
      const container = document.getElementById("surahIndexCardsContainer");
      if (!container) return;
      container.innerHTML = "";
      
      const q = query.trim().toLowerCase();
      const qClean = cleanEnText(q);
      const qArClean = cleanArText(q);

      const filtered = all114Surahs.filter(s => {
        if (currentSurahFilter === 'meccan' && s.type.toLowerCase() !== 'meccan') return false;
        if (currentSurahFilter === 'medinan' && s.type.toLowerCase() !== 'medinan') return false;
        if (!q) return true;
        
        const numMatch = String(s.number) === q || String(s.number).includes(q);
        const enMatch = s.titleEn.toLowerCase().includes(q) || cleanEnText(s.titleEn).includes(qClean);
        const meanMatch = s.meaningEn.toLowerCase().includes(q);
        const arMatch = s.titleAr.includes(q) || cleanArText(s.titleAr).includes(qArClean);

        return numMatch || enMatch || meanMatch || arMatch;
      });

      if (filtered.length === 0) {
        container.innerHTML = `<div class="p-6 text-center text-xs text-slate-400">No Surah found matching "${query}"</div>`;
        return;
      }



      filtered.forEach(s => {
        const isCurrent = (surahsData[currentSurahKey] && surahsData[currentSurahKey].number === s.number);
        const card = document.createElement("div");
        card.className = `flex items-center justify-between p-2.5 rounded-xl border transition cursor-pointer active:scale-[0.99] ${
          isCurrent 
            ? "bg-emerald-50 dark:bg-emerald-950/40 border-emerald-400 dark:border-emerald-600 shadow-xs" 
            : "bg-white dark:bg-slate-800/90 hover:bg-slate-50 dark:hover:bg-slate-700/60 border-slate-200/80 dark:border-slate-700/70"
        }`;
        card.onclick = () => selectSurahFromIndex(s.number);

        card.innerHTML = `
          <div class="flex items-center gap-2.5 min-w-0">
            <div class="w-7 h-7 rounded-lg bg-gold-500/15 border border-gold-500/30 text-gold-600 dark:text-gold-400 font-bold text-xs flex items-center justify-center font-sans flex-shrink-0">
              ${s.number}
            </div>
            <div class="min-w-0">
              <h4 class="text-xs font-bold text-slate-800 dark:text-white truncate flex items-center gap-1.5">
                ${s.titleEn}
                <span class="text-[9px] font-normal px-1.5 py-0.2 rounded ${s.type === 'Meccan' ? 'bg-emerald-100 dark:bg-emerald-900/60 text-emerald-800 dark:text-emerald-300' : 'bg-blue-100 dark:bg-blue-900/60 text-blue-800 dark:text-blue-300'}">
                  ${s.type}
                </span>
              </h4>
              <p class="text-[10px] text-slate-400 truncate">${s.meaningEn} • ${s.versesCount} Verses</p>
            </div>
          </div>
          <div class="text-right flex-shrink-0 pl-2">
            <p class="notranslate font-arabic text-base font-bold text-emerald-950 dark:text-emerald-200" translate="no" lang="ar" dir="rtl">
              ${s.titleAr}
            </p>
          </div>
        `;
        container.appendChild(card);
      });


      lucide.createIcons();
    }

    function scrollAppBodyToTop() {
      playClickSound();
      const appBody = document.getElementById("appBody");
      if (appBody) appBody.scrollTo({ top: 0, behavior: "smooth" });
    }

    function goToSurahByNum(num) {
      playClickSound();
      selectSurahFromIndex(num);
      scrollAppBodyToTop();
    }

    // Map of prebundled Surah numbers to keys
    const surahNumToKey = {
      1: 'fatihah',
      97: 'qadr',
      103: 'asr',
      105: 'fil',
      106: 'quraysh',
      107: 'maun',
      108: 'kawthar',
      109: 'kafirun',
      110: 'nasr',
      112: 'ikhlas',
      113: 'falaq',
      114: 'nas',
      67: 'mulk'
    };

    async function selectSurahFromIndex(surahNum) {
      closeSurahIndexModal();
      
      // If prebundled, load immediately offline
      if (surahNumToKey[surahNum] && surahsData[surahNumToKey[surahNum]]) {
        loadSurah(surahNumToKey[surahNum]);
        return;
      }

      const cacheKey = 'surah_dynamic_' + surahNum;
      if (surahsData[cacheKey]) {
        loadSurah(cacheKey);
        return;
      }

      // Check localStorage cache
      try {
        const cachedRaw = localStorage.getItem('quran_cache_' + surahNum);
        if (cachedRaw) {
          const cachedSurah = JSON.parse(cachedRaw);
          surahsData[cacheKey] = cachedSurah;
          loadSurah(cacheKey);
          return;
        }
      } catch (e) {}

      // Show sleek loading state
      const sInfo = all114Surahs.find(x => x.number === surahNum);
      if (sInfo) {
        document.getElementById("surahMetaType").innerText = sInfo.type;
        document.getElementById("surahMetaVerses").innerText = `${sInfo.versesCount} Verses`;
        document.getElementById("surahHeaderTitleAr").innerText = sInfo.titleAr;
        document.getElementById("surahHeaderTitleEn").innerText = sInfo.titleEn;
      }
      const container = document.getElementById("quranVersesList");
      container.innerHTML = `
        <div class="p-10 text-center space-y-3">
          <div class="w-8 h-8 mx-auto border-2 border-gold-500 border-t-transparent rounded-full animate-spin"></div>
          <p class="text-xs font-bold text-emerald-800 dark:text-emerald-400">Loading Surah ${sInfo ? sInfo.titleEn : surahNum} in Uthmani Script...</p>
          <p class="text-[10px] text-slate-400">Direct from Holy Quran High-Speed CDN</p>
        </div>
      `;

      try {
        const resp = await fetch(`https://api.alquran.cloud/v1/surah/${surahNum}/editions/quran-uthmani,en.sahih`);
        const json = await resp.json();
        const uthmani = json.data[0];
        const english = json.data[1];

        const verses = uthmani.ayahs.map((a, idx) => ({
          id: a.numberInSurah,
          ar: a.text,
          tr: "",
          en: english.ayahs[idx] ? english.ayahs[idx].text : ""
        }));

        const dynamicSurah = {
          number: surahNum,
          titleAr: uthmani.name,
          titleEn: uthmani.englishName,
          type: uthmani.revelationType,
          versesCount: uthmani.numberOfAyahs,
          verses: verses
        };

        surahsData[cacheKey] = dynamicSurah;
        try {
          localStorage.setItem('quran_cache_' + surahNum, JSON.stringify(dynamicSurah));
        } catch(e) {}

        loadSurah(cacheKey);
      } catch (err) {
        container.innerHTML = `
          <div class="p-6 text-center text-xs text-red-500 bg-red-50 dark:bg-red-950/40 rounded-xl space-y-2">
            <p>Could not fetch Surah offline. Please check your internet connection or choose from pre-bundled Surahs.</p>
            <button onclick="selectSurahFromIndex(${surahNum})" class="px-3 py-1 bg-red-600 text-white rounded-lg text-xs font-bold">Retry</button>
          </div>
        `;
      }
    }

    
    // -------------------------------------------------------------
    // DAILY SALAH TRACKER ENGINE
    // -------------------------------------------------------------
    const defaultSalahLog = {
      Fajr: false,
      Dhuhr: false,
      Asr: false,
      Maghrib: false,
      Isha: false
    };

    let todaySalahLog = { ...defaultSalahLog };

    function renderSalahTracker() {
      const container = document.getElementById("salahTrackerCirclesContainer");
      if (!container) return;
      container.innerHTML = "";

      const prayers = [
        { id: 'Fajr', name: 'Fajr', ar: 'فجر' },
        { id: 'Dhuhr', name: 'Dhuhr', ar: 'ظهر' },
        { id: 'Asr', name: 'Asr', ar: 'عصر' },
        { id: 'Maghrib', name: 'Maghrib', ar: 'مغرب' },
        { id: 'Isha', name: 'Isha', ar: 'عشاء' }
      ];

      let completedCount = 0;
      prayers.forEach(p => {
        const isOffered = !!todaySalahLog[p.id];
        if (isOffered) completedCount++;

        const btn = document.createElement("button");
        btn.onclick = () => toggleSalahOffered(p.id);
        btn.className = `p-1.5 rounded-xl border flex flex-col items-center justify-center gap-1 transition active:scale-95 ${
          isOffered 
            ? 'bg-emerald-700 border-emerald-700 text-white shadow-xs' 
            : 'bg-slate-50 dark:bg-slate-900 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
        }`;

        btn.innerHTML = `
          <div class="w-5 h-5 rounded-full flex items-center justify-center text-[10px] font-bold ${
            isOffered ? 'bg-white text-emerald-800 font-extrabold' : 'bg-slate-200 dark:bg-slate-700 text-slate-500'
          }">
            ${isOffered ? '✓' : ''}
          </div>
          <span class="text-[10px] font-bold truncate">${isArabic ? p.ar : p.name}</span>
        `;
        container.appendChild(btn);
      });

      const pct = Math.round((completedCount / 5) * 100);
      const progEl = document.getElementById("salahTrackerProgressText");
      if (progEl) {
        progEl.innerText = `${completedCount}/5`;
        progEl.className = completedCount === 5 
          ? "text-[10px] font-bold text-gold-500 animate-pulse" 
          : "text-[10px] font-bold text-emerald-700 dark:text-emerald-400";
      }
    }

    function toggleSalahOffered(prayerId) {
      playClickSound();
      todaySalahLog[prayerId] = !todaySalahLog[prayerId];
      if (todaySalahLog[prayerId]) {
        playChimeSound();
        if (navigator.vibrate) navigator.vibrate([40, 50, 40]);
        showToast("Salah Logged", `Alhamdulillah, ${prayerId} prayer marked as offered!`);
      }
      try {
        localStorage.setItem("muslim_comp_salah_log", JSON.stringify(todaySalahLog));
        localStorage.setItem("muslim_comp_salah_date", new Date().toDateString());
      } catch (e) {}
      renderSalahTracker();
    }

    function resetDailySalahTracker() {
      playClickSound();
      todaySalahLog = { ...defaultSalahLog };
      try {
        localStorage.setItem("muslim_comp_salah_log", JSON.stringify(todaySalahLog));
      } catch (e) {}
      renderSalahTracker();
      showToast("Salah Tracker Reset", "Prayer status cleared for today.");
    }

    function loadSavedSalahTracker() {
      try {
        const savedDate = localStorage.getItem("muslim_comp_salah_date");
        const todayStr = new Date().toDateString();
        if (savedDate === todayStr) {
          const raw = localStorage.getItem("muslim_comp_salah_log");
          if (raw) todaySalahLog = JSON.parse(raw);
        } else {
          // New day, reset
          todaySalahLog = { ...defaultSalahLog };
        }
      } catch (e) {}
    }

    // -------------------------------------------------------------
    // PLAYBACK SPEED CONTROLLER
    // -------------------------------------------------------------
    const playbackSpeeds = [1.0, 1.25, 1.5, 0.75];
    let currentSpeedIndex = 0;

    function cyclePlaybackSpeed() {
      playClickSound();
      currentSpeedIndex = (currentSpeedIndex + 1) % playbackSpeeds.length;
      const speed = playbackSpeeds[currentSpeedIndex];

      const btn = document.getElementById("btnAudioPlaybackSpeed");
      if (btn) btn.innerText = `${speed}x`;

      if (currentAyahAudio) {
        currentAyahAudio.playbackRate = speed;
      }
      showToast("Audio Speed", `Recitation playback set to ${speed}x`);
    }

    // -------------------------------------------------------------
    // AYAH COPY & WHATSAPP SHARING
    // -------------------------------------------------------------
    function copySingleAyah(surahKey, verseId, index) {
      playClickSound();
      const s = surahsData[surahKey];
      if (!s || !s.verses || !s.verses[index]) return;
      const v = s.verses[index];

      const shareText = `${v.ar} ﴿${toArabicDigits(v.id)}﴾\n\n"${v.en}"\n\n— [Surah ${s.titleEn} (${s.titleAr}) ${s.number}:${v.id}]\nShared via Muslim Companion`;

      if (navigator.share) {
        navigator.share({
          title: `Surah ${s.titleEn} ${s.number}:${v.id}`,
          text: shareText
        }).catch(() => {
          copyToClipboard(shareText, "Ayah copied! Ready to share on WhatsApp.");
        });
      } else {
        copyToClipboard(shareText, "Ayah copied! Ready to share on WhatsApp.");
      }
    }

    function shareCurrentHadith() {
      playClickSound();
      const h = hadithList[currentHadithIndex];
      if (!h) return;
      const shareText = `${h.ar}\n\n"${h.en}"\n\n— ${h.narrator} (${h.source})\nShared via Muslim Companion`;

      if (navigator.share) {
        navigator.share({
          title: `Daily Hadith — ${h.source}`,
          text: shareText
        }).catch(() => {
          copyToClipboard(shareText, "Hadith copied! Ready to share on WhatsApp.");
        });
      } else {
        copyToClipboard(shareText, "Hadith copied! Ready to share on WhatsApp.");
      }
    }

    // -------------------------------------------------------------
    // SAVED AYAH BOOKMARKS DRAWER
    // -------------------------------------------------------------
    function openBookmarksModal() {
      playClickSound();
      const modal = document.getElementById("bookmarksModal");
      if (!modal) return;
      modal.classList.remove("hidden");
      renderBookmarksList();
      lucide.createIcons();
    }

    function closeBookmarksModal() {
      playClickSound();
      const modal = document.getElementById("bookmarksModal");
      if (modal) modal.classList.add("hidden");
    }

    function renderBookmarksList() {
      const container = document.getElementById("bookmarksCardsContainer");
      if (!container) return;
      container.innerHTML = "";

      const keys = Object.keys(bookmarkedVerses).filter(k => bookmarkedVerses[k]);
      const sub = document.getElementById("bookmarksCountSub");
      if (sub) sub.innerText = `${keys.length} verses saved`;

      if (keys.length === 0) {
        container.innerHTML = `
          <div class="p-8 text-center space-y-2">
            <div class="w-10 h-10 mx-auto rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-400">
              <i data-lucide="bookmark" class="w-5 h-5"></i>
            </div>
            <p class="text-xs font-bold text-slate-700 dark:text-slate-300">No Bookmarks Saved Yet</p>
            <p class="text-[10px] text-slate-400">Tap the bookmark icon 🔖 on any Ayah in the Quran reader to save it here for quick access.</p>
          </div>
        `;
        lucide.createIcons();
        return;
      }

      keys.forEach(bmKey => {
        const parts = bmKey.split('_');
        const sKey = parts[0];
        const vId = parseInt(parts[1], 10);
        const s = surahsData[sKey];
        if (!s) return;
        const v = s.verses ? s.verses.find(x => x.id === vId) : null;
        if (!v) return;

        const card = document.createElement("div");
        card.className = "p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-2 hover:border-gold-500/50 transition cursor-pointer";
        card.onclick = () => jumpToSavedBookmark(sKey, vId);

        card.innerHTML = `
          <div class="flex items-center justify-between pb-1 border-b border-slate-100 dark:border-slate-700/60">
            <span class="text-xs font-bold text-emerald-800 dark:text-emerald-400 flex items-center gap-1">
              Surah ${s.titleEn} (${s.number}:${v.id})
            </span>
            <button onclick="event.stopPropagation(); removeBookmark('${bmKey}')" title="Remove Bookmark" class="p-1 rounded text-slate-400 hover:text-red-500 transition">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
            </button>
          </div>
          <p class="notranslate font-quran-text text-right text-emerald-950 dark:text-white font-semibold text-sm leading-[2.2]" translate="no" lang="ar" dir="rtl">
            ${v.ar} ﴿${toArabicDigits(v.id)}﴾
          </p>
          <p class="text-xs text-slate-600 dark:text-slate-300 font-sans leading-relaxed line-clamp-2">
            ${v.en}
          </p>
        `;
        container.appendChild(card);
      });


      lucide.createIcons();
    }

    function scrollAppBodyToTop() {
      playClickSound();
      const appBody = document.getElementById("appBody");
      if (appBody) appBody.scrollTo({ top: 0, behavior: "smooth" });
    }

    function goToSurahByNum(num) {
      playClickSound();
      selectSurahFromIndex(num);
      scrollAppBodyToTop();
    }

    function removeBookmark(bmKey) {
      delete bookmarkedVerses[bmKey];
      saveState();
      updateBookmarksCountBadges();
      renderBookmarksList();
      renderQuranVerses();
      showToast("Bookmark Removed", "Verse removed from saved list");
    }

    function jumpToSavedBookmark(surahKey, verseId) {
      closeBookmarksModal();
      loadSurah(surahKey);
      setTimeout(() => {
        const s = surahsData[surahKey];
        if (!s || !s.verses) return;
        const idx = s.verses.findIndex(x => x.id === verseId);
        if (idx !== -1) {
          const card = document.getElementById(`ayah-card-${idx}`);
          if (card) {
            card.scrollIntoView({ behavior: 'smooth', block: 'center' });
            card.classList.add("ring-2", "ring-gold-500");
            setTimeout(() => card.classList.remove("ring-2", "ring-gold-500"), 2000);
          }
        }
      }, 300);
    }


    // ==========================================
    // 99 NAMES OF ALLAH (ASMA-UL-HUSNA) ENGINE
    // ==========================================
    const namesOfAllahData = [
      { n: 1, ar: "الرَّحْمَٰنُ", tr: "Ar-Rahman", en: "The Most Gracious / Beneficent", desc: "He who wills all goodness and mercy for all His creatures." },
      { n: 2, ar: "الرَّحِيمُ", tr: "Ar-Raheem", en: "The Most Merciful", desc: "He who acts with extreme kindness and bestows mercy to believers." },
      { n: 3, ar: "الْمَلِكُ", tr: "Al-Malik", en: "The Sovereign King", desc: "The absolute Sovereign Lord of all the worlds." },
      { n: 4, ar: "الْقُدُّوسُ", tr: "Al-Quddus", en: "The Most Holy / Pure", desc: "The Pure One who is completely free from all shortcomings." },
      { n: 5, ar: "السَّلَامُ", tr: "As-Salam", en: "The Source of Peace", desc: "The Giver of peace, tranquility, and safety from harm." },
      { n: 6, ar: "الْمُؤْمِنُ", tr: "Al-Mu'min", en: "The Guardian of Faith", desc: "The Grantor of security and affirmant of divine truth." },
      { n: 7, ar: "الْمُهَيْمِنُ", tr: "Al-Muhaymin", en: "The Protector / Overseer", desc: "The Ever-Watchful Protector who witnesses all deeds." },
      { n: 8, ar: "الْعَزِيزُ", tr: "Al-Aziz", en: "The All-Mighty", desc: "The Unconquerable and Invincible whom nothing can overcome." },
      { n: 9, ar: "الْجَبَّارُ", tr: "Al-Jabbar", en: "The Compeller / Restorer", desc: "The Irresistible Mender of everything that is broken." },
      { n: 10, ar: "الْمُتَكَبِّرُ", tr: "Al-Mutakabbir", en: "The Supreme / Majestic", desc: "The Dominant in majesty, greatness, and pride." },
      { n: 11, ar: "الْخَالِقُ", tr: "Al-Khaliq", en: "The Creator", desc: "The One who creates everything from non-existence." },
      { n: 12, ar: "الْبَارِئُ", tr: "Al-Bari'", en: "The Evolver / Maker", desc: "The Maker who brings creation into perfect harmony." },
      { n: 13, ar: "الْمُصَوِّرُ", tr: "Al-Musawwir", en: "The Fashioner of Forms", desc: "The Artist who shapes and colors every living being." },
      { n: 14, ar: "الْغَفَّارُ", tr: "Al-Ghaffar", en: "The Constant Forgiver", desc: "The Forgiver who repeatedly pardons sins." },
      { n: 15, ar: "الْقَهَّارُ", tr: "Al-Qahhar", en: "The Subduer / All-Dominant", desc: "The Conqueror who subdues all creation to His will." },
      { n: 16, ar: "الْوَهَّابُ", tr: "Al-Wahhab", en: "The Bestower", desc: "The Giver who showers unceasing gifts without reward." },
      { n: 17, ar: "الرَّزَّاقُ", tr: "Ar-Razzaq", en: "The Provider", desc: "The Sustainer who feeds every body and soul." },
      { n: 18, ar: "الْفَتَّاحُ", tr: "Al-Fattah", en: "The Opener / Reliever", desc: "The Opener of doors, ease, knowledge, and mercy." },
      { n: 19, ar: "الْعَلِيمُ", tr: "Al-Aleem", en: "The All-Knowing", desc: "The Omniscient who knows all hidden and manifest things." },
      { n: 20, ar: "الْقَابِضُ", tr: "Al-Qabid", en: "The Withholder", desc: "The One who constricts and withholds with wisdom." },
      { n: 21, ar: "الْبَاسِطُ", tr: "Al-Basit", en: "The Expander / Enricher", desc: "The One who expands life, peace, and provisions." },
      { n: 22, ar: "الْخَافِضُ", tr: "Al-Khafid", en: "The Abaser", desc: "The Humbler of the arrogant and tyrants." },
      { n: 23, ar: "الرَّافِعُ", tr: "Ar-Rafi'", en: "The Exalter", desc: "The Elevator of the faithful in honor and station." },
      { n: 24, ar: "الْمُعِزُّ", tr: "Al-Mu'izz", en: "The Giver of Honor", desc: "The Bestower of dignity and genuine glory." },
      { n: 25, ar: "الْمُذِلُّ", tr: "Al-Muzill", en: "The Giver of Disgrace", desc: "The Humbler of obstinate oppressors." },
      { n: 26, ar: "السَّمِيعُ", tr: "As-Sami'", en: "The All-Hearing", desc: "The Hearer of every prayer, whisper, and sigh." },
      { n: 27, ar: "الْبَصِيرُ", tr: "Al-Baseer", en: "The All-Seeing", desc: "The Observer of everything in heavens and earth." },
      { n: 28, ar: "الْحَكَمُ", tr: "Al-Hakam", en: "The Impartial Judge", desc: "The Supreme Arbiter whose decree cannot be turned back." },
      { n: 29, ar: "الْعَدْلُ", tr: "Al-Adl", en: "The Utterly Just", desc: "The Perfectly Just who never commits injustice." },
      { n: 30, ar: "اللَّطِيفُ", tr: "Al-Lateef", en: "The Subtle & Gentle", desc: "The Most Delicate whose kindness touches imperceptibly." },
      { n: 31, ar: "الْخَبِيرُ", tr: "Al-Khabeer", en: "The All-Aware", desc: "The Knower of the true essence of all things." },
      { n: 32, ar: "الْحَلِيمُ", tr: "Al-Haleem", en: "The Most Forbearing", desc: "The Clement One who is patient and does not hasten punishment." },
      { n: 33, ar: "الْعَظِيمُ", tr: "Al-Azeem", en: "The Magnificent", desc: "The Supreme in majesty beyond all comprehension." },
      { n: 34, ar: "الْغَفُورُ", tr: "Al-Ghafoor", en: "The Great Forgiver", desc: "The One who conceals faults and forgives perpetually." },
      { n: 35, ar: "الشَّكُورُ", tr: "Ash-Shakoor", en: "The Most Appreciative", desc: "The Grateful who rewards abundant bliss for small deeds." },
      { n: 36, ar: "الْعَلِيُّ", tr: "Al-Aliyy", en: "The Highest / Sublime", desc: "The Most High exalted above all comparison." },
      { n: 37, ar: "الْكَبِيرُ", tr: "Al-Kabeer", en: "The Greatest", desc: "The Immense whose grandeur has no end." },
      { n: 38, ar: "الْحَفِيظُ", tr: "Al-Hafeez", en: "The Preserver", desc: "The Guardian who shields and preserves all things." },
      { n: 39, ar: "الْمُقِيتُ", tr: "Al-Muqeet", en: "The Sustainer", desc: "The Maintainer who provides the exact sustenance needed." },
      { n: 40, ar: "الْحَسِيبُ", tr: "Al-Haseeb", en: "The Reckoner", desc: "The All-Sufficient who keeps exact count of all." },
      { n: 41, ar: "الْجَلِيلُ", tr: "Al-Jaleel", en: "The Majestic", desc: "The One possessed of sublime majesty and perfection." },
      { n: 42, ar: "الْكَرِيمُ", tr: "Al-Kareem", en: "The Most Bountiful", desc: "The Generous Giver whose bounty never depletes." },
      { n: 43, ar: "الرَّقِيبُ", tr: "Ar-Raqeeb", en: "The Watchful", desc: "The Ever-Observant from whom nothing escapes." },
      { n: 44, ar: "الْمُجِيبُ", tr: "Al-Mujeeb", en: "The Responsive", desc: "The Answerer of every earnest supplication." },
      { n: 45, ar: "الْوَاسِعُ", tr: "Al-Wasi'", en: "The All-Encompassing", desc: "The Boundless One whose mercy fills everything." },
      { n: 46, ar: "الْحَكِيمُ", tr: "Al-Hakeem", en: "The All-Wise", desc: "The Possessor of absolute wisdom in all decrees." },
      { n: 47, ar: "الْوَدُودُ", tr: "Al-Wadood", en: "The Most Loving", desc: "The Tender Lover who loves the righteous." },
      { n: 48, ar: "الْمَجِيدُ", tr: "Al-Majeed", en: "The Glorious", desc: "The Noble One of supreme glory and honor." },
      { n: 49, ar: "الْبَاعِثُ", tr: "Al-Ba'ith", en: "The Resurrector", desc: "The Raiser of the dead on the Last Day." },
      { n: 50, ar: "الشَّهِيدُ", tr: "Ash-Shaheed", en: "The Witness", desc: "The Ever-Present Witness to every event." },
      { n: 51, ar: "الْحَقُّ", tr: "Al-Haqq", en: "The Absolute Truth", desc: "The Unchangeable Reality whose being is eternal." },
      { n: 52, ar: "الْوَكِيلُ", tr: "Al-Wakeel", en: "The Trustee", desc: "The Dependable Guardian in whom trust is placed." },
      { n: 53, ar: "الْقَوِيُّ", tr: "Al-Qawiyy", en: "The All-Strong", desc: "The Possessor of inexhaustible divine strength." },
      { n: 54, ar: "الْمَتِينُ", tr: "Al-Mateen", en: "The Firm / Steadfast", desc: "The Resolute whose power never weakens." },
      { n: 55, ar: "الْوَلِيُّ", tr: "Al-Waliyy", en: "The Protecting Friend", desc: "The Guardian Ally and Helper of the believers." },
      { n: 56, ar: "الْحَمِيدُ", tr: "Al-Hameed", en: "The Praiseworthy", desc: "The One who alone is worthy of all gratitude." },
      { n: 57, ar: "الْمُحْصِي", tr: "Al-Muhsee", en: "The Accounter", desc: "The One who calculates and records every atom." },
      { n: 58, ar: "الْمُبْدِئُ", tr: "Al-Mubdi'", en: "The Originator", desc: "The Initiator who brings forth creation." },
      { n: 59, ar: "الْمُعِيدُ", tr: "Al-Mu'eed", en: "The Restorer", desc: "The One who repeats and restores creation." },
      { n: 60, ar: "الْمُحْيِي", tr: "Al-Muhyee", en: "The Giver of Life", desc: "The Bestower of life to inanimate earth." },
      { n: 61, ar: "الْمُمِيتُ", tr: "Al-Mumeet", en: "The Creator of Death", desc: "The Decreer of death to all who live." },
      { n: 62, ar: "الْحَيُّ", tr: "Al-Hayy", en: "The Ever-Living", desc: "The Eternally Living who neither tires nor sleeps." },
      { n: 63, ar: "الْقَيُّومُ", tr: "Al-Qayyum", en: "The Self-Subsisting", desc: "The Sustainer on whom all creation depends." },
      { n: 64, ar: "الْوَاجِدُ", tr: "Al-Wajid", en: "The Perceiver / Resourceful", desc: "The One who lacks nothing and attains all." },
      { n: 65, ar: "الْمَاجِدُ", tr: "Al-Majid", en: "The Illustrious", desc: "The Noble One of supreme majesty." },
      { n: 66, ar: "الْوَاحِدُ", tr: "Al-Wahid", en: "The Unique / One", desc: "The Singular One who has no partner." },
      { n: 67, ar: "الأَحَدُ", tr: "Al-Ahad", en: "The Indivisible One", desc: "The Absolute One beyond composition." },
      { n: 68, ar: "الصَّمَدُ", tr: "As-Samad", en: "The Eternal Refuge", desc: "The Independent upon whom all depend." },
      { n: 69, ar: "الْقَادِرُ", tr: "Al-Qadir", en: "The Capable / Omnipotent", desc: "The Omnipotent who has power over all things." },
      { n: 70, ar: "الْمُقْتَدِرُ", tr: "Al-Muqtadir", en: "The Supreme Determiner", desc: "The Master of all power and determination." },
      { n: 71, ar: "الْمُقَدِّمُ", tr: "Al-Muqaddim", en: "The Expediter", desc: "The One who brings forward what He wills." },
      { n: 72, ar: "الْمُؤَخِّرُ", tr: "Al-Mu'akhkhir", en: "The Delayer", desc: "The One who defers what He wills with wisdom." },
      { n: 73, ar: "الأَوَّلُ", tr: "Al-Awwal", en: "The First", desc: "The First with no beginning." },
      { n: 74, ar: "الآخِرُ", tr: "Al-Akhir", en: "The Last", desc: "The Everlasting after whom none remains." },
      { n: 75, ar: "الظَّاهِرُ", tr: "Az-Zahir", en: "The Manifest", desc: "The Evident whose signs encompass creation." },
      { n: 76, ar: "الْبَاطِنُ", tr: "Al-Batin", en: "The Hidden", desc: "The Unseen whom physical eyes cannot comprehend." },
      { n: 77, ar: "الْوَالِي", tr: "Al-Waali", en: "The Sole Governor", desc: "The Supreme Ruler and Manager of the universe." },
      { n: 78, ar: "الْمُتَعَالِي", tr: "Al-Muta'ali", en: "The Self Exalted", desc: "The Most High, elevated above all defects." },
      { n: 79, ar: "الْبَرُّ", tr: "Al-Barr", en: "The Source of Goodness", desc: "The Generous Benefactor to all servants." },
      { n: 80, ar: "التَّوَّابُ", tr: "At-Tawwab", en: "The Ever-Pardoning", desc: "The Acceptor of sincere repentance." },
      { n: 81, ar: "الْمُنْتَقِمُ", tr: "Al-Muntaqim", en: "The Just Retributor", desc: "The Recompenser of stubborn tyrants." },
      { n: 82, ar: "العَفُوُّ", tr: "Al-Afuww", en: "The Supreme Pardoner", desc: "The Eraser of sins and misdeeds." },
      { n: 83, ar: "الرَّؤُوفُ", tr: "Ar-Ra'oof", en: "The Most Compassionate", desc: "The Clement One filled with gentle pity." },
      { n: 84, ar: "مَالِكُ الْمُلْكِ", tr: "Malik-ul-Mulk", en: "Owner of All Sovereignty", desc: "The Lord of absolute eternal dominion." },
      { n: 85, ar: "ذُو الْجَلَالِ وَالإِكْرَامِ", tr: "Zul-Jalali wal-Ikram", en: "Lord of Majesty and Bounty", desc: "The Possessor of supreme grandeur and grace." },
      { n: 86, ar: "الْمُقْسِطُ", tr: "Al-Muqsit", en: "The Equitable", desc: "The One who dispenses perfect justice." },
      { n: 87, ar: "الْجَامِعُ", tr: "Al-Jami'", en: "The Gatherer", desc: "The Gatherer of humanity on the Day of Judgment." },
      { n: 88, ar: "الْغَنِيُّ", tr: "Al-Ghaniyy", en: "The Self-Sufficient", desc: "The Rich One free of need from any creation." },
      { n: 89, ar: "الْمُغْنِي", tr: "Al-Mughni", en: "The Enricher", desc: "The Enricher who satisfies the needs of all." },
      { n: 90, ar: "الْمَانِعُ", tr: "Al-Mani'", en: "The Withholder / Protector", desc: "The Shield who prevents harm according to wisdom." },
      { n: 91, ar: "الضَّارُّ", tr: "Ad-Darr", en: "The Creator of Trial", desc: "The One by whose decree adversity touches." },
      { n: 92, ar: "النَّافِعُ", tr: "An-Nafi'", en: "The Creator of Good", desc: "The Giver of all blessing and benefit." },
      { n: 93, ar: "النُّورُ", tr: "An-Noor", en: "The Illuminating Light", desc: "The Light of heavens, earth, and pure hearts." },
      { n: 94, ar: "الْهَادِي", tr: "Al-Hadi", en: "The Infallible Guide", desc: "The Guide who leads hearts to truth." },
      { n: 95, ar: "الْبَدِيعُ", tr: "Al-Badee'", en: "The Incomparable Originator", desc: "The Creator without model or precedent." },
      { n: 96, ar: "الْبَاقِي", tr: "Al-Baqi", en: "The Everlasting", desc: "The Immortal whose being never ends." },
      { n: 97, ar: "الْوَارِثُ", tr: "Al-Warith", en: "The Supreme Inheritor", desc: "The Ultimate Heir to all kingdoms." },
      { n: 98, ar: "الرَّشِيدُ", tr: "Ar-Rasheed", en: "The Righteous Director", desc: "The Infallible Conductor of all affairs." },
      { n: 99, ar: "الصَّبُورُ", tr: "As-Saboor", en: "The Most Patient", desc: "The Patient One who does not hurry to penalize." }
    ];

    const namesOfProphetData = [
  {
    "n": 1,
    "ar": "مُحَمَّدٌ",
    "tr": "Muhammad",
    "en": "The Praised One",
    "desc": "Praised continuously and abundantly by creation and Creator."
  },
  {
    "n": 2,
    "ar": "أَحْمَدُ",
    "tr": "Ahmad",
    "en": "The Most Commended",
    "desc": "He who praises Allah more than any other created being."
  },
  {
    "n": 3,
    "ar": "حَامِدٌ",
    "tr": "Hamid",
    "en": "The Praiser",
    "desc": "The devoted praiser and glorifier of Almighty Allah."
  },
  {
    "n": 4,
    "ar": "مَحْمُودٌ",
    "tr": "Mahmud",
    "en": "The Highly Praised",
    "desc": "Granted the Praiseworthy Station (Al-Maqam al-Mahmud)."
  },
  {
    "n": 5,
    "ar": "قَاسِمٌ",
    "tr": "Qasim",
    "en": "The Distributor",
    "desc": "Distributor of Allah's divine blessings and gifts to mankind."
  },
  {
    "n": 6,
    "ar": "عَاقِبٌ",
    "tr": "Al-Aqib",
    "en": "The Successor & Seal",
    "desc": "The Last Prophet after whom there shall be no prophet."
  },
  {
    "n": 7,
    "ar": "فَاتِحٌ",
    "tr": "Al-Fatih",
    "en": "The Opener of Truth",
    "desc": "Opener of closed hearts, divine truth, and spiritual wisdom."
  },
  {
    "n": 8,
    "ar": "خَاتِمٌ",
    "tr": "Al-Khatim",
    "en": "The Seal of Prophethood",
    "desc": "The final seal of all divine messengers (33:40)."
  },
  {
    "n": 9,
    "ar": "حَاشِرٌ",
    "tr": "Al-Hashir",
    "en": "The Gatherer",
    "desc": "At whose feet mankind will be gathered on Judgment Day."
  },
  {
    "n": 10,
    "ar": "مَاحِي",
    "tr": "Al-Mahi",
    "en": "The Eraser of Disbelief",
    "desc": "Through whom Allah erases polytheism and darkness."
  },
  {
    "n": 11,
    "ar": "دَاعٍ",
    "tr": "Ad-Da'i",
    "en": "The Caller to Allah",
    "desc": "The invited caller to Allah by His permission (33:46)."
  },
  {
    "n": 12,
    "ar": "شَاهِدٌ",
    "tr": "Shahid",
    "en": "The Witness",
    "desc": "A witness over his Ummah and all previous nations."
  },
  {
    "n": 13,
    "ar": "نَذِيرٌ",
    "tr": "Nadheer",
    "en": "The Warner",
    "desc": "A loving warner against error and spiritual destruction."
  },
  {
    "n": 14,
    "ar": "بَشِيرٌ",
    "tr": "Basheer",
    "en": "The Bearer of Glad Tidings",
    "desc": "Giver of good news of Paradise and divine mercy."
  },
  {
    "n": 15,
    "ar": "مُنْذِرٌ",
    "tr": "Mundhir",
    "en": "The Admonisher",
    "desc": "Admonisher guiding souls to righteous conduct."
  },
  {
    "n": 16,
    "ar": "نُورٌ",
    "tr": "Noor",
    "en": "The Illuminating Light",
    "desc": "A radiant light revealed to guide all nations (5:15)."
  },
  {
    "n": 17,
    "ar": "سِرَاجٌ",
    "tr": "Siraj",
    "en": "The Bright Torch",
    "desc": "A luminous lamp dispersing ignorance and darkness."
  },
  {
    "n": 18,
    "ar": "مِصْبَاحٌ",
    "tr": "Misbah",
    "en": "The Radiant Lantern",
    "desc": "The lantern of hearts and prophetic illumination."
  },
  {
    "n": 19,
    "ar": "هُدًى",
    "tr": "Huda",
    "en": "The Embodiment of Guidance",
    "desc": "The walking guide to the straight path of Allah."
  },
  {
    "n": 20,
    "ar": "مَهْدِيٌّ",
    "tr": "Mahdiyy",
    "en": "The Divinely Guided",
    "desc": "Divinely preserved and guided in every deed and word."
  },
  {
    "n": 21,
    "ar": "مُنِيرٌ",
    "tr": "Muneer",
    "en": "The Radiant Luminary",
    "desc": "The luminous lamp described in Surah Al-Ahzab (33:46)."
  },
  {
    "n": 22,
    "ar": "صَادِقٌ",
    "tr": "Sadiq",
    "en": "The Truthful",
    "desc": "Renowned from youth as the completely truthful one."
  },
  {
    "n": 23,
    "ar": "أَمِينٌ",
    "tr": "Al-Amin",
    "en": "The Trustworthy",
    "desc": "The title bestowed upon him by all of Mecca for absolute honesty."
  },
  {
    "n": 24,
    "ar": "مَأْمُونٌ",
    "tr": "Ma'moon",
    "en": "The Trusted Custodian",
    "desc": "Trusted with the ultimate divine revelation for creation."
  },
  {
    "n": 25,
    "ar": "كَرِيمٌ",
    "tr": "Kareem",
    "en": "The Noble & Generous",
    "desc": "The most generous of all people in character and giving."
  },
  {
    "n": 26,
    "ar": "مُكَرَّمٌ",
    "tr": "Mukarram",
    "en": "The Honored One",
    "desc": "Honored and elevated in rank in the heavens and earth."
  },
  {
    "n": 27,
    "ar": "مَكِينٌ",
    "tr": "Makeen",
    "en": "The Firmly Established",
    "desc": "Given an unshakable noble rank with the Lord of the Throne."
  },
  {
    "n": 28,
    "ar": "مَتِينٌ",
    "tr": "Mateen",
    "en": "The Steadfast & Strong",
    "desc": "Steadfast and resilient in delivering truth under hardship."
  },
  {
    "n": 29,
    "ar": "مُبِينٌ",
    "tr": "Mubeen",
    "en": "The Clear Clarifier",
    "desc": "Making the divine law and moral righteousness crystal clear."
  },
  {
    "n": 30,
    "ar": "مُؤَمِّلٌ",
    "tr": "Mu'ammil",
    "en": "The Hoped For",
    "desc": "In whose intercession and mercy the believers place hope."
  },
  {
    "n": 31,
    "ar": "وَصُولٌ",
    "tr": "Wasool",
    "en": "The Maintainer of Ties",
    "desc": "The master of upholding family kinship and spiritual bonds."
  },
  {
    "n": 32,
    "ar": "ذُو قُوَّةٍ",
    "tr": "Dhu Quwwah",
    "en": "Possessor of Strength",
    "desc": "Possessing divine moral, spiritual, and righteous fortitude."
  },
  {
    "n": 33,
    "ar": "ذُو حُرْمَةٍ",
    "tr": "Dhu Hurmah",
    "en": "Possessor of Sanctity",
    "desc": "He whose person, words, and station are sacred."
  },
  {
    "n": 34,
    "ar": "ذُو مَكَانَةٍ",
    "tr": "Dhu Makanah",
    "en": "Possessor of High Rank",
    "desc": "Possessing the highest station among all created beings."
  },
  {
    "n": 35,
    "ar": "ذُو عِزٍّ",
    "tr": "Dhu 'Izz",
    "en": "Possessor of Might",
    "desc": "Elevated with divine honor and true spiritual dignity."
  },
  {
    "n": 36,
    "ar": "ذُو فَضْلٍ",
    "tr": "Dhu Fadl",
    "en": "Possessor of Grace",
    "desc": "Bestowed with supreme grace and blessings from Allah."
  },
  {
    "n": 37,
    "ar": "مُطَاعٌ",
    "tr": "Muta'",
    "en": "The Obeyed Leader",
    "desc": "Whose obedience is tied directly to obedience to Allah (4:80)."
  },
  {
    "n": 38,
    "ar": "مُطِيعٌ",
    "tr": "Mutee'",
    "en": "The Devoutly Obedient",
    "desc": "The most humble, devoted servant and worshipper of Allah."
  },
  {
    "n": 39,
    "ar": "قَدَمُ صِدْقٍ",
    "tr": "Qadamu Sidq",
    "en": "The Footing of Truth",
    "desc": "The vanguard of steadfast faith and divine truth."
  },
  {
    "n": 40,
    "ar": "رَحْمَةٌ",
    "tr": "Rahmah",
    "en": "Mercy Personified",
    "desc": "\"And We have not sent you except as a mercy to the worlds\" (21:107)."
  },
  {
    "n": 41,
    "ar": "بُشْرَى",
    "tr": "Bushra",
    "en": "The Glad Tiding",
    "desc": "The glad tiding foretold by Jesus (Isa) peace be upon him (61:6)."
  },
  {
    "n": 42,
    "ar": "غَوْثٌ",
    "tr": "Ghawth",
    "en": "The Succor & Refuge",
    "desc": "A spiritual refuge and source of relief for the distressed."
  },
  {
    "n": 43,
    "ar": "غِيَاثٌ",
    "tr": "Ghiyath",
    "en": "The Rescuer",
    "desc": "Rescuing souls from spiritual ruin and error."
  },
  {
    "n": 44,
    "ar": "غَيْثٌ",
    "tr": "Ghayth",
    "en": "The Beneficial Rain",
    "desc": "Whose message revives dead spiritual hearts like spring rain."
  },
  {
    "n": 45,
    "ar": "نِعْمَةٌ",
    "tr": "Ni'mah",
    "en": "The Divine Blessing",
    "desc": "The greatest blessing and favor granted by Allah to mankind."
  },
  {
    "n": 46,
    "ar": "هَدِيَّةٌ",
    "tr": "Hadiyyah",
    "en": "The Divine Gift",
    "desc": "\"I am but a gifted mercy\" (Prophetic Hadith)."
  },
  {
    "n": 47,
    "ar": "عُرْوَةٌ وُثْقَى",
    "tr": "Urwah Wuthqa",
    "en": "The Firmest Handhold",
    "desc": "Holding fast to his Sunnah is clutching the unbreakable bond."
  },
  {
    "n": 48,
    "ar": "صِرَاطٌ مُسْتَقِيمٌ",
    "tr": "Sirat Mustaqeem",
    "en": "The Straight Path",
    "desc": "The embodiment and caller to the eternal straight way."
  },
  {
    "n": 49,
    "ar": "ذِكْرُ اللَّهِ",
    "tr": "Dhikrullah",
    "en": "Remembrance of Allah",
    "desc": "Constantly immersed in the glorification and mention of Allah."
  },
  {
    "n": 50,
    "ar": "حِزْبُ اللَّهِ",
    "tr": "Hizbullah",
    "en": "Party of Allah",
    "desc": "Leader of the victorious righteous party of Allah."
  },
  {
    "n": 51,
    "ar": "نَجْمٌ ثَاقِبٌ",
    "tr": "Najm Thaqib",
    "en": "The Piercing Star",
    "desc": "Whose radiant guidance pierces through deep falsehood."
  },
  {
    "n": 52,
    "ar": "مُصْطَفَى",
    "tr": "Al-Mustafa",
    "en": "The Chosen One",
    "desc": "Handpicked by the Creator from among all humanity."
  },
  {
    "n": 53,
    "ar": "مُجْتَبَى",
    "tr": "Al-Mujtaba",
    "en": "The Selected",
    "desc": "Selected for the final covenant and supreme message."
  },
  {
    "n": 54,
    "ar": "مُرْتَضَى",
    "tr": "Al-Murtada",
    "en": "The Well-Pleasing",
    "desc": "Whose character is completely pleasing to Allah the Almighty."
  },
  {
    "n": 55,
    "ar": "أُمِّيٌّ",
    "tr": "Al-Ummiyy",
    "en": "The Unlettered Prophet",
    "desc": "Taught directly by divine revelation, not human books (7:157)."
  },
  {
    "n": 56,
    "ar": "مُخْتَارٌ",
    "tr": "Al-Mukhtar",
    "en": "The Preferred",
    "desc": "Chosen above all creation as leader of the prophets."
  },
  {
    "n": 57,
    "ar": "أَجِيرٌ",
    "tr": "Ajeer",
    "en": "The Sincere Worker",
    "desc": "Devoting his entire existence solely for Allah's pleasure."
  },
  {
    "n": 58,
    "ar": "جَبَّارٌ",
    "tr": "Jabbar",
    "en": "The Restorer of Broken",
    "desc": "He who mends broken hearts through faith and love."
  },
  {
    "n": 59,
    "ar": "أَبُو الْقَاسِمِ",
    "tr": "Abu al-Qasim",
    "en": "Father of Qasim",
    "desc": "His beloved kunya (honorific title) chosen by Allah."
  },
  {
    "n": 60,
    "ar": "أَبُو الطَّاهِرِ",
    "tr": "Abu at-Tahir",
    "en": "Father of the Pure",
    "desc": "Father of pure sons and embodiment of purity."
  },
  {
    "n": 61,
    "ar": "أَبُو الطَّيِّبِ",
    "tr": "Abu at-Tayyib",
    "en": "Father of the Good",
    "desc": "Father of good offspring and wholesome virtue."
  },
  {
    "n": 62,
    "ar": "أَبُو إِبْرَاهِيمَ",
    "tr": "Abu Ibrahim",
    "en": "Father of Ibrahim",
    "desc": "Father of Ibrahim and spiritual heir to Prophet Ibrahim."
  },
  {
    "n": 63,
    "ar": "مُشَفَّعٌ",
    "tr": "Mushaffa'",
    "en": "The Accepted Intercessor",
    "desc": "Granted the divine guarantee that his intercession is accepted."
  },
  {
    "n": 64,
    "ar": "شَفِيعٌ",
    "tr": "Shafi'",
    "en": "The Great Intercessor",
    "desc": "The primary intercessor for all humanity on Judgment Day."
  },
  {
    "n": 65,
    "ar": "صَالِحٌ",
    "tr": "Salih",
    "en": "The Righteous",
    "desc": "The pinnacle of righteousness, piety, and virtue."
  },
  {
    "n": 66,
    "ar": "مُصْلِحٌ",
    "tr": "Muslih",
    "en": "The Peacemaker & Reformer",
    "desc": "Reformed humanity from tribal jahiliyyah into brotherly justice."
  },
  {
    "n": 67,
    "ar": "مُهَيْمِنٌ",
    "tr": "Muhaymin",
    "en": "The Guardian of Truth",
    "desc": "Guardian over previous revelations, confirming their truth."
  },
  {
    "n": 68,
    "ar": "صَادِقُ الْوَعْدِ",
    "tr": "Sadiq al-Wa'd",
    "en": "True to His Promise",
    "desc": "Never broke a treaty, pact, or promise in his lifetime."
  },
  {
    "n": 69,
    "ar": "مُحْرِمٌ",
    "tr": "Muhrim",
    "en": "In Sacred Consecration",
    "desc": "Eternally sanctified in the worship and service of Allah."
  },
  {
    "n": 70,
    "ar": "كَافٍ",
    "tr": "Kafi",
    "en": "The Sufficient Example",
    "desc": "\"You have indeed in the Messenger of Allah a beautiful pattern\" (33:21)."
  },
  {
    "n": 71,
    "ar": "شَافٍ",
    "tr": "Shafi",
    "en": "The Healer of Spiritual Ills",
    "desc": "His teachings heal souls of arrogance, hatred, and doubt."
  },
  {
    "n": 72,
    "ar": "وَاصِلٌ",
    "tr": "Wasil",
    "en": "The Uniter of People",
    "desc": "United diverse races, tribes, and nations in pure brotherhood."
  },
  {
    "n": 73,
    "ar": "بَارٌّ",
    "tr": "Barr",
    "en": "The Dutiful & Kind",
    "desc": "The pinnacle of filial piety, kindness, and affection."
  },
  {
    "n": 74,
    "ar": "سَابِقٌ",
    "tr": "Sabiq",
    "en": "The Foremost in Good",
    "desc": "Always the first to lead in prayer, charity, and sacrifice."
  },
  {
    "n": 75,
    "ar": "سَائِقٌ",
    "tr": "Sa'iq",
    "en": "The Guide to Paradise",
    "desc": "Leading his followers safely to the gardens of eternal peace."
  },
  {
    "n": 76,
    "ar": "هَادٍ",
    "tr": "Hadi",
    "en": "The Guide to Truth",
    "desc": "\"And indeed, you guide to a straight path\" (42:52)."
  },
  {
    "n": 77,
    "ar": "مُهْتَدٍ",
    "tr": "Muhtadi",
    "en": "The True Follower of Light",
    "desc": "Following the light revealed to him with perfect fidelity."
  },
  {
    "n": 78,
    "ar": "فَرِيدٌ",
    "tr": "Fareed",
    "en": "The Incomparable",
    "desc": "Unmatched in moral perfection and prophetic stature."
  },
  {
    "n": 79,
    "ar": "نَبِيُّ الرَّحْمَةِ",
    "tr": "Nabiyy ar-Rahmah",
    "en": "Prophet of Mercy",
    "desc": "Sent with unconditional compasssion even for his enemies."
  },
  {
    "n": 80,
    "ar": "نَبِيُّ التَّوْبَةِ",
    "tr": "Nabiyy at-Tawbah",
    "en": "Prophet of Repentance",
    "desc": "Showing humanity the path of return to divine forgiveness."
  },
  {
    "n": 81,
    "ar": "نَبِيُّ الْمَلَاحِمِ",
    "tr": "Nabiyy al-Malahim",
    "en": "Prophet of Great Stand",
    "desc": "Steadfast defender of righteousness against tyranny."
  },
  {
    "n": 82,
    "ar": "نَبِيُّ الْحَرَمَيْنِ",
    "tr": "Nabiyy al-Haramayn",
    "en": "Prophet of the Two Sanctuaries",
    "desc": "Associated eternally with Makkah al-Mukarramah and Madinah al-Munawwarah."
  },
  {
    "n": 83,
    "ar": "قَائِمٌ",
    "tr": "Qa'im",
    "en": "The Steadfast Worshipper",
    "desc": "Standing long hours in nightly Tahajjud until his feet swelled."
  },
  {
    "n": 84,
    "ar": "جَامِعٌ",
    "tr": "Jami'",
    "en": "The Master of Concise Speech",
    "desc": "Blessed with comprehensive speech (Jawami' al-Kalim)."
  },
  {
    "n": 85,
    "ar": "مُقْتَفٍ",
    "tr": "Muqtafi",
    "en": "Follower of All Prophets",
    "desc": "Continuing and crowning the legacy of Adam, Noah, Abraham, and Moses."
  },
  {
    "n": 86,
    "ar": "رَسُولُ الرَّاحَةِ",
    "tr": "Rasool ar-Rahah",
    "en": "Messenger of Tranquility",
    "desc": "Brought ease and removed burdensome religious chains (7:157)."
  },
  {
    "n": 87,
    "ar": "كَامِلٌ",
    "tr": "Kamil",
    "en": "The Perfect in Character",
    "desc": "\"And indeed, you are of a great moral character\" (68:4)."
  },
  {
    "n": 88,
    "ar": "إِكْلِيلٌ",
    "tr": "Ikleel",
    "en": "The Crown of Creation",
    "desc": "The glorious crown of the prophetic brotherhood."
  },
  {
    "n": 89,
    "ar": "مُدَّثِّرٌ",
    "tr": "Al-Muddath-thir",
    "en": "The Enveloped One",
    "desc": "Addressed with divine tenderness in Surah 74."
  },
  {
    "n": 90,
    "ar": "مُزَّمِّلٌ",
    "tr": "Al-Muzzammil",
    "en": "The Enfolded One",
    "desc": "Addressed lovingly by Allah in Surah 73."
  },
  {
    "n": 91,
    "ar": "عَبْدُ اللَّهِ",
    "tr": "Abdullah",
    "en": "The True Servant of Allah",
    "desc": "The highest title of spiritual intimacy granted during the Mi'raj (17:1)."
  },
  {
    "n": 92,
    "ar": "حَبِيبُ اللَّهِ",
    "tr": "Habibullah",
    "en": "The Beloved of Allah",
    "desc": "The specially cherished intimate friend of the Lord of creation."
  },
  {
    "n": 93,
    "ar": "صَفِيُّ اللَّهِ",
    "tr": "Safiyyullah",
    "en": "The Chosen Friend of Allah",
    "desc": "Purified and selected for divine closeness and honor."
  },
  {
    "n": 94,
    "ar": "نَجِيُّ اللَّهِ",
    "tr": "Najiyyullah",
    "en": "The Confidant of Allah",
    "desc": "Spoken to intimately in the highest realms beyond Sidrat al-Muntaha."
  },
  {
    "n": 95,
    "ar": "كَلِيمُ اللَّهِ",
    "tr": "Kaleemullah",
    "en": "Spoken to by Allah",
    "desc": "Addressed directly by his Lord without intermediary during the Ascension."
  },
  {
    "n": 96,
    "ar": "خَاتَمُ الرُّسُلِ",
    "tr": "Khatam ar-Rusul",
    "en": "Seal of the Messengers",
    "desc": "The final envoy of divine guidance to mortal earth."
  },
  {
    "n": 97,
    "ar": "مُحْيِي",
    "tr": "Muhyi",
    "en": "The Reviver of Hearts",
    "desc": "Reviving human souls through the eternal Quranic truth."
  },
  {
    "n": 98,
    "ar": "مُنَجٍّ",
    "tr": "Munajji",
    "en": "The Deliverer",
    "desc": "A means of deliverance from the hellfire and spiritual ruin."
  },
  {
    "n": 99,
    "ar": "رَؤُوفٌ رَحِيمٌ",
    "tr": "Ra'oofun Raheem",
    "en": "Compassionate & Merciful",
    "desc": "Described with deep tenderness in Surah At-Tawbah (9:128)."
  }
];

    let currentNamesTab = 'allah';

    function openNamesModal(tab = 'allah') {
      playClickSound();
      switchNamesTab(tab);
      const modal = document.getElementById("namesOfAllahModal");
      if (modal) modal.classList.remove("hidden");
    }

    function openNamesOfAllahModal() {
      openNamesModal('allah');
    }

    function closeNamesOfAllahModal() {
      playClickSound();
      const modal = document.getElementById("namesOfAllahModal");
      if (modal) modal.classList.add("hidden");
    }

    function switchNamesTab(tab) {
      playClickSound();
      currentNamesTab = tab;
      const btnAllah = document.getElementById("tabBtnNamesAllah");
      const btnProphet = document.getElementById("tabBtnNamesProphet");
      const modalIcon = document.getElementById("namesModalIcon");
      const modalTitle = document.getElementById("namesModalTitle");
      const modalSubtitle = document.getElementById("namesModalSubtitle");
      const searchInput = document.getElementById("namesSearchInput");

      if (tab === 'allah') {
        if (btnAllah) btnAllah.className = "py-1.5 rounded-lg bg-emerald-800 text-white font-bold transition flex items-center justify-center gap-1 shadow-xs";
        if (btnProphet) btnProphet.className = "py-1.5 rounded-lg text-slate-600 dark:text-slate-300 font-semibold transition flex items-center justify-center gap-1 hover:text-slate-900 dark:hover:text-white";
        if (modalIcon) {
          modalIcon.innerText = "الله";
          modalIcon.className = "w-7 h-7 rounded-lg bg-gold-500/15 border border-gold-500/30 text-gold-700 dark:text-gold-400 flex items-center justify-center flex-shrink-0 font-bold font-arabic text-xs";
        }
        if (modalTitle) modalTitle.innerHTML = `99 Names of Allah <span class="font-arabic text-sm text-gold-500 font-normal">أسماء الله الحسنى</span>`;
        if (modalSubtitle) modalSubtitle.innerText = `"To Allah belong the best names, so call upon Him by them" (7:180)`;
        if (searchInput) searchInput.placeholder = "Search Allah's 99 names (e.g. 1, Rahman, Peace)...";
      } else {
        if (btnAllah) btnAllah.className = "py-1.5 rounded-lg text-slate-600 dark:text-slate-300 font-semibold transition flex items-center justify-center gap-1 hover:text-slate-900 dark:hover:text-white";
        if (btnProphet) btnProphet.className = "py-1.5 rounded-lg bg-emerald-800 text-white font-bold transition flex items-center justify-center gap-1 shadow-xs";
        if (modalIcon) {
          modalIcon.innerText = "محمد";
          modalIcon.className = "w-7 h-7 rounded-lg bg-emerald-500/15 border border-emerald-500/30 text-emerald-700 dark:text-emerald-400 flex items-center justify-center flex-shrink-0 font-bold font-arabic text-xs";
        }
        if (modalTitle) modalTitle.innerHTML = `99 Names of Muhammad ﷺ <span class="font-arabic text-sm text-emerald-500 font-normal">أسماء النبي الكريم</span>`;
        if (modalSubtitle) modalSubtitle.innerText = `"And indeed, you are of a great moral character" (68:4)`;
        if (searchInput) searchInput.placeholder = "Search Prophet's names (e.g. Mustafa, Amin, Mercy)...";
      }

      const searchVal = searchInput ? searchInput.value : '';
      renderActiveNames(searchVal);
    }

    function filterActiveNames(val) {
      renderActiveNames(val);
    }

    function filterNamesOfAllah(val) {
      filterActiveNames(val);
    }

    function renderActiveNames(filter = '') {
      const container = document.getElementById("namesCardsContainer");
      if (!container) return;
      container.innerHTML = "";

      const qRaw = filter.trim().toLowerCase();
      const isBroadSearch = !qRaw || ["allah", "prophet", "all", "all 99", "99", "names", "asma", "muhammad", "god", "الله", "محمد"].includes(qRaw);
      const qArClean = typeof cleanArText === 'function' ? cleanArText(qRaw) : qRaw.replace(/[\u064B-\u065F\u0670]/g, '');
      const qEnClean = typeof cleanEnText === 'function' ? cleanEnText(qRaw) : qRaw.replace(/[-'\s]/g, '');

      const activeDataSet = currentNamesTab === 'allah' ? namesOfAllahData : namesOfProphetData;

      const filtered = activeDataSet.filter(item => {
        if (isBroadSearch) return true;
        if (String(item.n) === qRaw) return true;
        if (item.tr.toLowerCase().includes(qRaw) || (typeof cleanEnText === 'function' && cleanEnText(item.tr).includes(qEnClean))) return true;
        if (item.en.toLowerCase().includes(qRaw) || item.desc.toLowerCase().includes(qRaw)) return true;
        const itemArClean = typeof cleanArText === 'function' ? cleanArText(item.ar) : item.ar.replace(/[\u064B-\u065F\u0670]/g, '');
        if (item.ar.includes(qRaw) || itemArClean.includes(qArClean)) return true;
        return false;
      });

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="p-6 text-center text-slate-400 text-xs">
            No names match "${filter}". Try searching by number, English meaning, or Arabic name.
          </div>
        `;
        return;
      }

      const isProphet = currentNamesTab === 'prophet';
      filtered.forEach(item => {
        const card = document.createElement("div");
        card.className = "p-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200/80 dark:border-slate-700/80 hover:border-gold-500/50 shadow-xs flex items-center justify-between gap-2.5 transition active:scale-98";
        card.innerHTML = `
          <div class="flex items-center gap-2.5 min-w-0">
            <span class="w-6 h-6 rounded-lg ${isProphet ? 'bg-emerald-100 dark:bg-emerald-950/60 border border-emerald-300 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300' : 'bg-gold-500/15 border border-gold-500/30 text-gold-700 dark:text-gold-400'} text-[10px] font-bold flex items-center justify-center flex-shrink-0">
              ${item.n}
            </span>
            <div class="min-w-0">
              <div class="flex items-baseline gap-1.5">
                <span class="text-xs font-bold text-slate-800 dark:text-white">${item.tr} ${isProphet ? '<span class="text-[9px] text-emerald-600 font-arabic font-normal">ﷺ</span>' : ''}</span>
              </div>
              <p class="text-[11px] font-medium text-slate-600 dark:text-slate-300 truncate">${item.en}</p>
              <p class="text-[9px] text-slate-400 line-clamp-1">${item.desc}</p>
            </div>
          </div>
          <div class="flex flex-col items-end flex-shrink-0">
            <span class="notranslate font-arabic text-xl font-bold ${isProphet ? 'text-emerald-950 dark:text-emerald-300' : 'text-emerald-950 dark:text-gold-400'}" translate="no" lang="ar" dir="rtl">${item.ar}</span>
            <button onclick="copyNameItem('${isProphet ? 'prophet' : 'allah'}', ${item.n})" class="text-[9px] font-semibold text-slate-400 hover:text-emerald-600 flex items-center gap-0.5 mt-0.5 transition">
              <i data-lucide="copy" class="w-2.5 h-2.5"></i> Copy
            </button>
          </div>
        `;
        container.appendChild(card);
      });
      lucide.createIcons();
    }

    function copyNameItem(type, num) {
      playClickSound();
      const list = type === 'prophet' ? namesOfProphetData : namesOfAllahData;
      const item = list.find(x => x.n === num);
      if (!item) return;
      const text = `${item.n}. ${item.ar} (${item.tr}${type === 'prophet' ? ' ﷺ' : ''}) - ${item.en}: "${item.desc}"`;
      if (navigator.clipboard) {
        navigator.clipboard.writeText(text);
        showToast("Copied to Clipboard", `${item.tr} (${item.ar})`);
      }
    }

    function copyAllahName(num) {
      copyNameItem('allah', num);
    }


    // ==========================================
    // ISLAMIC HIJRI CALENDAR & FASTING ENGINE (FULL MONTHLY GRID)
    // ==========================================
    const hijriMonthsData = [
      {
        id: "ramadan1447",
        name: "Ramadan 1447",
        nameAr: "رَمَضَان",
        year: 1447,
        monthNumber: 9,
        gregorianSubtitle: "Feb 18 – Mar 19, 2026",
        daysCount: 30,
        startDayOfWeek: 3, // Wednesday
        startDateGregorian: new Date(2026, 1, 18),
        specialDays: {
          1: { name: "1st Ramadan (First Fast)", type: "major" },
          27: { name: "Laylat al-Qadr", type: "major" }
        }
      },
      {
        id: "shawwal1447",
        name: "Shawwal 1447",
        nameAr: "شَوَّال",
        year: 1447,
        monthNumber: 10,
        gregorianSubtitle: "Mar 20 – Apr 18, 2026",
        daysCount: 30,
        startDayOfWeek: 5, // Friday
        startDateGregorian: new Date(2026, 2, 20),
        specialDays: {
          1: { name: "Eid al-Fitr (عيد الفطر)", type: "major" },
          13: { name: "White Day 1 (أيام البيض)", type: "white" },
          14: { name: "White Day 2 (أيام البيض)", type: "white" },
          15: { name: "White Day 3 (أيام البيض)", type: "white" }
        }
      },
      {
        id: "dhulqidah1447",
        name: "Dhul-Qi'dah 1447",
        nameAr: "ذُو الْقَعْدَة",
        year: 1447,
        monthNumber: 11,
        gregorianSubtitle: "Apr 19 – May 17, 2026",
        daysCount: 29,
        startDayOfWeek: 0, // Sunday
        startDateGregorian: new Date(2026, 3, 19),
        specialDays: {
          1: { name: "Sacred Month Begins", type: "major" },
          13: { name: "White Day 1", type: "white" },
          14: { name: "White Day 2", type: "white" },
          15: { name: "White Day 3", type: "white" }
        }
      },
      {
        id: "dhulhijjah1447",
        name: "Dhul-Hijjah 1447",
        nameAr: "ذُو الْحِجَّة",
        year: 1447,
        monthNumber: 12,
        gregorianSubtitle: "May 18 – Jun 16, 2026",
        daysCount: 30,
        startDayOfWeek: 1, // Monday
        startDateGregorian: new Date(2026, 4, 18),
        specialDays: {
          1: { name: "1st Dhul-Hijjah (10 Blessed Days)", type: "major" },
          9: { name: "Day of Arafah (يوم عرفة)", type: "major" },
          10: { name: "Eid al-Adha (عيد الأضحى)", type: "major" }
        }
      },
      {
        id: "muharram1448",
        name: "Muharram 1448",
        nameAr: "مُحَرَّم",
        year: 1448,
        monthNumber: 1,
        gregorianSubtitle: "Jun 17 – Jul 16, 2026",
        daysCount: 30,
        startDayOfWeek: 3, // Wednesday
        startDateGregorian: new Date(2026, 5, 17),
        specialDays: {
          1: { name: "Islamic New Year 1448 AH", type: "major" },
          9: { name: "Tasu'a Fast (9th Muharram)", type: "fast" },
          10: { name: "Day of Ashura (عاشوراء)", type: "major" },
          13: { name: "White Day 1", type: "white" },
          14: { name: "White Day 2", type: "white" },
          15: { name: "White Day 3", type: "white" }
        }
      }
    ];

    let currentHijriMonthIdx = 1; // Default: Shawwal 1447
    let selectedHijriDay = 18;    // Default: Today (18 Shawwal)
    let userFastingLog = {};

    const islamicEventsList = [
      { monthIdx: 1, day: 1, dateAr: "١ شَوَّال", dateEn: "1 Shawwal", title: "Eid al-Fitr", arTitle: "عيد الفطر", status: "Celebrated" },
      { monthIdx: 1, day: 13, dateAr: "١٣-١٥ شَوَّال", dateEn: "13–15 Shawwal", title: "Ayyam al-Beed", arTitle: "أيام البيض", status: "Active" },
      { monthIdx: 2, day: 1, dateAr: "١ ذُو الْقَعْدَة", dateEn: "1 Dhul-Qi'dah", title: "Sacred Month Begins", arTitle: "شهر حرام", status: "Upcoming" },
      { monthIdx: 3, day: 9, dateAr: "٩ ذُو الْحِجَّة", dateEn: "9 Dhul-Hijjah", title: "Day of Arafah", arTitle: "يوم عرفة", status: "Upcoming" },
      { monthIdx: 3, day: 10, dateAr: "١٠ ذُو الْحِجَّة", dateEn: "10 Dhul-Hijjah", title: "Eid al-Adha", arTitle: "عيد الأضحى", status: "Upcoming" },
      { monthIdx: 4, day: 1, dateAr: "١ مُحَرَّم", dateEn: "1 Muharram", title: "Islamic New Year", arTitle: "١٤٤٨ هـ", status: "Upcoming" },
      { monthIdx: 4, day: 10, dateAr: "١٠ مُحَرَّم", dateEn: "10 Muharram", title: "Day of Ashura", arTitle: "عاشوراء", status: "Upcoming" }
    ];

    function loadSavedFastingState() {
      try {
        const saved = localStorage.getItem("muslim_comp_fasting_log");
        if (saved) {
          userFastingLog = JSON.parse(saved);
        } else {
          // Pre-populate some historical Shawwal fasts as example
          userFastingLog = {
            "shawwal1447-13": true,
            "shawwal1447-14": true
          };
        }
      } catch (e) {
        userFastingLog = {};
      }
    }

    function saveFastingState() {
      try {
        localStorage.setItem("muslim_comp_fasting_log", JSON.stringify(userFastingLog));
      } catch (e) {}
    }

    function navigateHijriMonth(delta) {
      playClickSound();
      const newIdx = currentHijriMonthIdx + delta;
      if (newIdx >= 0 && newIdx < hijriMonthsData.length) {
        currentHijriMonthIdx = newIdx;
        selectedHijriDay = (currentHijriMonthIdx === 1) ? 18 : 1;
        renderCalendarData();
      }
    }

    function jumpToCurrentHijriMonth() {
      playClickSound();
      currentHijriMonthIdx = 1; // Shawwal 1447
      selectedHijriDay = 18;
      renderCalendarData();
    }

    function selectHijriDay(day) {
      playClickSound();
      selectedHijriDay = day;
      renderCalendarData();
    }

    function toggleSelectedDateFast() {
      playClickSound();
      const month = hijriMonthsData[currentHijriMonthIdx];
      const key = `${month.id}-${selectedHijriDay}`;
      userFastingLog[key] = !userFastingLog[key];
      saveFastingState();
      renderCalendarData();
      showToast(
        userFastingLog[key] ? "Fast Logged" : "Fast Unmarked",
        userFastingLog[key] ? `Marked fast for ${selectedHijriDay} ${month.name}. Taqabbal Allah!` : `Fast unmarked for this day.`
      );
    }

    function formatTimeDisplay(timeStr) {
      if (!timeStr) return "--:--";
      const parts = timeStr.split(':');
      let h = parseInt(parts[0], 10);
      const m = parts[1] || '00';
      const ampm = h >= 12 ? 'PM' : 'AM';
      h = h % 12;
      if (h === 0) h = 12;
      return `${h.toString().padStart(2, '0')}:${m} ${ampm}`;
    }

    function getGregorianDateForDay(month, day) {
      const d = new Date(month.startDateGregorian);
      d.setDate(d.getDate() + (day - 1));
      return d;
    }

    function renderCalendarData() {
      const month = hijriMonthsData[currentHijriMonthIdx];
      if (!month) return;

      // 1. Month Header Titles
      const monthTitleEl = document.getElementById("calMonthTitle");
      const monthSubEl = document.getElementById("calMonthSubtitle");
      if (monthTitleEl) {
        monthTitleEl.innerHTML = `${month.name} <span class="font-arabic text-emerald-600 dark:text-emerald-400 font-normal text-xs">${month.nameAr}</span>`;
      }
      if (monthSubEl) {
        monthSubEl.innerText = month.gregorianSubtitle;
      }

      // 2. Render 7-column Calendar Grid
      const gridEl = document.getElementById("hijriMonthGrid");
      if (gridEl) {
        gridEl.innerHTML = "";

        // Empty cells before startDayOfWeek
        for (let i = 0; i < month.startDayOfWeek; i++) {
          const emptyCell = document.createElement("div");
          emptyCell.className = "h-10";
          gridEl.appendChild(emptyCell);
        }

        // Days 1..daysCount
        for (let d = 1; d <= month.daysCount; d++) {
          const cell = document.createElement("button");
          const weekday = (month.startDayOfWeek + (d - 1)) % 7;
          const isMon = (weekday === 1);
          const isThu = (weekday === 4);
          const isSunnah = (isMon || isThu);
          const isWhiteDay = (d === 13 || d === 14 || d === 15);
          const isToday = (month.id === "shawwal1447" && d === 18);
          const isSelected = (d === selectedHijriDay);
          const isFastLogged = !!userFastingLog[`${month.id}-${d}`];

          const gregDate = getGregorianDateForDay(month, d);
          const gregDayNum = gregDate.getDate();

          let cellClass = "h-10 rounded-xl flex flex-col items-center justify-center relative transition active:scale-95 text-center ";

          if (isToday) {
            cellClass += "bg-emerald-700 text-white font-extrabold shadow-sm ";
          } else if (isSelected) {
            cellClass += "ring-2 ring-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 font-bold ";
          } else {
            cellClass += "hover:bg-slate-100 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-300 ";
          }

          cell.className = cellClass;
          cell.onclick = () => selectHijriDay(d);

          // Inner HTML: Hijri Day, Gregorian Day, and indicator dot
          let dotHtml = "";
          if (isFastLogged) {
            dotHtml = `<span class="w-1.5 h-1.5 rounded-full ${isToday ? 'bg-gold-400' : 'bg-emerald-600'}"></span>`;
          } else if (isWhiteDay) {
            dotHtml = `<span class="w-1.5 h-1.5 rounded-full ${isToday ? 'bg-amber-300' : 'bg-amber-500'}"></span>`;
          } else if (isSunnah) {
            dotHtml = `<span class="w-1 h-1 rounded-full ${isToday ? 'bg-emerald-200' : 'bg-emerald-500'}"></span>`;
          }

          cell.innerHTML = `
            <span class="text-xs leading-none ${isToday ? 'font-extrabold text-white' : 'font-semibold'}">${d}</span>
            <span class="text-[8px] leading-tight ${isToday ? 'text-emerald-200' : 'text-slate-400 dark:text-slate-500'} mt-0.5">${gregDayNum}</span>
            <div class="h-1 flex items-center justify-center mt-0.5">${dotHtml}</div>
          `;
          gridEl.appendChild(cell);
        }
      }

      // 3. Render Selected Date Detail Card
      const selHijriEl = document.getElementById("selDateHijri");
      const selTagsEl = document.getElementById("selDateTags");
      const btnFastEl = document.getElementById("btnToggleDateFast");
      const btnFastLabel = document.getElementById("btnFastLabel");

      if (selHijriEl && selTagsEl) {
        const gregDate = getGregorianDateForDay(month, selectedHijriDay);
        const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
        const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        const dateStr = `${dayNames[gregDate.getDay()]}, ${monthNames[gregDate.getMonth()]} ${gregDate.getDate()}`;

        selHijriEl.innerHTML = `${selectedHijriDay} ${month.name} <span class="text-[10px] font-normal text-slate-400">• ${dateStr}</span>`;

        // Tags
        let tagsHtml = "";
        const weekday = (month.startDayOfWeek + (selectedHijriDay - 1)) % 7;
        const isToday = (month.id === "shawwal1447" && selectedHijriDay === 18);
        const isWhiteDay = (selectedHijriDay === 13 || selectedHijriDay === 14 || selectedHijriDay === 15);
        const special = month.specialDays ? month.specialDays[selectedHijriDay] : null;

        if (isToday) {
          tagsHtml += `<span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300">Today</span>`;
        }
        if (weekday === 1) {
          tagsHtml += `<span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300">Monday Sunnah Fast</span>`;
        } else if (weekday === 4) {
          tagsHtml += `<span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300">Thursday Sunnah Fast</span>`;
        }
        if (special) {
          tagsHtml += `<span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-300">${special.name}</span>`;
        } else if (isWhiteDay) {
          tagsHtml += `<span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-300">Ayyam al-Beed (White Day)</span>`;
        }

        selTagsEl.innerHTML = tagsHtml || `<span class="text-[9px] text-slate-400">Regular Islamic Day</span>`;

        // Fasting Log Button
        const isFastLogged = !!userFastingLog[`${month.id}-${selectedHijriDay}`];
        if (btnFastEl) {
          if (isFastLogged) {
            btnFastEl.className = "px-2.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-[10px] font-bold flex items-center gap-1 shadow-xs transition active:scale-95 flex-shrink-0";
            btnFastEl.innerHTML = `<i data-lucide="check" class="w-3.5 h-3.5"></i> Fast Logged`;
          } else {
            btnFastEl.className = "px-2.5 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-750 text-slate-700 dark:text-slate-300 hover:bg-emerald-50 dark:hover:bg-emerald-950 text-[10px] font-bold flex items-center gap-1 border border-slate-200 dark:border-slate-700 active:scale-95 transition flex-shrink-0";
            btnFastEl.innerHTML = `<i data-lucide="plus" class="w-3.5 h-3.5"></i> Log Fast`;
          }
        }
      }

      // 4. Suhoor / Iftar from active city
      const city = cities[currentCityIndex];
      const suhoorEl = document.getElementById("calSuhoorTime");
      const iftarEl = document.getElementById("calIftarTime");
      if (suhoorEl && city) suhoorEl.innerText = formatTimeDisplay(city.fajr);
      if (iftarEl && city) iftarEl.innerText = formatTimeDisplay(city.maghrib);

      // 5. Islamic Events List (Clean, single-line pills, no text wrapping)
      const eventsContainer = document.getElementById("islamicEventsContainer");
      if (eventsContainer) {
        eventsContainer.innerHTML = "";
        islamicEventsList.forEach(ev => {
          const card = document.createElement("div");
          card.className = "p-2 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200/60 dark:border-slate-800 flex items-center justify-between cursor-pointer hover:bg-slate-100 dark:hover:bg-slate-850 transition";
          card.onclick = () => {
            currentHijriMonthIdx = ev.monthIdx;
            selectedHijriDay = ev.day;
            renderCalendarData();
          };

          let statusBadgeClass = "bg-slate-200 dark:bg-slate-800 text-slate-500";
          if (ev.status === "Active") {
            statusBadgeClass = "bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-300 border border-amber-300/60";
          } else if (ev.status === "Upcoming") {
            statusBadgeClass = "bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300 border border-emerald-300/60";
          }

          card.innerHTML = `
            <div>
              <p class="font-bold text-slate-800 dark:text-white text-xs flex items-center gap-1">
                ${ev.title} <span class="font-arabic font-normal text-slate-400 text-[10px]">(${ev.arTitle})</span>
              </p>
              <p class="text-[9px] text-slate-400 mt-0.5">${ev.dateEn} • <span class="font-arabic">${ev.dateAr}</span></p>
            </div>
            <span class="whitespace-nowrap px-2 py-0.5 rounded-full text-[9px] font-bold flex-shrink-0 ${statusBadgeClass}">
              ${ev.status}
            </span>
          `;
          eventsContainer.appendChild(card);
        });
      }

      lucide.createIcons();
    }

    function toggleEventNotifications(enabled) {
      playClickSound();
      showToast(
        "Notifications Updated",
        enabled ? "Reminders enabled for Sunnah fasts and major Islamic dates." : "Event reminders turned off."
      );
    }

    function openCalendarModal() {
      playClickSound();
      loadSavedFastingState();
      renderCalendarData();
      const modal = document.getElementById("islamicCalendarModal");
      if (modal) modal.classList.remove("hidden");
    }

    function closeCalendarModal() {
      playClickSound();
      const modal = document.getElementById("islamicCalendarModal");
      if (modal) modal.classList.add("hidden");
    }

    // ==========================================
    // FLUTTERFLOW BLUEPRINT & CUSTOM DART CODE
    // ==========================================
    const flutterflowSnippets = {
      prayer_action: {
        title: "PrayerTimesAction.dart (FlutterFlow Custom Action)",
        code: `import 'dart:math' as math;

class PrayerTimesResult {
  final String fajr;
  final String sunrise;
  final String dhuhr;
  final String asr;
  final String maghrib;
  final String isha;

  PrayerTimesResult({
    required this.fajr,
    required this.sunrise,
    required this.dhuhr,
    required this.asr,
    required this.maghrib,
    required this.isha,
  });
}

/// FlutterFlow Custom Action: calculateDailyPrayerTimes
Future<PrayerTimesResult> calculateDailyPrayerTimes(
  double latitude,
  double longitude,
  DateTime date,
  String juristicMethod, // 'hanafi' or 'standard'
) async {
  final int dayOfYear = date.difference(DateTime(date.year, 1, 1)).inDays + 1;
  final double gamma = 2 * math.pi / 365 * (dayOfYear - 1 + (date.hour - 12) / 24);
  
  final double eqtime = 229.18 * (0.000075 + 0.001868 * math.cos(gamma) - 0.032077 * math.sin(gamma)
      - 0.014615 * math.cos(2 * gamma) - 0.040849 * math.sin(2 * gamma));
      
  final double decl = 0.006918 - 0.399912 * math.cos(gamma) + 0.070257 * math.sin(gamma)
      - 0.006758 * math.cos(2 * gamma) + 0.000907 * math.sin(2 * gamma);

  final double timezoneOffset = date.timeZoneOffset.inMinutes / 60.0;
  final double solarNoon = 12.0 + timezoneOffset - (longitude / 15.0) - (eqtime / 60.0);
  
  // Asr Factor: Hanafi = 2.0, Standard (Shafi'i/Maliki/Hanbali) = 1.0
  final double asrFactor = juristicMethod.toLowerCase() == 'hanafi' ? 2.0 : 1.0;
  final double asrAngle = -math.atan(1.0 / (asrFactor + math.tan((latitude - (decl * 180 / math.pi)).abs() * math.pi / 180))) * 180 / math.pi;

  String formatHours(double hours) {
    int h = hours.floor() % 24;
    int m = ((hours - hours.floor()) * 60).round();
    return '\${h.toString().padLeft(2, '0')}:\${m.toString().padLeft(2, '0')}';
  }

  return PrayerTimesResult(
    fajr: formatHours(solarNoon - 6.25),
    sunrise: formatHours(solarNoon - 5.10),
    dhuhr: formatHours(solarNoon),
    asr: formatHours(solarNoon + 3.25),
    maghrib: formatHours(solarNoon + 5.50),
    isha: formatHours(solarNoon + 6.85),
  );
}`
      },
      qibla_action: {
        title: "CalculateQiblaBearing.dart (FlutterFlow Custom Action)",
        code: `import 'dart:math' as math;

/// FlutterFlow Custom Action: calculateQiblaBearing
/// Precise Great-Circle spherical trigonometry from user coords to Kaaba
Future<double> calculateQiblaBearing(
  double userLatitude,
  double userLongitude,
) async {
  const double kaabaLat = 21.422487;
  const double kaabaLng = 39.826206;

  final double phi1 = userLatitude * math.pi / 180.0;
  final double phi2 = kaabaLat * math.pi / 180.0;
  final double deltaLambda = (kaabaLng - userLongitude) * math.pi / 180.0;

  final double y = math.sin(deltaLambda);
  final double x = math.cos(phi1) * math.tan(phi2) - math.sin(phi1) * math.cos(deltaLambda);
  
  final double qiblaRadians = math.atan2(y, x);
  final double qiblaDegrees = (qiblaRadians * 180.0 / math.pi + 360.0) % 360.0;

  return double.parse(qiblaDegrees.toStringAsFixed(1));
}`
      },
      compass_widget: {
        title: "QiblaCompassWidget.dart (FlutterFlow Custom Widget)",
        code: `import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:math' as math;

class QiblaCompassWidget extends StatefulWidget {
  const QiblaCompassWidget({
    Key? key,
    this.width,
    this.height,
    required this.qiblaBearing,
    required this.deviceHeading,
  }) : super(key: key);

  final double? width;
  final double? height;
  final double qiblaBearing;
  final double deviceHeading;

  @override
  _QiblaCompassWidgetState createState() => _QiblaCompassWidgetState();
}

class _QiblaCompassWidgetState extends State<QiblaCompassWidget> {
  bool _hapticFired = false;

  @override
  Widget build(BuildContext context) {
    final double diff = ((widget.qiblaBearing - widget.deviceHeading + 540) % 360) - 180;
    final bool isAligned = diff.abs() <= 3.0;

    if (isAligned && !_hapticFired) {
      HapticFeedback.heavyImpact();
      _hapticFired = true;
    } else if (!isAligned) {
      _hapticFired = false;
    }

    return Center(
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 300),
        width: widget.width ?? 260,
        height: widget.height ?? 260,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: isAligned ? const Color(0xFF064E3B) : const Color(0xFF1E293B),
          boxShadow: [
            if (isAligned)
              BoxShadow(
                color: const Color(0xFFC5A059).withOpacity(0.6),
                blurRadius: 30,
                spreadRadius: 6,
              ),
          ],
        ),
        child: Transform.rotate(
          angle: ((widget.qiblaBearing - widget.deviceHeading) * (math.pi / 180) * -1),
          child: const Center(
            child: Icon(
              Icons.navigation_rounded,
              color: Color(0xFFC5A059),
              size: 48,
            ),
          ),
        ),
      ),
    );
  }
}`
      },
      database_schema: {
        title: "SQLite & AppState Schema (FlutterFlow / SQLite)",
        code: `{
  "database_name": "muslim_companion.db",
  "version": 1,
  "tables": [
    {
      "name": "daily_salah_log",
      "columns": [
        { "name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT" },
        { "name": "date", "type": "TEXT NOT NULL UNIQUE" },
        { "name": "fajr", "type": "INTEGER DEFAULT 0" },
        { "name": "dhuhr", "type": "INTEGER DEFAULT 0" },
        { "name": "asr", "type": "INTEGER DEFAULT 0" },
        { "name": "maghrib", "type": "INTEGER DEFAULT 0" },
        { "name": "isha", "type": "INTEGER DEFAULT 0" },
        { "name": "completed_count", "type": "INTEGER DEFAULT 0" }
      ]
    },
    {
      "name": "bookmarks",
      "columns": [
        { "name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT" },
        { "name": "surah_number", "type": "INTEGER NOT NULL" },
        { "name": "surah_name_en", "type": "TEXT NOT NULL" },
        { "name": "ayah_number", "type": "INTEGER NOT NULL" },
        { "name": "arabic_text", "type": "TEXT NOT NULL" },
        { "name": "translation_text", "type": "TEXT NOT NULL" },
        { "name": "created_at", "type": "DATETIME DEFAULT CURRENT_TIMESTAMP" }
      ]
    },
    {
      "name": "tasbeeh_history",
      "columns": [
        { "name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT" },
        { "name": "dhikr_phrase", "type": "TEXT NOT NULL" },
        { "name": "target_count", "type": "INTEGER NOT NULL" },
        { "name": "laps_completed", "type": "INTEGER DEFAULT 0" },
        { "name": "total_beads", "type": "INTEGER NOT NULL" },
        { "name": "date", "type": "TEXT NOT NULL" }
      ]
    }
  ]
}`
      }
    };

    let activeFFTab = 'prayer_action';

    function switchFFTab(tabKey) {
      playClickSound();
      activeFFTab = tabKey;
      ['prayer_action', 'qibla_action', 'compass_widget', 'database_schema'].forEach(k => {
        const btn = document.getElementById(`ffTabBtn-${k}`);
        if (btn) {
          if (k === tabKey) {
            btn.className = "px-2.5 py-1 rounded-full bg-emerald-800 text-white flex-shrink-0 font-bold";
          } else {
            btn.className = "px-2.5 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0 font-medium";
          }
        }
      });

      const snippet = flutterflowSnippets[tabKey];
      if (snippet) {
        const titleEl = document.getElementById("ffSnippetTitle");
        const codeEl = document.getElementById("ffSnippetCode");
        if (titleEl) titleEl.innerText = snippet.title;
        if (codeEl) codeEl.innerText = snippet.code;
      }
    }

    function copyCurrentFFSnippet() {
      playClickSound();
      const snippet = flutterflowSnippets[activeFFTab];
      if (snippet && navigator.clipboard) {
        navigator.clipboard.writeText(snippet.code);
        showToast("FlutterFlow Code Copied", `Copied ${snippet.title} to clipboard!`);
      }
    }

    function openFlutterflowModal() {
      playClickSound();
      switchFFTab('prayer_action');
      const modal = document.getElementById("flutterflowModal");
      if (modal) modal.classList.remove("hidden");
    }

    function closeFlutterflowModal() {
      playClickSound();
      const modal = document.getElementById("flutterflowModal");
      if (modal) modal.classList.add("hidden");
    }


    // ==========================================
    // DAILY SALAH TRACKER QUICK ACTIONS
    // ==========================================
    function markAllPrayersToday() {
      playClickSound();
      ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"].forEach(p => {
        todaySalahLog[p] = true;
      });
      try {
        localStorage.setItem("muslim_comp_salah_log", JSON.stringify(todaySalahLog));
        localStorage.setItem("muslim_comp_salah_date", new Date().toDateString());
      } catch (e) {}
      renderSalahTracker();
      if (navigator.vibrate) navigator.vibrate([40, 80, 40]);
      showToast("Masha'Allah! 🎉", "All 5 daily prayers marked as completed for today!");
    }


    // ==========================================
    // ADHKAR IN-CATEGORY LIVE SEARCH FILTER
    // ==========================================
    // Real-Time Adhkar & Duas Search Engine with Live Suggestions
    function clearAdhkarSearch() {
      const input = document.getElementById("adhkarSearchInput");
      if (input) input.value = "";
      const clearBtn = document.getElementById("adhkarSearchClearBtn");
      if (clearBtn) clearBtn.classList.add("hidden");
      const dropdown = document.getElementById("adhkarSuggestionsDropdown");
      if (dropdown) dropdown.classList.add("hidden");
      renderAdhkar();
    }

    function selectDuaFromSuggestion(mode, itemId) {
      clearAdhkarSearch();
      setAdhkarMode(mode);
      setTimeout(() => {
        const card = document.getElementById(`adhkar-card-${itemId}`);
        if (card) {
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
          card.classList.add('ring-2', 'ring-emerald-500');
          setTimeout(() => card.classList.remove('ring-2', 'ring-emerald-500'), 1500);
        }
      }, 100);
    }

    function handleAdhkarLiveSearch(val) {
      const q = val.trim().toLowerCase();
      const clearBtn = document.getElementById("adhkarSearchClearBtn");
      const dropdown = document.getElementById("adhkarSuggestionsDropdown");
      if (!dropdown) return;

      if (clearBtn) {
        if (q.length > 0) clearBtn.classList.remove("hidden");
        else clearBtn.classList.add("hidden");
      }

      if (q.length === 0) {
        dropdown.classList.add("hidden");
        dropdown.innerHTML = "";
        renderAdhkar();
        return;
      }

      const categoryLabels = {
        morning: 'Morning',
        evening: 'Evening',
        after_prayer: 'After Salah',
        daily: 'Daily Sunnah',
        quranic: 'Rabbana',
        sleep: 'Sleep'
      };

      const matches = [];
      Object.keys(adhkarData).forEach(cat => {
        const items = adhkarData[cat];
        if (!items) return;
        items.forEach(item => {
          const matchTitle = item.tr && item.tr.toLowerCase().includes(q);
          const matchMeaning = item.en && item.en.toLowerCase().includes(q);
          const matchRef = item.ref && item.ref.toLowerCase().includes(q);
          const matchAr = item.ar && item.ar.includes(q);
          if (matchTitle || matchMeaning || matchRef || matchAr) {
            matches.push({
              ...item,
              cat: cat,
              catLabel: categoryLabels[cat] || cat
            });
          }
        });
      });

      if (matches.length === 0) {
        dropdown.innerHTML = `
          <div class="p-3 text-center text-xs text-slate-400">
            No duas matching "${val}". Try "Bismillah", "sleep", "travel", or "forgive".
          </div>
        `;
        dropdown.classList.remove("hidden");
        return;
      }

      dropdown.innerHTML = "";
      matches.slice(0, 6).forEach(m => {
        const row = document.createElement("div");
        row.className = "p-2 rounded-xl hover:bg-emerald-50 dark:hover:bg-emerald-950/40 cursor-pointer flex items-center justify-between transition border border-transparent hover:border-emerald-200 dark:hover:border-emerald-800/60";
        row.onclick = () => selectDuaFromSuggestion(m.cat, m.id);

        row.innerHTML = `
          <div class="min-w-0 flex-1 pr-2">
            <div class="flex items-center gap-1.5">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-600 flex-shrink-0"></span>
              <p class="text-xs font-bold text-slate-800 dark:text-white truncate">${m.tr || m.ref}</p>
            </div>
            <p class="text-[10px] text-slate-500 dark:text-slate-400 truncate line-clamp-1 mt-0.5">${m.en}</p>
          </div>
          <span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 flex-shrink-0">
            ${m.catLabel}
          </span>
        `;
        dropdown.appendChild(row);
      });

      dropdown.classList.remove("hidden");
      lucide.createIcons();

      filterAdhkarList(val);
    }

    // Dismiss suggestions when clicking outside
    document.addEventListener('click', (e) => {
      const container = document.getElementById("adhkarSearchContainer");
      const dropdown = document.getElementById("adhkarSuggestionsDropdown");
      if (dropdown && container && !container.contains(e.target)) {
        dropdown.classList.add("hidden");
      }
    });

    function filterAdhkarList(val) {
      const q = val.trim().toLowerCase();
      const list = adhkarData[currentAdhkarMode];
      const container = document.getElementById("adhkarItemsList");
      if (!container) return;
      container.innerHTML = "";

      const filtered = list.filter(item => {
        return !q || item.ar.includes(q) || (item.tr && item.tr.toLowerCase().includes(q)) || item.en.toLowerCase().includes(q) || item.ref.toLowerCase().includes(q);
      });

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="p-6 text-center text-slate-400 text-xs">
            No adhkar match "${val}" in this category.
          </div>
        `;
        return;
      }

      filtered.forEach((item, index) => {
        const card = document.createElement("div");
        card.id = `adhkar-card-${item.id}`;
        card.className = `p-3 rounded-xl border transition-all ${item.done ? 'bg-emerald-50/60 dark:bg-emerald-950/30 border-emerald-300 dark:border-emerald-700/60' : 'bg-white dark:bg-slate-800 border-slate-100 dark:border-slate-700/60'}`;
        card.innerHTML = `
          <div class="space-y-1.5">
            <div class="flex items-start justify-between gap-2.5">
              <span class="text-[10px] font-semibold text-slate-400">${item.ref}</span>
              <button onclick="decrementAdhkar(${index})" class="px-2.5 py-1 rounded-lg flex-shrink-0 flex items-center gap-1 font-bold text-xs transition active:scale-90 border ${item.done ? 'bg-emerald-700 border-emerald-700 text-white shadow-xs' : 'bg-gold-500/10 border-gold-500/30 text-gold-600 dark:text-gold-400'}">
                ${item.done ? '✓ Completed' : `${item.current}x`}
              </button>
            </div>
            <p class="notranslate font-arabic text-right text-[19px] font-bold text-emerald-950 dark:text-emerald-100 leading-[2.2]" translate="no" lang="ar" dir="rtl">${item.ar}</p>
            ${showTransliteration && item.tr ? `<p class="text-left text-[13px] text-emerald-800/90 dark:text-emerald-400/90 font-sans italic leading-normal pt-0.5">${item.tr}</p>` : ''}
            <p class="text-left text-[14px] text-slate-700 dark:text-slate-200 leading-relaxed font-normal pt-0.5">${item.en}</p>
          </div>
        `;
        container.appendChild(card);
      });


      lucide.createIcons();
    }

    function scrollAppBodyToTop() {
      playClickSound();
      const appBody = document.getElementById("appBody");
      if (appBody) appBody.scrollTo({ top: 0, behavior: "smooth" });
    }

    function goToSurahByNum(num) {
      playClickSound();
      selectSurahFromIndex(num);
      scrollAppBodyToTop();
    }


    // ==========================================
    // PHONE SENSOR COMPASS INTEGRATION
    // ==========================================
    let isPhoneSensorActive = false;

    function handlePhoneOrientation(event) {
      let heading = null;
      if (event.webkitCompassHeading !== undefined) {
        // iOS device orientation
        heading = event.webkitCompassHeading;
      } else if (event.alpha !== null) {
        // Android standard orientation (counter-clockwise)
        heading = 360 - event.alpha;
      }

      if (heading !== null) {
        updateCompass(Math.round(heading), false);
        const slider = document.getElementById("headingSlider");
        if (slider) slider.value = Math.round(heading);
      }
    }

    function togglePhoneCompassSensor() {
      playClickSound();
      const btn = document.getElementById("phoneCompassBtn");
      const btnText = document.getElementById("phoneCompassBtnText");

      if (isPhoneSensorActive) {
        window.removeEventListener('deviceorientation', handlePhoneOrientation);
        window.removeEventListener('deviceorientationabsolute', handlePhoneOrientation);
        isPhoneSensorActive = false;
        if (btnText) btnText.innerText = "Enable Phone Compass Sensor";
        showToast("Compass Sensor", "Switched back to manual simulation mode.");
        return;
      }

      // Check for iOS 13+ permission request
      if (typeof DeviceOrientationEvent !== 'undefined' && typeof DeviceOrientationEvent.requestPermission === 'function') {
        DeviceOrientationEvent.requestPermission().then(permissionState => {
          if (permissionState === 'granted') {
            window.addEventListener('deviceorientation', handlePhoneOrientation, true);
            isPhoneSensorActive = true;
            if (btnText) btnText.innerText = "Sensor Active 🧭 (Rotate Phone)";
            showToast("Sensor Active", "Rotate your phone physically to find Kaaba!");
          } else {
            showToast("Permission Denied", "Compass sensor access was not allowed.");
          }
        }).catch(err => {
          showToast("Sensor Error", "Unable to access orientation sensor.");
        });
      } else if ('ondeviceorientationabsolute' in window) {
        window.addEventListener('deviceorientationabsolute', handlePhoneOrientation, true);
        isPhoneSensorActive = true;
        if (btnText) btnText.innerText = "Sensor Active 🧭 (Rotate Phone)";
        showToast("Sensor Active", "Rotate your phone physically to find Kaaba!");
      } else if ('ondeviceorientation' in window) {
        window.addEventListener('deviceorientation', handlePhoneOrientation, true);
        isPhoneSensorActive = true;
        if (btnText) btnText.innerText = "Sensor Active 🧭 (Rotate Phone)";
        showToast("Sensor Active", "Rotate your phone physically to find Kaaba!");
      } else {
        showToast("No Sensor Detected", "Using manual desktop simulation slider.");
      }
    }

    function init() {

      applyTypographySettings();
      autoDetectUserTimezone();
      loadSavedState();
      loadSavedSalahTracker();
      renderSalahTracker();
      updateBookmarksCountBadges();
      loadSavedAppSettings();
      applyActiveCity();
      renderHadith();
      loadSurah('fatihah');
      renderTasbeehSoundSelectors();
      renderAdhkar();
      updateTasbeehRing();
      lucide.createIcons();
      startCountdown();

      if (navigator.permissions && navigator.permissions.query) {
        navigator.permissions.query({ name: 'geolocation' }).then(result => {
          if (result.state === 'granted') {
            detectLocationGPS();
          }
        }).catch(() => {});
      }
    }

    window.onload = init;
  </script>
</body>
</html>
'''

# Write to index.html and preview/index.html
base_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\muslim_companion"
index_path = os.path.join(base_dir, "index.html")
preview_path = os.path.join(base_dir, "preview", "index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_content)

os.makedirs(os.path.dirname(preview_path), exist_ok=True)
shutil.copy2(index_path, preview_path)
print("Successfully updated index.html and preview/index.html!")
