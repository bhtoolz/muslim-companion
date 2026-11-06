import sys, os, time, shutil
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")

output_dirs = [
    r"C:\Users\DELL\.gemini\antigravity\scratch\muslim_companion\assets\screens",
    r"C:\Users\DELL\.gemini\antigravity\scratch\muslim_companion\preview\assets\screens"
]
for d in output_dirs:
    os.makedirs(d, exist_ok=True)

primary_dir = output_dirs[0]

screens_definitions = [
    {
        "id": "prayers",
        "setup": "closeAllModals(); switchTab('prayers');"
    },
    {
        "id": "quran",
        "setup": "closeAllModals(); switchTab('quran');"
    },
    {
        "id": "directory",
        "setup": "closeAllModals(); openSurahIndexModal();"
    },
    {
        "id": "adhkar",
        "setup": "closeAllModals(); switchTab('adhkar');"
    },
    {
        "id": "calendar",
        "setup": "closeAllModals(); openCalendarModal();"
    },
    {
        "id": "qibla",
        "setup": "closeAllModals(); switchTab('qibla');"
    },
    {
        "id": "tasbeeh",
        "setup": "closeAllModals(); switchTab('tasbeeh');"
    },
    {
        "id": "names",
        "setup": "closeAllModals(); openNamesModal('allah');"
    },
    {
        "id": "settings_audio",
        "setup": "closeAllModals(); openSettingsModal('reciters');"
    },
    {
        "id": "settings_fonts",
        "setup": "closeAllModals(); openSettingsModal('display');"
    }
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 950}, device_scale_factor=2)
    
    print("Navigating to http://localhost:4000/...")
    page.goto("http://localhost:4000/", wait_until="networkidle")
    time.sleep(1)

    page.evaluate('''() => {
        window.closeAllModals = function() {
            try { closeCityModal(); } catch(e){}
            try { closeSettingsModal(); } catch(e){}
            try { closeSurahIndexModal(); } catch(e){}
            try { closeBookmarksModal(); } catch(e){}
            try { closeNamesOfAllahModal(); } catch(e){}
            try { closeCalendarModal(); } catch(e){}
            try { closeFlutterflowModal(); } catch(e){}
        };
    }''')

    # ==========================
    # 1. CAPTURE ARABIC SCREENS
    # ==========================
    print("\n--- SWITCHING TO ARABIC MODE ---")
    page.evaluate('''() => {
        if (!isArabic) toggleLang();
    }''')
    time.sleep(0.5)

    for s in screens_definitions:
        sid = s["id"]
        print(f"Capturing Arabic: screen_{sid}_ar.png...")
        page.evaluate(s["setup"])
        time.sleep(0.4)
        device_el = page.locator("#deviceScreen")
        target_path_ar = os.path.join(primary_dir, f"screen_{sid}_ar.png")
        target_path_base = os.path.join(primary_dir, f"screen_{sid}.png")
        device_el.screenshot(path=target_path_ar)
        shutil.copyfile(target_path_ar, target_path_base)
        print(f"  ✓ Saved screen_{sid}_ar.png ({os.path.getsize(target_path_ar)} bytes)")

    # ==========================
    # 2. CAPTURE ENGLISH SCREENS
    # ==========================
    print("\n--- SWITCHING TO ENGLISH MODE ---")
    page.evaluate('''() => {
        if (isArabic) toggleLang();
    }''')
    time.sleep(0.5)

    for s in screens_definitions:
        sid = s["id"]
        print(f"Capturing English: screen_{sid}_en.png...")
        page.evaluate(s["setup"])
        time.sleep(0.4)
        device_el = page.locator("#deviceScreen")
        target_path_en = os.path.join(primary_dir, f"screen_{sid}_en.png")
        device_el.screenshot(path=target_path_en)
        print(f"  ✓ Saved screen_{sid}_en.png ({os.path.getsize(target_path_en)} bytes)")

    # Reset simulator back to default prayers tab in Arabic
    page.evaluate('''() => {
        if (!isArabic) toggleLang();
        closeAllModals();
        switchTab('prayers');
    }''')

    browser.close()

# Mirror everything to preview/assets/screens
preview_dir = output_dirs[1]
for fname in os.listdir(primary_dir):
    src = os.path.join(primary_dir, fname)
    if os.path.isfile(src):
        dst = os.path.join(preview_dir, fname)
        shutil.copyfile(src, dst)

print("\nSuccessfully captured and synced all 20 screenshots (10 Arabic + 10 English)!")
