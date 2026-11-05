-- SQLite Local Offline Schema (Bundled within FlutterFlow assets)
-- Zero network cost, zero latency offline reading inside mosques

-- 1. Quran Surahs & Verses
CREATE TABLE IF NOT EXISTS local_surahs (
    id INTEGER PRIMARY KEY,
    number INTEGER UNIQUE NOT NULL,
    name_ar TEXT NOT NULL,
    name_en TEXT NOT NULL,
    meaning TEXT NOT NULL,
    total_verses INTEGER NOT NULL,
    revelation_type TEXT NOT NULL -- 'Meccan' or 'Medinan'
);

CREATE TABLE IF NOT EXISTS local_ayahs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surah_number INTEGER NOT NULL,
    verse_number INTEGER NOT NULL,
    text_uthmani TEXT NOT NULL,
    transliteration TEXT,
    translation_en TEXT NOT NULL,
    juz_number INTEGER NOT NULL,
    is_bookmarked INTEGER DEFAULT 0,
    FOREIGN KEY (surah_number) REFERENCES local_surahs(number)
);

-- 2. Daily Adhkar & Duas (Hisn al-Muslim)
CREATE TABLE IF NOT EXISTS local_adhkar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL, -- 'morning', 'evening', 'after_prayer'
    text_arabic TEXT NOT NULL,
    transliteration TEXT,
    translation_en TEXT NOT NULL,
    target_count INTEGER NOT NULL DEFAULT 1,
    reference TEXT NOT NULL,
    order_index INTEGER DEFAULT 0
);

-- 3. Verified Daily Hadiths
CREATE TABLE IF NOT EXISTS local_hadiths (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arabic TEXT NOT NULL,
    translation_en TEXT NOT NULL,
    narrator TEXT NOT NULL,
    source TEXT NOT NULL,
    topic TEXT NOT NULL
);

-- 4. User Preferences & Offline App State
CREATE TABLE IF NOT EXISTS local_user_state (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ========================================================
-- Supabase Cloud Schema (PostgreSQL for Scalability & Phase 2)
-- ========================================================

-- Remote Daily Content (Client can push new Hadiths/Announcements from Supabase Studio)
CREATE TABLE IF NOT EXISTS public.daily_announcements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Phase 2 User Profiles (Cloud Sync for Bookmarks & Streaks)
CREATE TABLE IF NOT EXISTS public.user_profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    email TEXT,
    display_name TEXT,
    preferred_calculation_method INTEGER DEFAULT 4, -- 4: Umm al-Qura
    last_active_at TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.user_bookmarks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES public.user_profiles(id) ON DELETE CASCADE,
    surah_number INTEGER NOT NULL,
    verse_number INTEGER NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
