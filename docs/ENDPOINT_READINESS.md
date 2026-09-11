# Endpoint readiness evidence

## Live checks on September 10, 2026

- Confirmed that `OPTIONS https://mcp.akiflow.com/mcp` returns `200 OK` and accepts `GET`, `HEAD`, and `POST`.
- Confirmed that an unauthenticated MCP `initialize` request returns `401 Unauthorized` with `WWW-Authenticate: Bearer` and a protected-resource metadata URL.
- Confirmed that `https://mcp.akiflow.com/.well-known/oauth-protected-resource/mcp` returns the MCP resource `https://mcp.akiflow.com/mcp` and points to `https://web.akiflow.com` as its authorization server.
- Confirmed that the protected-resource metadata declares `mcp:read` and `mcp:write` scopes.
- Confirmed that `https://web.akiflow.com/.well-known/oauth-authorization-server` publishes authorization, token, dynamic registration, JWKS, authorization-code, refresh-token, and PKCE metadata.

## Readiness assessment

- Treat the production endpoint, HTTPS transport, OAuth discovery, and public documentation as ready to enter both review portals.
- Confirm every discovered tool has a human-readable title and correct read-only or destructive annotation before submitting.
- Confirm the OAuth authorization server preserves the MCP `resource` parameter through the authorization flow because OpenAI's review requirements call for it.
- Provide a reviewer account and a low-risk test workspace because the server exposes user-specific schedule and calendar data.
- Avoid building a local token-based proxy or a replacement server. Akiflow's official endpoint already has the architecture the directories expect.

## Public source

- [Akiflow MCP guide](https://product.akiflow.com/en/help/articles/4302815-akiflow-mcp) documents the production URL, OAuth sign-in, and supported task, calendar, time-slot, and transcript workflows.

