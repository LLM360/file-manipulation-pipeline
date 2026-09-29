# API Specification & Technical Architecture Design

**Macro Category:** J — Software & Technical Implementation
**Pattern ID:** J3

## 1. Pattern Description

The worker is a software developer or systems architect tasked with designing an API specification and/or technical architecture document for a complex system — without implementing the code itself. The primary deliverable is a machine-readable API specification (OpenAPI YAML, GraphQL schema, or similar) combined with human-readable architecture documentation describing how the system works and how components interact. The cognitive core is translating complex domain requirements (variable device sensor configurations, resumable uploads, priority tiering) into a formal, internally consistent API contract that correctly models the domain. This pattern is distinct from J1 (which implements code) and D1 (which writes prose architecture documents) because it requires both formal specification authoring AND domain modeling — the YAML must be technically valid AND conceptually correct.

## 2. O*NET Grounding

### Occupation Families
- **15-1252 Software Developers** — primary occupation; developers who own API contracts as part of system design work
- **15-1211 Computer Systems Analysts** — analysts who translate business requirements into technical system designs
- **15-1243 Database Architects** — when the specification must model data storage architecture (NoSQL schema design, object storage organization)
- **17-2051 Transportation Engineers** — domain-specific variant when the API serves transportation or logistics automation systems

### Key Work Activities (O*NET vocabulary)
- Analyzing system requirements to design technical specifications
- Documenting information using formal specification formats
- Developing software architecture and technical standards
- Evaluating design options against constraints (storage architecture, connection reliability)
- Programming-adjacent work: writing structured YAML/schema definitions

### Knowledge Domains (O*NET vocabulary)
- Computers and Electronics — API design, OpenAPI specification, RESTful architecture, cloud storage patterns
- Engineering and Technology — systems engineering, distributed systems, IoT data pipelines
- Mathematics — data modeling, schema validation, algorithmic upload sequencing

### Generalizable Work Context
An engineering team is beginning development on a new API surface or data integration layer. The trigger is a system design phase where the API contract must be established before implementation begins — multiple teams (mobile, backend, data pipeline) need a shared specification. The worker receives a detailed requirements brief describing the domain model, constraints, and use cases. Output is consumed directly by implementation teams or used to generate code stubs. No reference files required; all requirements are specified in the prompt.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a software developer, API designer, or solutions architect at a company building a specific type of system (device fleet management, IoT platform, logistics network). Specify the team context (large engineering org with multiple consumer teams, or a solo architect at a startup). The domain should be specific enough to ground the data model without being generic.

### Scenario Pattern
Open with the business context (scale of operations, type of data being managed, key operational constraints). Define the domain model entities explicitly (jobs, devices, sensors, data categories) before listing API requirements. State the architectural constraints upfront (specific storage services, authentication approach, connection reliability assumptions). Describe the consumer of the API (devices uploading, internal processing pipeline, external analytics teams).

### Instruction Pattern
Organize requirements into numbered sections: (1) domain model / data definitions, (2) specific API functional requirements (endpoints, upload patterns, priority tiers), (3) architectural constraints (storage, connection handling), (4) assumptions. End with the dual-output specification: the formal YAML spec and the prose data flow description. List both output files with their exact filenames.

### Constraint Injection Points
- **Specification format:** OpenAPI 3.0+ (YAML), GraphQL schema, JSON Schema, AsyncAPI
- **Storage architecture:** a managed NoSQL store + object storage combination, PostgreSQL + GCS, specific AWS/GCP/Azure services
- **Domain model variability:** fixed schema vs. variable sensor configurations per device type
- **Upload pattern complexity:** simple single-file upload vs. resumable multipart chunked upload
- **Priority tiering:** flat vs. two-tier (high-priority vs. low-priority data) vs. multi-tier
- **Connection reliability constraints:** assume reliable vs. assume intermittent (resume on reconnect)
- **Dual output:** YAML spec only vs. YAML + prose description vs. YAML + diagram description

### Structural Template

```
[PERSONA]: You are a [ROLE: Software Developer / API Designer / Solutions Architect] at [COMPANY_TYPE: a [INDUSTRY] company] managing [SYSTEM_SCALE: a fleet of N machines / a network of N devices / a platform serving N customers].

[SYSTEM_CONTEXT]:
Your team is building a [SYSTEM_NAME] API that allows [ACTORS] to [PRIMARY_ACTION]. The system currently handles [SCALE_DESCRIPTION].

[DOMAIN_MODEL]:
- [ENTITY_1]: [DESCRIPTION] — key attributes: [ATTRIBUTES]
- [ENTITY_2]: [DESCRIPTION] — key attributes: [ATTRIBUTES]
- [DATA_CATEGORY_A]: [DESCRIPTION] — priority: [HIGH/LOW], characteristics: [DESCRIPTION]
- [DATA_CATEGORY_B]: [DESCRIPTION] — priority: [HIGH/LOW], characteristics: [DESCRIPTION]

[OPERATIONAL_CONTEXT]: [WHEN_UPLOADS_HAPPEN, CONNECTION_CONDITIONS, TIMING_REQUIREMENTS]

[POST_UPLOAD_PIPELINE]: [WHAT_HAPPENS_AFTER_UPLOAD — processing stages, consumers]

[EXAMPLE_DATA_SET]: [EXAMPLE: A device with sensors A, B, C might upload the following files after a job...]

[KEY_CONSTRAINTS]:
- [CONSTRAINT_1: storage architecture — a NoSQL store for metadata, object storage for files]
- [CONSTRAINT_2: priority requirement — high-priority data must be prioritized over low-priority data]
- [CONSTRAINT_3: resumable uploads — must survive connection interruption]
- [CONSTRAINT_4: variable schema — different device types have different sensor configurations]

[KEY_ASSUMPTIONS]:
- [ASSUMPTION_1: devices authenticate via existing mechanism]
- [ASSUMPTION_2: partial job completion supported]

[DELIVERABLES]:
1. [OUTPUT_FILENAME_1].yaml — OpenAPI 3.0+ specification covering the complete [SYSTEM_NAME] API
2. [OUTPUT_FILENAME_2].txt — prose description of the expected data flow and how [ACTORS] use the API endpoints
```

## 4. Reference File Requirements

### File Types Needed
- **None (primary modality):** This pattern typically requires no reference files. All system requirements, domain model definitions, and architectural constraints are provided in the prompt.
- **Optional: Existing API spec for extension (yaml):** A variant could provide an existing partial OpenAPI spec that the worker must extend with new endpoints or resource types.
- **Optional: Data model document (pdf/docx):** A variant could provide a data model description as a reference file, requiring the worker to translate it into OpenAPI schema definitions.

### Data Characteristics
No reference data files required. The prompt serves as the requirements document. For variant generation, prompts should include: explicit entity definitions with attribute lists, example payloads (optional), constraint enumeration, storage architecture decisions, and the exact filenames for output files.

### File Complexity Spectrum
- **Minimal:** Single-resource API with CRUD endpoints. Fixed data schema, no upload patterns, no priority tiering. OpenAPI YAML with 3–5 paths.
- **Moderate:** Multi-resource API with relationships between entities. Single upload endpoint with file size constraints. Two resource types with different schemas. OpenAPI YAML with 8–12 paths + a prose data-flow file.
- **Complex:** Domain model with 4+ entity types, variable schemas per entity type, resumable multipart uploads, priority tiering, multi-stage post-upload pipeline, and support for partial/incomplete operations. OpenAPI YAML with 15+ paths and rich schema definitions + prose data flow description.

## 5. Output Specification

### Primary Deliverable
- **Format:** YAML (OpenAPI 3.0+)
- **Structure:** Complete OpenAPI specification with info section, servers, paths (all endpoints), components/schemas (all data models), and security schemes
- **Key quality signals:** Valid OpenAPI 3.0+ syntax, all domain entities modeled as schemas with correct data types, all specified endpoints present with correct HTTP methods and request/response bodies, resumable upload pattern correctly modeled (initiation + chunk upload + completion endpoints if required), priority tiering reflected in schema or endpoint design

### Secondary Deliverables (if any)
- **Data flow description (txt/md):** Prose narrative describing how the primary actors (devices, backend pipeline, analytics teams) interact with the API over the lifecycle of a typical operation. Should reference specific endpoint names from the YAML spec.

### Gold Output Characteristics
A gold output produces an OpenAPI YAML file that could be pasted into Swagger UI and rendered without errors. All domain entities from the requirements are present as named schemas in `components/schemas`. The resumable upload pattern uses the correct multi-step endpoint pattern (initiate → upload chunks → complete). Variable sensor configurations are correctly modeled (either with oneOf/discriminator or with a flexible additional properties pattern). Priority data categories are reflected in request/response structures. The secondary data-flow description file reads as a coherent operational narrative that someone could use to understand the system without reading the YAML — it names specific endpoints and explains the sequencing logic.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of API resource types | 2–3 | 4–6 | 7+ (e.g., jobs, devices, sensors, files, chunks, metadata, pipeline stages) |
| Schema variability | Fixed schema for all entities | Two resource types with different schemas | Variable schemas per entity instance type (different sensors per device type) |
| Upload pattern | Simple single-file POST | Multipart form upload | Resumable chunked upload with initiation, chunk, and completion endpoints |
| Priority tiering | None (flat) | Two tiers (high/low) | Two tiers with different upload endpoints, retry logic, and backpressure |
| Connection reliability modeling | Assume reliable | Idempotency keys for retry | Full resumable upload with session state, partial completion, recovery |
| Output files | YAML only | YAML + txt description | YAML + txt + sequence diagram description |
| Secondary consumers | Single consumer | Two consumers (uploader + pipeline) | Three consumers (devices + pipeline + analytics) with different access patterns |

## 7. Boundary Cases & Adjacent Patterns

**J1 (Full-Stack Application Development):** J1 implements the code that calls the API (and the API handlers themselves). J3 designs the API contract. If the deliverable includes runnable server or client code, use J1. If the deliverable is the YAML specification and documentation but not the implementation, use J3.

**D1 (Technical Design & Architecture Documents):** D1 produces prose architecture documents (Word/PDF) that describe system design in natural language. J3 produces a formal machine-readable specification (YAML) alongside prose. If the API spec is a formal YAML file that could be used to generate code stubs or power Swagger UI, use J3. If the output is entirely prose-based design documentation, use D1.

**J2 (Component/Utility Development with Tests):** J2 builds a software component. J3 designs a specification. These patterns do not overlap — if there is code to execute, it is J2. If the output is a schema or contract document (even a highly technical one), it is J3.
