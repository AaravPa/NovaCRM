# ADR 005: Redis Caching Strategy

## Context
Dashboard queries hitting 2-3 second latencies at 500 concurrent users.
Analysis showed repeated queries for:
- Contact aggregations (sales pipeline state)
- User settings
- Subscription status

## Decision
Implement Redis cache layer with Cache-Aside pattern:
- 1-hour TTL for aggregations
- 24-hour TTL for settings
- Explicit invalidation on writes

## Alternatives Considered
1. **Database query optimization**: Limited by JOIN complexity
2. **Connection pooling**: Tried first, only 15% improvement
3. **Elasticsearch**: Overkill for structured data

## Consequences
- Staleness accepted (up to 1 hour for aggregations)
- Infrastructure complexity (+1 service)
- Risk of cache stampedes under load

## Mitigations
- Implemented cache warming at low traffic periods
- Use mutex locks for cache misses
- Monitor Redis memory and eviction policies

## Evidence
- Dashboard queries: 2.8s → 200ms (93% improvement)
- Cost: +$50/mo for Redis hosting
- Cache hit rate: 87% after 2 weeks stabilization
