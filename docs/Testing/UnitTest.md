# TNNP Bookstore App – Unit Tests

| UT ID | Function / Feature | Input | Expected Output | Status | Responsible Member | React Component |
|-------|-----------------|-------|----------------|--------|------------------|----------------|
| UT01 | calculateSubtotal | Array of cart items | Correct subtotal | Pass | Bismark | Cart |
| UT02 | addItem | Cart array + item object | Item added | Pass | Bismark | Cart |
| UT03 | removeItem | Cart array + item ID | Item removed | Pass | Bismark | Cart |
| UT04 | updateQuantity | Cart array + item ID + quantity | Quantity updated | Pass | Bismark | Cart |
| UT05 | validateLogin | Username + password | true/false | Pass | Bismark | Login |
| UT06 | isAdmin | User object | true/false | Pass | Dominic | Login/Admin |
| UT07 | searchBooks | Search string | Filtered book array | Pass | Bismark | Catalog |
| UT08 | filterBooksByCategory | Category string | Filtered book array | Pass | Bismark | Catalog |
| UT09 | checkout | Cart array + user object | Success/failure | In Progress | Gilbert | Checkout |
| UT10 | calculateTax | Subtotal | Correct tax | Pass | Bismark | Cart |
| UT11 | applyDiscount | Subtotal + discount object | Discounted total | Pass | Bismark | Cart |
| UT12 | validateForm | Form object | true/false | Pass | Bismark | CheckoutForm |
| UT13 | sendOrderEmail | Order object | Success/failure | In Progress | Gilbert | Notification |
| UT14 | getOrderHistory | User ID | Array of orders | Pass | Dominic | Orders |
| UT15 | addBookAdmin | Book object | Added | Pass | Bismark | AdminBookForm |
| UT16 | updateBookAdmin | Book object | Updated | Pass | Bismark | AdminBookForm |
| UT17 | deleteBookAdmin | Book ID | Removed | Pass | Bismark | AdminBookForm |
| UT18 | checkPaymentStatus | Payment ID | Success/fail | Fail | Gilbert | Payment |
| UT19 | validateCartPersistence | None | Restored cart | Pass | Bismark | Cart |
| UT20 | validateResponsiveDesign | Screen size | Layout adjusts | In Progress | Dominic | All UI |
| UT21 | addToWishlist | Book ID | Added to wishlist | Pass | Bismark | Wishlist |
| UT22 | removeFromWishlist | Book ID | Removed from wishlist | Pass | Bismark | Wishlist |
| UT23 | calculateShipping | Cart array + address object | Correct shipping cost | Pass | Bismark | Checkout |
| UT24 | validatePaymentInput | Card info object | true/false | Pass | Gilbert | Payment |
| UT25 | logRiskAssessment | Test cycle data | Log updated | In Progress | Gilbert | QA Tools |
