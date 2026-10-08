# Akiflow directory publication handoff

## Recommendation

- Publish the existing `https://mcp.akiflow.com/mcp` endpoint as a remote MCP connector in the Claude Connectors Directory.
- Submit the same endpoint as an MCP-backed plugin through the OpenAI plugin portal for the shared ChatGPT and Codex directory.
- Publish the included Claude plugin as a complementary workflow package for Claude web chat, Desktop, Claude Code and Cowork.
- Keep one MCP server and one set of tool schemas. Do not fork server logic by provider.

## Current position

- Akiflow already documents an official MCP server for Claude, ChatGPT, Cursor, Windsurf, and other MCP clients.
- Akiflow already uses an OAuth-protected, stable HTTPS endpoint.
- Distinguish manual installation from an approved directory listing; the screenshots alone do not establish Akiflow's directory status or explain it.
- A GitHub repository helps with public source, versioned skills, tests, and Claude plugin publication. It does not replace either vendor's connector-review submission.

## OpenAI: ChatGPT and Codex

- Use the [OpenAI plugin submission portal](https://platform.openai.com/apps) from an Akiflow-owned Platform organization.
- Grant the submitter Apps Management write access before creating the draft.
- Complete individual or business verification under the Akiflow publisher identity.
- Create a **With MCP** submission using the universal production URL `https://mcp.akiflow.com/mcp`.
- Let the portal scan the live tools and correct the server if any schema, description, or annotation is rejected.
- Supply the listing copy, support, privacy, terms, country availability, and reviewer demo account from `LISTING_MATERIALS.md`.
- Supply five positive and three negative test cases. The portal explicitly requires them for review.
- Publish only after approval. OpenAI's public directory is shared by ChatGPT and Codex, so this creates the discovery entry visible in the first screenshot.

## Claude: connector directory

- Use the [Claude connector submission portal](https://claude.ai/admin-settings/directory/submissions/new) from Akiflow's Team or Enterprise organization.
- Verify that every MCP tool exposes a title and an accurate `readOnlyHint` or `destructiveHint` before the portal syncs its tools.
- Select the remote endpoint, confirm streamable HTTP, and use Akiflow's OAuth configuration.
- Supply the public documentation URL, privacy policy, icon, data-handling disclosure, and reviewer test credentials.
- Submit the remote server for review. After approval, the connector becomes discoverable across Claude.ai, Desktop, Mobile, Claude Code, and Cowork.
- Avoid an MCP Bundle unless Akiflow later builds a local desktop-only integration. It does not improve the remote server's directory path.

## Claude: complementary plugin

- Publish this public repository through the [Claude plugin submission flow](https://platform.claude.com/plugins/submit) after reviewing final branding and legal files.
- Run `claude plugin validate` in the repository before submission.
- Keep `.claude-plugin/plugin.json`, `.mcp.json`, and `skills/` at the plugin root exactly as structured here.
- Treat this as supplementary to the connector listing; the plugin adds reusable workflow guidance across Claude clients. See the [current plugin installation guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

## What Akiflow alone must do

- Submit under an Akiflow-owned OpenAI organization with verified business identity and Apps Management permission.
- Submit under an Akiflow-owned Claude Team or Enterprise organization with Directory management access.
- Grant reviewers a safe test account with resettable data.
- Confirm tool annotations, OAuth behavior, data handling, and policy attestations from the live server.
- Approve final branding, legal copy, launch countries, support ownership, and future server maintenance.

## What this repository can do now

- Give Claude Code and Cowork users one installable package for the existing remote MCP endpoint and workflow guidance.
- Give ChatGPT and Codex a portable Agent Plugins package for local testing and distribution.
- Give the Akiflow team complete listing copy, review evidence, test cases, and direct submission links.
- Keep the implementation provider-neutral because the same OAuth-protected Streamable HTTP endpoint serves both directories.

## Official references

- [OpenAI plugin architecture](https://developers.openai.com/plugins/concepts/plugins).
- [OpenAI MCP server requirements](https://developers.openai.com/plugins/concepts/mcp-server).
- [OpenAI authentication requirements](https://developers.openai.com/plugins/build/auth).
- [OpenAI plugin submission guide](https://developers.openai.com/plugins/deploy/submission).
- [OpenAI remote MCP review requirements](https://developers.openai.com/plugins/deploy/app-review).
- [Claude Connectors Directory](https://claude.com/docs/connectors/directory).
- [Claude connector submission requirements](https://claude.com/docs/connectors/building/submission).
- [Claude plugin submission guide](https://claude.com/docs/plugins/submit).
- [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference).
- [Agent Plugins MCP configuration](https://agent-plugins.org/plugin-authors/mcp-servers).

