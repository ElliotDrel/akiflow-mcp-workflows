# Install Akiflow Workflows

## ChatGPT and Codex archive

- Download `dist/akiflow-workflows-openai-0.2.2.zip` from this repository.
- Open [ChatGPT Plugins](https://chatgpt.com/plugins), choose **Add → Upload plugin archive**, and select the ZIP.
- Follow the client's prompts to authorize Akiflow through its sign-in page.
- Use the same archive wherever Codex offers plugin archive import; alternatively use the README's GitHub marketplace commands.
- Start with “Review my Akiflow schedule for today without making changes.”
- Treat archive checks as packaging validation, not proof of a working account connection; client permissions, OAuth and server behavior still need a live test.
- Keep personal installation separate from public discovery; uploading this community package does not create an official Akiflow listing.

## Claude plugin

- Download `dist/akiflow-workflows-claude-0.2.2.zip` from this repository.
- Open [Claude Plugins — Yours](https://claude.ai/new#customize/plugins/yours) and choose the custom plugin upload option under **Add**.
- Complete any connector authorization prompted by the imported package.
- Test using the read-only schedule prompt above.
- Consult [Claude's plugin installation guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) for account or organization restrictions.

## Claude custom connector

- Open [Claude Connectors — Yours](https://claude.ai/new#customize/connectors/yours).
- Choose **Add → Add custom connector**.
- Enter **Akiflow** as the name and `https://mcp.akiflow.com/mcp` as the remote MCP URL.
- Complete Akiflow OAuth through the displayed sign-in flow; do not supply credentials in chat.
- Use this route for the server without workflow guidance, or if plugin upload does not establish the connection; avoid duplicate server connections unnecessarily.
- Follow [Claude's custom connector guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) for account and administrator requirements.

## Build and verify

- Run `python scripts/package.py` from the repository root with Python 3.
- Inspect both ZIPs in `dist/`; each contains only its platform manifest, MCP declaration and shared skill, with no credentials or developer files.
- Read [OpenAI's package guide](https://developers.openai.com/plugins/build/plugins) and [archive validation requirements](https://developers.openai.com/plugins/deploy/submission-errors) for supported manifests and ZIP paths.
- Follow the [vendor publication handoff](MARKETPLACE_HANDOFF.md) for official submissions; Akiflow must verify identity and server ownership and provide legal and review materials.
