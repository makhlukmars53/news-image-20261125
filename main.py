"""Entry program: copy the repo's image to the output directory.

The competition runs this program twice and both runs must write the same
bytes, so it copies entry.png verbatim instead of re-drawing it. The copy
is checked by size afterwards, so a truncated write fails loudly.
"""
import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"

def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    dest = out / "entry.png"
    shutil.copyfile(SRC, dest)
    if dest.stat().st_size != SRC.stat().st_size:
        raise SystemExit("copy size mismatch")
    print("wrote", dest, dest.stat().st_size, "bytes")

if __name__ == "__main__":
    main()
