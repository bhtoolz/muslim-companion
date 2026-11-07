import os, sys
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

base_dir = "C:/Users/DELL/.gemini/antigravity/scratch/muslim_companion/temp_test_android/app/src/main"

# 1. Update MainActivity.kt
main_activity_path = os.path.join(base_dir, "kotlin/com/example/muslimcompanion/MainActivity.kt")
main_activity_content = '''package com.example.muslimcompanion

import android.annotation.SuppressLint
import android.os.Bundle
import android.webkit.GeolocationPermissions
import android.webkit.WebChromeClient
import android.webkit.WebResourceRequest
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.ComponentActivity
import androidx.activity.OnBackPressedCallback
import androidx.activity.enableEdgeToEdge

class MainActivity : ComponentActivity() {

    private lateinit var webView: WebView

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        webView = WebView(this).apply {
            settings.apply {
                javaScriptEnabled = true
                domStorageEnabled = true
                databaseEnabled = true
                allowFileAccess = true
                allowContentAccess = true
                mediaPlaybackRequiresUserGesture = false
                cacheMode = WebSettings.LOAD_DEFAULT
                useWideViewPort = true
                loadWithOverviewMode = true
            }

            isVerticalScrollBarEnabled = false
            isHorizontalScrollBarEnabled = false

            webChromeClient = object : WebChromeClient() {
                override fun onGeolocationPermissionsShowPrompt(
                    origin: String,
                    callback: GeolocationPermissions.Callback
                ) {
                    callback.invoke(origin, true, false)
                }
            }

            webViewClient = object : WebViewClient() {
                override fun shouldOverrideUrlLoading(
                    view: WebView?,
                    request: WebResourceRequest?
                ): Boolean {
                    return false
                }
            }

            loadUrl("file:///android_asset/index.html")
        }

        setContentView(webView)

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                webView.evaluateJavascript("window.handleAndroidBack ? window.handleAndroidBack() : false") { result ->
                    if (result != "true") {
                        isEnabled = false
                        onBackPressedDispatcher.onBackPressed()
                    }
                }
            }
        })
    }

    override fun onResume() {
        super.onResume()
        webView.onResume()
    }

    override fun onPause() {
        super.onPause()
        webView.onPause()
    }

    override fun onDestroy() {
        webView.destroy()
        super.onDestroy()
    }
}
'''
with open(main_activity_path, "w", encoding="utf-8") as f:
    f.write(main_activity_content)
print("Updated MainActivity.kt!")

# 2. Update AndroidManifest.xml
manifest_path = os.path.join(base_dir, "AndroidManifest.xml")
manifest_content = '''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.VIBRATE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:usesCleartextTraffic="true"
        android:windowSoftInputMode="adjustResize"
        android:theme="@style/Theme.MuslimCompanion">
        <activity
            android:name=".MainActivity"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
'''
with open(manifest_path, "w", encoding="utf-8") as f:
    f.write(manifest_content)
print("Updated AndroidManifest.xml!")

# 3. Update strings.xml
strings_path = os.path.join(base_dir, "res/values/strings.xml")
with open(strings_path, "w", encoding="utf-8") as f:
    f.write('''<resources>
    <string name="app_name">Muslim Companion</string>
</resources>
''')
print("Updated strings.xml!")

# 4. Generate Launcher Icons
icon_src = "C:/Users/DELL/.gemini/antigravity/scratch/muslim_companion/preview/assets/app_icon.png"
if os.path.exists(icon_src):
    img = Image.open(icon_src).convert("RGBA")
    sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192
    }
    for folder, size in sizes.items():
        folder_path = os.path.join(base_dir, "res", folder)
        os.makedirs(folder_path, exist_ok=True)
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(os.path.join(folder_path, "ic_launcher.png"), "PNG")
        resized.save(os.path.join(folder_path, "ic_launcher_round.png"), "PNG")
    print("Generated all launcher icons in res/mipmap-*!")
