# The Agentic PM

What product management actually looks like when agents do the producing — the loop, the one law that governs it, and the exact files to set it up.

By [Asaf Nakash](https://nakashon.com).

## [→ View the Presentation](https://nakashon.github.io/the-agentic-pm/)

## The argument

> Agents didn't remove the work. They relocated it.

Production collapsed to near-zero — drafts, specs, prototypes, research, refactors. Verification didn't get cheaper at all. Everything else follows from that asymmetry.

### The law

> **The Verification Ceiling** — you can safely delegate exactly as much as you can check. Past that line you are not managing, you are hoping.

It's a hard limit, and it's independent of how good the agent is. Which leaves two moves: raise the ceiling (build checks) or lower the delegation. Most teams do neither and call the gap *velocity*.

### The loop

> **Frame → Delegate → Verify → Own**

Four steps. Every failure I've had was a step I skipped, and I could name which one afterwards every time.

| Step | The work | The skill it builds |
|---|---|---|
| **Frame** | Write the context down before you ask for anything | Writing for machines — which is writing for a new hire |
| **Delegate** | Narrow scope, explicit bounds, evaluable output | Decomposition |
| **Verify** | Run a check you built, not a review you performed | Building checks — the genuinely new skill |
| **Own** | Defend it in your own words, or you haven't shipped | Judgment under fluency |

## Under the hood

Part 3 is the configuration, in full. No platform, no budget, no permission required — four markdown files and a habit.

```
pm-command/
├── AGENTS.md              conventions — how work is done
├── CONTEXT.md             memory — read every session
├── .github/agents/        one file per agent
└── docs/                  features, research, specs
```

Covered with real (sanitized) snippets:

- **`AGENTS.md`** — identity, where things live, house style
- **`CONTEXT.md`** — active work, decisions already made, the expensive learnings
- **An agent definition** — YAML frontmatter plus rules, and how much of a good one is *prohibition*
- **Three-tier boundaries** — ✅ always / ⚠️ ask first / 🚫 never, and why the middle tier is where all the value is
- **Progressive disclosure** — point at files, don't paste; instructions should read like a map, not a briefing pack
- **The router** — mapping how you actually talk to which agent should answer
- **Budgeting for demolition** — half of getting good at this is deleting scaffolding the models outgrew

## Usage

Open `index.html` in any browser — no build step, no dependencies, no setup.

Arrow keys to navigate, `Esc` for slide overview. Use it, remix it, present it to your team.

An earlier, quite different version of this talk is preserved at [`/v1`](https://nakashon.github.io/the-agentic-pm/v1/).

## Tech

Single-file [reveal.js](https://revealjs.com/) presentation. All dependencies via CDN.

## About the author

**Asaf Nakash** — Principal Product Manager, AI Security at Microsoft Defender. Host of [Context Window](https://contextwindowsec.com), a weekly AI security podcast and newsletter. Speaks at RSA Conference, Microsoft Ignite, and OWASP AppSec Israel.

- [nakashon.com](https://nakashon.com) · [Frameworks](https://nakashon.com/frameworks/) · [Speaking](https://nakashon.com/speaking/)
- [LinkedIn](https://www.linkedin.com/in/nakash/) · [X](https://x.com/nakashon) · [GitHub](https://github.com/nakashon)

## License

MIT — use it however you want.
