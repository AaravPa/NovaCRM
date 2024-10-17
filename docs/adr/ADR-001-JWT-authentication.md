# ADR 001: JWT vs Session-based Authentication

## Context
NovaCRM needed to implement authentication. The system would need to support:
- Browser-based access
- Mobile app access
- Third-party integrations

## Decision
Use JWT (JSON Web Tokens) with short-lived access tokens (24h) and refresh tokens.

## Alternatives Considered
1. **Session-based (server-side)**: Simpler implementation, easier revocation
2. **OAuth 2.0**: More complex, better for third-party integrations
3. **SAML**: Enterprise-focused, overkill for early stage

## Consequences
### Positive
- Stateless authentication (scales better)
- Works with mobile and API clients
- Industry standard
- No server-side session storage

### Negative
- Token revocation is challenging (requires blacklist)
- Cannot easily invalidate all tokens for a user
- Larger request payloads compared to session IDs

## Assumptions
- Early stage product with <10k users
- Token expiry is sufficient for security
- Clients can handle token refresh flow

## Evidence
- Industry adoption (Auth0, AWS Cognito)
- Performance metrics show 15% faster auth checks
- 3 integration partners requested JWT support
