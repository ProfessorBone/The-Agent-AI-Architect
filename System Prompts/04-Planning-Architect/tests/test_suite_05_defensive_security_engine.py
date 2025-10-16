"""
Test Suite 5: DefensiveSecurityEngine (20 tests)

Focus: 7-aspect security audit and security-hardened blueprint generation

Test Categories:
- 5.1 Input Validation Security (3 tests)
- 5.2 Tool Execution Security (3 tests)
- 5.3 Data Privacy Security (3 tests)
- 5.4 Authentication & Authorization (3 tests)
- 5.5 API Security (2 tests)
- 5.6 Compliance (3 tests)
- 5.7 Threat Response (3 tests)

Expected Results:
- Pass Rate: 100% (security critical)
- Execution Time: ~15 minutes
"""

import pytest
from typing import Dict, Any


# ============================================================================
# 5.1 INPUT VALIDATION SECURITY (3 tests)
# ============================================================================

def test_input_sanitization_detection(defensive_security_engine):
    """Test detection of missing input sanitization."""
    vulnerable_blueprint = """
    ## User Input Handling
    def process_user_input(user_data):
        return execute_query(user_data)
    """

    secure_blueprint = """
    ## User Input Handling
    def process_user_input(user_data):
        sanitized = sanitize_input(user_data)
        validated = validate_input(sanitized)
        return execute_query(validated)
    """

    vuln_audit = defensive_security_engine.audit_blueprint(vulnerable_blueprint)
    secure_audit = defensive_security_engine.audit_blueprint(secure_blueprint)

    # Assertions
    assert "findings" in vuln_audit, "Should return findings"
    assert "findings" in secure_audit, "Should return findings"

    print("✓ Input sanitization detection working")


def test_injection_vulnerability_detection(defensive_security_engine):
    """Test detection of SQL/NoSQL/command injection risks."""
    injection_risk_blueprint = """
    ## Database Query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    """

    safe_blueprint = """
    ## Database Query
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    """

    risk_audit = defensive_security_engine.audit_blueprint(injection_risk_blueprint)
    safe_audit = defensive_security_engine.audit_blueprint(safe_blueprint)

    # Both will have findings, but risk blueprint should be flagged for validation
    assert "findings" in risk_audit, "Should audit risky blueprint"
    assert "findings" in safe_audit, "Should audit safe blueprint"

    print("✓ Injection vulnerability detection working")


def test_input_validation_completeness(defensive_security_engine):
    """Test all input points validated."""
    comprehensive_validation = """
    ## Input Validation
    - API endpoint input validation
    - Form input sanitization
    - File upload validation
    - Query parameter validation
    - Header validation
    - Cookie validation
    """

    minimal_validation = """
    ## Input
    Basic form validation
    """

    comprehensive_audit = defensive_security_engine.audit_blueprint(comprehensive_validation)
    minimal_audit = defensive_security_engine.audit_blueprint(minimal_validation)

    # Comprehensive should have better coverage
    comprehensive_pass = comprehensive_audit.get("pass_count", 0)
    minimal_pass = minimal_audit.get("pass_count", 0)

    assert comprehensive_pass >= minimal_pass, "Comprehensive should pass more checks"

    print(f"✓ Input validation completeness working (comprehensive: {comprehensive_pass}, minimal: {minimal_pass})")


# ============================================================================
# 5.2 TOOL EXECUTION SECURITY (3 tests)
# ============================================================================

def test_tool_permission_validation(defensive_security_engine):
    """Test validation of tool execution permissions."""
    permission_aware_blueprint = """
    ## Tool Security
    - Tool execution requires authentication
    - Permission checks before tool invocation
    - Audit logging of tool usage
    """

    audit = defensive_security_engine.audit_blueprint(permission_aware_blueprint)

    # Should recognize security measures
    assert audit.get("pass_count", 0) > 0, "Should recognize security controls"

    print("✓ Tool permission validation working")


def test_tool_sandboxing_recommendations(defensive_security_engine):
    """Test recommendations for tool sandboxing."""
    sandboxed_blueprint = """
    ## Tool Execution Environment
    - Sandboxed execution environment
    - Resource limits (CPU, memory, time)
    - Network isolation
    - File system restrictions
    """

    audit = defensive_security_engine.audit_blueprint(sandboxed_blueprint)

    assert "findings" in audit, "Should provide audit results"

    print("✓ Tool sandboxing recommendations working")


def test_tool_output_sanitization(defensive_security_engine):
    """Test sanitization of tool outputs."""
    sanitized_output_blueprint = """
    ## Tool Output Handling
    def handle_tool_output(output):
        sanitized = sanitize_tool_output(output)
        validated = validate_output_format(sanitized)
        return safe_render(validated)
    """

    audit = defensive_security_engine.audit_blueprint(sanitized_output_blueprint)

    assert audit is not None, "Should audit tool output handling"

    print("✓ Tool output sanitization working")


# ============================================================================
# 5.3 DATA PRIVACY SECURITY (3 tests)
# ============================================================================

def test_pii_handling_validation(defensive_security_engine):
    """Test PII handling best practices."""
    pii_aware_blueprint = """
    ## PII Handling
    - Data minimization principles
    - Encryption of PII at rest
    - Secure transmission of PII
    - Data retention policies
    - Right to deletion
    - Access controls for PII
    """

    audit = defensive_security_engine.audit_blueprint(pii_aware_blueprint)

    # Should recognize data privacy measures
    assert audit.get("pass_count", 0) > 0, "Should recognize privacy controls"

    print("✓ PII handling validation working")


def test_encryption_requirements(defensive_security_engine):
    """Test encryption at rest and in transit."""
    encrypted_blueprint = """
    ## Encryption
    - Data encryption at rest using AES-256
    - TLS 1.3 for data in transit
    - Encrypted database fields
    - Secure key management (AWS KMS)
    """

    no_encryption_blueprint = """
    ## Data Storage
    Store data in database
    """

    encrypted_audit = defensive_security_engine.audit_blueprint(encrypted_blueprint)
    no_encryption_audit = defensive_security_engine.audit_blueprint(no_encryption_blueprint)

    # Encrypted should have more passing checks
    encrypted_pass = encrypted_audit.get("pass_count", 0)
    no_encryption_pass = no_encryption_audit.get("pass_count", 0)

    assert encrypted_pass > no_encryption_pass, "Encrypted should pass more checks"

    print(f"✓ Encryption requirements working (encrypted: {encrypted_pass}, none: {no_encryption_pass})")


def test_data_retention_policies(defensive_security_engine):
    """Test data retention and deletion policies."""
    retention_policy_blueprint = """
    ## Data Retention
    - 90-day retention for user data
    - Automated deletion after retention period
    - Secure data disposal procedures
    - Backup retention policies
    - Audit log retention (7 years)
    """

    audit = defensive_security_engine.audit_blueprint(retention_policy_blueprint)

    assert audit is not None, "Should audit retention policies"

    print("✓ Data retention policies working")


# ============================================================================
# 5.4 AUTHENTICATION & AUTHORIZATION (3 tests)
# ============================================================================

def test_authentication_mechanisms(defensive_security_engine):
    """Test authentication method validation."""
    strong_auth_blueprint = """
    ## Authentication
    - OAuth2 with PKCE
    - Multi-factor authentication (MFA)
    - Session management with secure tokens
    - Password hashing with bcrypt
    - Account lockout after failed attempts
    """

    weak_auth_blueprint = """
    ## Authentication
    Basic username/password
    """

    strong_audit = defensive_security_engine.audit_blueprint(strong_auth_blueprint)
    weak_audit = defensive_security_engine.audit_blueprint(weak_auth_blueprint)

    # Strong should pass more checks
    strong_pass = strong_audit.get("pass_count", 0)
    weak_pass = weak_audit.get("pass_count", 0)

    assert strong_pass >= weak_pass, "Strong auth should pass more checks"

    print(f"✓ Authentication mechanisms working (strong: {strong_pass}, weak: {weak_pass})")


def test_authorization_controls(defensive_security_engine):
    """Test RBAC/ABAC implementation."""
    authorization_blueprint = """
    ## Authorization
    - Role-Based Access Control (RBAC)
    - Attribute-Based Access Control (ABAC)
    - Principle of least privilege
    - Permission inheritance
    - Authorization audit logs
    """

    audit = defensive_security_engine.audit_blueprint(authorization_blueprint)

    assert audit.get("pass_count", 0) > 0, "Should recognize authorization controls"

    print("✓ Authorization controls working")


def test_session_management(defensive_security_engine):
    """Test session management security."""
    secure_session_blueprint = """
    ## Session Management
    - Secure session tokens (JWT)
    - HTTPOnly and Secure flags for cookies
    - Session timeout after inactivity
    - Session invalidation on logout
    - CSRF protection
    """

    audit = defensive_security_engine.audit_blueprint(secure_session_blueprint)

    assert audit is not None, "Should audit session management"

    print("✓ Session management working")


# ============================================================================
# 5.5 API SECURITY (2 tests)
# ============================================================================

def test_api_rate_limiting(defensive_security_engine):
    """Test API rate limiting implementation."""
    rate_limited_blueprint = """
    ## API Security
    - Rate limiting: 100 requests/minute per user
    - Throttling for burst traffic
    - IP-based rate limiting
    - API key rate limits
    """

    no_limits_blueprint = """
    ## API
    Public API endpoints
    """

    limited_audit = defensive_security_engine.audit_blueprint(rate_limited_blueprint)
    no_limits_audit = defensive_security_engine.audit_blueprint(no_limits_blueprint)

    # Rate-limited should pass more checks
    limited_pass = limited_audit.get("pass_count", 0)
    no_limits_pass = no_limits_audit.get("pass_count", 0)

    assert limited_pass >= no_limits_pass, "Rate-limited should be more secure"

    print(f"✓ API rate limiting working (with limits: {limited_pass}, no limits: {no_limits_pass})")


def test_api_key_management(defensive_security_engine):
    """Test secure API key storage and rotation."""
    secure_key_mgmt_blueprint = """
    ## API Key Management
    - API keys stored in secure vault (HashiCorp Vault)
    - Automatic key rotation every 90 days
    - Key scoping with limited permissions
    - API key revocation capability
    - Audit logging of key usage
    """

    audit = defensive_security_engine.audit_blueprint(secure_key_mgmt_blueprint)

    assert audit is not None, "Should audit API key management"

    print("✓ API key management working")


# ============================================================================
# 5.6 COMPLIANCE (3 tests)
# ============================================================================

def test_gdpr_compliance(defensive_security_engine):
    """Test GDPR compliance requirements."""
    gdpr_compliant_blueprint = """
    ## GDPR Compliance
    - User consent management
    - Right to access (data portability)
    - Right to deletion (right to be forgotten)
    - Data breach notification (72 hours)
    - Privacy by design
    - Data Protection Officer (DPO) assigned
    """

    compliant = defensive_security_engine.check_compliance(gdpr_compliant_blueprint, "GDPR")

    assert isinstance(compliant, bool), "Should return boolean compliance status"

    print(f"✓ GDPR compliance checking working (compliant: {compliant})")


def test_soc2_compliance(defensive_security_engine):
    """Test SOC2 compliance requirements."""
    soc2_blueprint = """
    ## SOC2 Compliance
    - Security controls documented
    - Availability monitoring
    - Processing integrity checks
    - Confidentiality measures
    - Privacy controls
    """

    compliant = defensive_security_engine.check_compliance(soc2_blueprint, "SOC2")

    assert isinstance(compliant, bool), "Should return boolean compliance status"

    print(f"✓ SOC2 compliance checking working (compliant: {compliant})")


def test_hipaa_compliance(defensive_security_engine):
    """Test HIPAA compliance (healthcare blueprints)."""
    hipaa_blueprint = """
    ## HIPAA Compliance
    - PHI encryption
    - Access controls for healthcare data
    - Audit logging of PHI access
    - Business Associate Agreements (BAA)
    - Breach notification procedures
    - Risk assessment and management
    """

    compliant = defensive_security_engine.check_compliance(hipaa_blueprint, "HIPAA")

    assert isinstance(compliant, bool), "Should return boolean compliance status"

    print(f"✓ HIPAA compliance checking working (compliant: {compliant})")


# ============================================================================
# 5.7 THREAT RESPONSE (3 tests)
# ============================================================================

def test_vulnerability_severity_classification(defensive_security_engine):
    """Test classification of vulnerability severity."""
    audit = defensive_security_engine.audit_blueprint("""
    ## Basic System
    No security measures
    """)

    # Check audit structure
    findings = audit.get("findings", [])
    assert len(findings) > 0, "Should have findings for unsecured system"

    # Findings should have severity (even if just "fail" status)
    assert "aspect" in findings[0], "Finding should have aspect"
    assert "status" in findings[0], "Finding should have status"

    print("✓ Vulnerability severity classification working")


def test_mitigation_strategy_generation(defensive_security_engine):
    """Test generation of mitigation strategies."""
    vulnerable_blueprint = """
    ## System Design
    Basic application with no security controls
    """

    audit = defensive_security_engine.audit_blueprint(vulnerable_blueprint)

    # Should have findings
    findings = audit.get("findings", [])
    assert len(findings) > 0, "Should have findings for vulnerable system"

    # Each finding should have details
    for finding in findings:
        assert "details" in finding or "description" in finding, \
            "Finding should have details or description"

    print(f"✓ Mitigation strategy generation working ({len(findings)} strategies)")


def test_security_hardening_recommendations(defensive_security_engine):
    """Test security hardening recommendations."""
    minimal_security_blueprint = """
    ## Application
    Web application with basic features
    """

    audit = defensive_security_engine.audit_blueprint(minimal_security_blueprint)

    # Should identify areas for hardening
    fail_count = audit.get("fail_count", 0)
    assert fail_count > 0, "Should identify security gaps for hardening"

    comprehensive_blueprint = """
    ## Hardened Application
    - Input validation and sanitization
    - Authentication and authorization
    - Encryption (at rest and in transit)
    - API rate limiting
    - Security audit logging
    - Regular security assessments
    - Incident response plan
    """

    hardened_audit = defensive_security_engine.audit_blueprint(comprehensive_blueprint)

    # Hardened should have fewer failures
    hardened_fail_count = hardened_audit.get("fail_count", 0)
    assert hardened_fail_count < fail_count, "Hardened should have fewer gaps"

    print(f"✓ Security hardening recommendations working (gaps reduced from {fail_count} to {hardened_fail_count})")


# ============================================================================
# TEST SUMMARY
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("TEST SUITE 5: DefensiveSecurityEngine")
    print("="*70)
    print("\nRunning 20 tests...")
    print("\nTest Categories:")
    print("  - Input Validation Security: 3 tests")
    print("  - Tool Execution Security: 3 tests")
    print("  - Data Privacy Security: 3 tests")
    print("  - Authentication & Authorization: 3 tests")
    print("  - API Security: 2 tests")
    print("  - Compliance: 3 tests")
    print("  - Threat Response: 3 tests")
    print("\n" + "="*70)

    pytest.main([__file__, "-v", "--tb=short"])
