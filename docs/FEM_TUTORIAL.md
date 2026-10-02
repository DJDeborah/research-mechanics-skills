# FEM Explicit / bifurcation tutorial

## 1. Reproduce the numerical smoke

From the repository root:

```bash
python tools/run_abaqus_smoke.py --abaqus abaqus --out local-runs/explicit --sensitivity
```

The runner creates three cases: 10 elements at 0.25 s, 20 at 0.25 s, and 20 at 0.50 s. Each run stores its config, registered selected nodes, INP, console completion evidence, ODB, exported histories, quality audit and event candidates. The summary compares final elastic reaction. It does not infer convergence order or buckling capacity.

The default is a 100 mm straight elastic cantilever, rectangular section 10 × 1 mm, E=210000 N/mm², ν=0.3, density=7.85e-9 tonne/mm³. ROOT fixes U1/U2/UR3; TIP ramps U2 to −0.1 mm. The section director is (0,0,−1). The small-deformation reference tip reaction is −0.0525 N.

## 2. Run individual stages

```bash
python skills/fem-explicit-bifurcation/scripts/prepare_explicit.py skills/fem-explicit-bifurcation/assets/beam-explicit.json --out local-runs/my-beam
```

Inspect `registration.json`, then change to `local-runs/my-beam` before launching:

```bash
abaqus job=beam_explicit input=beam_explicit.inp double=both interactive
```

Use absolute script/config paths for extraction when outside the repository root:

```text
abaqus python <absolute-skill-dir>/scripts/extract_odb.py beam_explicit.odb history.json
python <absolute-skill-dir>/scripts/audit_history.py history.json --config <absolute-config> --out quality.json
python <absolute-skill-dir>/scripts/detect_events.py history.json --config <absolute-skill-dir>/assets/events.json --out events.json
```

`history.json` is actual solver output. `events.json` identifies configured force-drop/opening candidates. The smoke should have no force-drop candidate with its supplied sign convention and 15% threshold.

## 3. Boundary reuse

Change the JSON, not a buried coordinate in a long prompt. `regions` contains named bounding boxes and expected selection counts. `constraints` refers to those names and explicit DOFs. The generator verifies actual selected IDs, rejects conflicts and restricts this adapter to its registered cantilever model.

Changing length requires moving the TIP selector with the physical endpoint. An interior node may still satisfy expected_count=1; the adapter additionally checks the endpoint identity. For a real mesh, replace the geometry/selection adapter with CAD faces or mesh sets, and preserve the same registration output contract.

## 4. Equilibrium stability is a separate analysis

```bash
python skills/fem-explicit-bifurcation/scripts/branch_benchmarks.py --out local-runs/branches.json
```

This samples exact fold and pitchfork branches to test residual and tangent-sign interpretation. It has no FE branch solver. To assess actual postbuckling, integrate a registered static/continuation backend, extract constrained modes and test branch identity/contact feasibility. Compare stable Explicit windows to those equilibria before interpreting dynamic transitions.

## Troubleshooting learned from actual runs

- Interactive R2019x can omit `.log`; extraction uses the STA success record plus a readable expected ODB step.
- Old Abaqus ODB repositories should be inspected using `.keys()` rather than assuming ordinary Python membership behavior.
- The Abaqus launcher can return 0 even after a Python traceback; the runner requires the resulting history artifact.
- A completed single-precision run drifted approximately 0.39% from its prescribed final displacement and was rejected. `double=both` removed the observed drift for this example; this is a measured case-specific finding.
- The deck's standard displacement-boundary warning was reviewed: there is one smooth-step ramp with no intended inter-step displacement jump. Warnings remain in local console/data records.
