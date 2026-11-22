#!/usr/bin/env python3
"""The picture that tastes of one ingredient.

Reads the hero image (asset.png, a JPEG-encoded photograph of one ripe
mango) from the repository root, validates it against the competition
gate, and writes it to /output/entry.png.

Standard library only. No network. Deterministic.
"""

import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIM = 1024
ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "asset.png")
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.png")


def read_jpeg_size(data):
    """Return (width, height) from a JPEG byte string, or None."""
    if len(data) < 4 or data[0:2] != b"\xff\xd8":
        return None
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height = struct.unpack(">H", data[i + 5:i + 7])[0]
            width = struct.unpack(">H", data[i + 7:i + 9])[0]
            return (width, height)
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg_len = struct.unpack(">H", data[i + 2:i + 4])[0]
        i += 2 + seg_len
    return None


def read_png_size(data):
    """Return (width, height) from a PNG byte string, or None."""
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return (width, height)


def main():
    with open(ASSET, "rb") as f:
        data = f.read()

    if len(data) > MAX_BYTES:
        sys.exit("asset too large: %d bytes (max %d)" % (len(data), MAX_BYTES))

    size = read_png_size(data) or read_jpeg_size(data)
    if size is None:
        sys.exit("asset is not a whole PNG or JPEG image")
    width, height = size
    if width > MAX_DIM or height > MAX_DIM:
        sys.exit("asset too big: %dx%d (max %dx%d)"
                 % (width, height, MAX_DIM, MAX_DIM))

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "wb") as f:
        f.write(data)

    print("wrote %s (%dx%d, %d bytes)" % (OUT_PATH, width, height, len(data)))


if __name__ == "__main__":
    main()
