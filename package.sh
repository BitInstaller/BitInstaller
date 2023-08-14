# package up the executible into a volume

mkdir dist/dmg
mv dist/BitInstaller.app dist/dmg/BitInstaller.app

create-dmg \
  --volname "BitInstaller" \
  --volicon "logo.png" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "BitInstaller.app" 175 120 \
  --hide-extension "BitInstaller.app" \
  --app-drop-link 425 120 \
  "dist/BitInstaller.dmg" \
  "dist/dmg/"