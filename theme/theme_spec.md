# Muslim Companion (Rafiq Al-Muslim) — Design System & Spec

## 1. Color Palette (Emerald & Burnished Gold)

| Role | Color Name | Hex Code | FlutterFlow Token |
| :--- | :--- | :--- | :--- |
| **Primary** | Deep Forest Emerald | `#0A2E23` | `Primary` |
| **Secondary** | Burnished Islamic Gold | `#C5A059` | `Secondary` |
| **Accent / Highlight** | Warm Sand Gold | `#E2C481` | `Accent 1` |
| **Success / Aligned** | Medina Green | `#10B981` | `Success` |
| **Background (Light)** | Alabaster Silk | `#F9F8F5` | `Primary Background` |
| **Surface (Light)** | Pure White | `#FFFFFF` | `Secondary Background` |
| **Text Primary (Light)**| Deep Basalt | `#111815` | `Primary Text` |
| **Text Muted (Light)**  | Warm Slate | `#73807B` | `Secondary Text` |
| **Background (Dark)**  | Night Jade | `#0D1513` | `Primary Background (Dark)` |
| **Surface (Dark)**     | Obsidian Emerald | `#141F1C` | `Secondary Background (Dark)` |
| **Text Primary (Dark)**| Cream Whisper | `#F5F7F6` | `Primary Text (Dark)` |

---

## 2. Typography Rules

* **English (UI & Translations):** `Plus Jakarta Sans` or `Inter`
  * Heading: SemiBold / Bold (w600 / w700), tight letter spacing (-0.02em).
  * Body: Regular / Medium (w400 / w500).
* **Arabic (Scripture, Dhikr & Hadith):** `Amiri` or `Scheherazade New`
  * Line height: minimum `1.8` to avoid vowel/diacritic clipping.
  * Weight: Bold (`w700`) for headers, Regular (`w400`) for verse text.

---

## 3. Strict 1-Word Navigation & UI Dictionary (No AI Slop)

| Feature | Tab / Label | Micro-State Labels |
| :--- | :--- | :--- |
| **Bottom Nav** | `Prayers` \| `Qibla` \| `Quran` \| `Adhkar` \| `Tasbeeh` | — |
| **Prayer Screen** | `Fajr`, `Sunrise`, `Dhuhr`, `Asr`, `Maghrib`, `Isha` | `Next`, `Remaining`, `Location` |
| **Qibla Screen** | `Compass` | `Bearing`, `Aligned`, `Calibrate` |
| **Tasbeeh Screen**| `Counter` | `Tap`, `Reset`, `Target`, `Cycle` |
| **Quran Screen**  | `Surah`, `Juz` | `Read`, `Listen`, `Bookmark` |
| **Adhkar Screen** | `Morning`, `Evening` | `Done`, `Repeat` |
| **Hadith Card**   | `Hadith` | `Share`, `Reference` |

---

## 4. UI/UX Rules
1. **No clutter**: Ample whitespace around prayer cards. Never overcrowd with decorative ornaments.
2. **Tactile feedback**: Every tasbeeh tap and Qibla alignment triggers clean system haptic feedback.
3. **Adaptive RTL**: When Arabic language is selected, entire layout mirrors naturally using Flutter's native `Directionality`.
