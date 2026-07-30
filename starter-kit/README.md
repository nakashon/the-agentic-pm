# Starter kit

The files from Part 3 of [The Agentic PM](https://nakashon.github.io/the-agentic-pm/),
ready to copy. Nothing here needs a platform, a budget, or permission.

## Fastest path

Paste this into any coding agent, in the repo you want to set up:

```
Read https://nakashon.github.io/the-agentic-pm/llms-full.txt
and set up a PM command center for me in this repo.

Interview me for what you need. Don't guess my context.
Show me the files before you write them.
```

## Manual path

```bash
git clone https://github.com/nakashon/the-agentic-pm.git
cp -r the-agentic-pm/starter-kit/. my-pm-repo/
cd my-pm-repo && git init
```

Then replace every `<angle bracket>` placeholder. They are deliberate: a generic command
center is worthless, and the placeholders are exactly the context an agent cannot get
anywhere else.

## What's here

Two files everyone needs, and four agent patterns to choose from.

| File | Answers |
| --- | --- |
| `AGENTS.md` | How is work done here? Conventions, boundaries, router. |
| `CONTEXT.md` | What's going on right now? Memory as a file you can edit. |
| `.github/agents/spec-writer.md` | Drafts specs with checkable acceptance criteria. |
| `.github/agents/meeting-prep.md` | One page that gets you through a review. |
| `.github/agents/feedback-analyzer.md` | Turns raw customer feedback into a weekly read. |
| `.github/agents/compete-research.md` | Maintains the vendor landscape, source-gated. |
| `docs/` | Where the work itself accumulates. |

**Take two or three agents, not all four.** Pick the ones matching what you actually ask
for most often, and delete the rest along with the `docs/` directories you won't use. An
agent you didn't need is worse than no agent: it sits unused and teaches you the system is
decorative. If none of the four fits, copy the shape of one and write your own — the
structure is the asset, not the job title.

## The one rule to keep

Every agent gets **three** tiers, not two: *Always*, *Ask first*, *Never*. Most people
write two. The middle tier is where all the value is — it's how an agent moves fast on
the safe 90% without quietly deciding the other 10% for you.

## Where agent files go

`.github/agents/*.md` is the convention used by GitHub Copilot. If your tool looks
elsewhere — `.cursor/rules/`, `.claude/agents/`, a project settings pane — move the files
there. The content is the asset; the path is not.
