| **TC ID** | **Test Case Description** | **Test Steps** | **Expected Result** | **Status** | **Responsible Member** |
|------------|---------------------------|----------------|---------------------|-------------|-------------------------|
| TC01 | Verify the homepage loads correctly | Open `/` in browser | Homepage displays book catalog | ✅ Passed | Bismark |
| TC02 | Verify catalog displays all books from database | Navigate to `/catalog` | All available books are listed | ✅ Passed | Bismark |
| TC03 | Verify “Add to Cart” button adds item to cart | Click "Add to Cart" on any book | Item count in cart increases | ✅ Passed | Bismark |
| TC04 | Verify cart page displays added items | Go to `/cart` | Added items appear in cart list | ✅ Passed | Bismark |
| TC05 | Verify total price calculation in cart | Add 2 different books | Total equals sum of prices | ✅ Passed | Bismark |
| TC06 | Verify “Remove from Cart” button removes an item | Remove a book from cart | Item disappears, total updates | ✅ Passed | Bismark |
| TC07 | Verify checkout form validation | Leave form fields empty | Validation error shown | ✅ Passed | Bismark |
| TC08 | Verify successful Paystack payment integration | Checkout with valid payment | Payment processed, success message displayed | ✅ Passed | Dominic |
| TC09 | Verify order appears in order history | Complete checkout, visit `/orders/:id` | New order appears in list | ✅ Passed | Dominic |
| TC10 | Verify admin can add a new book | Login as admin, add book | New book appears in catalog | ✅ Passed | Bismark |
| TC11 | Verify admin can update book details | Edit existing book info | Changes saved and visible | ✅ Passed | Bismark |
| TC12 | Verify user authentication (login) | Enter valid credentials | Redirects to user dashboard | ✅ Passed | Bismark |
| TC13 | Verify search functionality works | Search by book title | Relevant results displayed | ✅ Passed | Bismark |
| TC14 | Verify responsive design on mobile | Open app on small screen | Layout adjusts correctly | ✅ Passed | Dominic |
| TC15 | Verify app retains cart items after page refresh | Add items, refresh page | Cart items persist (localStorage) | ✅ Passed | Bismark |
| TC16 | Verify checkout fails when payment gateway is offline | Disconnect internet, attempt payment | Error message displayed | ❌ Failed | Gilbert |
| TC17 | Verify invalid user credentials show error | Enter wrong password | Error message appears | ❌ Failed | Bismark |
| TC18 | Verify admin dashboard access restricted to admin users | Login as normal user, access `/admin` | Unauthorized access error shown | ❌ Failed | Dominic |
| TC19 | Verify email notification sent on successful order | Place an order | Email received in inbox | ⏳ Pending | Gilbert |
| TC20 | Verify risk assessment log updates after each test cycle | Review risk log after testing | Log file updates with latest status | ⏳ Pending | Gilbert |



✅ Summary:

Total Cases: 20

Passed: 15

Failed: 3

Pending: 2

