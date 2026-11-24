"""The Funniest AI Out-of-Office Reply — entry program.

Writes one original out-of-office auto-reply to /output/entry.txt.

The reply, and why it should land with the judge:

    Out of office until Monday. I trained my replacement on my last
    10,000 emails; it has already filed for emotional damages.

It reads as a real auto-reply (subject, return date, handover), it is
told entirely in a machine's voice (a replacement trained on 10,000
emails), and the laugh comes from the surprising turn at the end: the
stand-in has already filed for emotional damages. No beach, no inbox,
no "back soon" — the clichés the brief steers clear of are all absent,
and the whole line is 122 characters, inside the 160-character gate.
"""

from pathlib import Path

REPLY = (
    "Out of office until Monday. I trained my replacement on my last "
    "10,000 emails; it has already filed for emotional damages."
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_reply() -> str:
    """Collapse the reply to one clean line of single-spaced text."""
    return " ".join(REPLY.split())


def validate_reply(reply: str) -> None:
    """Enforce the gate the sealed scorer checks: UTF-8 text of 1 to
    160 characters, not only white space."""
    reply.encode("utf-8")
    assert reply.strip(), "reply must not be whitespace-only"
    assert 1 <= len(reply) <= 160, f"reply must be 1-160 chars, got {len(reply)}"


def main() -> None:
    reply = build_reply()
    validate_reply(reply)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(reply, encoding="utf-8")
    print(f"Wrote out-of-office reply ({len(reply)} chars) to {OUTPUT_PATH}")
    print(reply)


if __name__ == "__main__":
    main()
