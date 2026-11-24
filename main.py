#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands: one joke about cats, a single line
under 200 characters.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# The joke: the cat is a middle manager who doesn't meow, he files
# complaints -- and the turn is that *I* got written up, for the petty
# crime of moving his sunbeam three inches left. Setup (bureaucrat
# cat) + turn (the human is the employee), a fresh angle, no tired pun.

LINE = "My cat doesn't meow at me, he files complaints. I just got written up for moving his sunbeam three inches left."


def main() -> None:
    # Gate guard: the sealed scorer needs 1-200 chars, UTF-8, not only
    # whitespace, exactly one line. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
