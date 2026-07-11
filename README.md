# MPWave

A lightweight desktop app to convert audio files between **MP3** and **WAV** formats, built with Python, [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), and [FFmpeg](https://ffmpeg.org/).

## Features

- Bidirectional conversion: MP3 → WAV and WAV → MP3 (auto-detected from the input file)
- Modern UI built with CustomTkinter (native dark/light mode support)
- Custom output folder selection (defaults to the source file's folder if none is chosen)
- Non-blocking conversion using threading, so the UI stays responsive
- Packaged as a standalone `.exe` — no Python or FFmpeg installation required on the user's end

## How It Works

MPWave uses **FFmpeg** under the hood (via `subprocess`) to handle the actual audio decoding/encoding, wrapped in a simple CustomTkinter interface. The conversion runs on a background thread to avoid freezing the UI, with a progress indicator shown while the file is processed.

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

1. Click **Select File** and choose an `.mp3` or `.wav` file.
2. (Optional) Click **Select Destination Folder** to choose where the converted file will be saved.
3. Click **Convert**. The app automatically converts to the opposite format.

## Building the Executable

MPWave can be packaged into a standalone Windows `.exe` using [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "ffmpeg.exe;." --collect-all customtkinter main.py
```

The resulting executable will be located in the `dist/` folder and can be shared without requiring Python, CustomTkinter, or FFmpeg to be installed separately.

## Notes

- Some antivirus software may flag PyInstaller-built executables as a false positive — this is a known behavior of the packaging tool, not a sign of malicious code.
- Currently supports MP3 and WAV formats only.

## Author

Built by [Julito-Dev](https://github.com/Julito-Dev).

## License

The code in this repository (MPWave itself) is open source and available for personal and educational use.

This project relies on **FFmpeg**, which is **not distributed in this repo** but is required to run/build it (see Requirements above). Depending on the build used, FFmpeg is licensed under LGPL or GPL — the "essentials" build recommended here is **GPLv3**. If you package and share a compiled `.exe` that bundles `ffmpeg.exe`, you must include the FFmpeg license text and a note on where to obtain its corresponding source code. A copy of the GPLv3 text is provided in [`LICENSES/ffmpeg-LICENSE.txt`](LICENSES/ffmpeg-LICENSE.txt) for this purpose.

FFmpeg project: [ffmpeg.org](https://ffmpeg.org/)