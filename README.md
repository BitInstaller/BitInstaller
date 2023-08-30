# BitInstaller <img src="https://raw.githubusercontent.com/BitInstaller/BitInstaller/main/AppIcon.png" alt="OSXLogo" width="50" style="vertical-align: middle; margin-bottom: 0px;" />

The Official BitInstaller Repository. Create Windows Installation Media On MacOS

![App Screenshot](https://raw.githubusercontent.com/BitInstaller/BitInstaller/main/github/Screenshot.png)

WARNING: POORLY WRITTEN CODE AHEAD

# Project Description:

  BitInstaller is a basic GUI application that burns windows ISO's on MacOS
  
**Note: This project is currently in heavy development, with frequent updates and improvements being made.**

**Features:**

- **User-Friendly Interface:** The application has a minimalistic and clean GUI

- **Cross-Platform Convenience:** While being developed using Python, the long-term vision includes the possibility of porting the application to the Swift programming language for better MacOS compatability.

- **Bootable Windows Media:** Easily create bootable Windows installation media for use on various devices.

# Installation
*Binaries are finally here!*
1. Go to the Github releses
2. Download BitInstaller.dmg
3. Double-click on the DMG and press open
4. Drag the app into the Applications folder
 
**Note(the following is because double clicking will result in an unverified developer error)**

5. Go to the Applications folder on Finder
6. Right-click on BitInstaller and select open
4. Accept any unverified developer warnings

# Usage:

1. Launch BitInstaller.
2. Select the Windows ISO file you wish to burn.
3. Choose your target storage media (e.g., USB drive).
4. Sit back and wait, this can take up to half an hour depending on your device
5. If the program says "Splitting Wimfile" just wait. This process takes a very long time

# Building:

To build BitInstaller on your macOS system from source, follow these simple steps:

1. Clone the repository: `git clone https://github.com/ShoneGK/BitInstaller`
2. Navigate to the project directory
3. Run the main script: `python main.py`

*Note: to package up the project into a .dmg run the following command*
`sh build.sh && sh package.sh`

**Future Developments:**

As improvements are made, our future goals include:

- Offering a comprehensive range of burning options and customization settings.
  
- Exploring the possibility of porting the application to the Swift programming language.

---

Feel free to contribute!
