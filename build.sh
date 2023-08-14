# Script to compile the program into an executible

pyinstaller --name 'BitInstaller' \
            --icon 'logo.png' \
            --windowed  \
            --add-data='./logo.png:.' \
            main.py