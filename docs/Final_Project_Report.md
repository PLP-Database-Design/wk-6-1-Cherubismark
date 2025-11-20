# 📄 TNNP BookStore QA Project — Final Test Report

*Document ID:* TR-TNNP-2025-001  
*Date of Report:* November 20, 2025  
*Prepared by:* TNNP QA Team  
*Version:* 1.0  

---

## Team members and their roles

| **Name**       | **Role**        |
| -------------- | --------------- |
| Dominic Kirui  | Project Manager |
| Gilbert Keter  | Risk Analyst    |
| Bismark Koskei | Test Executor   |


## 📝 Executive Summary
This report presents the results of comprehensive QA testing conducted on the *TNNP BookStore Web Application* until November 18, 2025.  
Testing focused on validating core features, detecting and logging defects, ensuring accessibility compliance, and evaluating performance across multiple devices and browsers.  

*Key Findings:*
- Core functionality (catalog, cart, checkout, order tracking) performed reliably.  
- 75% of assigned test cases passed; 3 major defects remain in progress.  
- Accessibility compliance achieved for WCAG 2.1 AA standards in tested flows.  
- Minor performance concerns noted on lower-end devices.  

*Recommendation:* Proceed with release after resolving high-priority defects and monitoring checkout/payment workflows.

---

## 1. Test Objective
The primary objective of this testing cycle was to ensure that all functional and non-functional requirements of the BookStore application were met, including:

1. Validation of catalog, cart, checkout, order tracking, and admin access.  
2. Verification of payments through Paystack sandbox mode.  
3. Ensuring accessibility and performance targets are achieved.  
4. Identification and logging of defects, with severity and priority classification.  

Testing was executed across multiple devices, browsers, and network conditions to simulate real-world usage.

---

## 2. Areas Covered

### 2.1 Functional Testing
- *User Authentication & Admin Access:* Login/logout, session handling, protected admin routes.  
- *Catalog & Search:* Browse categories, search by text/image, filters, and sorting.  
- *Shopping Cart & Checkout:* Add/remove items, subtotal calculations, Paystack payment flow.  
- *Order Tracking:* Persistent order history and CSV export functionality.

### 2.2 Non-Functional Testing
- *Accessibility (a11y):* WCAG 2.1 AA compliance, keyboard navigation, screen reader checks.  
- *Performance:* Lighthouse metrics (LCP, TTI), page load times, responsiveness.  
- *Compatibility:* Tested on Chrome, Firefox, Edge, Windows, and Ubuntu environments.  
- *Security Hygiene:* Route guards, session validation, input sanitization.  

---

## 3. Areas Not Covered
- Real Paystack server callback (sandbox only).  
- Integration with backend APIs (mocked).  
- Extended testing on devices older than 3 years.  

---

## 4. Testing Approach

### 4.1 Test Strategy
- *Risk-Based Testing:* Checkout, payments, and admin routes prioritized.  
- *Test Case Design:* Black-box and equivalence partitioning; boundary value analysis.  
- *Automation & Manual Testing Balance:* Manual execution for critical paths; optional automation scripts.  

### 4.2 Testing Process
1. *Test Planning:* Defined scope, environments, roles, and risks.  
2. *Test Execution:* Step-by-step verification of functional and non-functional requirements.  
3. *Defect Management:* Logged in tests/defect-log.md; triaged by severity/priority.  
4. *Reporting & Analysis:* Compiled evidence, analyzed results, and recommended actions.  

---

## 5. Defect Report

### 5.1 Defect Summary
| Severity Level | Number of Bugs | Bug IDs        |
| -------------- | -------------- | -------------- |
| **High**       | 1              | BUG-03         |
| **Medium**     | 2              | BUG-01, BUG-04 |
| **Low**        | 2              | BUG-02, BUG-05 |


### 5.2 Open High-Severity Defects
1. *Checkout Payment Error (TC-CHK-03-02):* Some sandbox payments fail intermittently.  
2. *Admin Route Access (FR-AUTH-05):* Route guard bypass under specific session conditions.


---

## 6. Platform Details

### 6.1 Test Environments
| Component | Details |
| --------- | ------- |
| OS        | Windows 10, Ubuntu 24.04 |
| Browser   | Chrome 130+, Firefox 125+, Edge 130+ |
| Backend   | Node.js 20.x (mocked APIs) |
| Database  | localStorage (mock) |

### 6.2 Network Conditions Tested
- High-speed Wi-Fi (100+ Mbps)  
- 4G LTE (10–20 Mbps)  
- Throttled 3G (1–2 Mbps)  
- Offline mode (data sync verification)

---

## 7. Test summary

| Cases                      | Result       |
| --------------------------- | ------------ |
| Test Cases Executed          | 20           |
| Test Cases Passed            | 15 (75%)     |
| Test Cases Failed            | 3            |
| Test Cases Pending           | 2            |
| Critical User Journeys Tested| 5/5 (100%)   |

*Observations:* Core flows pass consistently. High-severity defects require hotfix before production deployment.

---

## 8. Risk Assessment
| Risk | Impact | Mitigation |
| ---- | ------ | ---------- |
| Payment failure | High | Verify Paystack key; monitor sandbox flows |
| Admin route bypass | High | Implement additional session checks |
| LocalStorage limits | Medium | Graceful error handling and logging |
| Performance regression | Medium | Monitor LCP & TTI using Lighthouse |
| A11y non-compliance | Low | Use Axe plugin and keyboard audit |

---

## 9. Release Recommendation
- Proceed with release *after resolving high-severity defects*.  
- Implement a phased rollout: start with 10% of users to monitor issues.  
- Post-release monitoring for payments, performance, and accessibility.  

---

## 10. Post-Release Activities
1. Close monitoring of LCP, TTI, and checkout flows.  
2. Gather user feedback on accessibility and UX.  
3. Analyze logs and crash reports across browsers.  
4. Validate defect fixes once hotfixes are applied.

---
## 11. APENDIX.

1. 5 mins Video : (https://drive.google.com/file/d/19TX4oKjs9QCbHIXGtrsJLmVtDc26sO-A/view?usp=sharing)
2. Test cases : (https://github.com/PLP-Database-Design/wk-6-1-Cherubismark/blob/main/docs/Testing/Test_Cases.md)
3. Evidence/screenshots : (https://github.com/PLP-Database-Design/wk-6-1-Cherubismark/tree/main/docs/Testing/evidence/screenshots)
4. Defect log : (https://github.com/PLP-Database-Design/wk-6-1-Cherubismark/blob/main/docs/Testing/Defect_Log.md)
5. Test plan : (https://github.com/PLP-Database-Design/wk-6-1-Cherubismark/blob/main/docs/Testing/Test_Plan.md)
6. Automation/Selenium : (https://github.com/PLP-Database-Design/wk-6-1-Cherubismark/blob/main/docs/Testing/selenium_python.py)
7. Project Board/ Trello : (https://trello.com/invite/b/6909c8aede29d1fd8dca980b/ATTI5a567bb75b5e43570e5bd14960088f9881BA4206/bookstore-qa-project)

   
---

## 12. Approvals
| Role             | Name             | Date       | Approval Notes |
| ---------------- | ---------------- | ---------- | -------------- |
| QA Lead          | Dominic Kirui    | Nov 20, 2025 | Approves release with pending high-severity fixes |
| Development Lead | Bismark Koskei   | Nov 20, 2025 | Confirms core functionality complete |
| Risk analyst lead    | Gilbert Keter    | Nov 20, 2025 | Accepts risks and business value of release |

---

*End of Report*
