# GIS Query & Technical Documentation

**Macro Category:** J — Software & Technical Implementation
**Pattern ID:** J5

## 1. Pattern Description

The worker is a developer or engineer who must write a specialized geospatial or domain-specific query (OverpassQL, PostGIS SQL, SPARQL, or similar) to extract a precisely filtered dataset from a geographic or linked-data source, paired with Markdown-format technical documentation explaining how to use the query and interpret its output. The cognitive core is dual: the query requires syntactic correctness in a non-mainstream query language combined with accurate geographic or domain knowledge (which highway tags, which bounding box, which relation IDs). The documentation requires translating technical query logic into accessible usage instructions for a developer audience. The pattern is distinct from general SQL because it involves specialized geo-querying ecosystems (OpenStreetMap/Overpass, PostGIS) where data model knowledge is as important as query syntax.

## 2. O*NET Grounding

### Occupation Families
- **15-1252 Software Developers** — developers who write geospatial queries as part of data pipeline or routing software development
- **17-1021 Cartographers and Photogrammetrists** — GIS specialists who query and manipulate geographic datasets
- **17-2051 Transportation Engineers** — engineers who extract highway network data for routing, traffic modeling, or autonomous vehicle systems
- **15-1243 Database Architects** — database engineers specializing in geospatial or graph database query design

### Key Work Activities (O*NET vocabulary)
- Programming and writing queries to extract data from specialized databases
- Analyzing geospatial data requirements for specific use cases
- Documenting technical procedures in Markdown format
- Developing data pipelines and extraction procedures
- Applying knowledge of geographic data models (OSM data model, GIS schema)

### Knowledge Domains (O*NET vocabulary)
- Computers and Electronics — query languages (OverpassQL, PostGIS SQL, SPARQL), JSON/XML output formats, GIS software
- Geography — highway network data, geographic bounding boxes, coordinate systems, place names
- Transportation — highway classification systems, lane/speed metadata, routing data requirements

### Generalizable Work Context
A software or engineering team is building a data pipeline that requires extracting a specific subset of geospatial data from a large geographic database (OpenStreetMap, a PostGIS database, a linked data endpoint). The trigger is a new routing algorithm, autonomous system, or spatial analysis requirement that needs data extracted with specific filtering criteria. The worker must know both the query language syntax and the domain-specific tag vocabulary or schema that encodes the needed information. Deliverable is the query itself (usable by the team immediately) plus documentation that allows team members who didn't write the query to reproduce, extend, or troubleshoot it.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a software developer, GIS engineer, or data engineer at a company that operates in a location-dependent or transportation-adjacent domain (logistics company, autonomous vehicle startup, mapping company, environmental monitoring firm). Specify the specific system the query will support (route optimization, asset tracking, spatial analysis pipeline). Include what the downstream consumer of the data will do with it.

### Scenario Pattern
Describe the specific geographic or data scope that needs to be extracted: a named highway or region, a set of feature types, a temporal range. Explain what the data will be used for (speed analysis, lane modeling, hazard detection) because this determines which attributes must be included in the query. State what filtering logic is required (specific highway class, bounding box, relation type) and what the output format should be (JSON, XML, GeoJSON).

### Instruction Pattern
Specify the dual deliverable explicitly: (1) the working query, and (2) the Markdown documentation. For the query: specify the target data source, the filtering criteria, the geographic scope, and the required output attributes. For the documentation: specify the format (Markdown), what it must cover (how to execute the query, what tool to use, how to interpret the output, what the key fields mean). Specify any constraints on the query's scope (must not pull the entire highway network, must be targetable to a specific route segment).

### Constraint Injection Points
- **Query language:** OverpassQL vs. PostGIS SQL vs. SPARQL vs. custom DSL
- **Geographic scope specificity:** named highway + city pair vs. bounding box vs. relation ID
- **Data model knowledge required:** OSM tag vocabulary vs. database schema vs. ontology
- **Output format:** raw Overpass JSON vs. GeoJSON vs. CSV export
- **Metadata fields required:** which tags/columns must be in the output (lane count, speed limit, surface type, access restrictions)
- **Downstream use case:** autonomous routing (strict tag requirements), visualization (format flexibility), machine learning (volume constraints)
- **Documentation depth:** minimal (how to run the query) vs. full (how to run, what tools to use, how to interpret, how to extend)

### Structural Template

```
[PERSONA]: You are a [ROLE: Software Developer / GIS Engineer / Data Engineer] at [COMPANY_TYPE: a [INDUSTRY] company] building [SYSTEM_NAME]. [SYSTEM_CONTEXT: Your team is developing [SPECIFIC_APPLICATION] that requires precise geospatial data about [SUBJECT_MATTER].]

[DATA_REQUIREMENT]: You need to extract [DATA_DESCRIPTION: all [FEATURE_TYPE] within [GEOGRAPHIC_SCOPE] including [SPECIFIC_ATTRIBUTES]] from [DATA_SOURCE: OpenStreetMap via the Overpass API / a PostGIS database / a linked data endpoint]. This data will support [USE_CASE: speed analysis / lane modeling / hazard detection / routing algorithm training].

[QUERY_REQUIREMENTS]:
- Target data source: [SOURCE_NAME]
- Geographic scope: [NAMED_REGION / BOUNDING_BOX / RELATION_REFERENCE]
- Feature types to include: [WAYS / NODES / RELATIONS / SPECIFIC_TAGS]
- Required attributes/tags: [ATTR_1: speed limit tags], [ATTR_2: lane count tags], [ATTR_3: surface type], ...
- Output format: [JSON / XML / GeoJSON]
- Filtering criteria: [SPECIFIC_HIGHWAY_CLASS / RELATION_TYPE / ATTRIBUTE_FILTER]

[DOCUMENTATION_REQUIREMENTS]:
- Format: Markdown
- Must cover:
  1. How to execute the query (tool, endpoint, submission method)
  2. What the output structure contains (key fields and their meaning)
  3. [ADDITIONAL_REQUIREMENT: how to export to GeoJSON / how to filter results further / how to update the bounding box for a different route]

[OUTPUT_SPECIFICATION]:
- [OUTPUT_1]: [LANGUAGE] query targeting [SCOPE] — ready to execute
- [OUTPUT_2]: [FILENAME].md — Markdown documentation covering [EXECUTION + INTERPRETATION + EXTENSION]
```

## 4. Reference File Requirements

### File Types Needed
- **None (primary modality):** This pattern typically requires no reference files. Geographic scope and data model knowledge come from domain expertise. The worker must know which OSM tags encode the relevant attributes without being told.
- **Optional: Schema reference document (pdf/docx):** A variant could provide a database schema document describing which tables/columns contain the relevant geospatial data — eliminating the need for domain knowledge about the schema and shifting the task toward query composition from a spec.
- **Optional: Sample output file (json/csv):** A variant could provide a sample of what the output should look like, so the worker can verify their query produces correctly structured output.

### Data Characteristics
No reference files required. When geographic context is needed for the prompt, specify it inline: highway name and number, city names for endpoints, approximate coordinate bounding box (optional), OSM relation IDs if relevant. The worker must supply the correct OSM tag vocabulary (e.g., `highway=motorway`, `lanes=*`, `maxspeed=*`) from domain knowledge.

### File Complexity Spectrum
- **Minimal:** Single-entity query (extract all nodes of a named highway within a city bounding box), one output format, minimal documentation (3–5 steps).
- **Moderate:** Multi-entity query (ways + their nodes + relation membership for a highway corridor), filtering by highway class and geographic scope, documentation including output format explanation and a usage example.
- **Complex:** Full relational query (way relations + member nodes + metadata tags + spatial join for a multi-state highway corridor), filtering by multiple criteria, output includes multiple tag types (speed, lanes, access, surface), documentation covers execution, interpretation, and how to adapt the query for adjacent segments.

## 5. Output Specification

### Primary Deliverable
- **Format:** Query code (plain text in the target language — OverpassQL, SQL, SPARQL)
- **Structure:** A working, syntactically valid query with inline comments explaining key filtering decisions
- **Key quality signals:** Query is syntactically correct for the target language, geographic scope is correctly specified (right bounding box or relation reference), all required metadata tags are included in the output clause, the query does not over-fetch (does not return the entire global highway network), output format clause matches the stated requirement

### Secondary Deliverables (if any)
- **Markdown documentation file (.md):** Usage instructions covering how to submit the query to the target endpoint, what tool or API to use, what the output structure looks like, and how to interpret key fields

### Gold Output Characteristics
A gold OverpassQL query is structured in Overpass QL syntax with correct `[out:json]` or `[out:xml]` output format declaration, a `[timeout]` setting appropriate for the data volume, correct union or filter clauses that target the specific geographic area (using a `relation` filter for named highway routes, not just a bounding box), and an `out body` or `out geom` clause that includes the relevant metadata. The query returns highway ways, their constituent nodes, and the relevant tags — not the entire OSM dataset for the region. The Markdown documentation specifies the exact Overpass API endpoint URL, explains how to paste the query into Overpass Turbo or submit it via curl, describes the JSON output structure (elements array, type/id/tags fields), and includes a note on how to modify the geographic scope for a different route segment.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Query language familiarity | SQL (widely known) | PostGIS SQL with spatial extensions | OverpassQL (niche, non-SQL syntax) |
| Geographic scope specification | City boundary or simple bounding box | Named highway + two city endpoints | Multi-state corridor with intermediate waypoints |
| Data model knowledge required | Standard SQL schema provided | Database schema provided with field descriptions | OSM tag vocabulary must come from domain expertise alone |
| Number of entity types in output | 1 (ways only) | 2 (ways + nodes) | 3 (way relations + member ways + their nodes) |
| Required metadata fields | 2–3 basic tags | 4–6 tags including non-obvious ones | 8+ tags including highway-class-specific attributes |
| Documentation depth | How to run the query (3 steps) | How to run + how to interpret output | How to run + interpret + adapt for different geographic scopes |
| Output format complexity | Raw JSON | GeoJSON with geometry | Multiple formats + filtering script |

## 7. Boundary Cases & Adjacent Patterns

**J3 (API Specification & Technical Architecture Design):** J3 designs API specifications for how systems should communicate. J5 writes queries to extract data from existing geographic databases. If the output is a YAML spec for a new API, use J3. If the output is a query in a specific query language against an existing data source, use J5.

**J1 (Full-Stack Application Development):** J1 builds a complete application. J5 writes a query and documentation. If the output is a runnable application that queries the geospatial database as part of a larger system, use J1. If the output is just the query and its documentation (not the surrounding application), use J5.

**E4 (Regulatory Data Extraction & Comparison):** E4 extracts regulatory data from government websites through web research. J5 extracts geospatial or technical data through a formal query language against a database or API. The distinction is query mechanism: web scraping/browsing (E4) vs. formal query language (J5). If the data extraction requires writing code or a formal query, use J5.
