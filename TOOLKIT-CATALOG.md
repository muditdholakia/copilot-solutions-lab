# Mudit Dholakia — copilot toolkit and agent learning catalog

All forks preserve upstream attribution. The original portfolio implementations remain separate. No toolkit code was copied into this portfolio repository.

| Repository | Purpose / first exercise | License | Collection action |
| --- | --- | --- | --- |
| [microsoft/m365-agent-templates](https://github.com/muditdholakia/m365-agent-templates) | My Company Policy or Plan My Day | MIT | Curated fork |
| [microsoft/agent-academy](https://github.com/muditdholakia/agent-academy) | Recruit beginner course | MIT | Curated fork |
| [microsoft/mcs-labs](https://github.com/muditdholakia/mcs-labs) | Introductory Copilot Studio lab | MIT | Curated fork |
| [microsoft/copilot-camp](https://github.com/muditdholakia/copilot-camp) | Agent Builder on-ramp | MIT | Curated fork |
| [microsoft/ai-agents-for-beginners](https://github.com/muditdholakia/ai-agents-for-beginners) | Course setup, then introductory agent lesson | MIT | Curated fork |
| [microsoft/Agents](https://github.com/muditdholakia/Agents) | Language-specific QuickStart | MIT | Curated fork |
| [microsoft/skills-for-copilot-studio](https://github.com/muditdholakia/skills-for-copilot-studio) | Validate a basic agent YAML definition | MIT | Curated fork |
| [microsoft/agent-framework](https://github.com/muditdholakia/agent-framework) | python/samples/01-get-started | MIT | Curated fork |
| [microsoft/Power-CAT-Copilot-Studio-Kit](https://github.com/muditdholakia/Power-CAT-Copilot-Studio-Kit) | Evaluation, inventory, components, and deployment patterns; some features are preview | MIT | Curated fork |
| [OfficeDev/microsoft-365-agents-toolkit](https://github.com/OfficeDev/microsoft-365-agents-toolkit) | VS Code and CLI scaffolding; MIT verified in LICENSE despite NOASSERTION metadata | MIT (license text verified) | Reference only / install official tooling |

## Language SDKs — references

- [microsoft/Agents-for-net](https://github.com/microsoft/Agents-for-net): MIT; install the official SDK rather than mirroring implementation source.
- [microsoft/Agents-for-js](https://github.com/microsoft/Agents-for-js): MIT; install the official SDK rather than mirroring implementation source.
- [microsoft/Agents-for-python](https://github.com/microsoft/Agents-for-python): MIT; install the official SDK rather than mirroring implementation source.

## Current compatibility and security

- Use supported Microsoft 365 Agents SDK / Agent Framework examples; older TeamsFx paths need migration.
- Fabric data agent query examples should use current Responses/MCP guidance; the older external Assistants-based client is not a recommended starting point.
- Fabric data agent SDK and some Power CAT components are preview-dependent; verify versions and prerequisites.
- The Fabric Tools Workload repository has restrictive pre-release licensing and is not publicly mirrored.
- Fork workflows are disabled. Dependency/secret scans are point-in-time checks; remediate selected examples before execution.
- Do not commit production identifiers, secrets, user conversations, or customer data. Use synthetic inputs and development identities.

## Learning evidence

For each selected example, record architecture, SDK versions, setup, a successful prompt, negative grounding/permission tests, and one operational failure. Implement an original variation here and preserve attribution for adaptations. Do not present upstream agents as original authorship.

References: [Fabric data agent SDK](https://learn.microsoft.com/en-us/fabric/data-science/fabric-data-agent-sdk), [Microsoft agent samples](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-samples).

## Dependency audit snapshot — 2026-09-15

Counts span the entire repository, including unrelated examples. Select a documented starting exercise and review its own manifests before installing anything. Critical/high alerts require remediation. Fork Actions remain disabled; cloud execution was not tested. Zero alerts is not certification.

| Curated source | Open dependency alerts | Critical | High |
| --- | ---: | ---: | ---: |
| [CopilotStudioSamples](https://github.com/muditdholakia/CopilotStudioSamples) | 40 | 3 | 15 |
| [copilot-pro-dev-samples](https://github.com/muditdholakia/copilot-pro-dev-samples) | 920 | 24 | 461 |
| [m365-agent-templates](https://github.com/muditdholakia/m365-agent-templates) | 0 | 0 | 0 |
| [agent-academy](https://github.com/muditdholakia/agent-academy) | 6 | 0 | 3 |
| [mcs-labs](https://github.com/muditdholakia/mcs-labs) | 22 | 0 | 11 |
| [copilot-camp](https://github.com/muditdholakia/copilot-camp) | 306 | 30 | 110 |
| [ai-agents-for-beginners](https://github.com/muditdholakia/ai-agents-for-beginners) | 0 | 0 | 0 |
| [Agents](https://github.com/muditdholakia/Agents) | 63 | 0 | 23 |
| [skills-for-copilot-studio](https://github.com/muditdholakia/skills-for-copilot-studio) | 0 | 0 | 0 |
| [agent-framework](https://github.com/muditdholakia/agent-framework) | 0 | 0 | 0 |
| [Power-CAT-Copilot-Studio-Kit](https://github.com/muditdholakia/Power-CAT-Copilot-Studio-Kit) | 14 | 0 | 3 |
