# Architecture Review - 2024-06-05

**Attendees**: Sarah Chen, Maya Patel, James Liu, Emma Williams

## Topics

### 1. AI Lead Scoring MVP (45 min)
- Proposed model: logistic regression on engagement + firmographic data
- **Challenge**: Training data - need historical outcomes
- **Decision**: Start with rules-based model, migrate to ML in Q3
- **Success Metric**: Improve sales conversion rate by 15%
- **Owner**: Emma (3 weeks)

### 2. Search Performance Issues (30 min)
- Contact search timing out for queries > 5 words
- Current implementation: LIKE queries (O(n) full scans)
- **Options**:
  1. PostgreSQL full-text search (tsvector)
  2. Elasticsearch
  3. Optimize existing LIKE queries
- **Decision**: PostgreSQL FTS first, Elasticsearch if scales beyond 10M contacts
- **Owner**: James (2 weeks)

### 3. Incident Review: Dashboard Latency (20 min)
- Root cause: missing index on contacts(user_id, status)
- Process gap: no query analysis before deploy
- **Action**: Add query plan review to PR checklist

### 4. Scaling to 1M Contacts (25 min)
- Enterprise customer imported 2M contacts unexpectedly
- System designed for max 100k contacts per account
- **Issues encountered**:
  1. Memory spike during import (Celery worker crashed)
  2. Search queries timeout
  3. Aggregation queries become slow (10+ seconds)
- **Assumptions violated**: "Customers have <100k contacts" ← WRONG
- **New understanding**: Need to support 2M+ contacts
- **Action items**:
  - [ ] Implement chunked contact import
  - [ ] Add memory limits to Celery workers
  - [ ] Partition contacts table (by user_id)
  - [ ] Add query optimization for large datasets

### 5. Feature Flag System (15 min)
- Ready to release AI scoring to 50% of users
- Feature flags implemented, need monitoring
- **Decision**: Use feature flags for gradual rollout
- **Monitor**: Conversion rate, error rate, latency

## Decisions
1. Lead scoring: Rules-based MVP, ML in Q3
2. Search: PostgreSQL FTS + monitoring for Elasticsearch trigger point
3. Query analysis mandatory for PRs (added to template)
4. Rescale for 2M contacts (priority shift for Q3)
5. Feature flags for all major releases

## Updated Assumptions
- ~~Customers have <100k contacts~~ → Support up to 2M contacts
- New metric: Per-account contact limits need review

## Next Steps
- Emma: Lead scoring design doc (by 2024-06-10)
- James: Search rewrite plan (by 2024-06-10)
- Sarah: Partition strategy for contacts table (by 2024-06-12)

## Next Review
2024-06-19
