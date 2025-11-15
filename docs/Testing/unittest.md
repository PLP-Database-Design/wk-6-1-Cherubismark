| *UT ID* | *Function / Feature* | *Description* | *Input* | *Expected Output* | *Status* | *Responsible Member* |
|-----------|-----------------------|-----------------|-----------|-------------------|------------|-----------------------|
| UT01 | calculateSubtotal | Calculates total cart amount | Array of cart items | Correct subtotal | ✅ Pass | Bismark |
| UT02 | addItem | Adds a new item to cart | Cart array + item | Item added to cart | ✅ Pass | Bismark |
| UT03 | removeItem | Removes item from cart | Cart array + item ID | Item removed | ✅ Pass | Bismark |
| UT04 | updateQuantity | Updates quantity of a cart item | Cart array + ID + qty | Quantity updated | ✅ Pass | Bismark |
| UT05 | validateLogin | Checks valid credentials | username + password | true/false | ✅ Pass | Bismark |
| UT06 | isAdmin | Checks if user is admin | user object | true/false | ✅ Pass | Dominic |
| UT07 | searchBooks | Filters catalog by title | search string | filtered array | ✅ Pass | Bismark |
| UT08 | filterBooksByCategory | Filters catalog by category | category string | filtered array | ✅ Pass | Bismark |
| UT09 | checkout | Processes order checkout | cart array + user | success/failure | 🔄 In Progress | Gilbert |
| UT10 | calculateTax | Calculates tax for order | subtotal | correct tax | ✅ Pass | Bismark |
| UT11 | applyDiscount | Applies discount to order | subtotal + discount | discounted total | ✅ Pass | Bismark |
| UT12 | validateForm | Checks form fields for empty/invalid | form object | true/false | ✅ Pass | Bismark |
| UT13 | sendOrderEmail | Sends email confirmation | order object | success/failure | 🔄 In Progress | Gilbert |
| UT14 | getOrderHistory | Returns user orders | user ID | array of orders | ✅ Pass | Dominic |
| UT15 | addBookAdmin | Adds new book to catalog | book object | book added | ✅ Pass | Bismark |
| UT16 | updateBookAdmin | Updates book info | book object | info updated | ✅ Pass | Bismark |
| UT17 | deleteBookAdmin | Deletes book from catalog | book ID | book removed | ✅ Pass | Bismark |
| UT18 | checkPaymentStatus | Verifies Paystack payment | payment ID | success/fail | ❌ Fail | Gilbert |
| UT19 | validateCartPersistence | Checks cart persistence in localStorage | none | cart restored | ✅ Pass | Bismark |
| UT20 | validateResponsiveDesign | Verifies UI on mobile/tablet | screen size | layout adjusts | 🔄 In Progress | Dominic |
| UT21 | addToWishlist | Adds book to wishlist | book ID | book added | ✅ Pass | Bismark |
| UT22 | removeFromWishlist | Removes book from wishlist | book ID | book removed | ✅ Pass | Bismark |
| UT23 | calculateShipping | Calculates shipping cost | address + cart | correct shipping | ✅ Pass | Bismark |
| UT24 | validatePaymentInput | Checks card info format | card info object | true/false | ✅ Pass | Gilbert |
| UT25 | logRiskAssessment | Updates risk log file | test cycle data | log updated | 🔄 In Progress | Gilbert |
