# Component & Utility Development with Tests

**Macro Category:** J — Software & Technical Implementation
**Pattern ID:** J2

## 1. Pattern Description

The worker is a software developer tasked with implementing a single, focused software component or utility — not a full application — along with a coordinated test suite, supporting CSS or configuration files, and developer documentation. The component solves a specific, bounded technical problem (accessibility compliance, state management, a utility hook) and must integrate cleanly into an existing larger system. What distinguishes this pattern from J1 (full-stack application) is scope: the deliverable is a reusable building block, not an end-to-end product. The cognitive core is correctness at the interface boundary — the component must implement the exact behavior required by a specification (WCAG technique, business rule, API contract) while remaining modular and testable.

## 2. O*NET Grounding

### Occupation Families
- **15-1252 Software Developers** — primary occupation; component developers who implement reusable modules within larger codebases
- **15-1254 Web Developers** — frontend specialists implementing UI components with WCAG compliance, ARIA attributes, and CSS
- **15-1211 Computer Systems Analysts** — developers who analyze requirements (WCAG criteria, API contracts) and translate them into implementation decisions

### Key Work Activities (O*NET vocabulary)
- Programming and developing software components and utilities
- Analyzing technical specifications (WCAG, API contracts, accessibility standards)
- Developing automated test cases and test suites
- Documenting software usage and configuration
- Evaluating information to determine compliance with technical standards

### Knowledge Domains (O*NET vocabulary)
- Computers and Electronics — React/TypeScript, testing frameworks, CSS, DOM/accessibility tree
- English Language — documentation writing, README authoring, code commenting
- Engineering and Technology — accessibility standards (WCAG), ARIA specification, browser rendering behavior

### Generalizable Work Context
A software engineering team maintaining a large enterprise application needs a new reusable component or utility that meets a specific technical standard. The trigger is typically a compliance gap (accessibility audit, security review) or a recurring need that warrants a standardized solution. The worker receives a detailed specification from a technical lead, product owner, or standards document. The component will be reviewed by the team before integration, so test cases are essential for verifying correctness. No reference files are required; the specification is embedded in the prompt with links to standards documentation.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a frontend developer, accessibility engineer, or specialist developer on an existing team. Specify the team context (enterprise React/TypeScript application, component library, internal tooling). The persona does not need to be senior — what matters is the specialization area relevant to the component being built.

### Scenario Pattern
Describe the application context briefly (what the larger application does, who uses it) and then identify the specific gap or need the component addresses. Reference the relevant standard or specification (WCAG criterion, RFC, business rule document). Explain why this component is being built now (compliance audit, recurring bug, feature request). Provide URLs to the relevant specification documents where applicable.

### Instruction Pattern
Specify the component's interface first (props, behaviors, edge cases), then the test requirements (exact number of test cases, test framework, what each test verifies), then the file structure of the ZIP archive with exact filenames. Use a numbered or bulleted list for each category of requirements. Be precise about edge cases: what happens when multiple messages arrive simultaneously, how a variant-rendering prop changes the output, etc.

### Constraint Injection Points
- **Exact test case count:** specified precisely (e.g., an exact count of test cases, not "several")
- **Testing framework:** specific library required (React Testing Library + Sinon, not Jest mocks)
- **ARIA/compliance standard:** named criterion (e.g., a specific WCAG success criterion, paired with a named accessibility technique)
- **Rendering behavior:** default vs. variant behavior specified precisely (e.g., hidden by default vs. a variant prop that changes visibility)
- **Message type flexibility:** accepts string vs. JSX element
- **File structure:** exact filenames in ZIP archive
- **Role attribute behavior:** timing requirement (role set before content populated)
- **Queuing behavior:** multiple concurrent messages must not interfere

### Structural Template

```
[PERSONA]: You are a [SPECIALIZATION: Frontend Accessibility Engineer / Senior Frontend Developer] on a [TEAM_CONTEXT: large enterprise React/TypeScript application / open-source component library].

[APPLICATION_CONTEXT]: [BRIEF_APP_DESCRIPTION]. [COMPLIANCE_CONTEXT: Your team recently conducted an accessibility audit and identified a gap in [SPECIFIC_AREA]].

[REQUIREMENT]: Build a reusable [COMPONENT_NAME] component that [CORE_BEHAVIOR]. It must comply with [STANDARD: WCAG SC X.X.X / RFC XXXX / Business Rule Y].

[COMPONENT_SPECIFICATION]:
- Default behavior: [DEFAULT_RENDERING_DESCRIPTION]
- Variant behavior: [PROP_NAME] prop causes [VARIANT_BEHAVIOR]
- Accepts: [STRING / JSX / custom type]
- [EDGE_CASE_1: queuing / concurrency / timing behavior]
- [EDGE_CASE_2: additional edge case]

[REFERENCE_URLS]:
- [STANDARD_URL_1]
- [STANDARD_URL_2]

[TEST_REQUIREMENTS]:
- Framework: [TESTING_LIBRARY] + [MOCK_LIBRARY]
- Exactly [N] test cases:
  1. [TEST_CASE_1_DESCRIPTION] — verifies [BEHAVIOR]
  2. [TEST_CASE_2_DESCRIPTION] — verifies [BEHAVIOR]
  3. [TEST_CASE_3_DESCRIPTION] — verifies [BEHAVIOR]
  4. [TEST_CASE_4_DESCRIPTION] — verifies [BEHAVIOR]

[OUTPUT_SPECIFICATION]: ZIP file containing:
- [ComponentName].tsx — [DESCRIPTION]
- [ComponentName].test.tsx — [DESCRIPTION]
- [ComponentName].css — [DESCRIPTION]
- package.json — [TEST_SETUP_DESCRIPTION]
- README.md — [USAGE_AND_TEST_INSTRUCTIONS]
```

## 4. Reference File Requirements

### File Types Needed
- **None (primary modality):** This pattern typically requires no reference files. Specifications come from the prompt and linked standard documentation (WCAG, RFC).
- **Optional: Existing component for reference (tsx/js):** A variant could provide an existing component that the new component must integrate with — e.g., a notification container that the new component renders into.
- **Optional: Package.json / existing project config:** A partial package.json showing the project's existing test setup, so the new component's package.json is compatible.

### Data Characteristics
No structured data files required. When reference URLs are provided, they point to standards documentation (W3C, MDN, RFC), not data sources. The prompt itself must contain the complete behavioral specification.

### File Complexity Spectrum
- **Minimal:** Single component file + single test file with 2 test cases. No CSS. No README. Pure TypeScript/JavaScript, no framework-specific complexity.
- **Moderate:** Component (.tsx) + tests (.test.tsx) + CSS file + README. 3–4 test cases covering the main behaviors. One rendering variant (default only).
- **Complex:** Component + tests (4+ cases) + CSS + package.json + README. Multiple rendering modes (default hidden, variant prop that changes visibility). Queuing/concurrency behavior. Specific ARIA timing requirements. Coordinated across 5 files.

## 5. Output Specification

### Primary Deliverable
- **Format:** ZIP file
- **Structure:** 4–5 coordinated files: component implementation, test file, CSS, package.json (test config), README
- **Key quality signals:** Correct ARIA role timing, all specified test cases present and passing, visually hidden CSS pattern correctly implemented (visible to accessibility tree, hidden visually), variant-rendering prop renders correctly with an ARIA-hidden sibling to prevent duplication, all filename conventions followed exactly

### Secondary Deliverables (if any)
- None

### Gold Output Characteristics
A gold output implements the specified component behavior precisely, with no missing edge cases. The test file contains exactly the specified number of test cases, each verifying a distinct behavioral requirement from the specification (not just smoke tests). The CSS correctly uses a visually-hidden pattern (absolute positioning, clip, or equivalent) that hides the element visually while keeping it accessible. The README explains the component's purpose, usage API (props), and how to run the tests. The package.json configures the test runner correctly for the specified frameworks. No console errors in a browser; tests all pass.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of test cases | 2 | 3–4 | 5–6 |
| Number of rendering modes | 1 (default) | 2 (default + variant prop) | 3+ (multiple prop combinations) |
| Compliance standard specificity | Business rule (informal) | WCAG criterion (formal) | WCAG criterion + specific ARIA technique + timing constraints |
| Concurrency/queuing behavior | None | Single message at a time | Multiple concurrent messages from different sources must not interfere |
| Testing framework complexity | Jest + React Testing Library | React Testing Library + Sinon | Custom test utilities + specific query methods required |
| File count in ZIP | 2 (component + tests) | 4 (component + tests + CSS + README) | 5 (+ package.json with specific test config) |
| CSS implementation complexity | None | Simple class | Visually-hidden pattern with multiple fallback properties |

## 7. Boundary Cases & Adjacent Patterns

**J1 (Full-Stack Application Development):** J1 produces a complete application across all tiers. J2 produces a single component or utility. If the deliverable is a complete system that users interact with end-to-end, use J1. If the deliverable is a reusable module that developers integrate into their own application, use J2.

**J3 (API Specification & Technical Architecture Design):** J3 designs how a system should work (specification); J2 implements a specific thing that should work (code). If the output is a YAML spec or design document, use J3. If the output is TypeScript code and tests, use J2.

**D1 (Technical Design & Architecture Documents):** D1 produces architecture documents. J2 produces code. If the task is "design a component architecture" with a document as the output, it belongs in D1. If the task is "implement the component," it belongs in J2.
