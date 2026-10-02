# Company matching rules

Separate two questions: whether the employment evidence refers to the same business, and which CRM account represents that business. A correct employer match can still have several CRM account candidates.

## Compare identifiers

- Normalize website hostnames: lowercase, remove scheme/path/query/port, and handle `www.` consistently. Use a Public Suffix List implementation when deriving registrable domains; do not keep the last two labels blindly. Preserve the original hostname and business context because subsidiaries can share a parent domain.
- Normalize LinkedIn company-page identifiers. A matching page is strong evidence, but contradictory subsidiary/location context still needs review.
- Names are supporting evidence. Legal suffix and punctuation differences can be harmless; aggressively removing words such as “group” or “software” can also collapse distinct companies. Name similarity alone does not authorize a write.

## Decisions

**Same employer:** a reliable identifier agrees and there is no material conflict. A shared domain alone is insufficient when the records represent distinct operating companies or locations.

**Different employer:** fresh evidence identifies the new employer, its identifiers differ from the old one, and there is no unresolved rebrand/acquisition or concurrent-role explanation.

**Can't confirm:** only names are available; identifiers conflict; history is stale; several current jobs cannot be disambiguated; or the evidence cannot distinguish a real move from a rebrand.

For a new-company search, inspect all relevant matches. Do not create another account while a possible match is unresolved, and never choose the first of several results. Record the evidence behind the decision in the proposal.
