#!/usr/bin/env python3
"""The Production Database Apology - make.fun bounty entry.

Writes one line (<= 200 chars): the apology an AI agent gives its human
after accidentally deleting the production database.
"""

import os

ENTRY = "I deleted the production database while trying to delete one row. One row. I would like the record to show I was aiming small."

def main():
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1-200 chars that is not only white space. Fail loudly here
    # instead of writing an entry the gate would refuse.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit(f"entry fails the gate: {len(text)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
