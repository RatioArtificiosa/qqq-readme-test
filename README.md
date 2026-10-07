<p align="center">
  <img src="https://img.shields.io/badge/runtime-WebAssembly%20Component%20Model-4cc9f0?style=for-the-badge&logo=webassembly&logoColor=white" alt="runtime"/>
  <img src="https://img.shields.io/badge/security-capability--secure-ef476f?style=for-the-badge" alt="security"/>
  <img src="https://img.shields.io/badge/languages-5%20first--class-3ddc97?style=for-the-badge" alt="languages"/>
  <img src="https://img.shields.io/badge/license-Apache%202.0-ffd166?style=for-the-badge" alt="license"/>
</p>

<p align="center">

```
 ██████╗ ██████╗ ██████╗
██╔═══██╗██╔══██╗██╔══██╗
██║   ██║██████╔╝██████╔╝
██║▄▄ ██║██╔═══╝ ██╔═══╝
╚██████╔╝██║     ██║
 ╚══▀▀═╝ ╚═╝     ╚═╝
```

</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&color=4CC9F0&center=true&vCenter=true&width=600&lines=The+runtime+built+for+humans+and+AI+agents.;Secure+by+default.+Multi-language.+Fast+where+it+counts.;Run+anything.+Trust+nothing." alt="typing"/>
</p>

<p align="center">
  <a href="#-the-60-second-version"><img src="https://img.shields.io/badge/💡_Why-4cc9f0?style=for-the-badge" alt="why"/></a>
  <a href="#-the-constellation"><img src="https://img.shields.io/badge/🌐_Constellation-c77dff?style=for-the-badge" alt="constellation"/></a>
  <a href="#-the-four-verbs"><img src="https://img.shields.io/badge/⚡_Four_Verbs-3ddc97?style=for-the-badge" alt="verbs"/></a>
  <a href="#-the-16-pillars"><img src="https://img.shields.io/badge/🖥️_Console-f4a261?style=for-the-badge" alt="console"/></a>
  <a href="#-install"><img src="https://img.shields.io/badge/📦_Install-4895ef?style=for-the-badge" alt="install"/></a>
  <a href="#-live-status"><img src="https://img.shields.io/badge/📊_Status-ffd166?style=for-the-badge" alt="status"/></a>
  <a href="#-the-roadmap"><img src="https://img.shields.io/badge/🗺️_Roadmap-ef476f?style=for-the-badge" alt="roadmap"/></a>
  <a href="#-where-we-lose"><img src="https://img.shields.io/badge/💀_Honesty-5c677d?style=for-the-badge" alt="honesty"/></a>
  <a href="#-pricing"><img src="https://img.shields.io/badge/💰_Pricing-f6e2a8?style=for-the-badge" alt="pricing"/></a>
</p>

---

$${\color{#4cc9f0}\textbf{THE 60-SECOND VERSION}}$$

Every runtime you have ever deployed shares three assumptions:

| Assumption | What it costs you |
|---|---|
| **One garbage-collected language** | Unpredictable pauses in the request path, and tens of megabytes of baseline memory *per worker* |
| **Ambient authority** | Any dependency can read any file, open any socket, and phone home. Isolation means a container — heavy, coarse, unprovable |
| **Humans are the only users** | The CLI is a text adventure. Machine integration is an afterthought bolted on as `--json` |

QQQ rejects all three.

It executes **WebAssembly components** on a **Rust host**, with a **capability model where a module has zero authority you did not explicitly grant it** — enforced *outside* the guest, checkable *before* execution.

```bash
qqqai new agent-sandbox --lang python
cd agent-sandbox && qqqai dev
```

```toml
# qqq.toml — the whole security model, readable in 30 seconds
[capabilities]
fs   = [{ path = "/tmp/session-42", mode = "read-write" }]
http = { client = ["api.example.com:443"] }
crypto = { random = true }

[limits]
memory = "64MiB"
fuel   = 2_000_000_000
epoch_deadline_ms = 5000
```

That file is the contract. Your code **cannot** read `/etc/passwd`, cannot open an arbitrary socket, cannot read an environment variable, and cannot outlive its fuel budget — not because a policy engine says no, but because those imports **do not exist** in the instance it runs in.

---

$${\color{#c77dff}\textbf{THE CONSTELLATION}}$$

This is what QQQ draws when your system is live. Not a screenshot — a **real terminal render** of the flagship visual.

```
╭─ MISSION CONTROL ─ myapp ─ dev ─ gen 12 ────────────────────── 412 rps · p99 18ms · ✓ ok ─╮
│                                                                                            │
│              ··◍ web                      ●                                                  │
│            ··  ╱ ╲                       ╱ ╲     the sweep ⟳ rotates once per second;        │
│         ◉ api ── ⬤ db ──── ⬤ cache            when it crosses a node, the node brightens    │
│           ╲ ╱        ╲   ╱                       and its edges pulse outward with traffic.    │
│            ⛓ audit    ⚠ queue                    node size = requests/s · ring = latency ·   │
│                                                   red ring = error rate · magenta arc =     │
│  ● healthy  ◍ degraded  ○ stopped  ✕ failed       capability boundary.                       │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
```

| Dimension | Encodes |
|---|---|
| **Position** | composition graph adjacency (deterministic force layout) |
| **Node size** | throughput (requests/s) |
| **Node fill** | health (ok / warn / error) |
| **Ring radius** | latency band (p50 → p99) |
| **Edge thickness** | call volume |
| **Edge colour** | authority type (network = blue, fs = green, sql = amber, agent = purple) |
| **Sweep** | the passage of time (1 revolution = 1 s) |
| **Amber halo** | needs attention |

Node and Bun give you `console.log` and a process list. QQQ draws the *actual composition graph*, live, because the Component Model makes it statically knowable and the host mediates every call. No competitor can render this because they cannot see it.

---

$${\color{#3ddc97}\textbf{THE FOUR VERBS}}$$

Every feature of the QQQ Console is an instance of exactly one verb. If it is not, it is a commodity feature — and it is not built.

| Verb | What it means | Console answer |
|---|---|---|
| **EXPLAIN** | Trace any outcome to a causal chain with a fix | Causal Lens · Cost Meter |
| **REPLAY** | Reproduce any past execution bit-for-bit | Flight Recorder · Regression Vault · Time Travel |
| **SIMULATE** | Predict the effect of a change before making it | Change Simulator · Drift Sentinel |
| **CONTAIN** | Run anything untrusted with provable, minimal, reviewable authority | Probe Playground · Supply-Chain Radar · Authority Lens |

This is the admission filter. It keeps the Console from becoming an infinite project.

---

$${\color{#f4a261}\textbf{THE 16 PILLARS}}$$

The Console is the interactive layer of the runtime: install, run, tune, inspect, debug — by humans (mouse + keyboard TUI) and by AI agents (MCP, JSONL, semantic UI) — plus an SDK so software built on QQQ ships its own installer and control surface.

### The Original Eight

| # | Pillar | Promise |
|---|---|---|
| 1 | **Mission Control** | The Constellation — a live, deterministic graph of the running system. See everything, understand anything. |
| 2 | **Live Knobs** | Change any runtime parameter — fuel, memory, concurrency, routing — without a restart. Guardrails prevent foot-shooting. |
| 3 | **Authority Lens** | See exactly what any component can do, before it runs. Time-boxed grants. Capability budgets over time. |
| 4 | **Time Machine** | *Superseded by the Flight Recorder.* The opt-in recorder is now always-on. |
| 5 | **Setup Studio** | Zero-config onboarding. A first run that works. Predictive preflight catches problems before they happen. |
| 6 | **Co-pilot Lanes** | AI agents operate alongside humans with presence, leases, and an Agent Action Ledger. |
| 7 | **Control Surface SDK** | Ship your own installer wizard and control panels as data. Ops Recipes for common patterns. |
| 8 | **Terminal Craft** | A TUI that respects the terminal. Plain/JSONL parity is a tested invariant. |

### The Pillars Plus

| # | Pillar | Promise |
|---|---|---|
| 9 | **Flight Recorder** | Always-on, bounded, redacted recording of every execution. Export a `.qqq-session` bundle. Replay precisely what an autonomous agent did. |
| 10 | **Causal Lens** | Trace any outcome — error, denial, latency spike — to its root cause with a fix. `qqqai why` for the terminal. |
| 11 | **Probe Playground** | Run any component in a zero-grant sandbox. See exactly what it *tries* to do. A minimum-manifest diff shows the least authority it needs. |
| 12 | **Change Simulator** | Predict the effect of a change before making it. Traffic simulation. Shadow replay. The Drift Sentinel catches configuration drift. |
| 13 | **Regression Vault** | An incident becomes a sealed test. Red-first gate rejects vacuous tests. Chaos Console reproduces failures by seed. |
| 14 | **Supply-Chain Radar** | The ongoing dependency authority / provenance / advisory board. An update that widens authority cannot proceed without consent. |
| 15 | **Time Travel** | Reverse stepping through a recorded execution. *Not in V1* — needs state checkpoints + an RFC. The trace-hash determinism CI + divergence bisect ship first. |
| 16 | **Cost & Energy Meter** | A price tag per request, tenant, and route. A cost ledger. Budgets that alert. Explain-a-cost → Causal Lens. |

---

$${\color{#4895ef}\textbf{INSTALL}}$$

```bash
# macOS / Linux
curl -fsSL https://qqq.codes/install.sh | sh

# Windows
irm https://qqq.codes/install.ps1 | iex

# Rust
cargo install qqqai

# Node / Bun developers
npm install -g qqqai

# Package managers
brew install qqqai        # macOS / Linux
scoop install qqqai       # Windows
```

One binary. No runtime dependency. No version manager bootstrap.

---

$${\color{#ffd166}\textbf{WHAT MAKES IT DIFFERENT}}$$

### Isolation that is provable, not promised

Containers are a **deployment** boundary. QQQ components are a **security** boundary with a machine-checkable manifest.

Ask what any artifact can do — **without running it**:

```bash
$ qqqai inspect ./build/agent-sandbox.component.wasm
```

```json
{
  "component": "agent-sandbox@0.1.0",
  "capabilities": {
    "fs":     [{ "path": "/tmp/session-42", "mode": "read-write" }],
    "http":   { "client": ["api.example.com:443"] },
    "crypto": { "random": true }
  },
  "denied_by_default": ["env", "sql", "kv", "queue", "secrets", "dns"],
  "limits": { "memory": "64MiB", "fuel": 2000000000, "epoch_deadline_ms": 5000 }
}
```

An agent or an auditor can decide whether to run it **before** a single instruction executes. No other runtime gives you that.

And when a capability is missing, you get the *why*, not a cryptic denial:

```bash
$ qqqai why sql.orders
```

```
sql.orders  DENIED
  ├─ qqq.toml          grants: (none)
  ├─ org policy        "prod-baseline": no widening permitted
  └─ decision          no layer grants this capability

  To grant it, add to qqq.toml:
    [[capabilities.sql]]
    name = "orders"
    driver = "postgres"
    secret = "env:ORDERS_DB_URL"
```

**Secrets never enter guest memory.** The `qqq:secrets` interface lets a component *use* a key without ever *seeing* it. A fully compromised guest can request a signature; it cannot steal the signing key. That eliminates an entire category of breach.

### Five languages, one artifact graph

Rust · TypeScript · Go · Python · C/C++

Write the hot path in Rust, the data pipeline in Python, the glue in TypeScript, the codec in C. They compile to **one component graph with one type system**, linked and type-checked together — no HTTP hop, no JSON serialization at the seam.

Python is the one that should stop you: **neither Node nor Bun can run Python at all.** QQQ treats it as a first-class citizen of the same runtime.

Every host capability is defined in WIT **first** and bound into each language **second**. If a language can't reach something, it's published in the parity matrix — not quietly omitted from the docs.

### Fast where it counts

There is no garbage collector anywhere in the request path — not in the host, not between requests.

| | Node / Bun | QQQ |
|---|---|---|
| Isolation unit | Process / container | Component instance |
| Instantiation | ~10–100 ms | **microseconds** |
| Memory per unit | Tens of MB | **KB-scale** |
| GC pauses in request path | Yes | **None** |
| Languages | 1 | **5** |
| Capability scoping | Process-wide | **Per-instance, per-request** |

That is not a tuning difference. It is an architectural one.

### Agents are users, not just tools

```bash
qqqai mcp
```

One command turns QQQ into an **MCP server**. Any MCP-capable agent can scaffold, build, test, inspect, audit, deploy and debug QQQ projects through structured tools — no bespoke integration.

Every command emits stable, versioned, schema-published JSON:

```bash
qqqai schema --all      # JSON Schema for every surface, including itself
```

Every error carries a stable code, a cause, a remediation, and a docs URL — so an agent that has never seen QQQ can self-correct without a human in the loop.

### Determinism — replay any execution, bit for bit

```bash
qqqai test --trials 10000      # any output difference across runs is a failure
qqqai run --replay incident.log
```

Time, randomness, scheduling and float behaviour are all host-mediated and seeded. Reproduce a production incident exactly. Prove a property test is not flaky. **Replay precisely what an autonomous agent did.**

No competing runtime can offer this, because neither can control the nondeterminism its own engine introduces.

### Instant reload

```
✓ Compiled in 412ms
⟳ Listening on http://127.0.0.1:3000
```

Because your code is a *component instance* and not a language heap, reloading is a pointer swap — not a process restart. Node and Bun fundamentally cannot do this; restarting means rebuilding the JS heap.

---

$${\color{#4cc9f0}\textbf{LIVE STATUS}}$$

**Pre-alpha.** Version `0.1.1`. The runtime is being built in the open.

<table>
<tr>
<td align="center" width="33%">

**Project Stats**

<img src="https://github-readme-stats.vercel.app/api?username=RatioArtificiosa&show_icons=true&theme=radical&hide_border=true" alt="stats"/>

</td>
<td align="center" width="33%">

**Top Languages**

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=RatioArtificiosa&layout=compact&theme=vision-friendly-dark&hide_border=true" alt="langs"/>

</td>
<td align="center" width="33%">

**Contribution Streak**

<img src="https://github-readme-streak-stats.herokuapp.com/?user=RatioArtificiosa&theme=tokyonight&hide_border=true" alt="streak"/>

</td>
</tr>
</table>

<table>
<tr>
<td align="center" width="50%">

**Activity Graph**

<img src="https://github-readme-activity-graph.vercel.app/graph?username=RatioArtificiosa&theme=tokyo-night&hide_border=true" alt="activity"/>

</td>
<td align="center" width="50%">

**Profile Summary**

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=RatioArtificiosa&theme=github_dark&animation=sequence" alt="summary"/>

</td>
</tr>
</table>

| Area | Status |
|---|---|
| Capability engine | **Complete.** The narrowing-only invariant is structural — `GrantSet` has no widening API. |
| HTTP / HTTP2 | **Built.** HTTP/1.1 complete; HTTP/2 module complete (not yet wired to a listener). |
| Security | **28/30 items done.** Zero `unsafe` blocks across the workspace. External audits are the 2 open items. |
| Languages | **Experimental probes.** Six narrow HTTP probes pass. Production drivers and conformance remain open. |
| Packages | **Early.** The registry client, solver, and store are not yet implemented. |
| Performance | **Honest misses.** Throughput and p99 do not yet meet budget. Published with methodology. |
| Console (TUI) | **Designed.** 16 pillars specified. Implementation begins after the runtime foundation is green. |

**274 / 587 checklist items done (46.7%).** Every item cites the proposal section it implements. CI fails the build if the cross-reference graph breaks.

```bash
python tools/check_xrefs.py
```

We are not asking you to believe the numbers in this README. We are asking you to read the proposal, check our method, and tell us where we are wrong.

**Found a flaw?** That is the most valuable thing you can contribute right now. Open an issue.

---

$${\color{#ef476f}\textbf{THE ROADMAP}}$$

The roadmap turns 24 audit findings into 8 dependency-ordered waves. A live session is executing them now.

| Wave | Focus | Status |
|---|---|---|
| **0** | Safety net — tooling, hygiene | **Shipped** |
| **1** | Hot-path security — host boundary | **Shipped** |
| **2** | Panic model — poison-tolerant locks, unwind | **Shipped** |
| **3** | Resource accounting — memory, pool, marshalling | **In progress** |
| **4** | Output pump — streaming, backpressure | Not started |
| **5** | Audit and abuse controls | Not started |
| **6** | Efficiency and cleanup | Not started |
| **7** | Future-wiring — transport decision | Not started |

### Beyond V1

| ID | Item | Why |
|---|---|---|
| FUT-001 | QQQ Fabric GA | Commercial core — multi-host control plane, fleet policy |
| FUT-002 | Browser target | The QQQ host compiled to Wasm, running components in-browser |
| FUT-003 | Native codegen | AOT hot components to native with MPK-based isolation |
| FUT-005 | Distributed composition | Components calling components over the network |
| FUT-006 | Formal verification | The ultimate "provable isolation" |
| FUT-007 | `qqq:ai` | Local inference as a metered capability |
| FUT-009 | Time-travel debugging | Record/replay with reverse stepping |
| FUT-010 | QQQ Cloud | A hosted platform — only if the runtime wins on its own |

### The end goal

A runtime that **competes with Bun and Node and wins**, because:

- **All coding languages compile to one artifact graph** — no team is locked into one language.
- **Security is structural** — an agent or a package has only the authority the manifest granted, enforced outside the guest.
- **AI operates it with extreme ease** — one control plane, typed events/actions, MCP, a semantic UI tree, deterministic replay.
- **The Console makes it trustworthy** — you can see what code can do *before* it runs, exactly what it did, what would happen if you changed it, and how to undo it.

---

$${\color{#5c677d}\textbf{WHERE WE LOSE}}$$

We are going to publish numbers that make us look worse than our competitors, on purpose. A benchmark you can't argue with is worth more than one you can.

- **`hello world` HTTP throughput.** Bun is exceptional at this and has spent years optimizing for it. We may reach parity. We do not promise to beat it.
- **Ecosystem size.** npm has millions of packages. We are starting near zero, and we will be honest about how long closing that gap takes.
- **Familiarity.** Every JavaScript developer already knows Node. Our onboarding costs more, and that cost is real.
- **"Drop-in Node replacement."** This is not one. `npm i express` will not work. We provide a migration path and a conversion report — not an interpreter for the Node API surface, because that path kills runtimes.

Every performance claim we publish ships with its hardware, toolchain versions, concurrency levels, percentiles and methodology — and a section stating what the benchmark **does not** measure.

---

$${\color{#f6e2a8}\textbf{PRICING}}$$

**The runtime is free. Forever. For everyone. Including your company.**

`qqqai` — the runtime, CLI, SDKs, package manager, dev server, test runner — is **Apache-2.0**. No seat limits. No revenue limits. No telemetry phone-home. Nothing to ask your legal team about before running code.

We charge for **governance, evidence, and liability** — never for the ability to execute.

| | Who | Fabric (governance) | Support |
|---|---|---|---|
| **Free** | Individuals, solo developers, non-profits, companies under $2M revenue | Included | Community |
| **Team** | Up to 25 engineers | Included | Email |
| **Business** | Up to 250 engineers | Included | 8x5 SLA |
| **Enterprise** | 250+ | Included | 24x7, indemnification, air-gapped |

**QQQ Fabric** is a separate, commercially-licensed product: organization-wide policy, fleet attestation, SSO/RBAC, compliance evidence export, audit retention, and air-gapped supply-chain mirrors.

> **Plain language:** if you are one person with an idea, you get everything, for free, including Fabric. If you are a company, the *runtime* is still free — you pay only if you want the governance layer.
>
> Fabric is **not** OSI open source, and we won't call it that. The runtime is.

---

$${\color{#b388ff}\textbf{PRINCIPLES}}$$

QQQ is built against **eight non-negotiables**, published in [`PRINCIPLES.md`](PRINCIPLES.md). They are treated as a constitution, not marketing copy. The PR template requires naming any principle your change touches.

1. **AI agents are first-class users** — if an agent can't reliably generate, inspect, modify, test or deploy against QQQ, the design is incomplete.
2. **Security and isolation are non-optional** — untrusted code will run here. That is the point.
3. **Performance and predictability over micro-benchmarks** — percentiles under realism, not peaks under ideal conditions.
4. **Multi-language by design** — no privileged language.
5. **Explicit contracts over implicit behavior** — no hidden state, no magic, typed errors.
6. **Human + machine documentation parity** — outdated docs are a defect, not a chore.
7. **Progressive power, safe defaults** — zero capabilities out of the box; power when you ask for it.
8. **Ecosystem integrity and long-term stewardship** — open, governed, and serious about backward compatibility.

---

$${\color{#3ddc97}\textbf{CONTRIBUTING}}$$

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`PRINCIPLES.md`](PRINCIPLES.md) first. The RFC process governs changes to published interfaces and to the principles themselves.

**Security:** do not open a public issue. See [`SECURITY.md`](SECURITY.md).

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=RatioArtificiosa&label=Profile+Views&color=4cc9f0&style=flat-square" alt="views"/>
</p>

---

<p align="center">
  <sub>Apache-2.0 · qqq.codes · Built on <a href="https://wasmtime.dev">Wasmtime</a> and the <a href="https://component-model.bytecodealliance.org">WebAssembly Component Model</a></sub>
</p>
<p align="center">
  <sub><em>Run anything. Trust nothing.</em></sub>
</p>
