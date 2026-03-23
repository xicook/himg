# HIMG (Hex Image Format)

HIMG is a simple image format where every pixel is stored as readable HEX values.

Instead of compression or binary encoding, HIMG stores raw RGB data in plain text.

---

## Example

HIMG
4 2
FF0000 00FF00 0000FF FFFF00
FFFFFF 000000 808080 FF00FF

Each value represents one pixel in RGB format:

- FF0000 → Red
- 00FF00 → Green
- 0000FF → Blue

---

## Features

- Human-readable image format
- No compression (.himg)
- Compressed version available (.himgc)
- Pure HEX color values
- Easy to parse
- Works directly in the browser

---

## Web Tool (Official)

Use the online tool:

https://xicook.github.io/himg/

### Features

- Open .himg and .himgc
- Convert image → HIMG
- Preview .himg images
- Download .himg
- Download compressed .himgc

---

## HIMGC (Compressed Format)

.himgc is the compressed version of .himg.

- Based on gzip compression
- Much smaller file size
- Not human-readable
- Fully compatible with .himg (auto-decompressed in the tool)

---

## Deprecated

«[!WARNING]
The old Python tools (including generate.py) were experimental and have been discontinued.
The official way to use HIMG is now through the web tool.»

---

## Format Specification

HIMG
<width> <height>
<pixel row 1>
<pixel row 2>
...

### Pixel format

RRGGBB

- 6-digit HEX
- No #
- Space-separated

---

## Limitations

«[!NOTE]
HIMG is not optimized for performance or file size.»

- Large file sizes (.himg)
- No compression in base format
- No transparency support (yet)
- Slow for high resolutions

---

## Future Ideas

- RGBA support
- Custom compression (beyond gzip)
- Viewer improvements
- Image editor
- Drag & drop support

---

## Why

HIMG is a simple project to demonstrate how image data can be represented in a human-readable way.

---

## License

""License: Public Domain" (https://img.shields.io/badge/license-Public%20Domain-blue)" (./LICENSE)
