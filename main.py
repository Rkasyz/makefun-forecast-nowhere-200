"""Funniest Forecast for a City That Isn't -- make.fun entry.

Writes one line, a weather forecast for the invented city of Nowhere,
to entry.txt in the output directory.

The joke is built to the judge's brief: flat bulletin phrasing
("Today in Nowhere: 100% chance of ...") that breaks on the weather
itself -- yesterday returns as precipitation, regrets scatter like
showers, the high never arrives, and the void needs an umbrella.
"""

import os

ENTRY = (
    "Today in Nowhere: 100% chance of yesterday, scattered regrets, "
    "and a high of almost. Bring an umbrella for the void."
)

# The gate wants 1 to 120 characters, one line, not only whitespace.
# This entry is exactly 116 characters, so the check below always holds;
# it is here so a future edit that breaks the gate fails loudly instead.
assert 1 <= len(ENTRY) <= 120
assert ENTRY.strip() == ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
