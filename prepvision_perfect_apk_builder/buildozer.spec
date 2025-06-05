[app]
title = PrepVisionAI
package.name = prepvision
package.domain = org.prepvision
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
requirements = python3,kivy,pillow,sdl2_ttf==2.0.15,kivymd
orientation = portrait
fullscreen = 0
android.presplash_color = #FAFAFA
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,INTERNET
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.arch = arm64-v8a
icon.filename = prepvision_launcher_icon.png

# Material Design theme
android.material_theme = Blue

# Optimize APK size
android.enable_androidx = True
android.enable_maven_download = True
android.enable_pip_download = True
android.whitelist = lib-dynload/termios.so,lib-dynload/_imaging.so,lib-dynload/_imagingft.so
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

# Additional settings for better performance
android.allow_backup = True
android.backup_rules = @xml/backup_rules
android.enable_screens = True

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = true