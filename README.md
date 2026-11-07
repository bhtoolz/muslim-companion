# Muslim Companion (رفيق المسلم)

A refined, privacy-first Islamic daily companion built for iOS and Android. Designed with a calm, distraction-free aesthetic inspired by traditional Islamic geometry and modern mobile craftsmanship.

---

## Overview

Muslim Companion provides the essential daily spiritual tools a Muslim needs in a single lightweight, ad-free experience. The interface is engineered from the ground up to support both Arabic (RTL with Eastern Arabic numerals) and English (LTR) with seamless 1-tap switching.

---

## Core Features

- **Prayer Timetable & Daily Salah Tracker**
  - Solar-calculated prayer times with dynamic calculation methods (Karachi, Umm al-Qura, ISNA, MWL, Egyptian).
  - Live upcoming prayer countdown with elapsed interval progress indicator.
  - Daily 5-prayer checklist featuring celestial time-of-day iconography (Sunrise, Sun, Cloud-Sun, Sunset, Crescent Moon) with audio and haptic feedback.

- **Qibla Compass**
  - Great-circle spherical trigonometric bearing calculation pointing directly to the Kaaba.
  - Real device compass sensor support with smooth heading dampening and haptic alignment cues.
  - Manual calibration slider for testing and desktop simulation.

- **Holy Quran Reader**
  - Authentic Uthmani calligraphy with verse-by-verse audio recitation by Sheikh Mishary Rashid Alafasy.
  - Real-time word-by-word recitation highlighting with clean amber gold markers and synchronized playback.
  - Searchable 114 Surah directory and quick access to essential verses (Ayat al-Kursi, Dua Qunoot, 40 Rabbana).
  - Dynamic font selector (Amiri Quran, Scheherazade New, Noto Naskh) and fluid text sizing slider.

- **Authentic Adhkar (Hisn al-Muslim)**
  - Categorized morning, evening, post-prayer, and bedtime supplications.
  - Interactive tap-to-complete repetition counters and verified Arabic tashkeel.

- **Tactile Digital Tasbeeh**
  - Minimalist digital rosary with realistic bead physics.
  - 4 acoustic sound profiles (Wood, Click, Water, Digital) with customizable lap limits and haptics.

- **Interactive Hijri Calendar & Fasting Guide**
  - Monthly Umm al-Qura lunar grid highlighting White Days (Ayyam al-Beed) and major Islamic occasions.
  - Integrated Suhoor and Iftar timestamps calculated from local solar coordinates.

- **99 Names of Allah & Daily Sahih Hadith**
  - Reverent catalog of Asma ul-Husna and prophetic titles with classical meanings.
  - Daily rotating authentic narrations from Sahih al-Bukhari and Sahih Muslim.

- **Royal Identity & Smart Localization**
  - Signature 24K gold Rub el Hizb medallion and celestial crescent with Solfeggio acoustic soundscape.
  - Automatic locale and timezone detection defaulting to Arabic (RTL) for Arab countries and English (LTR) for international visitors.
  - Modern Android adaptive launcher icons (round, squircle, and square compatible) and crisp circular web favicons.

---

## Design System

- **Palette:** Deep Forest Emerald (`#0A2E23`), Burnished Gold (`#C5A059`), and Warm Alabaster Cream (`#F9F8F5`).
- **Typography:**
  - Arabic Display & UI: Tajawal & IBM Plex Sans Arabic
  - Quranic Calligraphy: Scheherazade New & Amiri Quran
  - Latin UI: Plus Jakarta Sans & Inter
- **Numerals:** Native Eastern Arabic numerals (`٠, ١, ٢...`) in Arabic mode; Western numerals in English mode.
- **Theme:** Full Dark Mode and Light Mode support with smooth transition.

---

## Repository Structure

```text
├── index.html                   # Interactive web prototype and mobile showcase
├── build_prototype.py           # Single-source prototype compiler and asset syncer
├── flutterflow_components/
│   ├── custom_widgets/
│   │   ├── qibla_compass.dart   # FlutterFlow widget (gyro sensor + haptics)
│   │   └── tasbeeh_counter.dart # FlutterFlow widget (circular bead counter)
│   └── custom_actions/
│       └── get_prayer_times.dart# AlAdhan client & offline astronomical fallback
├── data/
│   ├── adhkar_morning_evening.json  # Hisn al-Muslim authentic dataset
│   ├── daily_hadith.json            # Sahih Bukhari & Muslim authentic collection
│   └── quran_surahs.json            # Surah directory metadata and verse text
├── assets/
│   └── screens/                 # 20 high-res real application screenshots (Arabic & English)
├── preview/                     # Production distribution bundle
└── README.md
```

---

## Local Development & Preview

To preview the interactive mobile simulator and gallery locally:

```bash
# Using Python
python -m http.server 4000

# Using Node
npx serve .
```

Open `http://localhost:4000/` in your browser.

To regenerate `index.html` after modifying source components:

```bash
python build_prototype.py
```

---

## License

Proprietary. All rights reserved.
