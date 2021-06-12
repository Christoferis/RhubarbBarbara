# RhubarbBarbara

An Application intended to be used with Rhubarb Lip Sync

<https://github.com/DanielSWolf/rhubarb-lip-sync>

With the information given by Rhubarb, this can generate a video out of images, the images being the different Liptypes (A-X)

Under Developement

RhubarbBarbara is an app made to create Mouthanimations from Audio data using MoviePy and Rhubarb Lip Sync. Current version is 1.0 and is under development.

## Installation Tutorial

1. Download the latest version of Rhubarb Lip Sync from [here](https://github.com/DanielSWolf/rhubarb-lip-sync/releases/tag/v1.10.0)
2. Download the latest version of this by going to the [tags](https://github.com/Christoferis/RhubarbBarbara/tags) section
3. Run the installation script (installer_win.py)
    - 3a. Enter the path of the Rhubarb Lip Sync executable (ex.: D:\Documents\rhubarb-lip-sync-1.10.0-win32\rhubarb-lip-sync-1.10.0-win32\rhubarb.exe)
    - 3b. Specify a standard directory if desired (Type NONE to skip this)
    - 3c. Let the installer install the packages needed by typing "y"

### Usage

Upon opening, you are greeted with the main window which specifies the mouth types (the last three are optional)
Fill in your Mouth shapes (use images in icons as example) and specify the audio on the bottom right.
Next to the audio, specify an output location and method (currently: MP4 (not transparent), AVI (pseudo-transparent) and Image Sequence (fully transparent))

Click on start (the green Button) if you're ready.

---

*RhubarbBarbara only outputs a video with the mouth Animation without any video, Motion Tracking, Footage and alignment has to be done outside of RhubarbBarbara*

#### Development

RhubarbBarbara is currently under development and help would be appreciated. We try to do regular updates

**Roadmap:**

    - Complete redesign of the ui for better navigation and more features
    - More features: FPS, Resolution and bitrate
    - Add support for custom Backgrounds + Placement of mouth In-Editor
    - Script support + Emotions based on script (idea no real feature implementation planned)
    - Better Performance: 
        Better Memory Management, split into chunks
        Multithreaded Video Encoding
