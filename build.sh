# Script to compile the program into an executible

pyinstaller --name 'BitInstaller' \
            --icon 'AppIcon.png' \
            --windowed  \
            --add-data='./AppIcon.png:.' \
            --add-data='logo.png:.' \
            main.py
