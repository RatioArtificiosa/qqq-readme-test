<div style="background-color:#000000;color:#F5F7FA;padding:32px">

<p align="center">
  <img src="https://img.shields.io/badge/runtime-WebAssembly%20Component%20Model-0077FF?style=for-the-badge&logo=webassembly&logoColor=white" alt="runtime"/>
  <img src="https://img.shields.io/badge/security-capability--secure-FF3B4E?style=for-the-badge" alt="security"/>
  <img src="https://img.shields.io/badge/languages-5%20first--class-00E676?style=for-the-badge" alt="languages"/>
  <img src="https://img.shields.io/badge/license-Apache%202.0-FFB020?style=for-the-badge" alt="license"/>
  <img src="./pre-alpha-badge.svg" alt="status: pre-alpha"/>
</p>

<p align="center">
  <img src="./qqq-logo.png" alt="QQQ — Industrial Cyberpunk Terminal" width="100%"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1200&color=0077FF&center=true&vCenter=true&width=800&lines=The+runtime+built+for+humans+and+AI+agents.;Secure+by+default.+Multi-language.+Fast+where+it+counts.;Run+anything.+Trust+nothing." alt="typing"/>
</p>

<p align="center">
  <a href="#-run-anything-trust-nothing"><img src="https://img.shields.io/badge/HOOK-Run_anything-0077FF?style=for-the-badge" alt="hook"/></a>
  <a href="#-runtime-pulse"><img src="https://img.shields.io/badge/PULSE-Live_telemetry-00D9FF?style=for-the-badge" alt="pulse"/></a>
  <a href="#-the-wall"><img src="https://img.shields.io/badge/WALL-Allow_deny-FF3B4E?style=for-the-badge" alt="wall"/></a>
  <a href="#-five-languages-one-runtime"><img src="https://img.shields.io/badge/LANGS-5_to_1-8B5CF6?style=for-the-badge" alt="langs"/></a>
  <a href="#-node-bun-qqq"><img src="https://img.shields.io/badge/VS-Node_Bun-FFB020?style=for-the-badge" alt="versus"/></a>
  <a href="#-install"><img src="https://img.shields.io/badge/INSTALL-One_binary-00E676?style=for-the-badge" alt="install"/></a>
</p>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

### A Rust-native runtime for software written by humans and machines.

```text
RUST · TYPESCRIPT · GO · PYTHON · C/C++
              |
       WEBASSEMBLY COMPONENTS
              |
             QQQ
              |
   CAPABILITY-SECURE EXECUTION
```

A module has zero authority not explicitly granted in `qqq.toml`. That authority is enforced outside the guest, checkable before execution, recorded after every call.

```toml
# qqq.toml — the whole security model, readable in 30 seconds
[capabilities]
fs     = [{ path = "/tmp/session-42", mode = "read-write" }]
http   = { client = ["api.example.com:443"] }
crypto = { random = true }

[limits]
memory = "64MiB"
fuel   = 2_000_000_000
epoch_deadline_ms = 5000
```

That file is the contract. Code cannot read `/etc/passwd`, cannot open an arbitrary socket, cannot read the environment, cannot outlive fuel — because those imports do not exist in its instance.

</div>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{RUNTIME PULSE}}$$

Industrial telemetry first. Flat cells, hard blocks, tiny grid. No gradient wash.

```text
+-- QQQ RUNTIME / LIVE --------------------------------------------------+
| REQUESTS            LATENCY              MEMORY            COMPONENTS   |
| 412 rps             18 ms p99            64 MiB            27 ACTIVE    |
| [################]  [####..............] [#######.........] [*][*][*]   |
|                                                                         |
| CAPABILITIES                                                            |
| FS      [########] GRANTED                                               |
| HTTP    [###########] GRANTED                                            |
| CRYPTO  [####....] GRANTED                                               |
| SQL     [........] DENIED                                                |
+-------------------------------------------------------------------------+
```

Color carries meaning: blue granted, red denied, amber needs attention, green success, cyan live data, violet AI and components.

</div>

<div style="background-color:#000000;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{LOADING}}$$

```text
+----------------------------------------------------------------+
| LOADING..                                                      |
| [##..##..##..##................................]                |
+----------------------------------------------------------------+
```

</div>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{THE CAPABILITY GRAPH}}$$

```text
                 +---------+
                 |  AGENT  |
                 +----+----+
                      | HTTP CAPABILITY
                      v
+---------+    +---------+    +------+  +------+  +--------+
| PYTHON  |--->|   QQQ   |--->| FILE |  | HTTP |  | CRYPTO |
+---------+    +----+----+    +------+  +------+  +--------+
                    |            v         v          v
                    |          ALLOW     ALLOW      ALLOW
               +----+----+
               | DATABASE|
               +----+----+
                    X DENIED — NOT GRANTED
```

</div>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{THE WALL}}$$

```text
            UNTRUSTED COMPONENT
            +----------------+
            |   AI AGENT     |
            | Python + deps  |
            +-------+--------+
                    |
            +-------v--------+
            | QQQ WALL       |
            +---+--------+---+
                |        |
              ALLOW    DENY
                |        X
              /tmp     /etc
              api      secrets
              crypto   arbitrary
```

</div>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{FIVE LANGUAGES, ONE RUNTIME}}$$

```text
      RUST       TYPESCRIPT
        \           /
         \         /
          v       v
        +---------------+
        |               |
 GO --->|      QQQ      |<--- PYTHON
        |               |
        +-------+-------+
                |
              C/C++
```

# ONE RUNTIME. FIVE LANGUAGES.
# ONE COMPONENT GRAPH.

Write the hot path in Rust, the pipeline in Python, the glue in TypeScript, the codec in C. One component graph, one type system, no JSON at the seam. Python is first-class. Node and Bun cannot run it at all.

</div>

<div style="background-color:#05070B;border:1px solid #0077FF;padding:24px">

## $${\color{#0077FF}\textbf{AOT PIPELINE}}$$

### <span style="color:#0077FF">Compile once. Validate against the unchanged policy. Lease per request.</span>

<span style="color:#0077FF">AOT moves native compilation out of request dispatch. The request path never compiles. It leases an already-prepared generation and runs it.</span>

<span style="color:#0077FF">`qqqai build --release --aot --aot-cache /absolute/operator-owned/qqq-cache` emits content-addressed `.cwasm` plus JSON provenance in `target/qqq/aot/`. `qqqai serve --aot-cache &lt;same-path&gt;` reuses compatible native code across processes. No ambient Wasmtime cache config is read. The JSON fingerprint is diagnostic metadata, not authorization. Downloaded `.cwasm` is never auto-deserialized. Failed builds leave the last working generation live.</span>

```text

+-- QQQ AOT PIPELINE ---------------------------------------------------+
|  SOURCE / PACKAGE                                                     |
|  |                                                                    |
|  v                                                                    |
|  BOUNDED BUILD + PREPARE  (away from socket executor)                 |
|  |                                                                    |
|  +--> MANIFEST + CAPABILITY VALIDATION (policy unchanged)             |
|  |                                                                    |
|  v                                                                    |
|  MANAGED NATIVE CACHE  --aot-cache /operator-owned/qqq-cache          |
|  |  explicit path only, no ambient config                             |
|  +--> .cwasm + JSON provenance  target/qqq/aot/                       |
|  |  digest = actual loaded bytes, fingerprint = diagnostic            |
|  v                                                                    |
|  CANDIDATE GENERATION (immutable)                                     |
|  |  full handler signature validated, no business call                |
|  v                                                                    |
|  REVISION-CHECKED PUBLISH                                             |
|  |  stale build rejected, lock released before execution              |
|  +--> REGISTRY  name != revision != digest                            |
|  |                                                                    |
|  +--> LEASE PER REQUEST  (one generation pinned admission->done)      |
|  |         |                                                          |
|  |         +--> FRESH LIMITED WASMTIME STORE + WIT HANDLER            |
|  |                                                                    |
|  +--> RETIRE after last lease, then release                           |
|                                                                       |
|  SLOW PATH                       FAST PATH                            |
|  compile once                    reuse native code cross-process      |
|  FAILED BUILD -> last good stays live                                 |
+-----------------------------------------------------------------------+

```

</div>

<div style="background-color:#05070B;border:1px solid #0077FF;padding:24px">

## $${\color{#0077FF}\textbf{HOT SWAP}}$$

### <span style="color:#0077FF">Add and replace pieces without restarting. Node and Bun cannot do this.</span>

<span style="color:#0077FF">Your server never stops listening. Rebuild a component and the next request uses the new generation. Requests already running finish on the old one. Nothing drops, nobody reconnects. A plugin is just a component under a new name: register it and it serves, remove it and it drains, all while the listener stays bound.</span>

<span style="color:#0077FF">How it holds together: the registry keeps named generations; every request takes a lease on the current generation the moment it is admitted; publication is revision-checked so a stale build can never overwrite a newer one; removing a component stops new admissions while outstanding leases run to completion; a failed build leaves the last good generation live. A keep-alive connection simply sees the new generation on its next call. `qqqai dev` watches your source, rebuilds, validates the candidate against the unchanged manifest and full handler signature without calling your code, then activates.</span>

<span style="color:#0077FF">The one thing that still needs a restart is a manifest edit — a change of authority is never applied silently under a running component. That is deliberate.</span>

<span style="color:#0077FF">Why Node and Bun restart: your code IS the heap. Reloading means killing the process, rebuilding the JavaScript heap, rebinding the port, and dropping live connections. In QQQ your code is a component instance behind a registry pointer, so reloading is publishing a pointer while old leases drain.</span>

```text
+-- HOT SWAP -----------------------------------------------------------+
|  LISTENER stays bound, HOST stays alive                               |
|                                                                       |
|  gen 12 LIVE  <-- requests in flight finish here                      |
|  |                                                                    |
|  gen 13 PREPARED + VALIDATED (policy unchanged)                       |
|  |                                                                    |
|  PUBLISH (revision-checked, stale rejected)                           |
|  |                                                                    |
|  gen 13 LIVE  <-- new requests go here                                |
|  gen 12 RETIRES after its last lease                                  |
|  FAILED BUILD -> gen 12 stays live, nobody notices                    |
+-----------------------------------------------------------------------+
```

</div>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{NODE / BUN / QQQ}}$$

```text
+-- THE OLD MODEL ------------------------------------------------------+
|    NODE                              BUN                              |
|    |                                 |                                |
|    v                                 v                                |
|    JS / TS ONLY                      JS / TS FOCUSED                  |
|    |                                 |                                |
|    v                                 v                                |
|    PROCESS                           PROCESS                          |
|    |                                 |                                |
|    v                                 v                                |
|    ISOLATION                         ISOLATION                        |
+-----------------------------------------------------------------------+
```

```text
+-- QQQ ----------------------------------------------------------------+
|  COMPONENT                                                            |
|  Rust                                                                 |
|  Python                                                               |
|  Go                                                                   |
|  TypeScript                                                           |
|  C/C++                                                                |
|  |                                                                    |
|  CAPABILITY HOST                                                      |
|  |                                                                    |
|  ZERO AUTHORITY                                                       |
|  BY DEFAULT                                                           |
+-----------------------------------------------------------------------+
```

| | Node / Bun | QQQ |
|---|---|---|
| Isolation unit | Process / container | Component instance |
| Instantiation | ~10–100 ms | Microseconds |
| Memory per unit | Tens of MB | KB-scale |
| GC pauses in request path | Yes | None |
| Languages | 1 | 5 |
| Capability scoping | Process-wide | Per-instance, per-request |

Node changed JavaScript runtime economics.
Bun pushed the runtime layer forward.
QQQ is asking a different question:
What should a runtime look like when software is generated by machines?

That is positioning — and it connects directly to the AI-agent angle at the heart of this README.

</div>

<div style="background-color:#05070B;border:1px solid #0077FF;padding:24px">

## $${\color{#0077FF}\textbf{AI WROTE THIS}}$$

# SOFTWARE IS CHANGING.

```text
HUMAN                AI AGENT
  |                    |
  writes code          generates code
  |                    |
  runtime              downloads dependencies
  executes it          |
                       modifies code
                       |
                       executes code
                       |
                       calls tools
                       |
                       accesses resources
                       |
                       QQQ contains it
```

# THE RUNTIME HAS TO CHANGE TOO.

<span style="color:#0077FF">That is a stronger reason to exist than "we made another runtime in Rust." The mechanics, borrowed from direct response:</span>

<span style="color:#0077FF">1. **Big claim** — RUN ANYTHING. TRUST NOTHING.</span>
<span style="color:#0077FF">2. **Agitate the problem** — AI agents write code faster than humans can review it.</span>
<span style="color:#0077FF">3. **New mechanism** — the runtime itself becomes the security boundary.</span>
<span style="color:#0077FF">4. **Proof** — capability graph, denied access, replay, deterministic execution, telemetry.</span>
<span style="color:#0077FF">5. **Specific differentiation** — five languages, one component graph, zero ambient authority.</span>
<span style="color:#0077FF">6. **CTA** — see below.</span>

# RUN QQQ

</div>

<div style="background-color:#05070B;border:1px solid #0077FF;padding:24px">

## $${\color{#0077FF}\textbf{THE CONSOLE}}$$

### <span style="color:#0077FF">Your running system, drawn live in the terminal. Plain language below.</span>

<span style="color:#0077FF">The Console is QQQ's terminal dashboard. It draws every running component as a graph, so you see what talks to what, how fast, and with what powers. When something breaks, it tells you why in words, lets you replay the exact moment, shows what a change would do before you make it, and runs anything untrusted with almost no powers.</span>

<span style="color:#0077FF">- **Mission Control** — the live graph. Node size is traffic, the ring is latency, the color is health.</span>
<span style="color:#0077FF">- **Live Knobs** — turn fuel, memory, and routing up or down without a restart. Guardrails stop you shooting your own foot.</span>
<span style="color:#0077FF">- **Authority Lens** — see exactly what a component may touch before it runs. Nothing hidden.</span>
<span style="color:#0077FF">- **Flight Recorder** — every run is recorded. Rewind any moment and play it again exactly.</span>
<span style="color:#0077FF">- **Probe Playground** — run a stranger's code with zero powers and watch what it reaches for.</span>
<span style="color:#0077FF">- **Cost Meter** — every request gets a price tag per tenant and route.</span>

```text

+-- QQQ CONSOLE / MISSION CONTROL --------------------------------------+
|  myapp - dev - gen 12      412 rps - p99 18 ms - ok                   |
|                                                                       |
|  web ---- api ---- db ---- cache                                      |
|    o        *        o        o                                       |
|                                                                       |
|  * healthy    o degraded    . stopped    x failed                     |
|                                                                       |
|  EXPLAIN:  why did this happen, and what is the fix                   |
|  REPLAY:   run this exact moment again, bit for bit                   |
|  SIMULATE: what changes if I touch this first                         |
|  CONTAIN:  run it with almost no powers and watch                     |
+-----------------------------------------------------------------------+

```

</div>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{LIVE STATUS}}$$

Pre-alpha. Version `0.1.1`. Wasmtime 48.0.5 pinned. Checklist 274/587 done (46.7%, dashboard authoritative).

</div>

<div style="background-color:#05070B;border:1px solid #1E293B;padding:24px">

## $${\color{#0077FF}\textbf{INSTALL}}$$

```bash
# macOS / Linux
curl -fsSL https://qqq.codes/install.sh | sh

# Windows
irm https://qqq.codes/install.ps1 | iex

# Rust
cargo install qqqai
```

One binary. No runtime dependency. No version manager bootstrap.

</div>

<p align="center">
  <sub>Apache-2.0 · qqq.codes · Built on Wasmtime and the WebAssembly Component Model</sub>
</p>
<h1 align="center">RUN ANYTHING. TRUST NOTHING.</h1>

</div>
