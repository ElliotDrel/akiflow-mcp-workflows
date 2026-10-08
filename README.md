# Akiflow Workflows plugin

This package gives Akiflow a small, source-controlled starting point for publishing its existing remote MCP service in the ChatGPT and Claude directories.

This is a community-maintained plugin, not an official Akiflow release. It uses Akiflow's official server; it does not implement or host that server. Installing this GitHub package does not mean it has been approved for a public platform directory.

## Install in Codex

Add this repository as a plugin marketplace, then install the package:

```sh
codex plugin marketplace add ElliotDrel/akiflow-mcp-workflows
codex plugin add akiflow-mcp-workflows@akiflow-community
```

Refresh or restart your client if the plugin does not appear immediately. Complete Akiflow's OAuth connection when prompted. Never paste passwords or access tokens into chat or this repository. Start with: "Review my Akiflow schedule for today without making changes."

## ChatGPT and Codex packaging

The root `plugin.json` provides the portable manifest and OpenAI display metadata; `mcp.json` connects the remote server, and `skills/` contains the shared workflow guidance. `.agents/plugins/marketplace.json` makes the package discoverable from this GitHub marketplace. ChatGPT installation depends on the plugin installation options available in your client and account; the Codex commands above do not publish it to ChatGPT's public directory.

See the [official OpenAI plugin build documentation](https://developers.openai.com/plugins/build/plugins) for packaging and marketplace behavior. For public directory submission and vendor-owned requirements, read the [directory handoff](docs/MARKETPLACE_HANDOFF.md).

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
├── .agents/plugins/marketplace.json     # GitHub marketplace for Codex
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

