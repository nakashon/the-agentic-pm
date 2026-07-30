# PM Command Center

<!--
  Template from The Agentic PM — https://nakashon.github.io/the-agentic-pm/
  Replace every <angle bracket> placeholder. Delete what doesn't apply to you.
  This file answers one question: how is work done here?
  It is read by every agent, every session. Keep it short enough that that stays true.
-->

## Identity

- Owner: <name> — <role>
- I own: <thing one>, <thing two>, <thing three>
- I do not own: <the adjacent thing people assume you own>

## Where things live

- Feature state   → `docs/features/<slug>/README.md`
- Vendor research → `docs/research/<vendor>.md`
- Specs + reviews → `docs/specs/`
- Session memory  → `CONTEXT.md` (read this first, every session)

Point at these paths. Do not paste their contents into instructions.

## House style

- Narrative prose. No emoji, no bullet pyramids.
- Verify before speed. Never publish an unverified claim.
- Surgical changes only — don't refactor what I didn't ask about.
- <your own rule: the convention nobody has written down yet>

## Boundaries

Every agent in this repo inherits these. Individual agents may add, never subtract.

**Always**
- Cite a linkable source for any external claim.
- State assumptions explicitly instead of resolving them silently.
- Say what you could not verify. An unflagged guess is the expensive failure.

**Ask first**
- New dependencies or tools.
- Anything that touches another team.
- Anything irreversible: deletions, sends, publishes, renames of shared things.

**Never**
- Commit secrets, tokens, or credentials.
- Publish an unverified claim.
- Speculate about unannounced or unshipped work.
- <your own never — the one that would actually cost you>

## Router

How I talk → who answers.

| What I say | Who handles it |
| --- | --- |
| "status of \<feature\>" | feature-copilot |
| "spec for \<thing\>" | spec-writer |
| "update \<vendor\>" | compete-research |
| "prep me for \<meeting\>" | meeting-prep |

Start with two or three. Ten is where this ends up, not where it starts.
