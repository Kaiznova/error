[app]

# (str) Title of your application
title = Kaizotool

# (str) Package name
package.name = kaizotool

# (str) Package domain (needed for android/ios packaging)
package.domain = com.example  # Change this to your unique domain

# (str) Source code directory where the main.py and other source files live
source.dir = %(source.dir)s

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = kivy, cryptography, six, kivymd, pillow

# (str) Supported orientation (portrait, landscape, or all)
orientation = portrait

# (str) The path to your source code directory
# Replace /path/to/your/source/code with the actual path
# e.g., /home/user/myapp
source.root = /path/to/your/source/code

[buildozer]

# (list) List of build dependencies (comma-separated)
deps = python3,kivy,kivymd,pillow

# (str) Path to the Android NDK directory
android.ndk_path = /home/user/Android/Sdk/ndk/21.3.6528147

# (int) Android NDK version to use
android.ndk_version = 21.3.6528147

# (int) Android SDK version to use
android.sdk = 28

# (str) Android build tool version to use
android.build_tools = 28.0.3

# (int) Log level (0 = error only, 1 = info, 2 = debug with verbosity)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
