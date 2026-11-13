# ai-joke-03 entry: writes one one-liner joke about AI coding agents to
# /output/entry.txt. Deterministic: the same bytes on every run.
# (Python 3.13, standard library only.)
import os

JOKE = "I asked my agent to handle null user IDs. It made null the superuser \u2014 null now outranks me."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
