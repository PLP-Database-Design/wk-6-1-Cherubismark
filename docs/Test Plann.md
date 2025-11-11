# TNNP Bookstore App – Test Plan 



## 1. Test Plan Overview
**Purpose:** Ensure the TNNP Bookstore App functions correctly, meets requirements, and provides a smooth user experience.  
**Scope:** Functional testing, accessibility, performance, compatibility, and UI validation.  
**Objectives:**  
1. Verify all features work as intended.  
2. Identify defects and report them.  
3. Validate app performance and usability across platforms.  

---

## 2. Features to be Tested
| Feature | Description |
|---------|-------------|
| Homepage | Displays book catalog correctly, responsive layout |
| Add to Cart | Updates subtotal and count correctly |
| Checkout | Completes transactions using Paystack sandbox key |
| Accessibility | ARIA labels, alt text, keyboard navigation |
| Performance | Page load speed, cart update speed, Lighthouse score |
| Compatibility | Works on Chrome, Android browsers, mobile responsive layout |
| UI Validation | Header/footer consistency, button/icon alignment, error messages |

---

## 3. Features Not to be Tested
- Payment in live environment (sandbox only for testing)  
- Backend database security (covered in future phases)  
- External integrations not yet implemented  

---

## 4. Test Approach
- **Manual Testing:** Verify UI elements, navigation, and workflow.  
- **Automated Testing (if available):** Run scripts to test repetitive functions such as add/remove cart items.  
- **Exploratory Testing:** Check edge cases, unusual inputs, and layout issues.  

---

## 5. Test Environment
- **Browsers:** Chrome (Windows 10), Firfox, edge  
- **Devices:** Desktop, Android phones  
- **Tools:** VS Code, Lighthouse, Browser DevTools, Postman (if needed)  

---

## 6. Entry Criteria
- App deployed locally and running  
- Test data ready (books catalog, sample user accounts)  
- QA checklist created  

---

## 7. Exit Criteria
- All planned test cases executed  
- All critical/high defects resolved or documented  
- Test results reviewed and approved  

---

## 8. Test Deliverables
- Test cases and checklist (condensed version)  
- Early manual/automated test scripts  
- Initial defect log  
- Test execution report  
- Trello tasks  

---

## 9. Roles and Responsibilities
| Role | Responsibility |
|------|----------------| 
| Name              | Role            |
| **Dominic Kirui** | Project Manager |
| **Gilbert Keter** | Risk Analyst    |
| **Bismark Koskei**| Test Executor   |
| Team Members | Update Trello, review checklist and scoring |

---

## 10. Risks and Mitigation
| Risk | Mitigation |
|------|-----------|
| Delayed bug fixes | Prioritize critical defects, track in Jira |
| Environment issues | Use local server for testing |
| Missing test data | Prepare dummy accounts and sample catalog |
