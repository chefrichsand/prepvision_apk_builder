[app]
title = PrepVisionAI
package.name = prepvision
package.domain = org.prepvision
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pillow,sdl2_ttf==2.0.15
orientation = portrait
fullscreen = 0
android.presplash_color = #FFFFFF
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.arch = arm64-v8a
icon.filename = prepvision_launcher_icon.png

# Optimize APK size
android.enable_androidx = True
android.enable_maven_download = True
android.enable_pip_download = True
android.whitelist = lib-dynload/termios.so

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = true