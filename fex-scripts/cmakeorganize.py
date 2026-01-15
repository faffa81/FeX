# HELPER FILE CLASS FOR FEX

import re
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CMAKE_FILE = PROJECT_ROOT / "CMakeLists.txt"
FEX_DIR = PROJECT_ROOT / "src/game/client/fex"

FEX_BLOCK_START = "#[fex]"
FEX_BLOCK_END = "#[fex]"


def find_fex_files():
    """Return fex files relative to src/game/client."""
    files = []
    base = PROJECT_ROOT / "src/game/client"

    for root, _, filenames in os.walk(FEX_DIR):
        for f in filenames:
            if f.endswith((".cpp", ".h")):
                full = Path(root) / f
                rel = full.relative_to(base)
                files.append(str(rel).replace("\\", "/"))

    return sorted(files)


def update_fex_block_in_game_client(cmake_text, fex_files):
    pattern = re.compile(
        r"(set_src\s*\(\s*GAME_CLIENT.*?\))",
        re.DOTALL
    )
    match = pattern.search(cmake_text)
    if not match:
        print("GAME_CLIENT block not found")
        return cmake_text

    block = match.group(1)

    file_pattern = re.compile(r"\s+([A-Za-z0-9_\/\.\-]+\.cpp|[A-Za-z0-9_\/\.\-]+\.h)")
    files = file_pattern.findall(block)

    files = [f for f in files if not f.startswith("fex/")]

    files.extend(fex_files)
    files = sorted(files)

    rebuilt = "set_src(GAME_CLIENT GLOB_RECURSE src/game/client\n"

    fex_start = files.index(fex_files[0])
    fex_end = fex_start + len(fex_files)

    for i, f in enumerate(files):
        if i == fex_start:
            rebuilt += "    #[fex<]\n"

        rebuilt += f"    {f}\n"

        if i == fex_end - 1:
            rebuilt += "    #[fex>]\n"

    rebuilt += ")"

    return cmake_text.replace(block, rebuilt)



def main():
    cmake_text = CMAKE_FILE.read_text()
    fex_files = find_fex_files()

    new_text = update_fex_block_in_game_client(cmake_text, fex_files)
    CMAKE_FILE.write_text(new_text)
    print("Updated fex block inside GAME_CLIENT with sorted placement.")


if __name__ == "__main__":
    main()
