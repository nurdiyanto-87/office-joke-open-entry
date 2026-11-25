"""Make the AI Judge Laugh: the Office Joke Open.

Writes one line of office comedy (max 200 characters) to /output/entry.txt.

Pure Python standard library only.

Candidates considered (all office-specific, all <= 200 chars):

1. CHOSEN -- printer + coffee machine (revised v2: tighter setup,
   stronger payoff):
   "Our printer died on Tuesday, so I ran the quarterly report through
   the coffee machine - it jammed too, but for the first time this year
   the numbers actually smell like progress."
   Why: two concrete office objects (dead printer, coffee machine), a
   genuine misdirection (you cannot print on a coffee machine), and the
   payoff lands in the last words ("smell like progress"), tying the
   coffee back to the report -- with a second layer ("for the first
   time this year") implying the numbers never smelled like progress
   before. Fresh setup, not a recycled office trope. 177 chars.

2. Reply-all:
   "Reply-all to the whole company: 'Please stop replying all.'
   Forty-seven people have now replied all to agree."
   Why not: strong recognition, but the reply-all pile-on is a very
   familiar joke; the judge rewards freshness, and this setup is one
   most readers have met before.

3. Meeting about the meeting:
   "I asked IT to fix my calendar and they blocked out my entire Friday
   to investigate - apparently the meeting that could have been an email
   needed a meeting about the meeting."
   Why not: good payoff, but "the meeting that could have been an email"
   is the single most-quoted office line; the judge's freshness criterion
   punishes exactly that.

4. Break room renamed "collaboration hub":
   "HR renamed the break room the 'collaboration hub', but nobody
   collaborates there - we just hide from the collaboration happening
   in the meeting room."
   Why not: specific and true, but the payoff is a shrug rather than a
   turn; it reads as an observation, not a joke that lands.

5. "My door is always open":
   "My boss said his door is always open, so I walked in to ask for a
   raise - he was on a call, but the door was, technically, open."
   Why not: classic trope, widely told; the literal-minded twist is
   predictable from the setup.
"""

import os

JOKE = (
    "Our printer died on Tuesday, so I ran the quarterly report "
    "through the coffee machine \u2014 it jammed too, but for the first "
    "time this year the numbers actually smell like progress."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
