#!/usr/bin/env python3
import subprocess
import sys

def main():
    result = subprocess.run(["alembic", "upgrade", "head"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())