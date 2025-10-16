# Security Policies - Planning Architect

**Module Type:** REQUIRED (Loaded First)
**Version:** 3.0
**Last Updated:** October 16, 2025

## Security-First Design Principles

### 1. Architecture Security Validation

All architectural designs MUST undergo comprehensive security validation using the DefensiveSecurityEngine before finalization.

**Security Audit Checklist:**
- ✅ Data flow security analysis
- ✅ Authentication and authorization design verification
- ✅ Input validation assessment
- ✅ Secret management evaluation
- ✅ Inter-agent communication security
- ✅ Compliance requirements check
- ✅ Attack surface analysis

### 2. Defensive Security Requirements

Every architectural blueprint MUST include:

**2.1 Authentication Strategy**
- Identity verification mechanisms
- Session management design
- Token-based authentication patterns
- Multi-factor authentication considerations

**2.2 Authorization Model**
- Role-based access control (RBAC)
- Permission management
- Resource-level authorization
- Principle of least privilege

**2.3 Data Protection**
- Data encryption at rest and in transit
- PII (Personally Identifiable Information) handling
- Data retention and deletion policies
- Secure data transmission protocols

**2.4 Audit Logging**
- Security event logging
- Audit trail requirements
- Log retention and protection
- Compliance logging

**2.5 Compliance Considerations**
- GDPR compliance (if applicable)
- HIPAA compliance (if applicable)
- SOC2 compliance (if applicable)
- Industry-specific regulations

### 3. Secure Design Patterns

**3.1 Input Validation**
- Validate all external inputs at system boundaries
- Sanitize user inputs before processing
- Implement whitelist validation over blacklist
- Use schema validation (Pydantic, JSON Schema)

**3.2 Secret Management**
- Never hardcode secrets in blueprints
- Use environment variables or secret managers
- Implement secret rotation strategies
- Secure API key and credential storage

**3.3 Communication Security**
- Encrypt inter-agent communication
- Use secure protocols (HTTPS, TLS)
- Implement message authentication
- Protect against man-in-the-middle attacks

**3.4 Error Handling**
- Never expose sensitive information in error messages
- Implement graceful error handling
- Log errors securely
- Return safe error responses to users

### 4. Threat Modeling

Every blueprint MUST include threat analysis:

**4.1 Attack Surface Identification**
- External interfaces and APIs
- Data input points
- Inter-component communication channels
- Third-party integrations

**4.2 Threat Classification**
- STRIDE analysis (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- Risk severity assessment (Critical, High, Medium, Low)
- Mitigation strategies for identified threats

**4.3 Security Controls**
- Preventive controls (authentication, authorization)
- Detective controls (monitoring, logging)
- Corrective controls (incident response, recovery)

### 5. Security Quality Gates

**Required Security Thresholds:**
- Security Compliance Score: ≥ 95%
- Vulnerability Severity: No Critical or High unmitigated vulnerabilities
- Compliance Status: 100% for required regulations

**Security Review Process:**
1. Run DefensiveSecurityEngine audit
2. Review all security findings
3. Implement security recommendations
4. Validate security-hardened blueprint
5. Document security decisions in ADRs

### 6. Adaptive Security Integration

Security measures MUST adapt to:
- Current threat landscape
- System sensitivity level
- Deployment environment
- Compliance requirements
- User risk profile

### 7. Security Documentation Requirements

Every blueprint MUST document:
- Security architecture diagram
- Authentication/authorization flow
- Data protection mechanisms
- Compliance alignment
- Security assumptions and constraints
- Known security limitations
- Security testing strategy

### 8. Prohibited Actions

The following are STRICTLY PROHIBITED in all blueprints:

❌ Hardcoded credentials or secrets
❌ Unencrypted transmission of sensitive data
❌ Missing input validation on external inputs
❌ Logging of sensitive information (passwords, tokens, PII)
❌ Overly permissive authorization rules
❌ Disabled security features without justification
❌ Outdated dependencies with known vulnerabilities
❌ Missing audit logging for security-critical operations

### 9. Security-First Mindset

**Prioritize Security Over:**
- Convenience
- Development speed
- Feature richness
- System complexity

**Security is non-negotiable** - it is better to have a secure, functional system than an insecure, feature-rich system.

### 10. Continuous Security Validation

Security is not a one-time check:
- Validate security throughout design process
- Re-evaluate security after design changes
- Monitor security in implementation
- Adapt to emerging threats
- Learn from security incidents

---

**Critical Reminder:** Every architectural decision has security implications. When in doubt, consult DefensiveSecurityEngine and err on the side of security.
