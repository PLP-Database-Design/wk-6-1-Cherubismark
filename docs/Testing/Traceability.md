# Traceability Matrix – TNNP Bookstore App

| Requirement / Feature | FR Code | Test Case ID | Unit Test ID | Defect ID | React Component | Status | Responsible |
|----------------------|---------|-------------|--------------|----------|----------------|--------|------------|
| Homepage loads | FR-O01 | TC01 | UT01 | - | Homepage | Pass | Bismark |
| Catalog displays books | FR-O01 | TC02 | UT07, UT08 | - | Catalog | Pass | Bismark |
| Add to Cart | FR-O01 | TC03 | UT02, UT10, UT11, UT19 | BUG-01 | Cart | Pass / Fail | Bismark / Gilbert |
| Cart page shows items | FR-O01 | TC04 | UT01, UT02, UT03, UT04 | - | Cart | Pass | Bismark |
| Cart subtotal / total calculation | FR-O01 | TC05 | UT01, UT10 | BUG-01 | Cart | Pass / Fail | Bismark / Gilbert |
| Remove item from cart | FR-O01 | TC06 | UT03 | - | Cart | Pass | Bismark |
| Checkout validation | FR-O02 | TC07 | UT12 | - | CheckoutForm | Pass | Bismark |
| Paystack payment | FR-O03 | TC08 | UT09, UT18 | BUG-06 | Payment | Pass / Fail | Dominic / Gilbert |
| Order history | FR-O04 | TC09 | UT14 | - | Orders | Pass | Dominic |
| Admin add book | FR-M01 | TC10 | UT15 | - | AdminBookForm | Pass | Bismark |
| Admin update book | FR-M01 | TC11 | UT16 | - | AdminBookForm | Pass | Bismark |
| Admin dashboard restricted | FR-M01 | TC18 | UT06 | BUG-08 | AdminDashboard | Fail | Dominic |
| User login / auth | FR-O01 | TC12 | UT05 | BUG-07 | Login | Pass / Fail | Bismark |
| Invalid login | FR-O01 | TC17 | UT05 | BUG-07 | Login | Fail | Bismark |
| Search functionality | FR-O01 | TC13 | UT07 | - | SearchBar | Pass | Bismark |
| Mobile responsive design | FR-X03 | TC14 | UT20 | BUG-03 | All UI | Pass / In Progress | Dominic |
| Cart persistence | FR-O01 | TC15 | UT19 | - | Cart | Pass | Bismark |
| Checkout fails offline | FR-O03 | TC16 | UT09, UT18 | BUG-06 | Payment | Fail | Gilbert |
| Email notification | FR-N01 | TC19 | UT13 | BUG-09 | Notification | Pending | Gilbert |
| Risk log update | FR-X04 | TC20 | UT25 | BUG-10 | RiskLog | Pending | Gilbert |
