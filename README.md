[![One-Star Review of Something Essential](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/oponopon31/u-0xb3e689-one-star-review-of-something-essential-c7234629/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/oponopon31/u-0xb3e689-one-star-review-of-something-essential-c7234629/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

# One-Star Review of Something Essential

A single deadpan one-star review, at most 160 characters, of an everyday
essential everyone relies on — filed in earnest against a thing that
cannot be fixed, with the sting in the last few words. The program writes
that one line to `entry.txt`.

## How to run

```sh
python3 main.py
```

The program writes `entry.txt` (the review, plus one trailing newline) to
`$MAKEFUN_OUTPUT_DIR` if set, otherwise to `/output` if it exists, and
otherwise to the current directory. It validates the review (one line,
1–160 characters, not only whitespace, no control characters), re-reads
the file to confirm the exact bytes, and prints the review, its character
and byte counts, and the SHA-256 of the file. Pure Python standard
library, no dependencies, deterministic output.
