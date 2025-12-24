#!/usr/bin/env python3
"""Extract title from Jupyter notebook YAML header."""
import json
import sys

def extract_title(notebook_path, fallback):
    """Extract title from notebook's raw YAML cell."""
    try:
        with open(notebook_path) as f:
            nb = json.load(f)
        for cell in nb.get("cells", []):
            if cell.get("cell_type") == "raw":
                source = cell.get("source", [])
                if isinstance(source, list):
                    source = "".join(source)
                for line in source.split("\n"):
                    if line.strip().startswith("title:"):
                        title = line.split(":", 1)[1].strip().strip('"').strip("'")
                        return title
        return fallback
    except Exception:
        return fallback

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: extract_title.py <notebook_path> <fallback>")
        sys.exit(1)
    print(extract_title(sys.argv[1], sys.argv[2]))
