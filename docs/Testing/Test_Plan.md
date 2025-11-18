# TNNP Bookstore App – Test Plan

## 1. Test Plan Overview
**Purpose:** Ensure the TNNP Bookstore App functions correctly, meets requirements, and provides smooth user experience.  
**Scope:** Functional, accessibility, performance, compatibility, and UI validation.  
**Objectives:**  
- Verify all features work as intended.  
- Identify and report defects.  
- Validate app performance and usability across platforms.

---

## 2. Features to be Tested
| Feature | Description | React Notes |
|---------|-------------|------------|
| Homepage | Displays book catalog correctly, responsive layout | Check component rendering, props passed correctly |
| Add to Cart | Updates subtotal and count | Validate state updates and `localStorage` persistence |
| Checkout | Completes transactions using Paystack sandbox | Form validation and API call success |
| Accessibility | ARIA labels, alt text, keyboard navigation | Test React component accessibility props |
| Performance | Page load speed, cart update speed | Lighthouse and component render performance |
| Compatibility | Works on Chrome, Edge, Firefox, mobile browsers | Test responsive components |
| UI Validation | Header/footer consistency, buttons/icons | Visual check of React components |

---

## 3. Features Not to be Tested
- Payment in live environment (sandbox only)  
- Backend database security  
- External integrations not yet implemented  

---

## 4. Test Approach
- **Manual Testing:** Verify UI elements, navigation, and workflows in React dev server.  
- **Automated Testing:** Use Selenium, Jest, or React Testing Library for repetitive functions.  
- **Exploratory Testing:** Edge cases, unusual inputs, layout issues.

---

## 5. Test Environment
- **Browsers:** Chrome, Firefox, Edge  
- **Devices:** Desktop, Android phones  
- **Tools:** VS Code, Lighthouse, DevTools, Postman (if needed), React dev server

---

## 6. Entry Criteria
- App running locally (`npm start` or `yarn start`)  
- Test data ready (books, user accounts)  
- QA checklist prepared  

---

## 7. Exit Criteria
- All planned test cases executed  
- Critical defects resolved or documented  
- Test results reviewed

---

## 8. Test Deliverables
- Test cases and checklist  
- Manual/automated test scripts  
- Defect log  
- Test execution report  
- Trello tasks or Jira tickets

---

## 9. Roles and Responsibilities
| Role | Responsibility |
|------|----------------|
| Project Manager | Dominic Kirui |
| Risk Analyst | Gilbert Keter |
| Test Executor | Bismark Cheruiyot |
| Team Members | Update Trello/Jira, review checklist |

---

## 10. Risks and Mitigation
| Risk | Mitigation |
|------|-----------|
| Delayed bug fixes | Prioritize critical defects, track in Jira |
| Environment issues | Use local server for testing |
| Missing test data | Prepare dummy accounts and sample catalog |
