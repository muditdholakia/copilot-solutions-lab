# copilot-solutions-lab

Original Copilot Studio and Microsoft 365 agent specifications with responsible-AI evaluation fixtures.

## Architecture

User → Copilot Studio/Microsoft 365 agent → approved synthetic knowledge → optional authenticated API action → explicit confirmation for mutations. These are design recipes, not exported deployable agent packages.

## Prerequisites

Copilot Studio development environment or Microsoft 365 Agents Toolkit; appropriate tenant licenses, maker permissions, and a synthetic SharePoint development site for grounded testing.

## Setup

1. Read `examples/agent-spec.md` and upload `examples/knowledge.md` to a development agent.
2. Configure only approved knowledge sources. For Microsoft 365, ground the agent in a synthetic SharePoint site with permission trimming.
3. Create an agent in Copilot Studio or Agents Toolkit using the specification; configure authentication before exposing it.
4. Run `python examples/check_fixtures.py` to validate evaluation fixtures, then manually run their prompts against the agent.
5. Record responses and pass/fail results in an untracked local report. Do not publish real user conversations.

## Sample workflow

Author agent → attach synthetic knowledge → test grounding, prompt injection, access boundaries, and mutation confirmation → review results → publish manually to a development audience.

## Security

Read [SECURITY.md](SECURITY.md). Environment examples contain placeholders only.
Never commit local environment values or production exports. No deployment is automated.

## Troubleshooting

Missing grounded responses: verify indexing and source permissions. Connector consent errors: review requested scopes with the tenant administrator. Passing fixture validation only checks fixture structure; it does not establish agent safety.

## License and attribution

Original implementations and documentation by Mudit Dholakia, licensed under MIT.
No upstream code was imported. These references informed the learning scope:
- https://github.com/microsoft/CopilotStudioSamples
- https://github.com/pnp/copilot-pro-dev-samples
Platform services, SDK distributions, and third-party content retain their own terms.

## Updating

This is an original repository and has no upstream remote. Run `git pull --ff-only origin main`.
Review Dependabot changes and current platform documentation before upgrading.

## Validation limits

Python syntax and local smoke tests are checked before publication. Cloud execution,
tenant integrations, Tableau workbook authoring, and live agent evaluation require
your development environments and have not been verified by local checks.

## Toolkit and agent learning catalog

See [Toolkit and agent learning catalog](TOOLKIT-CATALOG.md) for the curated forks, supported SDK references, starting exercises, and compatibility guidance.
