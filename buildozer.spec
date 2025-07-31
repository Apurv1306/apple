[app]
# (str) Title of your application
title = Face App

# (str) Package name
package.name = faceapp

# (str) Package domain (reverse DNS style)
package.domain = org.archtech.faceapp

# (str) Source code where the main.py & other files are located
source.dir = .

# (str) Filename of the main entry point of your app
source.main = flaskapk.py

# (list) Source file extensions to include (comma-separated)
source.include_exts = py,png,jpg,kv,json,xml,mp3

# (list) Application requirements
requirements = python3,kivy,kivymd,opencv-python,numpy,requests,pandas,fpdf,pygame,edge-tts,apscheduler

# (str) Icon of the application (leave empty to ignore)
icon.filename =

# (list) Permissions your app needs
android.permissions = INTERNET,CAMERA

# (bool) If True, allow access to the internet
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Target API
android.sdk = 33

# (int) Android NDK version to use (auto-update as available)
android.ndk = 25b

# (str) Android NDK directory override (optional)
# android.ndk_path =

# (int) Android NDK API level
android.ndk_api = 21

# (list) Android SDK Build Tools version
android.sdk_build_tools = 33.0.0

# (bool) Copy libraries inside APK (True helps reduce problems)
android.copy_libs = True

# (list) Additional android libraries to add - if using Java code (empty)
# android.add_jars =

# (str) Additional source folders to include in the package
# android.add_src =

# (str) Presplash image (empty if none)
presplash.filename =

# (str) Android logcat filters to use (optional)
android.logcat_filters = *:S python:D

# (bool) If True, automatically accept all licenses during build (recommended)
android.accept_sdk_license = True

# (bool) Use `-d` debug flag with buildozer android debug
android.debug = True

# (bool) If True, disable automatic build dependencies (default False)
# android.disable_rebuild = False

# (str) Custom buildozer log level (default 'info')
log_level = 2

# (bool) Copy assets instead of symlinks (default False)
android.copy_assets = False
