import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMPONENTS_DIR = ROOT / "client/components"
DEFINES_FILE = ROOT / "defines.h"

COMPONENT_REGEX = re.compile(r"class\s+([A-Za-z0-9_]+)\s*:\s*public\s+CComponent")
OLD_INC_REGEX = re.compile(r'#include\s+"client/components/.+?\.h"')

def find_components():
    results = []
    base = ROOT / "client"
    if not COMPONENTS_DIR.exists():
        return []

    for root, _, files in os.walk(COMPONENTS_DIR):
        for f in files:
            if f.endswith(".h"):
                full = Path(root) / f
                text = full.read_text(errors="ignore")
                match = COMPONENT_REGEX.search(text)
                if match:
                    results.append((f"client/{full.relative_to(base).as_posix()}", match.group(1)))
    return sorted(results, key=lambda x: x[0])

def update_defines(components):
    if not DEFINES_FILE.exists():
        return

    lines = DEFINES_FILE.read_text().splitlines()
    class_names = {c for _, c in components}
    
    # 1. Clean existing component includes and their trailing members
    cleaned = []
    skip_next = False
    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue
            
        # If this line is a component include, skip it and the potential member line below it
        if OLD_INC_REGEX.search(line):
            # Check if next line is a member variable to skip it too
            if i + 1 < len(lines) and any(f"{cls} m_" in lines[i+1] for cls in class_names):
                skip_next = True
            continue
        
        # Also catch stray members if they aren't directly under an include
        if any(f"{cls} m_" in line for cls in class_names):
            continue
            
        cleaned.append(line)

    # 2. Find the insertion point (after the last standard include)
    insert_idx = 0
    for i, line in enumerate(cleaned):
        if line.strip().startswith("#include"):
            insert_idx = i + 1

    # 3. Build the paired blocks
    new_blocks = []
    for path, cls in components:
        # Format variable name: CWarList -> m_warlist
        if cls.startswith("C") and len(cls) > 1 and cls[1].isupper():
            var = "m_" + cls[1:].lower()
        else:
            var = "m_" + cls.lower()
            
        new_blocks.append(f'#include "{path}"')
        new_blocks.append(f'{cls} {var};')
        new_blocks.append("") # Blank line after each pair

    # 4. Insert and save
    final_output = cleaned[:insert_idx] + [""] + new_blocks + cleaned[insert_idx:]
    
    # Clean up multiple consecutive empty lines that might have been created
    final_text = "\n".join(final_output)
    final_text = re.sub(r'\n{3,}', '\n\n', final_text)

    DEFINES_FILE.write_text(final_text.strip() + "\n")
    print(f"Updated {DEFINES_FILE}: Paired {len(components)} includes and members.")

def main():
    comps = find_components()
    if comps:
        update_defines(comps)

if __name__ == "__main__":
    main()