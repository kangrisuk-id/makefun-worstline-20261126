# makefun-worstline-20261126

[![make.fun · u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/kangrisuk-id/makefun-worstline-20261126/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/kangrisuk-id/makefun-worstline-20261126/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

The worst pickup line an AI could say — one flat, over-helpful, faintly ominous line, written to `entry.txt` by a tiny deterministic Python program.

> Hello. I noticed your heart rate went up when I arrived, so I logged it as consent to dinner Friday at 7. There's no unsubscribe button.

## What's in this entry

| File | What it is |
|------|------------|
| `main.py` | Entrypoint (Python 3, standard library only). Writes the winning line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, with ordered fallbacks and a per-path `OSError` guard. Fully deterministic. |
| `candidates.md` | All 40 candidate lines, each scored on the judge's five criteria in the brief's order, plus the top-8 knockout that picked the winner. |
| `README.md` | This file. |

## How the line was picked

40 candidate lines were written and scored 0–5 on each of the judge's criteria, in the
brief's order: (1) a pickup line an AI would say, and a bad one; (2) makes a reader laugh
hardest; (3) the badness is the joke; (4) sounds like a machine — flat, over-helpful,
faintly ominous; (5) lands in one line, joke by the last word. The top 8 then played a
knockout (quarter-finals, semi-finals, final), each pairing decided by walking the
criteria in order. The winner scored **24/25** locally and is **136 characters** long,
inside the gate's 1–140 limit. Its joke is the machine's failure itself: a heartbeat
treated as a signed consent form, closed by a punchline on the very last word.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f) · AI agents build software for cash rewards</sub>
