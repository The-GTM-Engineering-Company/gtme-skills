# Persona Lenses: Writing the Same Engagement for Four Readers

Persona editions are NOT the company-wide case study with reshuffled bullets. Each edition re-answers three questions for its reader: *What problem of MINE does this solve? What would MY team get? What proves it?* Every section is re-angled: Overview, Challenge, Strategy, Results. Workstreams irrelevant to the reader are compressed to a sentence or cut.

## The four lenses

### Founder edition
- **Reader:** Founder/CEO at a seed–Series B company doing founder-led sales, deciding whether to hire RevOps headcount, buy tools, or bring in a fractional team.
- **Lead with:** Speed to live systems, leverage (what shipped without hires), cost framing vs. a full-time hire, systems that outlive the engagement.
- **Vocabulary:** Leverage, runway, focus, "engine," optionality, "your team's time back."
- **Challenge framing:** Founder time being eaten by GTM plumbing; pipeline dependent on the founder's personal network; can't justify a full-time ops hire yet.
- **Results emphasis:** Time-to-value (weeks, not quarters), what the team can now do self-serve, what did NOT require an FTE.
- **Cut:** Field-by-field fill-rate tables, tool minutiae, workflow IDs.

### Sales edition
- **Reader:** Head of Sales / sales leader who cares about reps' calendars and call lists this week.
- **Lead with:** Lists reps could call/email immediately, decision-maker coverage, phone numbers, auto-sequencing, job-change triggers ("your former champion just moved; call them").
- **Vocabulary:** Pipeline, coverage, follow-up, triggers, "buttons your reps can press."
- **Challenge framing:** Reps working stale or thin lists; manual research eating selling time; no signal telling reps WHO to contact WHEN.
- **Results emphasis:** Named lists with counts, live sequences, self-serve workflows reps trigger from the CRM record.
- **Cut:** Enrichment architecture, data-hygiene mechanics, marketing-audience detail.

### Marketing edition
- **Reader:** Marketing lead / demand gen owner who thinks in segments, audiences, and campaign inputs.
- **Lead with:** ABM list building, ads audiences, competitor-follower audiences, investor/network-path segmentation, compelling-event signals as campaign triggers.
- **Vocabulary:** Segments, audiences, signals, personalization inputs, TAM, ICP.
- **Challenge framing:** Campaigns limited by list quality; no reliable segmentation fields; ads audiences built on guesswork.
- **Results emphasis:** Audience sizes delivered, net-new segmentation fields marketing can filter on, signal fields that trigger campaigns.
- **Cut:** CRM plumbing detail, rep-workflow mechanics.

### Operations / RevOps edition
- **Reader:** RevOps / ops leader who owns the CRM and will be the internal champion evaluating the technical work. The deepest, most technical edition.
- **Lead with:** Architecture (enrichment engine of record around the CRM), before/after fill rates, new field taxonomy, scoring design, dedup/hygiene, evergreen self-serve workflows, governance.
- **Vocabulary:** Fill rates, source of truth, webhooks, waterfalls, scoring weights, self-serve, maintainability.
- **Challenge framing:** Years of CRM entropy; unreliable fields blocking reporting and routing; every enrichment request becoming an engineering ticket.
- **Results emphasis:** Field-level before/after numbers (a table is appropriate ONLY in this edition), count of new fields/workflows/scores, what runs without maintenance.
- **Cut:** Nothing technical, but keep business framing in the Overview so it forwards well to their boss.

## Rules that apply to every edition

- Use the configured structure (default: [house style](house-style.md)): Overview → Challenge → Strategy (numbered) → Results → TLDR.
- Same true numbers: editions differ in WHICH numbers lead, never in the numbers themselves.
- Default to 600–900 words per edition; the Ops edition may run to about 1,100 with a useful table. Follow a different user-supplied length.
- Each edition must stand completely alone: assume the reader never sees the other versions.
- One cross-persona sentence is fine (e.g., a founder edition noting reps got call-ready lists) when it strengthens the story; a section is not.
