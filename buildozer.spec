[app]
title = Insta Manager
package.name = instamanager
package.domain = org.test.insta
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.1.0
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
android.ant = auto

p4a.branch = master
