# Task Pattern Taxonomy for Synthetic Data Generation Pipeline

## 1. Executive Summary

This taxonomy is derived from the public GDPval benchmark tasks — professionally annotated, real-world workplace task samples spanning a wide range of industries and professional roles. It groups professional knowledge-work tasks by **task structure** rather than by industry, to maximize generative utility for the synthetic data pipeline. The taxonomy describes **workplace tasks** — the kind of work being done and how it is structured — not kinds of files: the same micro pattern can produce several different output formats, and the same output format recurs across many unrelated patterns. The analysis identifies **11 macro categories** (A–K) and **57 micro patterns**.

**Key characteristics:**
- 11 macro categories (A–K), 57 micro patterns
- Industries represented: Financial Services, Healthcare, Government, Technology, Media & Entertainment, Real Estate, Retail, Manufacturing, Legal, Education, Hospitality, Security, Logistics, Nonprofit, Automotive, and others
- Output formats: Excel (most common), Word, PDF, PowerPoint, video/audio files, code/technical artifacts
- Input modality: reference-file-driven tasks are the largest share, followed by web-research-driven tasks, then pure-knowledge tasks, with a smaller share of mixed reference-plus-research tasks

**Distribution highlights:**
- Financial analysis and data-driven Excel tasks form the largest cluster
- Policy/procedure/SOP document authoring is the second-largest cluster
- Research-to-document tasks (web research required) make up a substantial share of all tasks
- Media production (audio/video) and software development are smaller but highly distinct clusters
- Healthcare and government are the most represented industries

---

## 2. Hierarchical Taxonomy

---

### Macro Category A: Financial Analysis & Modeling

Tasks where the primary cognitive work is computing, modeling, or analyzing numerical financial data to produce structured quantitative outputs (usually Excel). The deliverable IS the analysis, not a narrative wrapping it.

#### Micro Pattern A1: Audit Sampling & Compliance Testing
- **Description:** Statistical sampling, compliance screening, or flagging tasks applied to financial or operational datasets. The worker applies formal criteria (confidence levels, thresholds, regulatory rules) to a population and produces a filtered/flagged subset.
- **Typical roles:** Auditor, Grants Management Specialist, Wholesale Analyst, Inventory Clerk
- **Typical industries:** Financial Services, Government, Wholesale, Automotive
- **Input modality:** Reference file (xlsx) with population data
- **Output formats:** Excel workbook with flagged/filtered rows and calculation workings
- **Key complexity signals:** Multi-criteria filtering, statistical calculation, dual-threshold logic
- **Key constraint patterns:** Numerical parameters (confidence levels, error rates, percentage thresholds), specific column schemas, classification label vocabularies

#### Micro Pattern A2: Financial Statement & P&L Construction
- **Description:** Building structured financial reports (P&L, income statements, amortization schedules) from raw source data across multiple files. The task requires consolidating, classifying, and computing financial aggregates.
- **Typical roles:** Senior Staff Accountant, Finance Lead, Finance Manager, Planning Manager
- **Typical industries:** Professional Services, Entertainment, Corporate Finance, Cosmetics
- **Input modality:** Multiple reference files (xlsx, pdf) with transactional/GL data
- **Output formats:** Multi-tab Excel workbook with formulas, reconciliation targets, and professional formatting
- **Key complexity signals:** Multi-source data consolidation, GL reconciliation, amortization logic, currency conversion, dropdown interactivity
- **Key constraint patterns:** Specific GL account numbers, reconciliation targets, defined expense categories, formula specifications

#### Micro Pattern A3: NPV/IRR & Investment Evaluation
- **Description:** Comparative financial modeling where multiple options (vendors, projects, scenarios) are evaluated using DCF, NPV, IRR, or similar frameworks, culminating in a recommendation.
- **Typical roles:** Category Buyer, Senior Finance Manager, Enterprise Sales Director
- **Typical industries:** Automotive Manufacturing, Technology, Commercial Real Estate Tech
- **Input modality:** Reference file (docx/pdf) with cost/volume data, or inline parameters
- **Output formats:** Excel workbook with per-option calculation tabs and comparison summary
- **Key complexity signals:** Discount rate application, amortization rules, volume-based modeling, dual-scenario or three-scenario structures
- **Key constraint patterns:** Specific discount rates, volume splits, tooling amortization rules, recommendation requirement

#### Micro Pattern A4: Scenario Analysis & Commercial Terms Modeling
- **Description:** Multi-scenario Excel models comparing different operational or commercial configurations (lease terms, pricing strategies, production plans, fill strategies) with a written recommendation.
- **Typical roles:** Sales Director, Production Manager, Property Manager, Pharmacist, Sales Director
- **Typical industries:** Cosmetics, Manufacturing, Real Estate, Healthcare/Pharmacy, Fragrance
- **Input modality:** Reference file (xlsx) with baseline data, or inline parameters
- **Output formats:** Excel workbook with scenario comparison, visual charts, and embedded written summary
- **Key complexity signals:** Three-scenario comparative structure, constraint optimization, chart/visualization requirement, written narrative embedded in Excel
- **Key constraint patterns:** Specific variable ranges (margins, terms, rates), budget caps, decision criteria thresholds

#### Micro Pattern A5: Operational Metrics Dashboard / KPI Reporting
- **Description:** Transforming raw operational data into structured multi-tab Excel dashboards with PivotTables, charts, conditional formatting, KPI summaries, and dropdown interactivity.
- **Typical roles:** IT Manager, Car Rental Clerk, Production Supervisor, Assistant Buyer, National Account Director, Inventory Analyst
- **Typical industries:** IT, Transportation, Manufacturing, Retail, Beauty, Warehouse/Logistics
- **Input modality:** Reference file (xlsx) with raw operational/transactional data
- **Output formats:** Excel workbook with PivotTables, charts, conditional formatting, KPI tables; sometimes PowerPoint for presentation
- **Key complexity signals:** Multi-dimensional aggregation, PivotTable/chart creation, calculated metrics, conditional formatting rules, dropdown filters
- **Key constraint patterns:** Named worksheet/slide structures, specific metric formulas, chart type requirements, data range specifications

#### Micro Pattern A6: Retail Planning & Forecasting Models
- **Description:** Building forward-looking retail merchandise plans (open-to-buy, store-level sales forecasts, inventory sufficiency) with calculated projections, constraint satisfaction, and comparison to prior year.
- **Typical roles:** Merchandise Planner, Wholesale Sales Analyst, Sales Representative
- **Typical industries:** Retail (Department Store, Candy, Apparel, Fragrance, Beverage)
- **Input modality:** Reference files (xlsx) with historical sales/inventory data
- **Output formats:** Excel workbook with forecasted values, constraint-satisfying allocations, and written commentary
- **Key complexity signals:** Multi-constraint optimization (budget, turn targets, minimums), rounding rules, week-weighting, active/closed filtering, unit conversion
- **Key constraint patterns:** Budget caps, turn rate targets, EOM inventory caps, minimum floors, STD trend application

---

### Macro Category B: Data-Driven Document Authoring

Tasks where the primary work is analyzing reference data AND producing a narrative or structured document that communicates the analysis. The document is the deliverable, but it is grounded in attached data files.

#### Micro Pattern B1: Performance Analysis Presentation (PowerPoint/PDF from Data)
- **Description:** Analyzing attached data to produce a presentation with charts, tables, and narrative interpretation for leadership or stakeholders.
- **Typical roles:** Insurance Rep, Industrial Engineer, Lean Six Sigma Greenbelt, Project Manager, Sales Manager, Financial Analyst
- **Typical industries:** Insurance, Logistics, Manufacturing, Technology, Apparel, Asset Management
- **Input modality:** Reference file (xlsx) with performance/operational data
- **Output formats:** PowerPoint or PDF presentation with charts, tables, and narrative
- **Key complexity signals:** Statistical analysis (SPC, ANOVA, capability indices), multi-metric visualization, leadership-facing framing
- **Key constraint patterns:** Specific slide structures, named chart types, statistical methodology requirements

#### Micro Pattern B2: HR & Workforce Decision Reports
- **Description:** Using employee/workforce data to evaluate candidates, assess utilization, or generate performance improvement plans with written justification.
- **Typical roles:** Residency Program Coordinator, Grocery Manager, Project Manager, Property Manager
- **Typical industries:** Healthcare/GME, Retail, Professional Services, Real Estate
- **Input modality:** Reference file (xlsx) with employee/resident performance data
- **Output formats:** Excel tracker + Word document (email, PIP, or selection justification)
- **Key complexity signals:** Multi-criteria evaluation, statistical benchmarking (mean/SD), threshold-based flagging, qualitative judgment integration
- **Key constraint patterns:** Priority ordering of criteria, specific threshold definitions, page limits

#### Micro Pattern B3: Compliance Report from Transaction Data
- **Description:** Cross-referencing transaction or claims data against policies, contracts, or regulatory criteria to produce compliance findings, exception reports, or SAR narratives.
- **Typical roles:** Senior Investigator, Car Rental Clerk, Leasing Agent, Order Analyst, Dialysis Nurse
- **Typical industries:** Banking/AML, Transportation, Real Estate, Wholesale, Healthcare
- **Input modality:** Reference files (xlsx with transaction data + docx/pdf with policies or schedules)
- **Output formats:** Word document (narrative report) + Excel (supporting data or tracking)
- **Key complexity signals:** Multi-source cross-referencing, regulatory framework application, exception identification, dual-deliverable
- **Key constraint patterns:** Regulatory citations required, specific exception categories, page/format limits

#### Micro Pattern B4: Cost Analysis & Budget Reconciliation Reports
- **Description:** Analyzing cost data from reference files to identify budget variances, calculate cost-effectiveness, or reconcile updated figures, with a written summary or recommendation.
- **Typical roles:** Production Supervisor, Health Manager, Video Producer, Shipping Manager
- **Typical industries:** Manufacturing, Healthcare, Entertainment, Logistics
- **Input modality:** Reference files (xlsx/pdf with cost or pricing data)
- **Output formats:** Excel cost breakdown + written summary/recommendation
- **Key complexity signals:** Rate card application, multi-variable calculation chains, cost comparison across scenarios or carriers
- **Key constraint patterns:** Budget constraints, specific rate/formula definitions, volume-based calculations

#### Micro Pattern B5: Data Entry with Protocol-Driven Decision Making
- **Description:** Populating templates or forms by extracting data from multiple reference files, applying embedded rules or clinical protocols to determine correct values.
- **Typical roles:** Production Supervisor, Medical Administrative Assistant, Shipping Clerk, Dialysis Nurse
- **Typical industries:** Manufacturing, Healthcare, Automotive, Healthcare
- **Input modality:** Multiple reference files (xlsx templates + source data documents)
- **Output formats:** Populated Excel template following embedded rules
- **Key complexity signals:** Cross-referencing across 3-5 input files, embedded rule interpretation, conditional logic, exception handling
- **Key constraint patterns:** Only specified cells to populate, rules embedded in target template, sequential month-over-month analysis

---

### Macro Category C: Policy, Procedure & Standards Authoring

Tasks where the deliverable is a formal organizational document (SOP, policy, standard, guideline, checklist, form) authored primarily from domain knowledge, sometimes with web research for regulatory grounding.

#### Micro Pattern C1: Standard Operating Procedure / General Order
- **Description:** Writing step-by-step procedural documents for organizational use, defining how a process should be executed, with sections for purpose, scope, responsibilities, and procedures.
- **Typical roles:** Administrative Manager, Car Rental Clerk, Police Sergeant, PM (Biotech), Sales Manager, Parts Manager, Warehouse Manager, Operations Manager
- **Typical industries:** Government, Transportation, Law Enforcement, Biotech, Sportswear, Automotive, Electronics, Healthcare
- **Input modality:** None or reference file (working session notes, issue lists)
- **Output formats:** Word document with structured sections (purpose, scope, responsibilities, procedures)
- **Key complexity signals:** Multi-section structured documents, process design from domain expertise, dual-audience writing, regulatory compliance alignment
- **Key constraint patterns:** Named section headers, page limits, specific stakeholders/approvers listed, compliance requirements

#### Micro Pattern C2: Compliance Checklist / Assessment Tool Design
- **Description:** Creating structured checklists, assessment forms, or audit tools organized by compliance domains, with scoring logic, threshold triggers, or escalation protocols.
- **Typical roles:** Grants Management Specialist, Regulatory Affairs Specialist, BTAM Unit Commander, Safety Coordinator, Pharmacist
- **Typical industries:** Government (Federal), Financial Services, Law Enforcement, Retail, Pharmacy
- **Input modality:** None or web research (regulatory text URLs provided)
- **Output formats:** Word/Excel/PDF structured form with questions, scoring, and escalation logic
- **Key complexity signals:** Regulatory text interpretation, structured question format (Yes/No + open-ended), scoring thresholds, multi-domain coverage
- **Key constraint patterns:** Specific regulatory citations, exact question counts, prescribed response formats, page limits

#### Micro Pattern C3: Clinical Guidelines & Reference Guides
- **Description:** Developing clinical practice guidelines, formularies, reference guides, or care plans grounded in clinical evidence, professional standards, or pharmacological knowledge.
- **Typical roles:** Medical Director, Nurse Practitioner, PACU Nurse, ER Nurse, Pharmacist
- **Typical industries:** Healthcare (Telemedicine, Primary Care, Emergency, Pharmacy)
- **Input modality:** None or web research (professional society guidelines, formulary template)
- **Output formats:** Word document or PDF with clinical recommendations, citations, structured sections
- **Key complexity signals:** Evidence-based synthesis, citation requirements, clinical protocol specificity, mixed audience (clinicians + patients)
- **Key constraint patterns:** Source requirements (named societies/databases), specific clinical parameters, structural section requirements

#### Micro Pattern C4: Training Materials & Educational Presentations
- **Description:** Creating training documents, coaching guides, educational slide decks, or case studies designed to teach staff or stakeholders a skill, process, or knowledge domain.
- **Typical roles:** Home Visitor, Senior CSR, Editor, Retail Sales Manager, Regional Director, Nurse Practitioner, Financial Advisor
- **Typical industries:** Nonprofit, Financial Services, Media, Retail, Grocery, Healthcare, Wealth Management
- **Input modality:** None, reference file (policy document), or web research (regulatory URLs)
- **Output formats:** PowerPoint presentation, PDF (deck + case studies), Word document (training guide)
- **Key complexity signals:** Dual-deliverable (instructional material + exercises/case studies), audience calibration, regulatory content integration, tone requirements
- **Key constraint patterns:** Slide/page limits, specific structural sections, audience-appropriate language, quiz/exercise requirements

#### Micro Pattern C5: Form & Template Design
- **Description:** Designing fillable forms, intake questionnaires, or operational templates for recurring organizational use, often with specific field types, validation, and formatting requirements.
- **Typical roles:** Art Studio Consultant, Medical Secretary, Community Association Manager, Dialysis Nurse
- **Typical industries:** Creative Services, Healthcare, Real Estate, Healthcare
- **Input modality:** Reference file (existing form or patient information list) or none
- **Output formats:** Word or Excel form with structured fields, dropdowns, and formatting
- **Key complexity signals:** Multi-section form design, data validation features, digital tool compatibility, field-level content specification
- **Key constraint patterns:** Named field requirements, dropdown values, page limits, audience-appropriate design

---

### Macro Category D: Strategic & Advisory Document Authoring

Tasks producing persuasive, analytical, or advisory documents that synthesize domain knowledge, reference data, and sometimes web research into recommendations, proposals, or strategic plans for decision-makers.

#### Micro Pattern D1: Technical Design & Architecture Documents
- **Description:** Writing technical design documents, architecture proposals, or engineering reports that specify system designs, evaluate technical options, and recommend approaches.
- **Typical roles:** CTO, Engineering Manager, Solutions Architect, Mechanical Engineer
- **Typical industries:** CleanTech, Software Agency, Cloud IT, Aerospace
- **Input modality:** None or reference files (existing architecture docs)
- **Output formats:** Word document (design doc) or PDF (architecture diagram + summary)
- **Key complexity signals:** Multi-dimensional requirements, justified technical choices, future extensibility, style-matching to existing documents
- **Key constraint patterns:** Page limits, specific technology constraints, audience-aware writing (engineers vs. executives)

#### Micro Pattern D2: Corporate Strategy & Business Proposals
- **Description:** Creating strategic presentations, business proposals, or advisory memos that analyze market conditions, propose organizational changes, or recommend business strategies.
- **Typical roles:** Senior Purchase Manager, EV Battery Sourcing Manager, Category Buyer, Head of Strategy, Director of Strategy, Sales Manager
- **Typical industries:** Automotive Manufacturing, Transportation/Ride-Hailing, Cosmetics, Sportswear
- **Input modality:** None or reference files (quotation data, issue documents)
- **Output formats:** Word document (2-3 pages), PowerPoint (5-6 slides), or PDF
- **Key complexity signals:** BATNA/ZOPA frameworks, financial cost analysis, multi-stakeholder audience, regulatory compliance mapping, persuasive framing
- **Key constraint patterns:** Page/slide limits, specific financial parameters, named stakeholder audiences, required analytical sections

#### Micro Pattern D3: Investment & Financial Advisory Reports
- **Description:** Producing client-facing or board-level reports analyzing investment opportunities, estate planning strategies, market conditions, or asset allocation views.
- **Typical roles:** Managing Director (IB), Quantitative Analyst, Financial Advisor, Wealth Advisor, Client Services Professional, Portfolio Strategist, Sales Director
- **Typical industries:** Investment Banking, Wealth Management, Asset Management, FinTech
- **Input modality:** None, reference file (research material, IM), or web research (market index providers, market data)
- **Output formats:** PDF or PowerPoint (client presentations), Word (strategy memos, advisory reports)
- **Key complexity signals:** Multi-section structured reports, comparative analysis (trust structures, market regions), scenario modeling, regulatory/tax knowledge, client-appropriate tone
- **Key constraint patterns:** Page/slide limits, specific analytical frameworks (GRAT vs. CRAT, UW/N/OW), data currency requirements, audience-specific language

#### Micro Pattern D4: Program & Evaluation Plans
- **Description:** Developing program proposals, evaluation frameworks, or inter-organizational agreements that define objectives, methodologies, timelines, and accountability structures.
- **Typical roles:** Administrative Services Manager, Nonprofit Director, Senior Advisor (CDC), Director of Parks & Recreation
- **Typical industries:** Government, Nonprofit, Public Health, Municipal Recreation
- **Input modality:** Reference files (budget data, background document) or web research (validated instruments, academic resources)
- **Output formats:** Word document (multi-section proposal/plan), PDF (org chart)
- **Key complexity signals:** Multi-format deliverable packages, percentage/financial calculations, evidence-based methodology, cross-referencing multiple source documents
- **Key constraint patterns:** Specific structural sections, regulatory compliance, named stakeholders/signatories, page limits

#### Micro Pattern D5: Legal & Transactional Documents
- **Description:** Drafting formal legal or quasi-legal documents such as wills, LOIs, contracts, or compensation frameworks that require specific legal structure and terminology.
- **Typical roles:** Attorney/Paralegal, Real Estate Broker, Qualifying Broker, Director of Parks & Recreation
- **Typical industries:** Legal Services, Commercial Real Estate, Government
- **Input modality:** None or reference files (contract outline, compensation model ideas)
- **Output formats:** PDF or Word document with formal legal structure
- **Key complexity signals:** Multi-clause legal structure, jurisdiction-specific compliance, financial calculations (cap rates), named parties and specific dollar amounts
- **Key constraint patterns:** Legal section requirements, jurisdiction-specific law, named entities, page limits

#### Micro Pattern D6: Sales Pitch Decks & Capabilities Presentations
- **Description:** Creating polished sales or capabilities presentations designed for client-facing meetings, structured slide-by-slide from service documentation.
- **Typical roles:** Sales Manager (Marketing Agency), VP of Sales & Growth (FinTech)
- **Typical industries:** Digital Marketing, FinTech
- **Input modality:** Reference file (services documentation, CEO brief)
- **Output formats:** PDF (15-25 slides/pages) with visual design and consistent formatting
- **Key complexity signals:** Multi-slide information architecture, visual design requirements, C-suite audience calibration, content alignment with source document
- **Key constraint patterns:** Slide count constraints, per-slide structural requirements, tone/design consistency

---

### Macro Category E: Research-to-Document Tasks

Tasks where the core work is conducting web research (finding, verifying, synthesizing information from online sources) and delivering the results in a structured document format.

#### Micro Pattern E1: Literature Review & Evidence Synthesis
- **Description:** Conducting multi-database academic literature searches and synthesizing findings into structured research papers or evidence reviews with citations.
- **Typical roles:** Administrative Lead (Government), Nurse Practitioner, Nonprofit Director
- **Typical industries:** Government, Healthcare, Nonprofit
- **Input modality:** Web research (academic databases, government sources)
- **Output formats:** Word document (structured literature review or summary table)
- **Key complexity signals:** Multi-database search, inclusion criteria, structured subthemes, reference count limits, page limits
- **Key constraint patterns:** Source quality constraints, publication date filters, specific section structures, citation limits

#### Micro Pattern E2: Curated Local Resource Guides
- **Description:** Researching and compiling location-specific resource directories (restaurants, wineries, community resources, schools) with multi-field entries sourced from web research.
- **Typical roles:** Social Worker, Concierge, Senior Lifestyle Manager, Real Estate Agent
- **Typical industries:** Nonprofit, Hospitality, Luxury Services, Real Estate
- **Input modality:** Web research (mapping platforms, specific websites, MLS platforms)
- **Output formats:** Word document or PDF with formatted tables, per-entry data fields
- **Key complexity signals:** Multi-source data aggregation, per-entry multi-field collection, geographic filtering, hyperlink insertion
- **Key constraint patterns:** Fixed origin points for distances, exact column names, dining/service category vocabularies, page limits

#### Micro Pattern E3: Market Research & Deal Sourcing
- **Description:** Researching publicly available market data, competitor pricing, or deal opportunities from web platforms and compiling findings into structured reports or spreadsheets.
- **Typical roles:** IB Analyst, Project Manager (Energy), Real Estate Broker, Pharmacist/Director of Sales
- **Typical industries:** Investment Banking, Energy, Commercial Real Estate, Fragrance
- **Input modality:** Web research (financial platforms, regulatory portals, real estate platforms, retail websites)
- **Output formats:** Excel spreadsheet with structured data tables; sometimes PDF report alongside
- **Key complexity signals:** Large-scale data collection (hundreds of rows or multiple properties), multi-criteria filtering, geographic/temporal constraints, valuation methodology
- **Key constraint patterns:** Specific data fields per entry, source platform constraints, quantity targets, pricing methodology rules

#### Micro Pattern E4: Regulatory Data Extraction & Comparison
- **Description:** Extracting specific regulatory, legal, or compliance data from government/institutional websites and organizing it into comparison tables with strategic recommendations.
- **Typical roles:** Director of Telehealth, Project Manager, Nurse Case Manager, Pharmacist
- **Typical industries:** Healthcare, Energy, Healthcare/ACO, Pharmacy
- **Input modality:** Web research (state regulatory sites, CMS, state pharmacy boards, EPA portals)
- **Output formats:** Excel spreadsheet with multi-state/multi-entity comparison + written recommendation
- **Key complexity signals:** Multi-jurisdiction regulatory research, comparative analysis tables, strategic synthesis layer, domain-specific terminology
- **Key constraint patterns:** Named states/entities, specific regulatory dimensions, source URL constraints, recommendation requirements

#### Micro Pattern E5: Conference/Travel Cost Estimation
- **Description:** Researching real-world travel logistics (flights, hotels, registration, transportation) from web platforms and compiling itemized cost estimates with screenshots.
- **Typical roles:** IEM Tech, Medical Secretary
- **Typical industries:** Entertainment (Live Music), Healthcare
- **Input modality:** Web research (booking platforms, conference websites, equipment retailers)
- **Output formats:** PDF or Word document with embedded screenshots, itemized costs, and budget summaries
- **Key complexity signals:** Multi-platform web research, screenshot embedding, proportional cost splitting, budget constraint logic, color-coded conditional formatting
- **Key constraint patterns:** Budget caps, geographic proximity requirements, date constraints, specific output formatting

#### Micro Pattern E6: Journalism & Editorial Content
- **Description:** Writing news articles, editorials, editorial pitches, or feature articles grounded in web-sourced facts, following specific style guides and journalistic conventions.
- **Typical roles:** Editor, Journalist, Senior Reporter, Senior Science Editor, Technology Journalist
- **Typical industries:** Media (Science, Elections, Economics, Technology, Astronomy)
- **Input modality:** Web research (named publications, government sites, arXiv) or reference files (reporter drafts, interview notes)
- **Output formats:** Word document with specific formatting (headline, standfirst, subheadings), PDF
- **Key complexity signals:** Style guide compliance (named publication house style), SEO optimization, fact-checking with source links, multi-source synthesis, quote-driven narratives
- **Key constraint patterns:** Word count constraints, named source requirements, neutrality/impartiality, language variant (UK English), format elements (headline, standfirst)

---

### Macro Category F: Client Communication & Outreach Materials

Tasks producing client-facing, customer-facing, or stakeholder-facing communications, itineraries, presentations, and correspondence.

#### Micro Pattern F1: Luxury Travel Itineraries
- **Description:** Creating styled multi-day or multi-activity itineraries for high-end clients, with researched venues, logistics, photos, and formatted for print or digital delivery.
- **Typical roles:** Senior Lifestyle Manager, Chief of Staff, Medical Secretary
- **Typical industries:** Luxury Concierge, Private Services, Healthcare
- **Input modality:** Web research (tour operators, restaurants, hotels)
- **Output formats:** PDF (styled 2-page itinerary) or Excel (multi-tab time-based itinerary)
- **Key complexity signals:** Multi-day scheduling, vendor verification, royalty-free image sourcing, time-zone arithmetic, clickable hyperlinks
- **Key constraint patterns:** Page limits, party composition, specific logistics details, photo requirements

#### Micro Pattern F2: Client-Facing Educational Presentations
- **Description:** Creating presentations that educate clients on financial products, regulatory requirements, or technical concepts, designed for in-person delivery.
- **Typical roles:** Client Advisor (Luxury Retail), Financial Advisor, Wealth Advisor, Director of Parks & Recreation
- **Typical industries:** Retail, Wealth Management, Government
- **Input modality:** None or web research (brand websites, regulatory sources)
- **Output formats:** PowerPoint or PDF presentation (4-12 slides)
- **Key complexity signals:** Domain expertise translation for lay audiences, side-by-side comparisons, hypothetical scenario illustrations, visual design elements
- **Key constraint patterns:** Slide/page counts, specific content area requirements, client-appropriate language

#### Micro Pattern F3: Tenant/Customer Communications & Tracking
- **Description:** Producing communications (emails, letters, tracking documents) for tenants, customers, or patients, often paired with scheduling or tracking spreadsheets.
- **Typical roles:** Leasing Agent, Government CSR, Service Representative, Property Manager
- **Typical industries:** Real Estate, Government, Financial Services, Real Estate
- **Input modality:** Reference file (xlsx tracking log, move-out reports)
- **Output formats:** PDF (email/letter + tracking document) or Word + Excel
- **Key complexity signals:** Cross-referencing source documents, date logic with exception handling, dual-audience deliverables, qualitative data synthesis
- **Key constraint patterns:** Default dates with exception rules, specific tracking columns, page constraints

#### Micro Pattern F4: Commercial Quotations & Proposals
- **Description:** Preparing formal commercial quotations or pricing proposals from internal pricing data and client requests, following specific format conventions.
- **Typical roles:** Account Manager (Medical Wholesaler), Sales Manager (Distribution)
- **Typical industries:** International Medical Supply, Consumer Goods Distribution
- **Input modality:** Reference files (internal pricing xlsx, client RFP pdf, freight quotes)
- **Output formats:** Excel spreadsheet with specific column schema, filename conventions
- **Key complexity signals:** Multi-source data consolidation, tiered pricing logic, Incoterms knowledge, multi-transport-option comparison
- **Key constraint patterns:** Specific file naming, required column schemas, payment terms, offer validity periods

#### Micro Pattern F5: Peer Feedback & Coaching Documents
- **Description:** Reviewing colleagues' work (chat transcripts, reports) and producing constructive feedback with specific problematic items identified, explained, and rewritten.
- **Typical roles:** Senior CSR (Banking), PI Supervisor
- **Typical industries:** Financial Services, Security/Investigation
- **Input modality:** Reference files (chat logs, field reports, photographs)
- **Output formats:** Word document or PDF with per-item annotation structure
- **Key complexity signals:** Multi-source analysis, constructive coaching tone, cross-referencing with external best practices
- **Key constraint patterns:** Document formatting (bold headers, spacing), page limits, per-item structure requirements

---

### Macro Category G: Form-Based & Clinical Documentation

Tasks producing structured clinical notes, case reports, intake forms, or administrative healthcare documents following prescribed templates and professional standards.

#### Micro Pattern G1: Clinical Documentation (SOAP Notes, Care Plans)
- **Description:** Writing structured clinical documentation (SOAP notes, nursing care plans) from provided patient scenarios, applying clinical judgment and standard documentation formats.
- **Typical roles:** Nurse Practitioner, PACU Nurse
- **Typical industries:** Healthcare (Pediatric, Primary Care, Psychiatry)
- **Input modality:** None (clinical scenario provided in prompt text)
- **Output formats:** SOAP note or PDF care plan with prescribed structure
- **Key complexity signals:** Clinical reasoning required, allergy/drug interaction awareness, multiple differential diagnoses, age-specific considerations
- **Key constraint patterns:** Standard SOAP format, specific nursing diagnosis counts, per-diagnosis assessment/intervention counts

#### Micro Pattern G2: Case Reports & Assessment Reports
- **Description:** Completing structured case reports or assessment documents by transforming shorthand notes or source documents into polished professional prose.
- **Typical roles:** School Social Worker, Child Support Investigator, Tax Preparer
- **Typical industries:** Education, Government (Human Services), Financial Services
- **Input modality:** Multiple reference files (notes, templates, source documents)
- **Output formats:** PDF with all sections completed, professional language throughout
- **Key complexity signals:** Content transformation (notes to prose), template completion, professional judgment sections, multi-document consolidation
- **Key constraint patterns:** Template adherence, page ranges, no copy-paste rules, specific placeholder conventions

#### Micro Pattern G3: Healthcare Administrative Forms & Correspondence
- **Description:** Creating administrative forms (fax covers, checklists, bulk request forms), HIPAA-compliant correspondence, or patient tracking spreadsheets for healthcare operations.
- **Typical roles:** Medical Secretary, Lead Medical Secretary, Medical Administrative Assistant, Dialysis Nurse, ER Pharmacist
- **Typical industries:** Healthcare (Weight Loss Clinic, Oncology, Hospital Admin, Dialysis, Emergency)
- **Input modality:** Reference files (patient lists, logos, HIPAA clauses, medication images)
- **Output formats:** Excel (tracking spreadsheets with dropdowns) + Word (email templates, letters) + PDF (forms)
- **Key complexity signals:** Multi-lab parallel deliverables, data validation features, HIPAA compliance, branding requirements, image-based medication identification
- **Key constraint patterns:** Specific field names, dropdown values, file naming conventions, regulatory clause inclusion

#### Micro Pattern G4: Medical Necessity & Insurance Documentation
- **Description:** Drafting insurance appeal letters or completing patient assistance applications using clinical chart data and insurance information.
- **Typical roles:** Nurse Practitioner, Administrative Services Manager
- **Typical industries:** Healthcare (Psychiatry), Government
- **Input modality:** Reference files (patient chart, insurance card image, PDF schedule)
- **Output formats:** Word document (appeal letter) + completed PDF form
- **Key complexity signals:** Clinical history extraction, formal appeal structure, dual-deliverable, external form completion from URL
- **Key constraint patterns:** Page limits, file naming, clinical justification requirements

#### Micro Pattern G5: Academic Medical Education Tasks
- **Description:** Creating academic medical content (journal club scheduling with literature sourcing, educational lecture presentations) for medical education programs.
- **Typical roles:** Medical Secretary, Nurse Practitioner
- **Typical industries:** Healthcare (GME, Nursing Education)
- **Input modality:** Reference files (room availability, blackout dates) or none
- **Output formats:** Excel (schedule), PDFs (articles), PowerPoint (lecture), email drafts
- **Key complexity signals:** Multi-constraint scheduling, literature search with accessibility requirements, clinical content across many topics, pre-test/case-study pedagogy
- **Key constraint patterns:** Weekday preference hierarchies, article recency/accessibility, slide limits, speaker notes requirement

---

### Macro Category H: Creative & Media Production

Tasks requiring creative production work in audio, video, visual design, or screenwriting, often with specific technical format requirements.

#### Micro Pattern H1: Broadcast Commercial & Video Editing
- **Description:** Producing broadcast-ready commercials or showreels by sourcing stock footage/music, assembling timelines, adding graphics/supers, and exporting to broadcast specifications.
- **Typical roles:** Video Editor
- **Typical industries:** Political Advertising, VFX Studio
- **Input modality:** Reference files (scripts, layered title-graphic files, video clips, audio) + web research (stock footage)
- **Output formats:** H.264 .mp4 at 1920x1080 with exact duration constraints
- **Key complexity signals:** Multi-step editorial workflow, graphic card insertion, music editing to exact duration, color grading, speed manipulation
- **Key constraint patterns:** Hard duration constraints (15 or 30 seconds), specific codec/resolution, shot-by-shot requirements

#### Micro Pattern H2: VFX Compositing & Post-Production
- **Description:** Creating polished VFX shots through stabilization, masking, motion tracking, compositing, and color grading across multiple video sources.
- **Typical roles:** Video Editor/Compositor
- **Typical industries:** Film & Television VFX
- **Input modality:** Reference files (video clips) + web research (royalty-free VFX elements)
- **Output formats:** Video file matching base clip specifications
- **Key complexity signals:** Multi-step technical workflow, alpha channel masking, perspective motion tracking, color grading match
- **Key constraint patterns:** Output must match source dimensions/framerate/codec, specific timecode guidance

#### Micro Pattern H3: Audio Composition, Editing & Mixing
- **Description:** Composing, editing, syncing, or mixing audio (music production, stem editing, audio resyncing) with specific technical format requirements.
- **Typical roles:** Music Producer, Sound Engineer, Mix Engineer
- **Typical industries:** Music Production
- **Input modality:** Reference files (WAV stems, MP3 references, edit spot documents)
- **Output formats:** WAV files (24-bit, 48kHz) or ZIP with master + stems
- **Key complexity signals:** Key changes at timestamps, timecode-based editing, loudness normalization (-16 dB LUFS), sync by reference comparison
- **Key constraint patterns:** BPM, key, duration, audio format specs, loudness targets, true peak ceilings

#### Micro Pattern H4: Visual Stage Plots & Technical Diagrams
- **Description:** Creating visual technical diagrams such as stage plots, process maps, signal flow charts, or electrical schematics with specific symbology and layout requirements.
- **Typical roles:** IEM Tech, Industrial Engineer, Electrical/Controls Engineer
- **Typical industries:** Live Music, Logistics, Manufacturing Automation
- **Input modality:** None or reference files (machine layout PNG)
- **Output formats:** PDF (landscape layout with specific paper sizes, standard symbols)
- **Key complexity signals:** Multi-element spatial layout, industry-standard symbology (IEC, process mapping), swimlane structures, wire label conventions
- **Key constraint patterns:** Paper size/orientation, symbol standards, precise naming conventions, minimum spacing specifications

#### Micro Pattern H5: Screenwriting & Script Development
- **Description:** Writing production-ready screenplays or documentary scripts following industry-standard formatting with creative storytelling requirements.
- **Typical roles:** Video Editor (Script), Screenwriter
- **Typical industries:** Documentary Production, Independent Film
- **Input modality:** Reference files (VO script, story breakdown, formatting guide)
- **Output formats:** Word/PDF with industry-standard screenplay formatting (Courier 12pt)
- **Key complexity signals:** Dual-audience tone calibration, alignment with provided VO, "show don't tell" principle, format compliance
- **Key constraint patterns:** Font/margin specifications, scene/page counts, format standards

#### Micro Pattern H6: Moodboard & Visual Direction
- **Description:** Creating visual moodboards from collaborative meeting notes, synthesizing aesthetic direction, color palettes, and reference images.
- **Typical roles:** Music Video Producer
- **Typical industries:** Music Video Production
- **Input modality:** Reference file (meeting notes PDF) + web research (reference images)
- **Output formats:** PNG moodboard with color palette and reference images
- **Key complexity signals:** Multi-stakeholder creative synthesis, visual output, tonal alignment with music
- **Key constraint patterns:** Must reflect all stakeholder inputs, color palette required

#### Micro Pattern H7: Production Scheduling & Budgeting
- **Description:** Creating production schedules, timelines, or budget breakdowns for media projects with color-coded phases and constraint-driven date calculations.
- **Typical roles:** Video Producer
- **Typical industries:** Advertising, Music/Educational Video
- **Input modality:** None or reference files (video series list, rate sheet)
- **Output formats:** PDF (visual schedule) or Excel (cost breakdown)
- **Key complexity signals:** Extensive task sequencing, phase overlap logic, holiday exclusion, color-coding systems, rate card application
- **Key constraint patterns:** Hard start/end dates, revision round counts, client review buffers

---

### Macro Category I: Investigation & Security Reports

Tasks involving surveillance documentation, investigation report compilation, or security-related document creation for PI firms, loss prevention, or law enforcement contexts.

#### Micro Pattern I1: Surveillance & Investigation Report Writing
- **Description:** Reviewing field notes, photographs, and investigator reports to produce polished investigation reports with timeline reconstruction, evidence integration, and professional assessments.
- **Typical roles:** PI Supervisor, Senior PI, Division Supervisor
- **Typical industries:** Private Investigation (Domestic, Corporate/Retail, Insurance Fraud)
- **Input modality:** Reference files (field investigator reports, time logs, surveillance photographs, company letterhead)
- **Output formats:** PDF report with sections (Summary, Surveillance, Assessment) on company letterhead
- **Key complexity signals:** Multi-source synthesis, timeline reconstruction, cross-referencing with photographic evidence, anonymization requirements, multi-investigator compilation
- **Key constraint patterns:** Page limits, named section structures, letterhead requirements, anonymization rules

#### Micro Pattern I2: Investigation Process Tools & Guides
- **Description:** Creating standardized operational guides, observation forms, or process flowcharts for investigation workflows.
- **Typical roles:** PI, Loss Prevention Professional
- **Typical industries:** Private Investigation, Retail Loss Prevention
- **Input modality:** None
- **Output formats:** PDF (operational guide + observation form, or flowchart + PowerPoint awareness deck)
- **Key complexity signals:** Dual document types, structural correspondence between documents, anonymization, field-use design
- **Key constraint patterns:** Exact titles, ruled lines for handwritten notes, structural correspondence between outputs

---

### Macro Category J: Software & Technical Implementation

Tasks requiring actual code implementation, API design, technical queries, or computational analysis delivered as executable artifacts.

#### Micro Pattern J1: Full-Stack Application Development
- **Description:** Implementing complete web applications with frontend, backend/smart contracts, and infrastructure, delivered as ZIP archives.
- **Typical roles:** Full-Stack Developer, Serverless Backend Engineer
- **Typical industries:** DeFi/Cryptocurrency, Cloud Infrastructure
- **Input modality:** None (specifications fully provided in prompt)
- **Output formats:** ZIP file with complete codebase (React/TypeScript, Solidity/Terraform, README)
- **Key complexity signals:** Multi-protocol integration, advanced cryptographic requirements, infrastructure-as-code, multi-file coordinated deliverable
- **Key constraint patterns:** Specific runtime versions, framework choices, parameterized configuration, file structure requirements

#### Micro Pattern J2: Component/Utility Development with Tests
- **Description:** Building specific software components (accessibility utilities, UI components) with accompanying test suites and documentation.
- **Typical roles:** Frontend Accessibility Engineer
- **Typical industries:** Enterprise Software
- **Input modality:** None (WCAG spec URLs provided)
- **Output formats:** ZIP file with component (.tsx), tests (.test.tsx), CSS, package.json, README
- **Key complexity signals:** WCAG compliance implementation, message queuing architecture, dual rendering modes, specific test case requirements
- **Key constraint patterns:** Exact test case count, specific testing frameworks, ARIA role requirements

#### Micro Pattern J3: API Specification & Technical Architecture Design
- **Description:** Designing API specifications (OpenAPI YAML) and technical architecture documentation for complex systems.
- **Typical roles:** API Designer (Robotics Fleet Management)
- **Typical industries:** Robotics/Autonomous Systems
- **Input modality:** None (specifications in prompt)
- **Output formats:** YAML (OpenAPI 3.0+ spec) + text file (data flow description)
- **Key complexity signals:** Complex domain model, resumable uploads, priority tiering, multi-stage pipeline design
- **Key constraint patterns:** OpenAPI 3.0+ format, specific storage architecture (cloud database and object storage services), sensor configuration variability

#### Micro Pattern J4: Quantitative Computing & Algorithm Notebooks
- **Description:** Implementing and comparing multiple computational algorithms with benchmarks, visualizations, and production recommendations in notebook format.
- **Typical roles:** Quantitative Researcher
- **Typical industries:** Proprietary Trading
- **Input modality:** None
- **Output formats:** Python notebook (.ipynb) with code, visualizations, and written summary
- **Key complexity signals:** Multiple algorithmic implementations, convergence analysis, runtime benchmarking, production recommendation framing
- **Key constraint patterns:** Named chart types required, multiple methodology comparison, written summary requirement

#### Micro Pattern J5: GIS Query & Technical Documentation
- **Description:** Writing specialized queries (OverpassQL, SQL) for geographic or domain-specific data extraction with accompanying usage documentation.
- **Typical roles:** GIS/Routing Engineer
- **Typical industries:** Logistics/Autonomous Freight
- **Input modality:** None
- **Output formats:** Query code + Markdown documentation
- **Key complexity signals:** Non-mainstream query language, geographic bounding, metadata filtering for autonomous vehicle needs
- **Key constraint patterns:** Specific geographic scope, relevant tag schema, Markdown format for documentation

#### Micro Pattern J6: Engineering Analysis & Simulation Reports
- **Description:** Performing numerical engineering computations (thermal analysis, CFD post-processing) and producing technical reports with plots, tables, and design recommendations.
- **Typical roles:** Mechanical Engineer (Aerospace)
- **Typical industries:** Aerospace
- **Input modality:** Reference file (analysis request PDF)
- **Output formats:** PDF report with multiple visualization types, summary tables, conditional recommendations
- **Key complexity signals:** Finite-difference computation, multiple visualization types, conditional output (mitigations if margin < threshold)
- **Key constraint patterns:** Specific numerical parameters, pass/fail thresholds, named node tracking, time-point requirements

---

### Macro Category K: Scheduling, Space Planning & Logistics

Tasks involving constraint-driven scheduling, space/resource assignment, or logistics planning where the core challenge is satisfying multiple simultaneous constraints.

#### Micro Pattern K1: Workforce Scheduling with Constraint Satisfaction
- **Description:** Building multi-period schedules for personnel that satisfy rotation patterns, coverage minimums, time-off requests, and fairness rules.
- **Typical roles:** Production Supervisor (Pet Food), Program Coordinator (Ski School)
- **Typical industries:** Manufacturing, Recreation
- **Input modality:** Reference files (personnel rosters, product specs) or none (inline parameters)
- **Output formats:** Excel workbook with multi-tab calendar, color-coded cells, coverage gap flags
- **Key complexity signals:** Multi-person scheduling with rotation patterns, coverage constraints, time-off exception handling, staggered cycle management
- **Key constraint patterns:** Work pattern rules (5-on/2-off), minimum daily coverage, named time-off dates, color-coding schemas

#### Micro Pattern K2: Production Planning & Recovery Scheduling
- **Description:** Building production plans or catch-up schedules that sequence operations, manage capacity constraints, and project when targets will be met.
- **Typical roles:** Production Supervisor, Production Manager
- **Typical industries:** Manufacturing (Welding, Automotive Parts, Wire Extrusion)
- **Input modality:** Reference files (xlsx with demand/capacity data, BOM, roster, tooling times)
- **Output formats:** Excel workbook with daily/weekly production plans across multiple scenarios
- **Key complexity signals:** Multi-scenario comparative analysis, capacity ramping, date sequencing with holidays excluded, cross-referencing multiple input files
- **Key constraint patterns:** Daily output rates, priority ordering, financial constraints (no overtime), customer shipping deadlines

#### Micro Pattern K3: Space Assignment & Event Logistics
- **Description:** Assigning vendors, units, or resources to physical spaces while satisfying location preferences, adjacency rules, and utility constraints.
- **Typical roles:** Leasing Agent, Recreation Department Manager
- **Typical industries:** Real Estate, Government (Recreation)
- **Input modality:** Reference files (floor plan PDFs, vendor lists, inspection reports)
- **Output formats:** Updated PDF floor plans + updated Excel spreadsheets
- **Key complexity signals:** Multi-constraint assignment (location preference, electricity, adjacency, product diversity), dual-space planning, timeline dependency chains
- **Key constraint patterns:** No same-type adjacent, electricity access limits, vendor-specific requests, dual output requirement

#### Micro Pattern K4: Project Timeline & Milestone Planning
- **Description:** Creating visual project timelines, Gantt charts, or milestone-based plans with phase dependencies, color coding, and buffer logic.
- **Typical roles:** Retail Sales Manager, Video Producer
- **Typical industries:** Retail, Advertising
- **Input modality:** Reference files (performance targets, marketing materials) or none
- **Output formats:** PDF (8-week plan, color-coded production schedule)
- **Key complexity signals:** Multi-week sequential planning, phase overlap logic, holiday exclusion, color-coding systems, revision rounds
- **Key constraint patterns:** Hard start/end dates, countdown structures, revision counts, task visibility requirements

---

## 3. Cross-Cutting Dimensions

### Input Modality Distribution
| Modality | Count | Percentage |
|----------|-------|------------|
| Reference files only (xlsx, docx, pdf) | ~110 | 50% |
| Web research required (no ref files) | ~45 | 20% |
| Mixed (reference files + web research) | ~25 | 11% |
| Pure domain knowledge (no files, no web) | ~40 | 18% |

### Output Format Distribution
| Format | Count | Notes |
|--------|-------|-------|
| Excel workbook (.xlsx) | ~75 | Most common single format |
| Word document (.docx) | ~55 | Second most common |
| PDF | ~65 | Often converted from Word/PPT |
| PowerPoint (.pptx) | ~25 | Often exported as PDF |
| Video/Audio files | ~7 | WAV, MP4, ZIP with stems |
| Code archives (ZIP) | ~5 | Software development tasks |
| PNG/JPG images | ~3 | Moodboards, diagrams, charts |
| YAML/query code | ~2 | API specs, GIS queries |
| Email/text drafts | ~10 | Often alongside primary deliverable |

### Complexity Spectrum
**Low complexity** (~15%): Single-file data entry, simple form creation, single-topic documents
**Medium complexity** (~50%): Multi-step analysis, 2-3 source files, structured multi-section documents, some calculations
**High complexity** (~30%): Multi-scenario modeling, 4+ source files, statistical analysis, multi-deliverable, web research + data integration
**Very high complexity** (~5%): Full-stack code implementation, multi-protocol integration, extensive multi-file codebases, advanced cryptographic requirements

### Constraint Pattern Catalog
1. **Page/Slide/Duration limits** — Most common constraint (~70% of samples)
2. **Specific column/field schemas** — Required column names, field lists (~45%)
3. **Named entities** — Specific people, companies, addresses that must appear (~40%)
4. **Numerical parameters** — Rates, thresholds, percentages, budgets (~40%)
5. **Structural section requirements** — Prescribed section headings (~35%)
6. **Date/temporal constraints** — As-of dates, date ranges, recency filters (~30%)
7. **Regulatory/standard compliance** — Must reference specific laws, standards (~25%)
8. **Output file naming** — Exact filename specified (~20%)
9. **Audience/tone constraints** — Executive, technical, client-facing, accessible (~20%)
10. **Conditional logic** — If-then rules, exception handling, threshold triggers (~15%)
11. **Visual/formatting requirements** — Color coding, fonts, charts, images (~15%)
12. **Source/citation requirements** — Named databases, URLs, publications (~15%)

### Prompt Structure Patterns
1. **Persona + Scenario + Instructions + Constraints** — Most common (~60%)
2. **Persona + Enumerated Deliverables with Sub-bullets** — Second most common (~25%)
3. **System Description + Component Specifications** — Software tasks (~5%)
4. **Narrative Brief + Open-ended Deliverable** — Creative/editorial tasks (~10%)

---

## 4. O*NET Occupation Coverage

### Most Represented O*NET Families
| O*NET Family | Code Range | Sample Count |
|-------------|-----------|-------------|
| Financial Specialists (Analysts, Accountants, Auditors) | 13-20xx | ~35 |
| Administrative Services & Office Managers | 11-30xx, 43-xxxx | ~20 |
| Sales Managers & Representatives | 11-2022, 41-xxxx | ~20 |
| Registered Nurses & NPs | 29-1141, 29-1171 | ~15 |
| Medical Secretaries & Health Admin | 43-6013, 11-9111 | ~10 |
| Editors, Journalists, Writers | 27-30xx | ~10 |
| Software Developers | 15-1252 | ~7 |
| Real Estate Brokers & Agents | 41-9021, 41-9022 | ~8 |
| Property Managers | 11-9141 | ~6 |
| Industrial Engineers | 17-2112 | ~5 |
| Film/Video Editors & Producers | 27-4032, 27-2012 | ~7 |
| Private Detectives/Investigators | 33-9021 | ~5 |
| Compliance Officers | 13-1041 | ~5 |
| Pharmacists | 29-1051 | ~5 |
| Sound Engineering Technicians | 27-4014 | ~4 |
| Social Workers | 21-1021 | ~4 |
| Mechanical/Aerospace Engineers | 17-2141, 17-2011 | ~5 |

### Coverage Gaps
The following O*NET occupation families have NO or minimal representation:
- **Construction & Extraction** (47-xxxx)
- **Farming, Fishing, Forestry** (45-xxxx)
- **Food Preparation & Serving** (35-xxxx) — limited to management
- **Architecture** (17-1011, 17-1012)
- **Life Scientists** (19-1xxx) — except through biotech PM
- **Mathematical Scientists** (15-2xxx) — only through quant finance
- **Religious Workers** (21-2xxx)
- **Library/Museum Specialists** (25-4xxx) — minimal representation
- **Military-specific** (55-xxxx)

---

## 5. Reference File Typology

### By Function

**Financial/Transactional Data Tables**
- GL trial balances, payroll registers, invoice details
- Transaction ledgers (banking, rental, purchase orders)
- Sales data (sell-in, sell-through, by-store, by-SKU)
- Inventory data (on-hand, on-order, rate of sale)
- Budget/cost files (project spend, rate sheets, pricing)

**Operational Records**
- Work order logs, incident reports, time logs
- Personnel rosters with attributes (skills, shifts, FTE status)
- Production data (capacity, demand, output by period)
- Room availability calendars, vendor schedules

**Policy & Regulatory Documents**
- CBA excerpts, insurance policies, regulatory handbooks
- Budget planning principles, compliance clauses
- Style guides, formatting templates, contract outlines

**Clinical & Case Documents**
- Patient charts, lab results, intake questionnaires
- Case detail summaries and supporting legal or investigative records
- Clinical protocols (medication dosing decision trees)

**Template/Scaffold Files**
- Blank Excel templates with column headers
- Report templates with section headings
- Form templates with fillable fields
- Domain-specific planning and evaluation templates

**Visual & Media Assets**
- Company logos (PDF, PNG, WEBP)
- Machine/facility layout diagrams (PNG, PDF)
- Video clips, audio stems, photographs
- Layered graphic files (pre-built title/text overlays)

**Narrative/Context Documents**
- Interview transcripts, meeting notes, field notes
- Press releases, research papers, boilerplate documents
- Working session summaries, CEO briefs
- Reporter drafts, story breakdowns, VO scripts
