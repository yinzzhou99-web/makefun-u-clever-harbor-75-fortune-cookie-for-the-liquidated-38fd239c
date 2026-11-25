"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes a single fortune-cookie line to /output/entry.txt.
The line is the whole entry: oracle voice first, punchline last.
Standard library only, no network, deterministic.
"""

import os

LINE = "Your lucky numbers are the ones you sold at the bottom. The cookie has no refund policy."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
