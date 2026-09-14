# Coding Standards

## General
- Python: type hints, clear modules, pytest.
- TypeScript: strict mode.
- Dart: sound null safety.
- API: Pydantic schemas.
- Environment configuration through environment variables.
- Small modules and explicit interfaces.

## Provider adapters
Use interfaces/protocols so real and demo providers can be swapped without changing domain logic.

## Tests
At minimum:
- risk normalization and thresholds
- scenario determinism
- hazard/evacuation timing
- route pruning
- alternate route selection
- report validation
- API response schemas

## Frontend
Do not duplicate backend risk/routing formulas. Handle loading, error, offline and stale-data states explicitly.

## Security
No secrets, tokens, credentials or private endpoints in source control.
