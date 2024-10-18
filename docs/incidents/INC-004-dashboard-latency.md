# INC-004: Dashboard Latency Spike

**Date**: 2024-04-10  
**Duration**: 2 hours  
**Impact**: Dashboard load time: 200ms → 4.2s  
**Severity**: High  

## Summary
Dashboard queries degraded to 4+ seconds due to missing database index.

## Timeline
- 10:30 AM: Customer reports slow dashboard
- 10:35 AM: Support escalates, confirmed affecting 15% of users
- 10:42 AM: Identified slow query: contact aggregation for sales pipeline
- 10:50 AM: Index added to contacts(user_id, status, created_at)
- 11:15 AM: Dashboard latency back to 200ms

## Root Cause
Recent code change added new filtering on `status` field without adding required index.
This caused full table scans for large contact lists (10k+ records).

## Impact Analysis
- Affected primarily enterprise customers (2M contacts)
- API response time: 200ms → 4.2s (21x degradation)
- 12 customers reported issues before fix deployed

## Resolution
1. Added missing index
2. Added monitoring for slow queries (>1s)
3. Query analysis before deploying

## Action Items
- [x] Deploy index (10 mins)
- [x] Alert on slow queries (30 mins)
- [x] Analyze query plan for all dashboard queries (2 hours)
- [x] Add EXPLAIN ANALYZE to code review checklist (15 mins)
- [ ] Investigate other potential index gaps (backlog)

## Lessons Learned
- Schema changes need query analysis
- Monitoring lag was 5 minutes (acceptable but could be faster)
- Index strategy needed for rapid feature development
