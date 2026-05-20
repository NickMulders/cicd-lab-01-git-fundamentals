# Lab 01 — Git Fundamentals

Day 1, Blocks A and B of the [CI/CD for Ignition Masterclass](https://github.com/mustry-academy/cicd-masterclass).

> Build a working mental model of Git, and learn to operate confidently with branches, commits, merges, and rebases.

This is the first lab in the course. We deliberately stay out of Ignition territory for now — the only subject of our Git exercises is a tiny generic Python app in [`sample-app/`](./sample-app/). Ignition-specific deployments arrive in Lab 04.

## Prerequisites

- Pass [`cicd-preflight`](https://github.com/mustry-academy/cicd-preflight)
- Read the Day 1 brief in your welcome packet
- Clone this repo before the live session

## Quick start

```bash
gh repo clone mustry-academy/cicd-lab-01-git-fundamentals
cd cicd-lab-01-git-fundamentals
python -m venv .venv && source .venv/bin/activate
pip install -r sample-app/requirements.txt
pytest sample-app/tests
```

If you'd rather skip the local Python setup, the lab also runs in [GitHub Codespaces](https://github.com/features/codespaces) — see [`.devcontainer/devcontainer.json`](./.devcontainer/devcontainer.json).

## Lab structure

| Block | Topic | Exercise |
|---|---|---|
| A | Why version control matters; Git's object model demystified | [`exercises/block-a.md`](./exercises/block-a.md) |
| B | Everyday workflows: add, commit, branch, merge, rebase | [`exercises/block-b.md`](./exercises/block-b.md) |

## Checkpoints

This repo uses **Git tags** as immutable checkpoints. If you get lost, you can always reset:

```bash
git fetch --tags
git checkout block-a-start    # back to the start of Block A
git checkout block-a-end      # to see the instructor's reference solution
git checkout block-b-start
git checkout block-b-end
```

| Tag | What it represents |
|---|---|
| `block-a-start` | Starting point for Block A — `sample-app/` with a seeded multi-commit history |
| `block-a-end` | Reference solution after Block A |
| `block-b-start` | Starting point for Block B — clean `main` with the seed script available |
| `block-b-end` | Reference solution after Block B: three-commit feature branch rebased into `main`, plus a `--no-ff` demonstration branch |

## Repo layout

```
cicd-lab-01-git-fundamentals/
├── README.md
├── PLAN.md                       ← design doc for this lab
├── .devcontainer/                ← Codespaces fallback config
├── exercises/
│   ├── block-a.md
│   └── block-b.md
├── docs/                         ← reference reading
│   ├── why-version-control.md
│   └── git-object-model.md
├── instructor-notes/             ← answer keys (read after solo work)
│   ├── block-a-key.md
│   └── block-b-key.md
├── scripts/
│   ├── seed-messy-state.sh       ← deterministic dirty working tree for Block B
│   └── verify-block-a.sh         ← sanity-check the Block A solo exercise
└── sample-app/                   ← the tiny Python app we'll version together
    ├── app.py
    ├── requirements.txt
    ├── tests/
    │   └── test_app.py
    └── README.md
```

## Licence

Apache 2.0 — see [`LICENSE`](./LICENSE).
