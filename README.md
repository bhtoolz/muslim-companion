# Muslim Companion (رفيق المسلم) — MVP

> Modern, minimal, and high-performance Islamic companion application built for iOS & Android with FlutterFlow.

![FlutterFlow](https://img.shields.io/badge/Platform-FlutterFlow-10B981?style=flat-square)
![Flutter](https://img.shields.io/badge/Language-Flutter%20%2F%20Dart-02569B?style=flat-square)
![License](https://img.shields.io/badge/License-Proprietary-gold?style=flat-square)

---

## 🌟 Key Highlights & Architecture

- **Zero AI-Slop UI:** Minimalist, calm, and distraction-free design inspired by award-winning apps like *Pillars* and *Quranly*.
- **1-Word Clean Navigation:** `Prayers` | `Qibla` | `Quran` | `Adhkar` | `Tasbeeh`.
- **Emerald & Gold Palette:** Deep Forest Emerald (`#0A2E23`), Burnished Gold (`#C5A059`), and Alabaster Cream (`#F9F8F5`).
- **Hardware Sensor Integration:** Real-time device compass tracking with smooth interpolation and tactile haptic vibration when aligned with Makkah.
- **Offline-First Data:** Pre-bundled authentic Hadith and Hisn al-Muslim Adhkar in local JSON to eliminate ongoing database/server fees.
- **Full Bilingual (RTL/LTR):** Seamless dynamic switching between English and Arabic with automated layout mirroring.

---

## 📱 Phase 1 MVP Feature Set

| # | Feature | Technical Implementation |
|---|---|---|
| **1** | **Prayer Times** | AlAdhan REST API client with local offline caching and auto-calculation. |
| **2** | **Countdown & Alerts** | Active real-time countdown to the upcoming prayer (`HH:mm:ss`) + local alert scheduler. |
| **3** | **Qibla Compass** | Custom FlutterFlow Widget using `flutter_compass` & spherical trigonometric bearing formula. |
| **4** | **Quran Reader** | Clean Arabic Uthmani font with verse-by-verse English translations and audio hooks. |
| **5** | **Morning & Evening Adhkar** | Categorized Hisn al-Muslim remembrance cards with tap-to-complete tracker. |
| **6** | **Digital Tasbeeh** | Tactile circular counter with cycle tracking (33/99/100) and haptic feedback. |
| **7** | **Daily Hadith** | Verified daily rotating Bukhari & Muslim authentic narrations. |
| **8** | **Bilingual Support** | English & Arabic localization with native RTL support. |
| **9** | **Design System** | Luxury Islamic theme tokens for both Light and Dark mode. |

---

## 📂 Repository Structure

```text
├── index.html                   # Interactive live mobile web prototype (Vercel ready)
├── flutterflow_components/
│   ├── custom_widgets/
│   │   ├── qibla_compass.dart   # FlutterFlow Custom Widget (Compass + Haptics)
│   │   └── tasbeeh_counter.dart # FlutterFlow Custom Widget (Circular Tasbeeh)
│   └── custom_actions/
│       └── get_prayer_times.dart# FlutterFlow Custom Action (AlAdhan API + Countdown)
├── data/
│   ├── adhkar_morning_evening.json  # Authentic Hisn al-Muslim dataset
│   ├── daily_hadith.json            # Sahih Bukhari & Muslim authentic collection
│   └── quran_surahs.json            # Surah metadata and sample Surah Al-Fatiha
├── theme/
│   └── theme_spec.md            # Exact color tokens, typography, and styling rules
└── README.md
```

---

## 🚀 Live Demo Deployment

The root `index.html` is configured for instant 1-click deployment on **Vercel**:
1. Connect this GitHub repository to Vercel.
2. Select default settings (Framework Preset: **Other** / Static).
3. Click **Deploy**.
