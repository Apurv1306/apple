[app]
title = Face App
package.name = faceapp
package.domain = org.archtech.faceapp
source.dir = .
source.main = flaskapk.py
source.include_exts = py,png,jpg,kv,json,xml,mp3

# Your main requirements (copy exactly)
requirements = python3,kivy,kivymd,opencv-python,numpy,requests,pandas,fpdf,pygame,edge-tts,apscheduler

android.permissions = INTERNET,CAMERA

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.sdk_build_tools = 33.0.0

android.copy_libs = True
android.accept_sdk_license = True
log_level = 2
