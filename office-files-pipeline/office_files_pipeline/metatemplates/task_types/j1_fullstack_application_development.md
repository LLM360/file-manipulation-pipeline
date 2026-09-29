# Full-Stack Application Development

**Macro Category:** J — Software & Technical Implementation
**Pattern ID:** J1

## 1. Pattern Description

The worker is a software developer tasked with implementing a complete, production-ready application from a detailed specification provided in the prompt. The deliverable is a multi-file codebase delivered as a ZIP archive covering all tiers: frontend UI, backend logic or smart contracts, infrastructure configuration, and documentation. What makes this pattern distinct is the scope — the worker must produce a coherent, coordinated, multi-layer system in a single pass, not just a snippet or module. The cognitive core is holding the full system architecture in mind while implementing each component in isolation, then ensuring they integrate correctly. Specifications are fully provided in the prompt; no reference files or web research are required.

## 2. O*NET Grounding

### Occupation Families
- **15-1252 Software Developers** — the primary occupation; full-stack developers who implement complete systems end-to-end
- **15-1299 Computer and Information Research Scientists (Cloud Computing Specialists)** — serverless and cloud-native infrastructure implementations
- **15-1221 Computer and Information Research Scientists** — specialized blockchain/cryptography implementations requiring research-level domain knowledge

### Key Work Activities (O*NET vocabulary)
- Programming and developing software applications and systems
- Analyzing system requirements and specifications
- Designing software systems or technical architectures
- Testing and debugging software components
- Documenting technical systems and implementation details
- Developing software or applications for internet use

### Knowledge Domains (O*NET vocabulary)
- Computers and Electronics — programming languages, frameworks, cloud platforms, blockchain protocols
- Engineering and Technology — system design, infrastructure as code, distributed systems
- Mathematics — cryptography, protocol mathematics (ZK proofs), algorithmic complexity

### Generalizable Work Context
A development team or individual contractor is building a new feature, product, or service and needs the complete implementation produced from a specification. The trigger is a fully specified product requirement (not exploratory or ambiguous). The worker operates independently — no pairing or review cycle is implied — and delivers a complete artifact that a team could theoretically deploy or integrate. Industries span DeFi/cryptocurrency, cloud services, enterprise SaaS, and any domain requiring a self-contained web application.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a software developer or engineer with a specialization relevant to the stack (full-stack blockchain developer, serverless backend engineer, cloud infrastructure engineer). Specify the organizational context: a startup, an established development team, or a contractor. Optionally name the project or product to give context for naming conventions and tone.

### Scenario Pattern
Describe the system or product being built at a high level before listing requirements. Specify: what the system does, who uses it, and what the key technical constraints are (privacy requirements, compliance requirements, performance targets). State any scope exclusions explicitly (e.g., "domain registration and DNS configuration assumed to be pre-existing"). Include the purpose of the README in the deliverable.

### Instruction Pattern
Organize requirements into numbered sections by architectural tier: (1) frontend, (2) backend/smart contracts/infrastructure, (3) documentation. Within each section, provide a bulleted list of specific requirements. End with a ZIP file packaging instruction that explicitly lists all filenames the archive must contain.

### Constraint Injection Points
- **Tech stack specificity:** runtime version (e.g., pinning a specific Node.js version rather than an older one), framework version (React vs. Vue), library choices (e.g., pinning a specific AWS SDK major version rather than an older one)
- **File structure:** exact filenames required in the ZIP archive
- **Parameterization:** real credentials/domains must be placeholders, not hardcoded
- **Scope exclusions:** what the implementation does NOT need to include (pre-existing infrastructure, electrical design, etc.)
- **Security/compliance requirements:** WCAG compliance, ZK privacy guarantees, CAPTCHA validation, IAM least-privilege
- **API/protocol versions:** OpenAPI 3.0, Terraform HCL syntax, Solidity version
- **Functional specifics:** fixed input field lists, HTTP response code sets, deposit size constraints

### Structural Template

```
[PERSONA]: You are a [SPECIALIZATION: Full-Stack Blockchain Developer / AWS Serverless Backend Engineer] working on [PROJECT_NAME] at [ORG_TYPE: a DeFi startup / a web development agency].

[SYSTEM_DESCRIPTION]: [HIGH_LEVEL_DESCRIPTION of what the system does, who uses it, and why it matters].

[SCOPE_ASSUMPTIONS]:
- [ASSUMPTION_1: existing infrastructure that is out of scope]
- [ASSUMPTION_2: external services assumed to be configured]

[DELIVERABLES]:

1. [TIER_1: Frontend / Infrastructure Configuration]
   - [FRAMEWORK]: [React/TypeScript / Terraform HCL]
   - Required components/resources:
     - [COMPONENT_1]
     - [COMPONENT_2]
   - [SPECIFIC_REQUIREMENTS]

2. [TIER_2: Backend / Smart Contracts / Lambda Function]
   - [RUNTIME]: [Solidity / Node.js with a pinned AWS SDK major version]
   - Required functionality:
     - [FUNCTION_1]
     - [FUNCTION_2]
   - Input fields: [FIELD_LIST]
   - Response codes: [CODE_LIST]

3. [TIER_3: Documentation (README.md)]
   - Setup and [DEPLOYMENT/CONFIGURATION] instructions
   - [ADDITIONAL_DOCS if any]

[CONSTRAINTS]:
- [PARAMETERIZATION: All real domains/keys/emails must be placeholders]
- [VERSION_CONSTRAINT: Use [SPECIFIC_VERSION]]
- [SECURITY_REQUIREMENT]

[OUTPUT_SPECIFICATION]: ZIP file containing: [FILENAME_1], [FILENAME_2], [FILENAME_3], [FILENAME_4], README.md
```

## 4. Reference File Requirements

### File Types Needed
- **None (primary modality):** This pattern typically requires no reference files — all specifications are provided in the prompt text.
- **Optional: Reference URL(s):** May include one or two URLs to external documentation (e.g., an infrastructure-as-code tool's tutorial, WCAG technique page) for the worker to consult, but these are not required inputs.

### Data Characteristics
No reference data files required. The prompt must be highly detailed — it effectively serves as the specification document. For variant generation, prompts should include: complete input field lists, exact HTTP response code sets, named AWS services, technology version requirements, and an explicit list of ZIP file contents.

### File Complexity Spectrum
- **Minimal:** Single-tier implementation — a Lambda function with one input/output and a README. No frontend, no IaC.
- **Moderate:** Two-tier implementation — backend + README. E.g., a serverless API backend with Terraform infrastructure and a Node.js Lambda function.
- **Complex:** Three-tier full-stack implementation — frontend + smart contracts/backend + infrastructure + optional relay service + README. Multiple protocol integrations, ZK cryptography, cross-chain architecture.

## 5. Output Specification

### Primary Deliverable
- **Format:** ZIP file
- **Structure:** Multiple coordinated source files — frontend code, backend/contract code, configuration files, README
- **Key quality signals:** All specified files present in the archive, parameterization (no hardcoded credentials), correct runtime/framework versions, all required functional behaviors implemented, README provides sufficient setup instructions for a developer to deploy independently

### Secondary Deliverables (if any)
- None standard

### Gold Output Characteristics
A gold output is a complete, deployable codebase that requires only substitution of real values for parameterized placeholders. The frontend correctly integrates with the backend. Smart contracts or Lambda functions implement all specified behaviors with correct error handling (returning the right HTTP status codes, handling edge cases). Infrastructure-as-code files are complete and valid (no syntax errors, no missing resource declarations). The README covers all deployment steps in order. No dead code, no stub implementations — every specified feature is actually implemented.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of application tiers | 1 (backend only) | 2 (frontend + backend) | 3+ (frontend + contracts + IaC + optional relay) |
| External protocol integrations | 0 (pure AWS SDK) | 1–2 (e.g., a CAPTCHA-verification service and a transactional-email service) | 3+ (e.g., a lending protocol, a cross-chain bridge, a proof system, and a wallet connector) |
| Number of files in ZIP | 2–3 | 4–5 | 6+ |
| Cryptography/security requirements | Standard auth (API keys) | CAPTCHA token validation | ZK-SNARKs, nullifier commitment schemes |
| Infrastructure-as-code | None | Single Terraform file | Multi-file Terraform with variables, outputs, data sources |
| Domain specificity | Generic web (e.g., a basic form-handling site) | Fintech (e.g., payments, transactional email) | DeFi/Web3 (e.g., Solidity smart contracts, a lending-protocol integration, cross-chain transfers) |
| Parameterization complexity | 2–3 placeholders | 5–8 variables in variables.tf | 10+ configuration parameters with environment-specific settings |

## 7. Boundary Cases & Adjacent Patterns

**J2 (Component/Utility Development with Tests):** J2 is about a single focused component with a test suite — not a full application. If the deliverable is a self-contained component that plugs into a larger system (a React component, a utility function, an npm package), use J2. If the deliverable is the full application itself (frontend + backend + infrastructure), use J1.

**J3 (API Specification & Technical Architecture Design):** J3 designs the API spec (YAML) and describes the architecture without implementing it. J1 implements the code. If the output is a working codebase, use J1. If the output is a specification document describing how the system should be built, use J3.

**D1 (Technical Design & Architecture Documents):** D1 produces architecture documents and design proposals — written deliverables, not code. J1 produces executable code artifacts. The test is simple: does the output include runnable code or only prose/diagrams? If code, use J1.
