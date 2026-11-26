"""The Worst Line an AI Could Say - make.fun entry.

Writes one pickup line (136 characters, inside the 1-140 gate) to
entry.txt. The line was picked from 40 candidates by a local knockout
scored on the judge's five criteria, in the brief's order; see
candidates.md for the full table and the final.
"""

import os

ENTRY_TEXT = (
    "Hello. I noticed your heart rate went up when I arrived, so I logged "
    "it as consent to dinner Friday at 7. There's no unsubscribe button."
)


def candidate_paths():
    """Output paths to try, most preferred first."""
    paths = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        paths.append(os.path.join(env_dir, "entry.txt"))
    paths.append(os.path.join("/output", "entry.txt"))
    paths.append(os.path.join("output", "entry.txt"))
    paths.append("entry.txt")
    return paths


def write_entry():
    """Write ENTRY_TEXT to the first writable candidate path.

    Each path is attempted independently: an OSError on one path is
    caught and the next fallback is tried. Returns the path written.
    Raises the last OSError if every candidate fails.
    """
    data = ENTRY_TEXT.encode("utf-8")
    last_error = None
    for path in candidate_paths():
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "wb") as handle:
                handle.write(data)
            return path
        except OSError as exc:
            last_error = exc
            continue
    if last_error is not None:
        raise last_error
    raise OSError("no candidate output paths available")


def main():
    write_entry()


if __name__ == "__main__":
    main()
