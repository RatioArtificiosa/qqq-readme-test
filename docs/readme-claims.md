# README claim ledger

Integrity mechanism for this README: every important claim, its status, its evidence, and the exact wording that is safe to use. Re-check a row when the implementation moves; never upgrade a status without evidence.

| Claim | Status | Evidence | README wording |
|---|---|---|---|
| Rust-native host on Wasmtime | IMPLEMENTED | `Cargo.toml` pins `wasmtime = "48"`, `Cargo.lock` resolves 48.0.5 | "Rust-native WebAssembly runtime", "Wasmtime 48.0.5 pinned" |
| Five-language component graph | DESIGNED | Proposal §2.4, §6.10; probes experimental | "designed for a multi-language component graph spanning…" |
| Rust narrow HTTP probe | IMPLEMENTED | `crates/qqq-run/tests/lang001_rust_guest.rs`, CI language-probes job | "Narrow probe passing" |
| AssemblyScript / C / C++ / TS probes | EXPERIMENTAL | `docs/languages/evidence/*.json`, `docs/languages/phase3.md` in main repo | "Experimental probe", "5/5 vectors" |
| Go TinyGo probe | EXPERIMENTAL | Same evidence; 64 KiB fails under precise GC | "Experimental, bounded" with the failure stated |
| Python probe | EXPERIMENTAL | Same evidence; `--stub-wasi` deterministic probe | "Experimental" with startup/bindings open |
| Capability linker absent-not-denied | IMPLEMENTED | `crates/qqq-host/src/linker.rs`, hostile-guest suite | "An import the manifest did not grant is absent" |
| Bound host modules (5) | IMPLEMENTED | `host_*::register` calls in `linker.rs` | Named list; others "declared, not yet bound" |
| MCP stdio server, 12 tools | IMPLEMENTED | `crates/qqq-run/src/mcp.rs` | "stdio server, 12 tools" |
| `--json` CLI, schemas, error codes | IMPLEMENTED | `crates/qqq-run/src/output.rs`, `qqq-core/src/error.rs` | As worded in README |
| Deterministic replay | IN PROGRESS | `crates/qqq-host/src/replay.rs`, `docs/determinism.md` | "IN PROGRESS" with built/absent split |
| AOT native cache | IN PROGRESS | `crates/qqq-run/src/aot.rs`, live-components RFC | "IN PROGRESS", `.wasm` stays source of truth |
| Hot swap generations | IN PROGRESS | `crates/qqq-run/src/generations.rs`, `live_components.rs` | "IN PROGRESS", no zero-downtime promise |
| Console/TUI | DESIGNED | `F:\QQQ-AUDIT\TUI-Build` design package (not in runtime) | "Status: DESIGNED", no screenshots |
| Telemetry dashboard | DESIGNED | Audit stream exists; no dashboard output | No numeric dashboard in README |
| ABI ~900 ns/crossing | MEASURED | `docs/abi-cost-measured.md`, commit `d3e71fd`, Xeon E5-1650 v4 | With hardware, commit, and methodology link |
| Published packages (cargo/npm/brew) | NOT YET AVAILABLE | Registries have no `qqqai` artifact | Install section is build-from-source only |
| Version number | Withheld | Pre-alpha; no stable release line | PRE-ALPHA badge, no version string |
| Checklist counts | Withheld | Moves daily; would rot as marketing | Not in README |

## Review triggers

Flag for manual review any README wording resembling: "412 rps", "18 ms p99", "27 ACTIVE", "274/587", "microseconds", "KB-scale", "~10-100 ms", "No other runtime", "cannot do this", "nothing drops", "nobody reconnects", "bit for bit", "production-ready", "first-class" (for languages), "only runtime".
