# The Agentic PM

**v2 — Honest Notes from the Field.** A talk by [Asaf Nakash](https://nakashon.com).

## [→ View the Presentation](https://nakashon.github.io/the-agentic-pm/)

## Why there's a v2

Version 1 was a teaching deck. It explained what a PM does, argued that AI changes the job, and closed on *"the future isn't AI vs. humans — it's humans who use AI vs. humans who don't."*

That line is true. It's also unfalsifiable, unactionable, and agreed with by everyone in the room. Which is how you know it isn't a finding.

Then I spent a year actually handing real work to agents. v2 is what I'd say instead.

**v1 is still here, unedited, at [`/v1`](https://nakashon.github.io/the-agentic-pm/v1/).** Deleting it would rather undermine the point.

## The argument

> Agents didn't remove the work. They relocated it.

Production collapsed to near-zero — drafts, specs, prototypes, research, refactors. Verification didn't get cheaper at all. Every hard thing in the talk falls out of that one asymmetry.

### The Verification Ceiling

> You can safely delegate **exactly as much as you can check**. Past that line you are not managing — you are hoping.

Two moves follow: raise the ceiling (evals, harnesses, checkable acceptance criteria) or lower the delegation. Most teams do neither and call the gap *velocity*.

### The revised loop

> **Frame → Delegate → Verify → Own**

Bounded by the Verification Ceiling — the loop only runs as fast as its slowest check.

## What's inside

27 slides in four parts.

**1 — Six field notes.** Drawn from a year of running AI security product with agents in the loop:

- One spec, seven versions, seventeen days — and fourteen commits that only rebuild deliverables
- One column name, five spellings, fourteen days: renaming became free, naming did not
- 86 documents vs. 30 features — a PM's repo is a prose repo, and prose is where the failure mode hides
- Competitive research that wrote the most *satisfying* version of the market rather than the truest
- The document built perfectly on my own misconception, citing my own notes back to me
- 23 review comments answered flawlessly by something that couldn't read the room

**2 — The system I actually run.** The part usually left out: version-controlled context files, a roster of ten narrow agents behind a router, config-as-source-of-truth, progressive disclosure, three-tier boundaries (✅ always / ⚠️ ask first / 🚫 never), and the two rules I'd never drop.

**3 — What it means.** The new economics, the Verification Ceiling, why "orchestration" undersells the problem, and taste as the scarce input.

**4 — What I'd actually do.** Four practices, all boring, all load-bearing.

## Usage

Open `index.html` in any browser — no build step, no dependencies, no setup.

Navigate with arrow keys. Press `Esc` for slide overview.

Use it, remix it, present it to your team. The field notes are mine — swap in your own. A talk called *notes from the field* is only worth as much as its least verifiable slide.

## Tech

Single-file [reveal.js](https://revealjs.com/) presentation. All dependencies via CDN.

## About the author

**Asaf Nakash** — Principal Product Manager, AI Security at Microsoft Defender. Host of [Context Window](https://contextwindowsec.com), a weekly AI security podcast and newsletter. Speaks at RSA Conference, Microsoft Ignite, and OWASP AppSec Israel.

- [nakashon.com](https://nakashon.com) · [Frameworks](https://nakashon.com/frameworks/) · [Speaking](https://nakashon.com/speaking/)
- [LinkedIn](https://www.linkedin.com/in/nakash/) · [X](https://x.com/nakashon) · [GitHub](https://github.com/nakashon)

## License

MIT — use it however you want.
