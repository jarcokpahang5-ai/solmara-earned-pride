"""One Line of Earned Pride -- make.fun entry.

One line of 1 to 240 characters, a quiet, earned moment of pride:
after three years of night shifts and burnt dinners, a mother
finally frames her nursing certificate above the sink where she used
to study. The program checks the line, prints it, and writes it to
/output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "After three years of night shifts and burnt dinners, my mother "
    "finally framed her nursing certificate above the sink where she "
    "used to study."
)

LIMIT = 240
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed line is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
