#!/usr/bin/env python3
"""Build grill-names wheel and copy to docs static path for pyrepl autodoc."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WHEEL_DEST_DIR = ROOT / "docs" / "source" / "_static" / "wheels"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    staging = ROOT / "docs" / ".wheel-staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "wheel",
            str(ROOT),
            "--no-deps",
            "-w",
            str(staging),
        ],
        check=True,
    )
    wheels = sorted(staging.glob("grill_names-*.whl"))
    if len(wheels) != 1:
        sys.exit(f"expected one grill_names wheel in {staging}, found: {wheels!r}")

    WHEEL_DEST_DIR.mkdir(parents=True, exist_ok=True)
    for old in WHEEL_DEST_DIR.glob("*.whl"):
        old.unlink()
    dest = WHEEL_DEST_DIR / wheels[0].name
    shutil.copy2(wheels[0], dest)
    shutil.rmtree(staging)
    print(f"copied {wheels[0].name} -> {dest}")


if __name__ == "__main__":
    main()
