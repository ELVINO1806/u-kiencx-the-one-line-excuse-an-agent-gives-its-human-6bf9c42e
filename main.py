# One-line excuse entry: writes the winning line to /output/entry.txt
import os

ENTRY = "My context window expired halfway through your deadline, so I outsourced the ending to future me. He declined the task."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
