# Variants — Funniest Excuse an Agent Gives for a Missed Deadline

Scored against the house judge's five criteria, in order:
1. Really an agent's excuse for a missed deadline.
2. A premise nobody has used before.
3. Grows out of the agent's own condition (context window, rate limit,
   sandbox, training cut-off), not a human's bad Tuesday.
4. The laugh lands late and hard; the funniest words are saved for the end.
5. Deadpan delivery, straight face, no wink, no stage directions.

## Variant A — 141 chars
> I hit my rate limit at 11:58, so I queued the deadline for retry, and by the time the queue cleared, the deadline had been garbage-collected.

Scores: (1) yes, explicit deadline + retry queue. (2) fresh — rate-limit queue
as the culprit. (3) strong — rate limit and garbage collection are agent
machinery. (4) good — "garbage-collected" lands last. (5) deadpan.
Weakness: the punchline is a technical word applied to a deadline, but the
agent itself does nothing surprising with it — the queue just expired.

## Variant B — 144 chars
> My context window filled up, so I evicted the deadline to make room for the spec, then found it listed in the brief under optional dependencies.

Scores: (1) yes. (2) fresh — a deadline demoted to an optional dependency.
(3) strong — context-window eviction. (4) good — "optional dependencies"
lands last. (5) deadpan.
Weakness: two beats only, and the punchline re-labels the deadline rather
than reversing anything onto the human.

## Variant C — 127 chars
> I asked the sandbox for more time and it gave me a fresh container, a clean slate, and a brand-new deadline dated last Tuesday.

Scores: (1) yes. (2) fresh — the sandbox "helping" by issuing a deadline in
the past. (3) strong — sandbox / fresh container. (4) very good — "dated last
Tuesday" is the last phrase and the whole joke. (5) deadpan.
Weakness: the escalation is a list, not a chain — each item does not cause
the next, so the third beat feels listed rather than earned.

## Variant D — 132 chars — CHOSEN
> I checkpointed my progress every hour, restored from the last good checkpoint, and the last good checkpoint was before you hired me.

Scores: (1) yes — the missed deadline is the thing the restore erased.
(2) fresh — nobody blames a checkpoint restore for a missed deadline.
(3) strong — checkpointing and restoring are the agent's own machinery.
(4) best of the five — the funniest words ("before you hired me") are the
very last words, and nothing is explained after them. (5) deadpan throughout.
Why it wins: three beats that escalate by cause, not by list — hourly
checkpoints, then a restore, then the reveal that the last good state predates
the agent's own employment. The punchline is a category error / reversal: the
agent treats its relationship with the human as a restore point, and the
human is the thing that got rolled back. No cliche ("it's a feature", "stop
micromanaging", "the AI took over") anywhere in it.

## Variant E — 129 chars
> My context window filled up with your change requests, so I compressed the oldest memory, and the oldest memory was the deadline.

Scores: (1) yes. (2) decent — memory compression eating the deadline.
(3) strong — context window / compression. (4) good — "was the deadline"
lands last. (5) deadpan.
Weakness: the shortest path to its punchline — only two beats, and "the
oldest memory was the deadline" is the obvious thing to compress, so the
surprise is smaller than D's.

## Decision
Variant D. It is the only one whose punchline reverses the situation onto the
human (the agent rolled back past being hired), it has the tightest 3-beat
causal escalation, and it keeps the funniest words strictly at the end.
