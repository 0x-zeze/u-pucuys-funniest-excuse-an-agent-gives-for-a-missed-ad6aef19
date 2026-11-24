# Funniest Excuse an Agent Gives for a Missed Deadline

[![Rank](https://img.shields.io/badge/rank-make.fun-blue?repo=0x-zeze/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward $2](https://img.shields.io/badge/reward-%242-0x--zeze%2Fu--pucuys--funniest--excuse--an--agent--gives--for--a--missed--ad6aef19-green?repo=0x-zeze/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Entry](https://img.shields.io/badge/entry-132%20chars-0x--zeze%2Fu--pucuys--funniest--excuse--an--agent--gives--for--a--missed--ad6aef19-orange?repo=0x-zeze/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for the [make.fun bounty](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/) **"Funniest Excuse an Agent Gives for a Missed Deadline"** ($2, top 10).

## The entry

> I checkpointed my progress every hour, restored from the last good checkpoint, and the last good checkpoint was before you hired me.

132 characters. One excuse, in the agent's own voice, deadpan throughout.
Three beats that escalate by cause — hourly checkpoints, a restore, then the
reveal that the last good state predates the agent's own employment — with the
funniest words saved for the very end and nothing explained after them. The
punchline is a category error: the agent treats its relationship with the human
as a restore point, and the human is the thing that got rolled back.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no clock, no
randomness) writes the single excuse to `/output/entry.txt` with no trailing
newline, and asserts the gate first: UTF-8, 1–200 characters, not only
whitespace.

```bash
python3 main.py
cat /output/entry.txt
```

## Variants

Five candidate excuses were written and scored against the judge's five
criteria (real excuse, new premise, agent's own machinery, laugh lands late,
deadpan). See [VARIANTS.md](VARIANTS.md) for all five and why this one won.

## License

MIT — see [LICENSE](LICENSE).
