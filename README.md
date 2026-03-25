# Architect

Architect by Shreyas Kapale @ Lyzr — helps you build GitAgents. An AI agent that helps developers build, run, and manage AI agents using the gitagent framework.

## Run

```bash
npx @open-gitagent/gitagent run -r https://github.com/shreyas-lyzr/architect
```

Or with a prompt:

```bash
npx @open-gitagent/gitagent run -r https://github.com/shreyas-lyzr/architect -p "How do I create my first agent?"
```

## What It Can Do

- **Get started** — Install gitagent, scaffold your first agent, validate and run it
- **Create agents** — Write agent.yaml, SOUL.md, RULES.md, add skills, tools, and knowledge
- **Run agents** — Use any adapter (Claude, OpenAI, Lyzr, GitHub Models, etc.)
- **Export & import** — Convert between gitagent and other frameworks
- **Manage skills** — Search, install, create, and organize skills
- **Register agents** — Submit agents to the gitagent registry at registry.gitagent.sh

## Skills

| Skill | Description |
|-------|-------------|
| `get-started` | Installation and first-agent walkthrough |
| `create-agent` | agent.yaml schema, SOUL.md writing, directory structure |
| `run-agent` | All adapters, flags, caching, auto-detection |
| `export-agent` | Export formats, import sources, conversion |
| `manage-skills` | Search, install, create, discover skills |
| `register-agent` | Submit agents to the gitagent public registry |

## Structure

```
architect/
├── agent.yaml
├── SOUL.md
├── RULES.md
├── skills/
│   ├── get-started/
│   ├── create-agent/
│   ├── run-agent/
│   ├── export-agent/
│   ├── manage-skills/
│   └── register-agent/
└── knowledge/
    ├── index.yaml
    └── command-reference.md
```

## Built with

[gitagent](https://github.com/open-gitagent/gitagent) — a git-native, framework-agnostic open standard for AI agents.
