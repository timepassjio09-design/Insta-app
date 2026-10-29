[app]
title = Insta Manager
package.name = instamanager
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.1
android.accept_sdk_license_agreements = True
android.permissions = INTERNET
p4a.branch = develop
