# Croppa

**Split dual-page PDF spreads into sequential single pages.**

Croppa takes a PDF where each page is a two-page spread (left + right), crops each half, and merges them into one ordered PDF: left, right, left, right, …

Ideal for scanned books, magazine scans, and print-on-demand layouts that ship as spreads.

```
┌──────────┬──────────┐          ┌────┐ ┌────┐ ┌────┐ ┌────┐
│  left    │  right   │   ──►    │ L1 │ │ R1 │ │ L2 │ │ R2 │  …
│   page   │   page   │          └────┘ └────┘ └────┘ └────┘
└──────────┴──────────┘                 out.pdf
```

## Features

- Crops every page into left and right halves
- Interleaves halves into a single `out.pdf`
- Works from the command line or via an interactive prompt
- Prebuilt Windows and Linux binaries on [Releases](https://github.com/Devcon324/croppa/releases)

## Quick start (binaries)

Download the latest release from [Releases](https://github.com/Devcon324/croppa/releases):

| Platform | Asset |
|----------|--------|
| Windows (x64) | `croppa-windows-amd64.exe` |
| Linux (x64) | `croppa-linux-amd64` |

```bash
# Windows
croppa-windows-amd64.exe my-spread.pdf

# Linux
chmod +x croppa-linux-amd64
./croppa-linux-amd64 my-spread.pdf
```

## Install from source

Requires Python 3.8+ and [PyPDF2](https://pypdf2.readthedocs.io/).

```bash
git clone https://github.com/Devcon324/croppa.git
cd croppa
pip install -r requirements.txt
```

## Usage

**Pass a file as an argument:**

```bash
python croppa.py my-spread.pdf
```

**Or run interactively** (you’ll be prompted for the filename):

```bash
python croppa.py
```

### Output

| File        | Description                                      |
|-------------|--------------------------------------------------|
| `left.pdf`  | Left half of every input page                    |
| `right.pdf` | Right half of every input page                   |
| `out.pdf`   | Final interleaved PDF (left → right → left → …)  |

Files are written to the **current working directory**.

## Build a Windows executable

With [PyInstaller](https://pyinstaller.org/) installed:

```bash
pip install pyinstaller
python -m PyInstaller --onefile --icon=croppa_icon.ico croppa.py
```

Or use the included spec file:

```bash
pyinstaller croppa.spec
```

The binary will appear under `dist/croppa.exe`.

## Project layout

```
croppa.py          # main script
croppa.spec        # PyInstaller config
croppa_icon.ico    # app icon
croppa_icon.jpg    # icon source
requirements.txt
README.md
```

## License

MIT — see [LICENSE](LICENSE).

---

Made by [Devcon324](https://github.com/Devcon324)
