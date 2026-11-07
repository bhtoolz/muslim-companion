import os
import shutil
from PIL import Image

base_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\muslim_companion"
android_res = os.path.join(base_dir, r"temp_test_android\app\src\main\res")

fullbleed_src = os.path.join(base_dir, "icon_fullbleed.png")
round_src = os.path.join(base_dir, "icon_round.png")
foreground_src = os.path.join(base_dir, "icon_foreground.png")

img_fullbleed = Image.open(fullbleed_src).convert("RGBA")
img_round = Image.open(round_src).convert("RGBA")
img_foreground = Image.open(foreground_src).convert("RGBA")

# 1. Update Project & Web Assets
web_targets = [
    os.path.join(base_dir, "assets", "app_icon.png"),
    os.path.join(base_dir, "preview", "assets", "app_icon.png"),
    os.path.join(base_dir, "preview", "app_icon.png"),
    os.path.join(base_dir, "temp_test_android", "app", "src", "main", "assets", "assets", "app_icon.png")
]

for t in web_targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    img_fullbleed.save(t, "PNG")
    print(f"Updated web target: {t}")

# Generate favicon.ico (16, 32, 48, 64)
img_round.resize((64, 64), Image.Resampling.LANCZOS).save(
    os.path.join(base_dir, "favicon.ico"),
    format="ICO",
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]
)
shutil.copyfile(os.path.join(base_dir, "favicon.ico"), os.path.join(base_dir, "preview", "favicon.ico"))
print("Updated favicons!")

# 2. Update Android Mipmap Folders (Legacy & Adaptive Foreground)
# Standard launcher sizes: mdpi: 48, hdpi: 72, xhdpi: 96, xxhdpi: 144, xxxhdpi: 192
# Adaptive foreground sizes (108dp): mdpi: 108, hdpi: 162, xhdpi: 216, xxhdpi: 324, xxxhdpi: 432
density_config = {
    "mipmap-mdpi": (48, 108),
    "mipmap-hdpi": (72, 162),
    "mipmap-xhdpi": (96, 216),
    "mipmap-xxhdpi": (144, 324),
    "mipmap-xxxhdpi": (192, 432)
}

for folder, (icon_sz, fg_sz) in density_config.items():
    fdir = os.path.join(android_res, folder)
    os.makedirs(fdir, exist_ok=True)
    
    # Save fullbleed square ic_launcher.png (zero white, 100% emerald)
    resized_fb = img_fullbleed.resize((icon_sz, icon_sz), Image.Resampling.LANCZOS)
    resized_fb.save(os.path.join(fdir, "ic_launcher.png"), "PNG")
    
    # Save true circular ic_launcher_round.png (transparent outside circle, 100% emerald inside)
    resized_rd = img_round.resize((icon_sz, icon_sz), Image.Resampling.LANCZOS)
    resized_rd.save(os.path.join(fdir, "ic_launcher_round.png"), "PNG")
    
    # Save adaptive foreground ic_launcher_foreground.png
    resized_fg = img_foreground.resize((fg_sz, fg_sz), Image.Resampling.LANCZOS)
    resized_fg.save(os.path.join(fdir, "ic_launcher_foreground.png"), "PNG")
    
    print(f"Generated {folder}: ic_launcher.png ({icon_sz}x{icon_sz}), ic_launcher_round.png ({icon_sz}x{icon_sz}), foreground ({fg_sz}x{fg_sz})")

# 3. Create Android Background Drawable & Color
drawable_dir = os.path.join(android_res, "drawable")
os.makedirs(drawable_dir, exist_ok=True)

bg_drawable_path = os.path.join(drawable_dir, "ic_launcher_background.xml")
with open(bg_drawable_path, "w", encoding="utf-8") as f:
    f.write('''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <solid android:color="#041b12" />
</shape>
''')
print("Created ic_launcher_background.xml!")

# 4. Create Adaptive Icon XML in mipmap-anydpi-v26
anydpi_dir = os.path.join(android_res, "mipmap-anydpi-v26")
os.makedirs(anydpi_dir, exist_ok=True)

adaptive_xml_content = '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@mipmap/ic_launcher_foreground" />
</adaptive-icon>
'''

with open(os.path.join(anydpi_dir, "ic_launcher.xml"), "w", encoding="utf-8") as f:
    f.write(adaptive_xml_content)

with open(os.path.join(anydpi_dir, "ic_launcher_round.xml"), "w", encoding="utf-8") as f:
    f.write(adaptive_xml_content)

print("Created mipmap-anydpi-v26 adaptive icon XMLs!")
print("ALL ICONS DEPLOYED FLAWLESSLY!")
