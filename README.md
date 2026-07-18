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
- Managed with [uv](https://docs.astral.sh/uv/)

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

Requires [uv](https://docs.astral.sh/uv/) (Python 3.8+ is pulled in automatically if needed).

```bash
git clone https://github.com/Devcon324/croppa.git
cd croppa
uv sync
```

## Usage

**With uv (recommended):**

```bash
uv run croppa my-spread.pdf
```

**Or run the script directly after syncing:**

```bash
uv run python croppa.py my-spread.pdf
```

**Interactive mode** (prompted for the filename):

```bash
uv run croppa
```

### Output

| File        | Description                                      |
|-------------|--------------------------------------------------|
| `left.pdf`  | Left half of every input page                    |
| `right.pdf` | Right half of every input page                   |
| `out.pdf`   | Final interleaved PDF (left → right → left → …)  |

Files are written to the **current working directory**.

## Build native binaries

Install the build dependency group, then use PyInstaller:

```bash
uv sync --group build

# Windows
uv run pyinstaller --onefile --name croppa-windows-amd64 --icon=croppa_icon.ico croppa.py

# Linux
uv run pyinstaller --onefile --name croppa-linux-amd64 croppa.py
```

Or use the included spec file:

```bash
uv run pyinstaller croppa.spec
```

Binaries land in `dist/`.

## Project layout

```
croppa.py          # main script
pyproject.toml     # project metadata + deps (uv)
uv.lock            # locked dependency versions
croppa.spec        # PyInstaller config
croppa_icon.ico    # app icon
croppa_icon.jpg    # icon source
README.md
```

## License

MIT — see [LICENSE](LICENSE).

---

Made by [Devcon324](https://github.com/Devcon324)
