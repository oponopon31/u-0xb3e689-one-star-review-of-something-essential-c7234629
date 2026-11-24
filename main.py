"""One-star review of something essential.

The entry is a single deadpan one-star review, at most 160 characters, of
an everyday essential everyone relies on. The house judge compares two
reviews at a time, weighing in order: (1) is it a one-star review of an
everyday essential, deadpan and about the thing itself; (2) does it find
the sharpest true grievance, the small daily annoyance everyone
recognises but has never seen written down; (3) does it hold the deadpan,
no winking, no explaining, no exclamation marks; (4) does it turn in the
last few words, so the sting arrives after the complaint has been read
straight; (5) is it tight and specific, one joke told cleanly.

Candidate lines, drafted for this competition and judged pairwise:

1. Gravity: "One star. Gravity works fine until you drop your phone,
   then suddenly it is the fastest thing in the house."
2. Sun: "One star. The sun is late every winter morning, early every
   summer one, and has never once apologised."
3. Sleep: "One star. Sleep promised eight hours of rest and delivered
   four hours of dreaming about being late for work."
4. Monday: "One star. Monday arrives every week without fail, brings
   nothing new, and still acts surprised when nobody is glad to see it."
5. Water: "One star. Water is tasteless, colourless, and after a
   lifetime of drinking it I still have to be reminded to drink it."

Pairwise reasoning:
- (1) vs (2): both are deadpan complaints against an unfixable thing
  with the turn in the last few words. Gravity wins on criterion 2:
  the phone-drop panic is a sharper, more visceral daily grievance
  than the sun's seasonal schedule, and "the fastest thing in the
  house" is a specific, concrete sting. The sun's grievance is
  observational; gravity's is felt in the hand.
- (1) vs (3): sleep's "promised eight hours / delivered four hours
  of dreaming about being late" is a good grievance, but it explains
  itself a little (the dream detail does the joke's work for the
  reader) and the turn lands mid-line rather than in the last few
  words. Gravity's turn is the final phrase.
- (1) vs (4): Monday is the most obvious target in the brief's own
  examples, so a Monday review starts from the most crowded angle;
  its turn ("acts surprised") is a personification joke rather than
  a grievance. Gravity is a fresher target with a truer complaint.
- (1) vs (5): water's grievance ("still have to be reminded to
  drink it") is real but gentle, and the line spends its first half
  listing properties (tasteless, colourless) instead of complaining.
  Gravity complains from the first clause and never lets up.

Winner: candidate 1, gravity. One star stated up front, one concrete
grievance (it only ever shows its speed when your phone is falling),
deadpan throughout, turn in the final words, 107 characters, one joke.
"""

import hashlib
import os
import sys

LINE = (
    "One star. Gravity works fine until you drop your phone, "
    "then suddenly it is the fastest thing in the house."
)


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
    # not only white space, a single line.
    if not (1 <= len(LINE) <= 160):
        print(f"invalid line length: {len(LINE)} characters", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("invalid line: blank or padded", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("invalid line: not a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 for ch in LINE):
        print("invalid line: control character", file=sys.stderr)
        return 1
    if "!" in LINE:
        print("invalid line: exclamation mark breaks the deadpan", file=sys.stderr)
        return 1
    if not LINE.endswith("."):
        print("invalid line: must end with a full stop", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else os.getcwd()
    )
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and assert the exact bytes we meant to write.
    with open(path, "rb") as fh:
        written = fh.read()
    assert written == data, "entry.txt bytes differ from the line"
    assert written.decode("utf-8").rstrip("\n") == LINE

    print(LINE)
    print(f"chars: {len(LINE)}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
