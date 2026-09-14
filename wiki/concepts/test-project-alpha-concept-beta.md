---
type: concept
title: JWT Token Structure and Claims
created: '2026-07-20'
project: 99.TestProjectAlpha
related:
  - '[[Decision-002-Session-Token-Strategy]]'
captured_at: '2026-07-21T05:31:37.264Z'
captured_via: capture-cli
project_slug: test-project-alpha
ingested_via: put_page
ingested_at: '2026-07-21T05:31:37.615Z'
source_kind: put_page
tags:
  - authentication
  - dag
  - jwt
  - refined
  - research
  - security
  - test-project-alpha
source: brain/ (retired 2026-09-13)
---

[[99.TestProjectAlpha-INDEX]]

# JWT Token Structure and Claims

## Overview
JSON Web Tokens (JWT) are compact, URL-safe tokens used for authentication and information exchange. They consist of three parts: Header, Payload, and Signature.

## Structure

### Header
Specifies token type and signing algorithm:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### Payload
Contains claims (statements about entity):
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022,
  "exp": 1516242622
}
```

### Signature
Cryptographic signature ensuring token integrity:
```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

## Standard Claims

### Registered Claims
- **iss:** Issuer
- **sub:** Subject (user ID)
- **aud:** Audience
- **exp:** Expiration time
- **nbf:** Not before
- **iat:** Issued at
- **jti:** JWT ID (unique identifier)

### Custom Claims
Application-specific data like permissions, roles, or session context.

## Access Token vs Refresh Token

### Access Token
- Short-lived (15 minutes)
- Contains user context
- Stateless verification
- Used for API requests

### Refresh Token
- Long-lived (30 days)
- Stored in database
- Enables token revocation
- Used to obtain new access tokens

## Security Considerations

### Best Practices
- Use strong signing algorithms (RS256 preferred over HS256)
- Set appropriate expiration times
- Validate all claims
- Use HTTPS for transmission
- Store refresh tokens securely (hashed, like passwords)

### Common Vulnerabilities
- **None algorithm:** Accept tokens without signature
- **Weak secrets:** Brute-forceable HMAC keys
- **Missing expiration:** Tokens valid indefinitely
- **Token leakage:** URL parameters or logs

## Implementation in Hybrid Approach
```python
access_token = create_jwt(
    user_id=user.id,
    exp=now + timedelta(minutes=15),
    secret=JWT_SECRET
)

refresh_token = generate_secure_token()
store_refresh_token(user.id, refresh_token, expires_in=30*24*60*60)
```

This provides balance between security (short-lived access tokens) and usability (refresh tokens for seamless re-authentication).
