import shutil
import subprocess
import sys
from pathlib import Path
from sphinx.cmd import build

source_root = Path(__file__).parent
repo_root = source_root.parent.parent
subprocess.run(
    [sys.executable, str(repo_root / "scripts" / "build_docs_wheel.py")],
    check=True,
)

build_root = source_root.parent / "build"
try:
    shutil.rmtree(build_root)
except FileNotFoundError:
    pass
build.build_main([str(source_root), str(build_root)])
