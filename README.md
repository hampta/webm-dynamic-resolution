# Webm dynamic resolution

## Create cursed video for discord
**Video examples:**
 - https://cdn.discordapp.com/attachments/942477358613540916/1002718193976094871/temp.webm
 - https://cdn.discordapp.com/attachments/942477358613540916/1002708609651708024/output.webm
 - https://cdn.discordapp.com/attachments/942477358613540916/1002715505544667187/temp.webm
 - https://cdn.discordapp.com/attachments/984219336648556544/1002711077865402398/output.webm
 - https://cdn.discordapp.com/attachments/984219336648556544/1002710813661990953/output.webm
 - https://cdn.discordapp.com/attachments/984219336648556544/1002722110118047744/kafif.webm

### How to use

#### Installing FFmpeg

Before using `webm-dynamic-resolution`, FFmpeg must be installed and accessible via the `$PATH` environment variable.

There are a variety of ways to install FFmpeg, such as the [official download links](https://ffmpeg.org/download.html), or using your package manager of choice (e.g. `sudo apt install ffmpeg` on Debian/Ubuntu, `brew install ffmpeg` on OS X, etc.).

Regardless of how FFmpeg is installed, you can check if your environment path is set correctly by running the `ffmpeg` command from the terminal, in which case the version information should appear, as in the following example (truncated for brevity):

```
$ ffmpeg
ffmpeg version 4.2.4-1ubuntu0.1 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 9 (Ubuntu 9.3.0-10ubuntu2)
```
**Windows**:
```
git clone https://github.com/hampta/webm-dynamic-resolution
cd webm-dynamic-resolution
pip install requirements.txt
Paste video.mp4 for random scale mode or image.png for Press Mode to webm-dynamic-resolution directory
python main.py
```
**Linux**
```
git clone https://github.com/hampta/webm-dynamic-resolution
cd webm-dynamic-resolution
pip3 install requirements.txt
Paste video.mp4 for random scale mode or image.png for Press Mode to webm-dynamic-resolution directory
python3 main.py
```

