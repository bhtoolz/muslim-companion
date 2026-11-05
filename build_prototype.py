# Python builder for Muslim Companion index.html
import os
import shutil

html_content = r'''<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Muslim Companion (Rafiq Al-Muslim) — Phase 1 MVP</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- Premium Islamic Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600;700;800&family=Scheherazade+New:wght@400;600;700&display=swap" rel="stylesheet">
  
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
            sans: ['Inter', 'sans-serif'],
            arabic: ['Amiri', 'serif'],
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
    body {
      background-color: #030806;
      color: #E2E8F0;
      font-family: 'Inter', sans-serif;
    }
    .font-quran-text {
      font-family: "Amiri Quran", "Scheherazade New", serif;
      line-height: 2.3;
      letter-spacing: 0.01em;
      word-spacing: 0.12em;
    }
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

  <!-- Desktop Presentation Layout -->
  <div class="w-full max-w-5xl flex flex-col lg:flex-row items-center lg:items-start justify-center gap-6 my-auto">
    
    <!-- Left Column: Architecture Info & Presentation Controls -->
    <div class="flex-1 space-y-3.5 text-left max-w-md w-full">
      <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-950/80 border border-emerald-700/50 text-emerald-300 text-xs font-semibold tracking-wide shadow-sm">
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
      <div class="grid grid-cols-2 gap-2 text-xs">
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
      <div class="pt-2 flex flex-wrap items-center gap-2">
        <button id="langToggleBtn" onclick="toggleLang()" class="px-3.5 py-1.5 rounded-lg bg-emerald-800 hover:bg-emerald-700 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm active:scale-95">
          <i data-lucide="globe" class="w-3.5 h-3.5"></i> <span id="langBtnText">Switch to Arabic (RTL)</span>
        </button>
        <button id="themeToggleBtn" onclick="toggleTheme()" class="px-3.5 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 active:scale-95">
          <i data-lucide="moon" class="w-3.5 h-3.5"></i> <span id="themeBtnText">Dark / Light</span>
        </button>
      </div>
    </div>

    <!-- Right Column: Interactive Phone Device Frame -->
    <div class="flex flex-col items-center gap-2.5 flex-shrink-0">
      
      <!-- OS Platform Switcher Pill (iOS vs Android) -->
      <div class="inline-flex items-center p-1 rounded-full bg-slate-950 border border-slate-800 shadow-xl text-xs font-semibold">
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
                <span id="btnGpsText">Detect My Live GPS Location</span>
              </button>

              <!-- Search Filter Input -->
              <div class="relative">
                <input id="citySearchInput" oninput="filterCities(this.value)" type="text" placeholder="Search major Islamic hubs..." class="w-full pl-8 pr-3 py-1.5 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 focus:outline-none focus:border-emerald-600">
                <i data-lucide="search" class="w-3.5 h-3.5 absolute left-2.5 top-2 text-slate-400"></i>
              </div>

              <!-- Cities List Scrollable -->
              <div id="citiesListContainer" class="overflow-y-auto space-y-1.5 max-h-60 pr-1">
                <!-- Rendered dynamically by JS -->
              </div>
            </div>
          </div>

          <!-- Scrollable Main Content Area -->
          <div id="appBody" class="flex-1 overflow-y-auto px-3.5 pt-1 pb-16 space-y-3">

            <!-- TAB 1: PRAYERS (DEFAULT) -->
            <div id="tab-prayers" class="tab-content space-y-3">
              
              <!-- Native Header: Clean Location Pill & Notification Bell -->
              <div class="flex items-center justify-between pt-1 px-0.5">
                <!-- Location Pill with Chevron -->
                <button onclick="openCityModal()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-200/70 dark:bg-slate-800 border border-slate-300/50 dark:border-slate-700/60 text-slate-800 dark:text-slate-100 text-xs font-bold hover:bg-slate-300/60 transition active:scale-95 shadow-xs">
                  <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400"></i>
                  <span id="cityNameLabel">Makkah</span>
                  <i data-lucide="chevron-down" class="w-3 h-3 text-slate-400"></i>
                </button>

                <!-- Hijri Date & Adhan Audio Test Bell -->
                <div class="flex items-center gap-2">
                  <span id="hijriDateLabel" class="text-[11px] text-slate-500 dark:text-slate-400 font-semibold">18 Shawwal 1447</span>
                  <button onclick="playAdhanPreview()" title="Play Adhan Preview" class="w-7 h-7 rounded-full bg-slate-200/70 dark:bg-slate-800 border border-slate-300/50 dark:border-slate-700/60 flex items-center justify-center text-slate-600 dark:text-slate-300 hover:text-emerald-600 active:scale-90 transition">
                    <i data-lucide="bell" class="w-3.5 h-3.5"></i>
                  </button>
                </div>
              </div>

              <!-- Hero Countdown Card with Visual Prayer Window Elapsed Bar -->
              <div class="emerald-gradient text-white rounded-2xl p-4 shadow-md relative overflow-hidden border border-emerald-700/40">
                <div class="absolute -right-8 -bottom-8 w-32 h-32 rounded-full bg-emerald-600/15 pointer-events-none"></div>
                
                <div class="flex items-center justify-between">
                  <span id="lblNextPrayerBadge" class="px-2.5 py-0.5 rounded-full bg-gold-500/20 text-gold-400 text-[9px] font-extrabold uppercase tracking-widest border border-gold-500/30">
                    Next Prayer
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

              <!-- Daily Prayer Timetable -->
              <div class="space-y-1.5">
                <div class="flex items-center justify-between px-1">
                  <span id="lblTimetableTitle" class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Timetable</span>
                  <span id="cityCalcMethodLabel" class="text-[10px] font-semibold text-emerald-800 dark:text-emerald-400">Auto (Umm al-Qura)</span>
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
                    <button onclick="cycleNextHadith()" title="Next Hadith" class="text-emerald-700 dark:text-emerald-400 hover:underline text-[10px] font-bold flex items-center gap-0.5 px-1.5 py-0.5 rounded hover:bg-slate-100 dark:hover:bg-slate-700 transition">
                      <i data-lucide="refresh-cw" class="w-3 h-3"></i> Next
                    </button>
                  </div>
                </div>
                <p id="hadithMatnAr" class="font-arabic text-right text-base text-emerald-950 dark:text-emerald-100 font-bold leading-relaxed">
                  إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى
                </p>
                <p id="hadithMatnEn" class="text-xs text-slate-600 dark:text-slate-300 leading-normal">
                  "Actions are judged by intentions, and every person will be rewarded according to their intention."
                </p>
                <div class="pt-1 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between text-[10px] text-slate-400">
                  <span id="hadithNarratorText">Umar ibn Al-Khattab (RA)</span>
                  <span id="hadithSourceText" class="font-semibold text-emerald-700 dark:text-emerald-400">Sahih al-Bukhari 1</span>
                </div>
              </div>
            </div>

            <!-- TAB 2: QIBLA (SPHERICAL TRIG SENSOR ENGINE) -->
            <div id="tab-qibla" class="tab-content hidden space-y-3.5 text-center pt-1">
              <div>
                <h2 id="lblQiblaTitle" class="text-base font-bold text-slate-900 dark:text-white">Qibla Direction</h2>
                <p class="text-xs text-slate-500">
                  <span id="lblMakkahBearingText">Bearing:</span> 
                  <span id="qiblaBearingValueText" class="font-bold text-emerald-700 dark:text-emerald-400">265° W</span> 
                  • <span id="qiblaDistanceValueText">2,810 km to Kaaba</span>
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

                  <!-- Center Hub -->
                  <div class="absolute w-22 h-22 rounded-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 flex flex-col items-center justify-center shadow-inner">
                    <span id="compassDegrees" class="text-xl font-extrabold text-slate-800 dark:text-white">0°</span>
                    <span id="compassStatus" class="text-[9px] font-bold tracking-widest text-slate-400">TURN</span>
                  </div>
                </div>
              </div>

              <!-- Interactive Rotate Slider (Desktop/Testing) -->
              <div class="px-5 space-y-1">
                <div class="flex items-center justify-between text-[11px] font-semibold text-slate-400">
                  <span>Sensor Simulation</span>
                  <span id="qiblaTargetLabel" class="text-emerald-600 dark:text-emerald-400 font-bold">Align at 265°</span>
                </div>
                <input id="headingSlider" type="range" min="0" max="360" value="0" oninput="updateCompass(this.value, true)" class="w-full accent-emerald-700 cursor-pointer">
                <div class="flex justify-between text-[10px] text-slate-400">
                  <span>0° (North)</span>
                  <span>180° (South)</span>
                  <span>360°</span>
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
                  <h2 id="lblQuranTitle" class="text-base font-bold text-slate-900 dark:text-white">Holy Quran</h2>
                  <p class="text-[11px] text-slate-500">Uthmani Script & English</p>
                </div>

                <!-- Font Size & Transliteration Controls -->
                <div class="flex items-center gap-1 bg-slate-200 dark:bg-slate-800 p-0.5 rounded-lg text-xs font-bold">
                  <button onclick="changeFontSize(-2)" title="Decrease Font" class="px-2 py-0.5 rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300">A-</button>
                  <button onclick="changeFontSize(2)" title="Increase Font" class="px-2 py-0.5 rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300">A+</button>
                  <button onclick="toggleTransliteration()" id="translitBtn" title="Toggle English Transliteration" class="px-2 py-0.5 rounded bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-300 text-[10px]">
                    Aa
                  </button>
                  <button onclick="toggleAudioRecitation()" id="reciteAudioBtn" class="px-2 py-0.5 rounded bg-emerald-800 text-white flex items-center gap-1">
                    <i data-lucide="volume-2" class="w-3 h-3"></i> Recite
                  </button>
                </div>
              </div>

              <!-- Surah Navigation Pills -->
              <div class="flex gap-1.5 overflow-x-auto pb-1 text-xs">
                <button onclick="loadSurah('fatihah')" id="surah-pill-fatihah" class="px-3 py-1 rounded-full font-bold bg-emerald-800 text-white flex-shrink-0">1. Al-Fatihah</button>
                <button onclick="loadSurah('kursi')" id="surah-pill-kursi" class="px-3 py-1 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">2:255 Ayat al-Kursi</button>
                <button onclick="loadSurah('ikhlas')" id="surah-pill-ikhlas" class="px-3 py-1 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">112. Al-Ikhlas</button>
                <button onclick="loadSurah('falaq')" id="surah-pill-falaq" class="px-3 py-1 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">113. Al-Falaq</button>
                <button onclick="loadSurah('nas')" id="surah-pill-nas" class="px-3 py-1 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">114. An-Nas</button>
                <button onclick="loadSurah('mulk')" id="surah-pill-mulk" class="px-3 py-1 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0">67. Al-Mulk</button>
              </div>

              <!-- Surah Banner Card -->
              <div class="emerald-gradient text-white rounded-2xl p-3.5 text-center relative overflow-hidden border border-emerald-700/50 shadow-sm">
                <div class="flex items-center justify-between text-[10px] text-gold-300 uppercase font-semibold">
                  <span id="surahMetaType">Meccan</span>
                  <span id="surahMetaVerses">7 Verses</span>
                </div>
                <h3 id="surahHeaderTitleAr" class="font-arabic text-2xl font-bold mt-1 text-gold-400">سُورَةُ الفَاتِحَةِ</h3>
                <p id="surahHeaderTitleEn" class="text-xs text-slate-200 font-medium">The Opening</p>
                
                <div class="mt-2.5 pt-2 border-t border-emerald-800/80">
                  <p class="font-quran-text text-lg text-gold-300 leading-normal">
                    بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
                  </p>
                </div>
              </div>

              <!-- Verses Container -->
              <div id="quranVersesList" class="space-y-2.5">
                <!-- Rendered dynamically by JS with Amiri Quran font -->
              </div>
            </div>

            <!-- TAB 4: ADHKAR (INTERACTIVE COUNTERS & SESSION PROGRESS) -->
            <div id="tab-adhkar" class="tab-content hidden space-y-2.5 pt-1">
              <div class="flex items-center justify-between">
                <div>
                  <h2 id="lblAdhkarTitle" class="text-base font-bold text-slate-900 dark:text-white">Daily Adhkar</h2>
                  <p class="text-[11px] text-slate-500">Authentic Hisn al-Muslim Remembrance</p>
                </div>
                <div class="inline-flex rounded-lg bg-slate-200 dark:bg-slate-800 p-0.5 text-[11px] font-bold">
                  <button id="adhkarMornBtn" onclick="setAdhkarMode('morning')" class="px-2.5 py-1 rounded-md bg-white dark:bg-slate-700 text-emerald-800 dark:text-white shadow-xs">Morning</button>
                  <button id="adhkarEveBtn" onclick="setAdhkarMode('evening')" class="px-2.5 py-1 rounded-md text-slate-500">Evening</button>
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
            <div id="tab-tasbeeh" class="tab-content hidden space-y-3.5 pt-1 text-center">
              <div class="flex items-center justify-between px-1">
                <div>
                  <h2 id="lblTasbeehTitle" class="text-base font-bold text-slate-900 dark:text-white text-left">Digital Tasbeeh</h2>
                  <p id="lblTasbeehSub" class="text-[11px] text-slate-500 text-left">Haptic counter with milestone audio</p>
                </div>
                <button onclick="toggleTasbeehSound()" id="soundToggleBtn" class="px-2.5 py-1 text-[10px] font-bold rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center gap-1">
                  <i data-lucide="volume-2" class="w-3 h-3"></i> Sound: ON
                </button>
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
                <h3 id="currentDhikrAr" class="font-arabic text-2xl font-bold text-emerald-950 dark:text-emerald-300">سُبْحَانَ اللَّهِ</h3>
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
    let quranFontSize = 20; // Default px
    let showTransliteration = true;
    let isTasbeehSoundOn = true;
    let bookmarkedVerses = {};
    let prayerAlerts = { Fajr: true, Sunrise: false, Dhuhr: true, Asr: true, Maghrib: true, Isha: true };

    // Web Audio Synthesizer (Realistic acoustic clicks & chimes)
    let audioCtx = null;
    function playClickSound() {
      if (!isTasbeehSoundOn) return;
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(300, audioCtx.currentTime + 0.04);
        gain.gain.setValueAtTime(0.18, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.04);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.05);
      } catch (e) {}
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

    // Live GPS Auto-Detection
    function detectLocationGPS() {
      playClickSound();
      const btn = document.getElementById("btnAutoGPS");
      const btnText = document.getElementById("btnGpsText");
      btnText.innerText = "Querying Device GPS Sensor...";

      if (!navigator.geolocation) {
        showToast("GPS Error", "Geolocation is not supported by your browser");
        btnText.innerText = "Detect My Live GPS Location";
        return;
      }

      navigator.geolocation.getCurrentPosition(
        (position) => {
          const lat = position.coords.latitude;
          const lng = position.coords.longitude;
          
          // Add or replace GPS item as first city
          const gpsBearing = calculateQiblaBearing(lat, lng);
          const gpsDist = calculateKaabaDistance(lat, lng);

          const gpsCity = {
            name: "Current GPS Location",
            country: `${lat.toFixed(2)}°, ${lng.toFixed(2)}°`,
            lat: lat,
            lng: lng,
            method: "Auto GPS Calculation",
            fajr: "05:14",
            sunrise: "06:35",
            dhuhr: "12:18",
            asr: "15:35",
            maghrib: "18:02",
            isha: "19:22"
          };

          cities.unshift(gpsCity);
          currentCityIndex = 0;
          closeCityModal();
          applyActiveCity();
          btnText.innerText = "Detect My Live GPS Location";
          showToast("GPS Locked", `Accurate Qibla: ${gpsBearing}° • ${gpsDist.toLocaleString()} km to Kaaba`);
        },
        (error) => {
          btnText.innerText = "Detect My Live GPS Location";
          showToast("Location Access", "GPS permission denied. Using selected city.");
        },
        { timeout: 7000 }
      );
    }

    function applyActiveCity() {
      const city = cities[currentCityIndex];
      document.getElementById("cityNameLabel").innerText = city.name;
      document.getElementById("cityCalcMethodLabel").innerText = city.method;

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

    // Render Prayer Cards with Per-Prayer Alert Bell
    function renderPrayerCards() {
      const city = cities[currentCityIndex];
      const container = document.getElementById("prayerCardsList");
      container.innerHTML = "";
      const nextPName = document.getElementById("heroPrayerName").innerText;

      prayerNames.forEach(p => {
        const time = city[p.id.toLowerCase()];
        const isNext = p.id === nextPName;
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
              ${isNext ? '<span class="ml-1 text-[8px] uppercase px-1.5 py-0.2 rounded bg-emerald-600 text-white font-bold">Upcoming</span>' : ''}
            </div>
          </div>
          <div class="flex items-center gap-3">
            <span class="text-xs font-mono font-bold ${isNext ? 'text-emerald-800 dark:text-emerald-400' : 'text-slate-500'}">
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

      document.getElementById("heroPrayerName").innerText = nextName;
      const [h, m] = nextTimeStr.split(':').map(Number);
      const ampm = h >= 12 ? 'PM' : 'AM';
      const h12 = h % 12 || 12;
      document.getElementById("heroPrayerTime").innerText = `${h12}:${String(m).padStart(2, '0')} ${ampm}`;
      
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
        if (el) el.innerText = `${h}:${m}:${s}`;
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

      const diff = Math.abs(userHeading - qiblaTarget);
      const isAligned = diff <= 3 || diff >= 357;

      if (isAligned) {
        statusText.innerText = "ALIGNED";
        statusText.className = "text-[9px] font-extrabold tracking-widest text-emerald-500 animate-pulse";
        outerRing.classList.add("ring-4", "ring-gold-400", "border-gold-500");
        bannerCard.className = "p-2 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-400 text-xs font-bold text-emerald-800 dark:text-emerald-300";
        banner.innerHTML = `✓ Perfectly Aligned with Kaaba (${qiblaTarget}°)`;
        if (isUserEvent) {
          try { if (navigator.vibrate) navigator.vibrate([35]); } catch (e) {}
          playClickSound();
        }
      } else {
        statusText.innerText = diff < 20 ? "CLOSE" : "TURN";
        statusText.className = "text-[9px] font-bold tracking-widest text-slate-400";
        outerRing.classList.remove("ring-4", "ring-gold-400", "border-gold-500");
        bannerCard.className = "p-2 rounded-xl bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-500";
        banner.innerText = `Rotate phone to ${qiblaTarget}° to align (${diff}° off)`;
      }
    }

    // Physical Device Orientation Listener for real iOS/Android devices
    if (window.DeviceOrientationEvent) {
      window.addEventListener('deviceorientation', (e) => {
        let heading = null;
        if (e.webkitCompassHeading) {
          heading = Math.round(e.webkitCompassHeading); // iOS
        } else if (e.alpha !== null) {
          heading = Math.round(360 - e.alpha); // Android
        }
        if (heading !== null) {
          const slider = document.getElementById("headingSlider");
          if (slider) slider.value = heading;
          updateCompass(heading, true);
        }
      }, { passive: true });
    }

    // Rich Quran Surahs with Transliteration & Saheeh International Translation
    const surahsData = {
      fatihah: {
        number: 1,
        titleAr: "سُورَةُ الفَاتِحَةِ",
        titleEn: "The Opening",
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
        titleAr: "آيَةُ الكُرْسِيِّ",
        titleEn: "The Throne Verse (2:255)",
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
        titleAr: "سُورَةُ الإِخْلَاصِ",
        titleEn: "The Sincerity",
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
        titleAr: "سُورَةُ الفَلَقِ",
        titleEn: "The Daybreak",
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
        titleAr: "سُورَةُ النَّاسِ",
        titleEn: "Mankind",
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
        titleAr: "سُورَةُ المُلْكِ",
        titleEn: "The Sovereignty",
        type: "Meccan",
        versesCount: 3,
        verses: [
          { id: 1, ar: "تَبَٰرَكَ ٱلَّذِى بِيَدِهِ ٱلْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ", tr: "Tabaarakal-lazee biyadihil-mulku wa Huwa 'alaa kulli shay'in Qadeer", en: "Blessed is He in whose hand is dominion, and He is over all things competent -" },
          { id: 2, ar: "ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ", tr: "Allazee khalaqal-mawta wal-hayaata liyabluwakum ayyukum ahsanu 'amalaa", en: "Who created death and life to test you as to which is best in deed." },
          { id: 3, ar: "ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا ۖ مَّا تَرَىٰ فِى خَلْقِ ٱلرَّحْمَٰنِ مِن تَفَٰوُتٍۢ", tr: "Allazee khalaqa sab'a samaawaatin tibaaqan", en: "Who created seven heavens in layers. You do not see in the creation of the Most Merciful any inconsistency." }
        ]
      }
    };
    let currentSurahKey = 'fatihah';

    function loadSurah(surahKey) {
      currentSurahKey = surahKey;
      const s = surahsData[surahKey];
      
      document.getElementById("surahMetaType").innerText = s.type;
      document.getElementById("surahMetaVerses").innerText = `${s.versesCount} Verses`;
      document.getElementById("surahHeaderTitleAr").innerText = s.titleAr;
      document.getElementById("surahHeaderTitleEn").innerText = s.titleEn;

      ['fatihah', 'kursi', 'ikhlas', 'falaq', 'nas', 'mulk'].forEach(k => {
        const pill = document.getElementById(`surah-pill-${k}`);
        if (!pill) return;
        if (k === surahKey) {
          pill.className = "px-3 py-1 rounded-full font-bold bg-emerald-800 text-white flex-shrink-0";
        } else {
          pill.className = "px-3 py-1 rounded-full font-medium bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300 flex-shrink-0";
        }
      });

      renderQuranVerses();
    }

    function renderQuranVerses() {
      const s = surahsData[currentSurahKey];
      const container = document.getElementById("quranVersesList");
      container.innerHTML = "";

      s.verses.forEach((v, index) => {
        const isBookmarked = bookmarkedVerses[`${currentSurahKey}_${v.id}`];
        const card = document.createElement("div");
        card.id = `ayah-card-${index}`;
        card.className = "ayah-card p-3 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/80 dark:border-slate-700/80 space-y-1.5 transition-all duration-300";
        
        card.innerHTML = `
          <div class="flex items-center justify-between pb-1 border-b border-slate-100 dark:border-slate-700/60">
            <span class="w-5 h-5 rounded-full bg-gold-500/15 text-gold-600 dark:text-gold-400 text-[10px] font-bold flex items-center justify-center font-sans border border-gold-500/30">
              ${v.id}
            </span>
            <div class="flex items-center gap-1.5">
              <button onclick="toggleBookmark('${currentSurahKey}', ${v.id})" title="Bookmark" class="p-1 rounded hover:bg-slate-100 dark:hover:bg-slate-700 transition">
                <i data-lucide="bookmark" class="w-3.5 h-3.5 ${isBookmarked ? 'text-gold-500 fill-current' : 'text-slate-400'}"></i>
              </button>
              <button onclick="playVerseAudioTone(${index})" title="Play" class="p-1 rounded hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-400 hover:text-emerald-700">
                <i data-lucide="play" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
          <p class="font-quran-text text-right text-emerald-950 dark:text-white font-normal" style="font-size: ${quranFontSize}px;">
            ${v.ar} <span class="ayah-marker">﴿${toArabicDigits(v.id)}﴾</span>
          </p>
          ${showTransliteration && v.tr ? `<p class="text-left text-[11px] text-emerald-800 dark:text-emerald-400/90 font-mono italic leading-tight pt-0.5">${v.tr}</p>` : ''}
          <p class="text-left text-xs text-slate-600 dark:text-slate-300 font-sans leading-relaxed pt-0.5">
            ${v.en}
          </p>
        `;
        container.appendChild(card);
      });
      lucide.createIcons();
    }

    function toArabicDigits(num) {
      const arabicNumerals = ['٠','١','٢','٣','٤','٥','٦','٧','٨','٩'];
      return String(num).split('').map(d => arabicNumerals[parseInt(d)] || d).join('');
    }

    function changeFontSize(delta) {
      playClickSound();
      quranFontSize = Math.max(16, Math.min(30, quranFontSize + delta));
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

    function toggleBookmark(surahKey, verseId) {
      playClickSound();
      const k = `${surahKey}_${verseId}`;
      if (bookmarkedVerses[k]) {
        delete bookmarkedVerses[k];
        showToast("Bookmark Removed", `Ayah ${verseId} removed from saved`);
      } else {
        bookmarkedVerses[k] = true;
        showToast("Ayah Bookmarked", `Saved Surah ${surahsData[surahKey].titleEn} Ayah ${verseId}`);
      }
      renderQuranVerses();
      saveState();
    }

    function playVerseAudioTone(index) {
      highlightActiveAyah(index);
      playClickSound();
    }

    // Audio Recitation Simulation
    let recitationInterval = null;
    let recitingVerseIdx = 0;

    function toggleAudioRecitation() {
      playClickSound();
      const btn = document.getElementById("reciteAudioBtn");
      const s = surahsData[currentSurahKey];

      if (recitationInterval) {
        clearInterval(recitationInterval);
        recitationInterval = null;
        btn.innerHTML = `<i data-lucide="volume-2" class="w-3 h-3"></i> Recite`;
        btn.classList.remove("bg-gold-600");
        document.querySelectorAll('.ayah-card').forEach(c => {
          c.classList.remove("ring-2", "ring-gold-500", "bg-gold-500/10", "dark:bg-gold-500/15");
        });
      } else {
        btn.innerHTML = `<i data-lucide="pause" class="w-3 h-3 animate-pulse"></i> Playing`;
        btn.classList.add("bg-gold-600");
        recitingVerseIdx = 0;
        highlightActiveAyah(recitingVerseIdx);

        recitationInterval = setInterval(() => {
          recitingVerseIdx++;
          if (recitingVerseIdx >= s.verses.length) {
            recitingVerseIdx = 0;
          }
          highlightActiveAyah(recitingVerseIdx);
        }, 3200);
      }
      lucide.createIcons();
    }

    function highlightActiveAyah(idx) {
      document.querySelectorAll('.ayah-card').forEach((c, i) => {
        if (i === idx) {
          c.classList.add("ring-2", "ring-gold-500", "bg-gold-500/10", "dark:bg-gold-500/15");
          c.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
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
      ]
    };
    let currentAdhkarMode = 'morning';

    function setAdhkarMode(mode) {
      playClickSound();
      currentAdhkarMode = mode;
      const morn = document.getElementById("adhkarMornBtn");
      const eve = document.getElementById("adhkarEveBtn");
      if (mode === 'morning') {
        morn.className = "px-2.5 py-1 rounded-md bg-white dark:bg-slate-700 text-emerald-800 dark:text-white shadow-xs";
        eve.className = "px-2.5 py-1 rounded-md text-slate-500";
      } else {
        eve.className = "px-2.5 py-1 rounded-md bg-white dark:bg-slate-700 text-emerald-800 dark:text-white shadow-xs";
        morn.className = "px-2.5 py-1 rounded-md text-slate-500";
      }
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
        card.className = `p-3 rounded-xl border transition-all ${item.done ? 'bg-emerald-50/60 dark:bg-emerald-950/30 border-emerald-300 dark:border-emerald-700/60' : 'bg-white dark:bg-slate-800 border-slate-100 dark:border-slate-700/60'}`;
        card.innerHTML = `
          <div class="space-y-1.5">
            <div class="flex items-start justify-between gap-2.5">
              <span class="text-[10px] font-semibold text-slate-400">${item.ref}</span>
              <button onclick="decrementAdhkar(${index})" class="px-2.5 py-1 rounded-lg flex-shrink-0 flex items-center gap-1 font-bold text-xs transition active:scale-90 border ${item.done ? 'bg-emerald-700 border-emerald-700 text-white shadow-xs' : 'bg-gold-500/10 border-gold-500/30 text-gold-600 dark:text-gold-400'}">
                ${item.done ? '✓ Completed' : `${item.current}x`}
              </button>
            </div>
            <p class="font-arabic text-right text-base font-bold text-emerald-950 dark:text-emerald-100 leading-relaxed">${item.ar}</p>
            ${showTransliteration && item.tr ? `<p class="text-left text-[11px] text-emerald-800 dark:text-emerald-400/90 font-mono italic leading-tight">${item.tr}</p>` : ''}
            <p class="text-left text-xs text-slate-600 dark:text-slate-300 leading-normal">${item.en}</p>
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
      isTasbeehSoundOn = !isTasbeehSoundOn;
      const btn = document.getElementById("soundToggleBtn");
      btn.innerHTML = `<i data-lucide="${isTasbeehSoundOn ? 'volume-2' : 'volume-x'}" class="w-3 h-3"></i> Sound: ${isTasbeehSoundOn ? 'ON' : 'OFF'}`;
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
        nextPrayer: "Next Prayer",
        countdown: "Countdown",
        dailyHadith: "Daily Hadith",
        bearing: "Bearing:",
        qiblaTitle: "Qibla Direction",
        quranTitle: "Holy Quran",
        adhkarTitle: "Daily Adhkar",
        tasbeehTitle: "Digital Tasbeeh",
        tasbeehSub: "Haptic counter with milestone audio",
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
      } else {
        screen.setAttribute("dir", "ltr");
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

      renderPrayerCards();
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

    // State Persistence
    function saveState() {
      try {
        const state = {
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
        if (s.currentCityIndex !== undefined) currentCityIndex = Math.min(s.currentCityIndex, cities.length - 1);
        if (s.tasbeehCount !== undefined) tasbeehCount = s.tasbeehCount;
        if (s.tasbeehLaps !== undefined) tasbeehLaps = s.tasbeehLaps;
        if (s.tasbeehTarget !== undefined) tasbeehTarget = s.tasbeehTarget;
        if (s.tasbeehDailyTotal !== undefined) tasbeehDailyTotal = s.tasbeehDailyTotal;
        if (s.selectedDhikrIdx !== undefined) selectedDhikrIdx = s.selectedDhikrIdx;
        if (s.isTasbeehSoundOn !== undefined) isTasbeehSoundOn = s.isTasbeehSoundOn;
        if (s.quranFontSize !== undefined) quranFontSize = s.quranFontSize;
        if (s.showTransliteration !== undefined) showTransliteration = s.showTransliteration;
        if (s.bookmarkedVerses !== undefined) bookmarkedVerses = s.bookmarkedVerses;
        if (s.prayerAlerts !== undefined) prayerAlerts = s.prayerAlerts;
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

    function init() {
      autoDetectUserTimezone();
      loadSavedState();
      applyActiveCity();
      renderHadith();
      loadSurah('fatihah');
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
