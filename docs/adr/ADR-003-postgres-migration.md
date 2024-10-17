# ADR 003: PostgreSQL Migration Strategy

## Context
Initially launched with SQLite for simplicity, but hitting limitations:
- Concurrent write issues during billing operations
- No native array/JSON support needed for features
- Scaling to multiple servers required shared database

## Decision
Migrate to PostgreSQL with zero-downtime using dual-write approach:
1. Set up PostgreSQL shadow database
2. Dual-write to both SQLite and PostgreSQL for 2 weeks
3. Validate data consistency
4. Switch read traffic to PostgreSQL
5. Deprecate SQLite

## Alternatives Considered
1. **MySQL**: Similar capabilities, chose PG for JSON support
2. **DynamoDB**: Overkill, added AWS lock-in
3. **MongoDB**: Document model less suitable for CRM data

## Consequences
- 2-week migration window added overhead
- Dual-write complexity (~200 LOC)
- Better concurrency and reliability

## Evidence
- 47% reduction in transaction conflicts post-migration
- 3 incidents during testing revealed data sync issues
- Performance improved 40% for contact bulk operations
