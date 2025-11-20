# Software Test Report
**Project:** TNNP BookStore QA Project  
**Document ID:** TR-TNNP-2025-06  
**Date of Report:** November 20, 2025  
**Prepared by:** Gilbert Keter & TNNP Team  
**Version:** 1.0

---

## Executive Summary
This report presents the results of comprehensive testing conducted on the TNNP BookStore application from November 1 to November 18, 2025. Testing focused on validating core features, verifying bug fixes, ensuring performance across supported platforms, and confirming compatibility on multiple devices.

**Key Findings:**  
- All critical and high-severity issues have been addressed, except for minor UI inconsistencies on mobile devices.  
- Core functionality, including user login, book search, and checkout, performs reliably with a 92% test case pass rate.  
- New features, such as wishlist and cart management, function as expected.  
- Minor performance delays observed when loading large book catalogs.

**Recommendation:** Proceed with deployment, with monitoring for UI fixes on mobile screens and performance optimization in future updates.

---

## 1. Test Objective
The primary objective of this testing cycle was to evaluate the **quality, functionality, performance, and usability** of the TNNP BookStore application. Specifically, testing aimed to:  
1. Validate all newly implemented features, including book catalog search, cart functionality, and wishlist management.  
2. Ensure bug fixes from previous testing cycles have been successfully resolved.  
3. Verify application performance under various network conditions.  
4. Assess compatibility across Android, iOS, and web platforms.  
5. Validate security measures for user data protection, including password storage and checkout processes.

Testing was conducted over three weeks from November 1 to November 18, 2025.

---

## 2. Areas Covered

### 2.1 Functional Testing
- **User Authentication & Account Management:** Registration, login/logout, password reset, account info management.  
- **Book Catalog & Search:** Browsing, category navigation, search (text-based), filtering, sorting, book details display.  
- **Shopping Cart & Checkout:** Add/remove books, modify quantities, save for later, shipping options, order confirmation.  
- **Wishlist & Recommendations:** Add/remove books to wishlist, track recently viewed books.

### 2.2 Non-Functional Testing
- **Performance:** Response time for critical functions, behavior under varying network conditions, memory/battery usage.  
- **Compatibility:** Testing across Android (v10–v14), iOS (v15–v18), and web browsers (Chrome, Firefox).  
- **Security:** Input validation, authentication, secure storage of sensitive data, session management.  
- **Usability:** Navigation flow, accessibility compliance, error message clarity.

---

## 3. Areas Not Covered
- Admin dashboard for book inventory (planned for next release).  
- Full penetration testing (specialized third-party testing scheduled later).  
- Performance testing on devices older than 3 years (focused on 95% of current user base).

---

## 4. Testing Approach

### 4.1 Test Strategy
- **Risk-Based Testing:** Priority given to login, checkout, and wishlist functionality.  
- **Test Case Design:** Black-box and white-box techniques, boundary value analysis, equivalence partitioning.  
- **Automation & Manual Testing Balance:** Regression suite automated; new features initially manual.

### 4.2 Testing Process
1. **Test Planning (Nov 1–3, 2025):** Environment setup, test case review, prioritization.  
2. **Test Execution (Nov 4–15, 2025):** Smoke testing, full regression, feature-specific testing, non-functional testing.  
3. **Defect Management (Ongoing):** Defects logged in JIRA, daily triage meetings, verification of fixed defects.  
4. **Reporting & Analysis (Nov 16–18, 2025):** Results compilation, metrics analysis, recommendations.

### 4.3 Testing Tools
- **Test Management:** TestRail  
- **Defect Tracking:** JIRA  
- **Automation Framework:** Selenium with Python 3.11  
- **Performance Testing:** JMeter 5.6  
- **Compatibility Testing:** BrowserStack  
- **Security Testing:** OWASP ZAP  
- **Accessibility Testing:** Android Accessibility Scanner, VoiceOver/TalkBack

### 4.4 Sample Key Test Cases
| Test Case ID | Title | Preconditions | Steps | Expected Results | Status |
|--------------|-------|---------------|-------|-----------------|--------|
| TC-LOGIN-001 | User Login | User registered | Enter email/password → Login | Dashboard loads | PASS |
| TC-CART-002 | Add Book to Cart | User logged in | Add book to cart | Book added, quantity correct | PASS |
| TC-WISHLIST-003 | Wishlist Sync | User logged in | Add book to wishlist → Log out → Log in | Wishlist persists | PASS |

---

## 5. Defect Report

### 5.1 Defect Summary
| Severity | Count | Closed | Open |
|----------|-------|--------|------|
| Critical | 3 | 3 | 0 |
| High | 7 | 6 | 1 |
| Medium | 20 | 18 | 2 |
| Low | 15 | 10 | 5 |
**Total:** 45 defects (37 closed, 8 open)

### 5.2 Critical Defects (Resolved)
1. **Login Failure on Special Characters (DEF-101)** – Fixed input validation error.  
2. **Cart Quantity Mismatch (DEF-102)** – Fixed calculation logic.  
3. **App Crash on Book Details (DEF-103)** – Resolved memory leak issue.

### 5.3 Open High-Severity Defect
- **Wishlist Sync Delay (DEF-110):** Occasionally items added offline do not sync immediately. Mitigation: Warning message added; fix planned in next release.

---

## 6. Platform Details

### 6.1 Test Environment
- Backend: PostgreSQL 15, Node.js API, Redis Cache  
- Frontend: React Native (Android/iOS) and React.js (Web)

### 6.2 Client Devices
- **Android:** Samsung S23, Pixel 7, OnePlus 10T (v12–v14)  
- **iOS:** iPhone 15, iPhone 14, iPad Pro 12.9 (v17–v18)  
- **Web:** Chrome, Firefox, Edge

### 6.3 Network Conditions Tested
- High-speed Wi-Fi, 4G, 5G, throttled 3G, intermittent connections, offline mode.

---

## 7. Overall Status

### 7.1 Testing Summary
- Test Cases Executed: 150 / 150 (100%)  
- Test Case Pass Rate: 138 / 150 (92%)  
- Automation Coverage: 65%  
- Critical User Journeys: 100% passing

### 7.2 Quality Assessment
**Strengths:**  
- Core functionality stable; wishlist, cart, and checkout reliable.  
- Application handles network interruptions gracefully.

**Areas of Concern:**  
- Wishlist sync issue affects ~5% of offline users.  
- Minor performance delays on large catalogs.

### 7.3 Risk Assessment
- Wishlist Sync Issue: Low risk, mitigation in place.  
- Performance on older devices: Low risk, monitoring planned.

### 7.4 Release Recommendation
Proceed with deployment, with monitoring for wishlist sync and catalog performance issues.

### 7.5 Post-Release Activities
- Monitor app performance and crash reports.  
- Collect user feedback on wishlist and checkout features.  
- Verify fixes in next release cycle.

---

## 8. Requirements Traceability
| Requirement ID | Description | Test Case IDs | Status |
|----------------|------------|---------------|--------|
| REQ-LOGIN-001 | User shall login successfully | TC-LOGIN-001 | PASSED |
| REQ-CART-001 | Add/remove books from cart | TC-CART-002 | PASSED |
| REQ-WISH-001 | Wishlist persists across sessions | TC-WISHLIST-003 | PASSED* |
*Pending final hotfix for offline sync

---

## 9. Testing Challenges & Lessons Learned
**Challenges:**  
1. Device availability limited scheduling.  
2. Test data generation for realistic book histories.  
3. Third-party payment sandbox availability issues.

**Lessons Learned:**  
1. Early API testing reduces end-to-end blockers.  
2. Automated visual testing saves manual effort.  
3. Daily triage improves defect resolution speed.

---

## 10. Appendices
- Test Case Execution: TestRail project “TNNP-BookStore”  
- Performance Test Results: JMeter reports  
- Traceability Matrix: Document TRM-TNNP-2025  
- Test Data Inventory: TDI-TNNP-2025  
- Defect Details: JIRA project TNNP-QA

---

## 11. Approvals
| Role | Name | Approval Date | Notes |
|------|------|---------------|-------|
| Risk Analyst | Gilbert Keter | Nov 20, 2025 | Approves release with minor concerns |
| Test Executor | Bismark Cheruiyot | Nov 20, 2025 | Confirms all critical fixes applied |
| Project Manager  | Dominic Kimutai | Nov 20, 2025 | Accepts risks and confirms business value |

---
