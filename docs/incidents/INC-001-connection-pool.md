# INC-001: Database Connection Pool Exhaustion

**Date**: 2024-02-15  
**Duration**: 45 minutes  
**Impact**: 100% of users unable to login  
**Severity**: Critical  

## Summary
Connection pool exhausted during billing batch job, causing all new connections to fail.

## Timeline
- 02:15 PM: Monitoring alerts trigger high query queue
- 02:18 PM: Engineering on-call paged
- 02:25 PM: Root cause identified: stripe sync job holding connections
- 02:35 PM: Rolled back recent connection pool change
- 03:00 PM: Service recovered

## Root Cause
Stripe webhook handler not properly closing database connections. When monthly billing
kicked off with 1000+ invoice operations, connections leaked and exhausted the pool.

## Contributing Factors
- No connection monitoring/alerting in place
- Stripe sync job marked as "non-blocking" but was actually synchronous
- Production connection pool size: 20 (appropriate for normal load, not batch)

## Resolution
1. Added connection lifecycle logging
2. Implemented batch job connection pool (separate from web pool)
3. Added monitoring for active connections > 80%
4. Forced connection pool reset after batch operations

## Action Items
- [x] Implement connection monitoring (45 mins)
- [x] Review all long-running jobs for connection leaks (2 hours)
- [x] Add integration test for connection exhaustion (1 hour)
- [ ] Document best practices for connection handling (backlog)

## Prevention
Similar issues unlikely due to:
- Connection pool monitoring now in place
- Batch jobs isolated to separate pool
- Alerting at 80% threshold allows 15+ min response window
