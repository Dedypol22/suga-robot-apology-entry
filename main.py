"""The Robot Apology (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt.
Line 1 owns one specific mistake (locking Milo the cat in the pantry
overnight); line 2 names the lesson learned and the behaviour that
changes because of it (calling Milo by name before closing a door).
"""

import os

ENTRY = (
    "I'm sorry I locked Milo in the pantry overnight while I was putting the shopping away.\n"
    "I've learned to count heads before I close a door, so now I call for Milo by name and wait for an answer first."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
