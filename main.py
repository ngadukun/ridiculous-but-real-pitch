"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes the one-sentence pitch to output/entry.txt. Python stdlib
only, no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "We rent grandmothers by the hour to scold grown adults into filing "
    "their taxes on time, and professionals pay $29 a month because a "
    "stranger's grandma's disappointment beats any reminder app."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"


MAX_CHARS = 200  # the brief caps the pitch at 200 characters, one sentence


def check_entry(text: str) -> str:
    """Return the pitch unchanged, or raise if it breaks the brief."""
    if len(text) > MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars, over the {MAX_CHARS} cap")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("the pitch must be exactly one sentence")
    for needed in ("grandmothers", "pay", "$29"):
        if needed not in text:
            raise ValueError(f"pitch lost its {needed!r} — the odd product, "
                             "the customer and the money must all be named")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
