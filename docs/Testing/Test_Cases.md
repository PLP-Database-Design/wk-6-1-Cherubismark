# TNNP Bookstore App – Test Cases

| TC ID | Description | Steps | Expected Result | Status | Responsible | FR Code | React Component |
|-------|-------------|-------|----------------|--------|------------|---------|----------------|
| TC01 | Homepage loads | Open `/` | Book catalog displays | Pass | Bismark | FR-O01 | Homepage |
| TC02 | Catalog displays books | Navigate to `/catalog` | All books listed | Pass | Bismark | FR-O01 | Catalog |
| TC03 | Add to Cart | Click "Add to Cart" | Cart count & subtotal update | Pass | Bismark | FR-O01 | Cart |
| TC04 | Cart page shows items | Go to `/cart` | Items appear | Pass | Bismark | FR-O01 | Cart |
| TC05 | Total price calculation | Add 2 books | Sum equals total | Pass | Bismark | FR-O01 | Cart |
| TC06 | Remove item | Remove book from cart | Item disappears, total updates | Pass | Bismark | FR-O01 | Cart |
| TC07 | Checkout validation | Leave form empty | Validation error shown | Pass | Bismark | FR-O02 | CheckoutForm |
| TC08 | Paystack payment | Checkout with valid info | Payment success | Pass | Dominic | FR-O03 | Payment |
| TC09 | Order history | Complete checkout, visit `/orders/:id` | New order appears | Pass | Dominic | FR-O04 | Orders |
| TC10 | Admin add book | Login as admin, add book | New book visible | Pass | Bismark | FR-M01 | AdminBookForm |
| TC11 | Admin update book | Edit book | Changes saved | Pass | Bismark | FR-M01 | AdminBookForm |
| TC12 | User login | Enter valid credentials | Dashboard loads | Pass | Bismark | FR-O01 | Login |
| TC13 | Search functionality | Search title | Relevant results | Pass | Bismark | FR-O01 | SearchBar |
| TC14 | Mobile responsive | Open on small screen | Layout adjusts | Pass | Dominic | FR-X03 | All UI |
| TC15 | Cart persistence | Refresh page | Items remain | Pass | Bismark | FR-O01 | Cart |
| TC16 | Checkout fails offline | Disconnect internet | Error displayed | Fail | Gilbert | FR-O03 | Payment |
| TC17 | Invalid login | Wrong credentials | Error message | Fail | Bismark | FR-O01 | Login |
| TC18 | Admin dashboard restricted | Non-admin access `/admin` | Unauthorized error | Fail | Dominic | FR-M01 | AdminDashboard |
| TC19 | Email notification | Place order | Email received | Pending | Gilbert | FR-N01 | Notification |
| TC20 | Risk log update | After test cycle | Log updated | Pending | Gilbert | FR-X04 | RiskLog |

**Summary:** 20 Cases – Pass 15, Fail 3, Pending 2
