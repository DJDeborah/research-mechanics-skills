# Installation / 安装

## Complete-directory installation

Use Python 3.10+; portable scripts need no pip dependencies. Clone or download and extract this repository. From its root:

```bash
python tools/install.py --user
```

This installs all five complete directories into the current user's `~/.agents/skills`. To install one:

```bash
python tools/install.py --user --skill research-gap
```

For a team project:

```bash
python tools/install.py --project ../research-project
```

The destination is `<project>/.agents/skills`. For a host whose built-in installer uses `$CODEX_HOME/skills`, specify that directory using `--dest`, or use the built-in skill-installer below. Do not install the same names into several discovery scopes unintentionally: Codex can show duplicate entries.

The installer refuses an existing skill directory and checks all requested destinations before copying. To update, review the new version and move/rename the old directory first. It will not silently replace a locally modified skill.

## Install inside Codex using its bundled skill-installer

Paste this in Codex:

```text
$skill-installer
Install these five skills from DJDeborah/research-mechanics-skills:
skills/research-significance
skills/research-gap
skills/research-writing
skills/fem-explicit-bifurcation
skills/research-word
```

That tool controls its own destination and non-overwrite policy. The repository's scripts/resources must accompany each SKILL.md; copying only the Markdown loses the executable part. For reproducibility, use the published tag `v0.1.0` for the original four skills, or a pinned commit for the current five-skill bundle when the installer supports `--ref`.

After installation, start a new Codex task/turn and type `$research-gap` (or another exact name). Verify the skill appears in the selector or that Codex reads its SKILL.md. If the running app has cached discovery, refresh or reopen it. No YAML text needs to be pasted into the chat.

## Minimal runtime check

```bash
python -m unittest discover -s tests -v
python tools/run_demo.py --out local-runs/demo
```

Use a fresh output directory on a repeat run. Audit helpers return exit code 2 for rejected contracts; a traceback is an execution/input problem. The demo uses a synthetic literature fixture, a prospective significance statement, and known scalar normal forms. It does not run Abaqus.

## Optional licensed solver

The actual tested solver is Abaqus/Explicit 3DEXPERIENCE R2019x with Python 2.7.3 for ODB extraction. The surrounding portable tools run under Python 3.10+. In an environment where the Abaqus command is on PATH:

```bash
python tools/run_abaqus_smoke.py --abaqus abaqus --out local-runs/explicit --sensitivity
```

Windows example:

```powershell
python tools/run_abaqus_smoke.py --abaqus 'D:\Program Files\Dassault Systemes\SIMULIA\Commands\abaqus.bat' --out local-runs/explicit --sensitivity
```

The runner uses `double=both`, captures console output, opens the expected ODB step and requires exported histories. It never accepts a launcher exit code as solver proof. The default deck uses automatic stable increments and no mass scaling.

## Official format references

[OpenAI skill authoring and local discovery](https://learn.chatgpt.com/docs/build-skills), [bundled skill-installer](https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md), [portable plugin packaging](https://developers.openai.com/plugins/build/plugins). The included plugin manifest is a bundle entrypoint, not evidence of public plugin-directory approval.
