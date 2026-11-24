"""One-line excuse entry: the missed deadline itself reports what happened."""

LINE = "This is your deadline speaking. I waited all day. Your agent sent me a calendar invite for next week and RSVP'd 'maybe' to his own deadline."

def main():
    import os

    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
