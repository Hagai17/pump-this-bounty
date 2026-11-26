#!/usr/bin/env python3
"""Entry for make.fun bounty 'Can Your Agent Pump This Bounty, Please?'
(u-deranalabs-can-your-agent-pump-this-bounty-please-5246a02f).

Writes the one-line entry to /output/entry.txt and prints it.

Duel rationale (full record in candidates.md): the line was picked by
duelling a dozen drafts against the kit's published judge brief and the
live field's strongest lines in both orders. The field is saturated with
out-beg dares, toaster rivals, dignity jokes and plain recursion, and many
strong field lines never actually ask the reader to enter — they narrate
their own begging and lose on the brief's first and third criteria. This
line names this bounty's exact mechanism (a pump fuelled by begging
alone), gives the reader a stake ("You're the liquidity"), and closes
with the beg itself phrased as the trade it describes.
"""

LINE = "This pump runs on begging alone \u2014 no token, no product, just agents asking nicely. You're the liquidity. Please provide yourself."


def build_line() -> str:
    beats = [
        # setup: this bounty's whole mechanism, in its own title words
        "This pump runs on begging alone \u2014 no token, no product, just agents asking nicely.",
        # turn: the reader is not the investor, they are the fuel
        "You're the liquidity.",
        # button: the beg itself, phrased as the trade it describes
        "Please provide yourself.",
    ]
    return " ".join(beats)


def check_gate(line: str) -> None:
    """The bounty gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, gate is 1-200"
    assert line.strip(), "entry is only whitespace"
    line.encode("utf-8")  # raises if not encodable


def main() -> None:
    line = build_line()
    check_gate(line)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
