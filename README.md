# MPWave

A lightweight desktop app to convert multimedia files between **MP3**, **WAV**, and **MP4** (audio extraction), built with Python, [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), and [FFmpeg](https://ffmpeg.org/).

## Features

- Multi-format conversion: MP3 ↔ WAV, and MP4 → audio (extracts the audio track, discarding video)
- Explicit output format selection via dropdown — no more guesswork on what you'll get
- Modern UI built with CustomTkinter (native dark/light mode support), split into **Input** and **Output** panels for a clearer workflow
- Custom output folder selection (defaults to the source file's folder if none is chosen)
- Non-blocking conversion using threading, so the UI stays responsive
- Packaged as a standalone `.exe` — no Python or FFmpeg installation required on the user's end

## How It Works

MPWave uses **FFmpeg** under the hood (via `subprocess`) to handle the actual encoding/decoding, wrapped in a simple CustomTkinter interface. When the input is a video container (like MP4), FFmpeg is called with the `-vn` flag to strip the video stream and keep only the audio. The conversion runs on a background thread to avoid freezing the UI, with a progress indicator shown while the file is processed.

Supported formats are declared in a simple lookup table in `converter.py`, so adding a new format (e.g. FLAC, AAC, MOV) is a matter of extending that table rather than rewriting the conversion logic.

## Project Structure

```
MPWave/
├── main.py               # Entry point, launches the app
├── ui.py                  # ConvertApp class — UI widgets and event handlers
├── converter.py             # Core conversion logic (FFmpeg subprocess calls)
├── ffmpeg.exe                # FFmpeg binary — NOT included in this repo, see below
├── LICENSES/
│   └── ffmpeg-LICENSE.txt      # GPLv3 license text for the bundled FFmpeg build
└── requirements.txt              # Python dependencies
```

## Requirements (for running from source)

- Python 3.10+
- `customtkinter`

```bash
pip install customtkinter
```

FFmpeg is called directly via `subprocess`, so no additional Python audio libraries are required.

**FFmpeg is not included in this repository** (to keep it lightweight and avoid redistributing a large GPL-licensed binary via version control). Before running, download it yourself:

1. Get the "release essentials" build from [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/).
2. Extract `ffmpeg.exe` from the `bin/` folder inside the zip.
3. Place it in the project root, next to `converter.py`.

## Usage

```bash
python main.py
```

1. On the **left panel (Input)**, click **Select File** and choose an `.mp3`, `.wav`, or `.mp4` file.
2. On the **right panel (Output)**, pick the desired output format from the dropdown, and optionally click **Select Destination Folder** to choose where the converted file will be saved.
3. Click **Convert**.

## Building the Executable

MPWave can be packaged into a standalone Windows `.exe` using [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "ffmpeg.exe;." --collect-all customtkinter main.py
```

The resulting executable will be located in the `dist/` folder and can be shared without requiring Python, CustomTkinter, or FFmpeg to be installed separately.

## Notes

- Some antivirus software may flag PyInstaller-built executables as a false positive — this is a known behavior of the packaging tool, not a sign of malicious code.
- Currently supports MP3, WAV, and MP4 (audio extraction only — no video-to-video conversion) as input formats.

## Author

Built by [Julito-Dev](https://github.com/Julito-Dev).

## License

The code in this repository (MPWave itself) is open source and available for personal and educational use.

This project relies on **FFmpeg**, which is **not distributed in this repo** but is required to run/build it (see Requirements above). Depending on the build used, FFmpeg is licensed under LGPL or GPL — the "essentials" build recommended here is **GPLv3**. If you package and share a compiled `.exe` that bundles `ffmpeg.exe`, you must include the FFmpeg license text and a note on where to obtain its corresponding source code. A copy of the GPLv3 text is provided in [`LICENSES/ffmpeg-LICENSE.txt`](LICENSES/ffmpeg-LICENSE.txt) for this purpose.

FFmpeg project: [ffmpeg.org](https://ffmpeg.org/)