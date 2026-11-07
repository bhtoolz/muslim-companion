import os, sys

sys.stdout.reconfigure(encoding="utf-8")

index_path = "C:/Users/DELL/.gemini/antigravity/scratch/muslim_companion/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract clean <head>
head_start = html.find("<head>")
head_end = html.find("</head>")
assert head_start != -1 and head_end != -1, "head markers not found"
head_html = html[head_start:head_end + 7]

# 2. Extract #deviceScreen inner content
screen_start_marker = '<div id="deviceScreen"'
screen_start = html.find(screen_start_marker)
assert screen_start != -1, "screen_start not found"

home_bar_marker = '<!-- Device Home Indicator Bar -->'
screen_end = html.find(home_bar_marker)
assert screen_end != -1, "home_bar_marker not found"

screen_html = html[screen_start:screen_end].strip()

# Adjust #deviceScreen for Android:
# Remove rounded corners & borders since Android phone already has hardware screen
screen_html = screen_html.replace(
    'class="w-full h-full bg-[#FAF8F5] text-slate-800 rounded-[38px] overflow-hidden flex flex-col relative transition-all duration-200"',
    'class="w-full h-full min-h-screen bg-[#FAF8F5] text-slate-800 flex flex-col relative overflow-hidden"'
)

# On real Android, hide the fake iOS status bar (09:41 clock & battery)
old_status_bar_tag = '<div id="statusBarContainer" class="pt-3 px-5 pb-1 flex items-center justify-between text-[11px] font-bold text-slate-600 dark:text-slate-400 z-40 select-none">'
if old_status_bar_tag in screen_html:
    # Replace with a hidden status bar container (keeps IDs intact so JS doesn't error)
    screen_html = screen_html.replace(
        old_status_bar_tag,
        '<div id="statusBarContainer" class="hidden">'
    )

# Adjust bottom navigation bar padding for Android navigation bar
old_bottom_nav = 'id="bottomNav" class="absolute bottom-0 left-0 right-0 bg-white/95 dark:bg-slate-900/95 border-t border-slate-200/80 dark:border-slate-800 flex items-center justify-around py-2 px-1 backdrop-blur-md z-40"'
new_bottom_nav = 'id="bottomNav" class="absolute bottom-0 left-0 right-0 bg-white/95 dark:bg-slate-900/95 border-t border-slate-200/80 dark:border-slate-800 flex items-center justify-around pt-2 pb-3.5 px-1 backdrop-blur-md z-40"'
if old_bottom_nav in screen_html:
    screen_html = screen_html.replace(old_bottom_nav, new_bottom_nav)

# Close #deviceScreen
screen_html = screen_html + "\n  </div>"

# 3. Extract scripts
script_start = html.find("<script>", screen_end)
script_end = html.rfind("</body>")
assert script_start != -1 and script_end != -1, "script markers not found"
script_html = html[script_start:script_end].strip()

# Android hardware back button handler
android_back_handler = """
    // Native Android Hardware Back Button Hook
    window.handleAndroidBack = function() {
      const modals = [
        { id: "settingsModal", fn: closeSettingsModal },
        { id: "islamicCalendarModal", fn: closeCalendarModal },
        { id: "surahIndexModal", fn: closeSurahIndexModal },
        { id: "bookmarksModal", fn: closeBookmarksModal },
        { id: "namesOfAllahModal", fn: closeNamesOfAllahModal },
        { id: "cityModal", fn: closeCityModal }
      ];
      for (const m of modals) {
        const el = document.getElementById(m.id);
        if (el && !el.classList.contains("hidden")) {
          m.fn();
          return true;
        }
      }
      if (currentTab !== 'prayers') {
        switchTab('prayers');
        return true;
      }
      return false;
    };
"""

script_html = script_html.replace("window.onload = init;", android_back_handler + "\n    window.onload = init;")

mobile_page = f"""<!DOCTYPE html>
<html lang="en" class="h-full">
{head_html}
<body class="w-full h-full m-0 p-0 overflow-hidden bg-[#0A1612] text-slate-800 select-none">
{screen_html}
{script_html}
</body>
</html>
"""

# Write to temp_test_android assets
assets_dir = "C:/Users/DELL/.gemini/antigravity/scratch/muslim_companion/temp_test_android/app/src/main/assets"
os.makedirs(assets_dir, exist_ok=True)

out_index = os.path.join(assets_dir, "index.html")
with open(out_index, "w", encoding="utf-8") as f:
    f.write(mobile_page)

print(f"Generated clean mobile asset: {out_index} ({os.path.getsize(out_index)} bytes)!")

# Sync assets
src_assets = "C:/Users/DELL/.gemini/antigravity/scratch/muslim_companion/assets"
dst_assets = os.path.join(assets_dir, "assets")
if os.path.exists(src_assets):
    import shutil
    shutil.copytree(src_assets, dst_assets, dirs_exist_ok=True)
    print("Synced assets to Android assets folder!")
