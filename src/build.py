#!/usr/bin/env python3
"""
Build script for the img site.
Scans an images directory and generates an HTML file with the image catalog
embedded directly in a <script> tag, so no external images.js is needed.

Usage:
    python build.py --img-dir docs/img --template src/index.html --output docs/index.html
"""

import argparse
import json
import mimetypes
from pathlib import Path

SUPPORTED_EXTENSIONS = {".gif", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".bmp"}

PLACEHOLDER_START = "/* IMAGES_PLACEHOLDER */"
PLACEHOLDER_END = "/* IMAGES_PLACEHOLDER */"


def build_catalog(img_dir: Path, output_file: Path, template_file: Path) -> int:
    """Scan img_dir and write an HTML file with embedded image catalog."""
    img_dir = img_dir.resolve()
    output_file = output_file.resolve()
    template_file = template_file.resolve()

    # URL prefix is the relative path from the output file's directory to the images directory.
    try:
        url_prefix = img_dir.relative_to(output_file.parent)
    except ValueError:
        url_prefix = img_dir.name

    images = []
    if img_dir.exists():
        for file_path in sorted(img_dir.iterdir()):
            if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
                mime, _ = mimetypes.guess_type(str(file_path))
                images.append(
                    {
                        "name": file_path.name,
                        "url": f"{url_prefix}/{file_path.name}",
                        "type": mime or "image/png",
                    }
                )

    template = template_file.read_text(encoding="utf-8")

    placeholder = f"{PLACEHOLDER_START}[]{PLACEHOLDER_END}"
    replacement = f"{PLACEHOLDER_START}{json.dumps(images, indent=2)}{PLACEHOLDER_END}"

    if placeholder not in template:
        raise ValueError(
            f"Template {template_file} must contain the placeholder: {placeholder}"
        )

    output = template.replace(placeholder, replacement, 1)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(output, encoding="utf-8")
    return len(images)


def main():
    parser = argparse.ArgumentParser(
        description="Generate an HTML file with embedded image catalog."
    )
    parser.add_argument(
        "--img-dir",
        type=Path,
        default=Path("img"),
        help="Directory containing images (default: img).",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("src/index.html"),
        help="HTML template file (default: src/index.html).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/index.html"),
        help="Output HTML file (default: docs/index.html).",
    )
    args = parser.parse_args()

    count = build_catalog(args.img_dir, args.output, args.template)
    print(f"Generated {args.output} with {count} image(s) embedded.")


if __name__ == "__main__":
    main()
