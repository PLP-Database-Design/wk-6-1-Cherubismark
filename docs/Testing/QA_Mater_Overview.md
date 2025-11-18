# TNNP Bookstore App – QA Master Overview

| FR Code | Requirement / Feature | TC ID(s) | UT ID(s) | Bug ID(s) | Status | Responsible | React Component |
|---------|----------------------|----------|----------|-----------|--------|------------|----------------|
| FR-O01 | Homepage & Catalog | TC01, TC02, TC03, TC04, TC05, TC06, TC12, TC13, TC15, TC17 | UT01, UT02, UT03, UT04, UT05, UT07, UT08, UT19, UT24 | BUG-01, BUG-02, BUG-07 | Pass / Fail | Bismark / Gilbert | Homepage, Catalog, Cart, Login, SearchBar |
| FR-O02 | Checkout Wizard & Validation | TC07 | UT09, UT12 | - | Pass / In Progress | Bismark / Gilbert | CheckoutForm |
| FR-O03 | Payments (Paystack) | TC08, TC16 | UT09, UT18 | BUG-06 | Pass / Fail | Dominic / Gilbert | Payment |
| FR-O04 | Order History | TC09 | UT14 | - | Pass | Dominic | Orders |
| FR-M01 | Admin Catalog Management | TC10, TC11, TC18 | UT15, UT16, UT17 | BUG-08 | Pass / Fail | Bismark / Dominic | AdminBookForm, AdminDashboard |
| FR-N01 | Notifications / Email | TC19 | UT13 | BUG-09 | In Progress | Gilbert | Notification |
| FR-X03 | Responsive Design | TC14 | UT20 | BUG-03, BUG-05 | Pass / In Progress | Dominic / QA Team | All UI |
| FR-X04 | Risk Log / Audit | TC20 | UT25 | BUG-10 | In Progress | Gilbert | RiskLog |

---

## Notes:
- **TC ID(s):** All test cases mapped to this requirement.  
- **UT ID(s):** All unit tests covering this requirement.  
- **Bug ID(s):** Known defects affecting this requirement.  
- **Status:** Combined view from Test Cases, Unit Tests, and Defects.  
- **Responsible:** Primary owners for testing and defect fixes.  
- **React Component:** Key component(s) involved for testing and defect tracking.  

---

### Recommendations:
- Any FR Code without a linked TC or UT indicates **missing tests**.  
- Any TC with status “Fail” or “Pending” should reference its **Bug ID**.  
- Maintain this file as a single source of truth for QA coverage.
