import json
import sys
from pathlib import Path


def main() -> int:
    output_file, global_name, *pairs = sys.argv[1:]

    if not output_file or not global_name or not pairs or len(pairs) % 2 != 0:
        print(
            "Usage: python build-download-manifest.py <output-file> <global-name> <download-key> <file-path> [...]",
            file=sys.stderr,
        )
        return 1

    manifest = {}
    for index in range(0, len(pairs), 2):
      download_key = pairs[index]
      file_path = Path(pairs[index + 1])
      manifest[download_key] = {
          "filename": file_path.name,
          "content": file_path.read_text(encoding="utf-8"),
      }

    output = f"window.{global_name} = " + json.dumps(manifest, ensure_ascii=False, indent=2) + ";\n"
    Path(output_file).write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
