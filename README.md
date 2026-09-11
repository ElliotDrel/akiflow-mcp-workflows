# Akiflow marketplace readiness package

This package gives Akiflow a small, source-controlled starting point for publishing its existing remote MCP service in the ChatGPT and Claude directories.

## What already exists

- Akiflow operates its official remote MCP endpoint at `https://mcp.akiflow.com/mcp`.
- The endpoint requests OAuth before MCP initialization.
- The endpoint advertises `mcp:read` and `mcp:write` scopes.
- Akiflow's public guide documents task, calendar, time-slot, and Meeting Assistant operations.

## What this repository adds

- Packages workflow guidance with the existing server as a portable Agent Plugin.
- Packages the same remote connection as a Claude Code and Cowork plugin.
- Collects the exact review materials and direct submission links for ChatGPT and Claude.
- Keeps platform-specific manifests separate from the server implementation.

## Repository layout

```text
.
├── plugin.json                         # Portable Agent Plugins manifest
├── mcp.json                            # ChatGPT and Codex remote-MCP declaration
├── .claude-plugin/plugin.json          # Claude plugin manifest
├── .mcp.json                           # Claude remote-MCP declaration
├── skills/akiflow-workflows/SKILL.md   # Shared workflow guidance
└── docs/                               # Publication and review handoff
```

## Publish under Akiflow

- Transfer this repository to the Akiflow GitHub organization before any public directory submission.
- Replace the draft publisher details in the manifests and add Akiflow's final `LICENSE`, support channel, privacy policy, and terms URLs.
- Submit the production server from Akiflow-owned OpenAI and Claude organizations.
- Keep the MCP server URL stable after publication because existing directory connections stay tied to the installed endpoint.

## Start with the handoff

- Read [the complete directory handoff](docs/MARKETPLACE_HANDOFF.md).
- Review [the verified endpoint evidence](docs/ENDPOINT_READINESS.md).
- Use [the proposed listing copy and tests](docs/LISTING_MATERIALS.md).

