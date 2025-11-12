| **Test ID**    | **Feature**    | **Test Case Description**                        | **Preconditions**              | **Test Steps**                                                        | **Expected Result**                       | **Actual Result**         | **Status (Pass/Fail)** | **Evidence / Notes**                       |
| -------------- | -------------- | ------------------------------------------------ | ------------------------------ | --------------------------------------------------------------------- | ----------------------------------------- | ------------------------- | ---------------------- | ------------------------------------------ |
| **TC-CAT-01**  | Search         | Verify catalog search bar filters books by title | Catalog page loaded with books | 1. Open `/catalog` <br> 2. Type a book name <br> 3. Press Enter       | Display only books matching keyword       | As expected               | ✅ Pass                 | Screenshot: `catalog_search.png`           |
| **TC-CAT-02**  | Search         | Verify Navbar search bar filters books           | Application home page loaded   | 1. Use Navbar search bar <br> 2. Enter book title <br> 3. Press Enter | Filtered results appear                   | Search bar not responding | ❌ Fail                 | Bug logged: *Navbar search not functional* |
| **TC-CAT-03**  | Search         | Verify search is case-insensitive                | Catalog loaded                 | 1. Enter keyword “Kill” in search <br> 2. Observe results             | Books titled “To kill a mockingbird” appear        | As expected               | ✅ Pass                 | Screenshot: `case_insensitive.png`         |
| **TC-CART-01** | Shopping Cart  | Verify adding a book to cart                     | Catalog visible                | 1. Click “Add to Cart” on a book <br> 2. Open `/cart`                 | Book appears in cart with correct details | As expected               | ✅ Pass                 | Screenshot: `add_to_cart.png`              |
| **TC-CART-02** | Shopping Cart  | Verify updating quantity updates total           | Cart has items                 | 1. Change quantity from 1 to 2 <br> 2. Observe total                  | Total updates accordingly                 | As expected               | ✅ Pass                 | Screenshot: `cart_update.png`              |
| **TC-CART-03** | Shopping Cart  | Verify removing an item updates cart             | Cart contains 1+ items         | 1. Click “Remove” <br> 2. Confirm action                              | Item disappears from cart                 | As expected               | ✅ Pass                 | Screenshot: `remove_cart.png`              |
| **TC-CHK-01**  | Checkout       | Verify checkout button navigates correctly       | Cart not empty                 | 1. Click “Checkout” <br> 2. Observe navigation                        | Redirects to `/checkout`                  | As expected               | ✅ Pass                 | Screenshot: `checkout_nav.png`             |
| **TC-CHK-02**  | Checkout       | Verify test payment via Paystack works           | Checkout form filled           | 1. Click “Pay with Paystack” <br> 2. Use test card                    | Payment success displayed                 | As expected               | ✅ Pass                 | Screenshot: `paystack_success.png`         |
| **TC-AUTH-01** | Authentication | Verify unauthorized user cannot access admin     | Logged in as normal user       | 1. Go to `/admin`                                                     | Access denied message shown               | As expected               | ✅ Pass                 | Screenshot: `unauthorized_admin.png`       |
| **TC-AUTH-02** | Authentication | Verify admin access granted for admin users      | Logged in as admin             | 1. Go to `/admin`                                                     | Admin dashboard loads                     | As expected               | ✅ Pass                 | Screenshot: `admin_access.png`             |
| **TC-A11Y-01** | Accessibility  | Verify keyboard navigation works                 | App running                    | 1. Press `Tab` to move across links <br> 2. Press `Enter`             | Focus visible, navigation works           | As expected               | ✅ Pass                 | Screenshot: `keyboard_nav.png`             |
| **TC-PERF-01** | Performance    | Verify page load performance (Lighthouse)        | App running                    | 1. Run Lighthouse audit                                               | LCP ≤ 2.5s, TTI ≤ 1s                      | As expected               | ✅ Pass                 | Lighthouse report attached                 |



| **TC ID** | **Test Case Description** | **Test Steps** | **Expected Result** | **Status** |
|------------|---------------------------|----------------|---------------------|-------------|
| TC01 | Verify the homepage loads correctly | Open `/` in browser | Homepage displays book catalog | ✅ Passed |
| TC02 | Verify catalog displays all books from database | Navigate to `/catalog` | All available books are listed | ✅ Passed |
| TC03 | Verify “Add to Cart” button adds item to cart | Click "Add to Cart" on any book | Item count in cart increases | ✅ Passed |
| TC04 | Verify cart page displays added items | Go to `/cart` | Added items appear in cart list | ✅ Passed |
| TC05 | Verify total price calculation in cart | Add 2 different books | Total equals sum of prices | ✅ Passed |
| TC06 | Verify “Remove from Cart” button removes an item | Remove a book from cart | Item disappears, total updates | ✅ Passed |
| TC07 | Verify checkout form validation | Leave form fields empty | Validation error shown | ✅ Passed |
| TC08 | Verify successful Paystack payment integration | Checkout with valid payment | Payment processed, success message displayed | ✅ Passed |
| TC09 | Verify order appears in order history | Complete checkout, visit `/orders/:id` | New order appears in list | ✅ Passed |
| TC10 | Verify admin can add a new book | Login as admin, add book | New book appears in catalog | ✅ Passed |
| TC11 | Verify admin can update book details | Edit existing book info | Changes saved and visible | ✅ Passed |
| TC12 | Verify user authentication (login) | Enter valid credentials | Redirects to user dashboard | ✅ Passed |
| TC13 | Verify search functionality works | Search by book title | Relevant results displayed | ✅ Passed |
| TC14 | Verify responsive design on mobile | Open app on small screen | Layout adjusts correctly | ✅ Passed |
| TC15 | Verify app retains cart items after page refresh | Add items, refresh page | Cart items persist (localStorage) | ✅ Passed |
| TC16 | Verify checkout fails when payment gateway is offline | Disconnect internet, attempt payment | Error message displayed | ❌ Failed |
| TC17 | Verify invalid user credentials show error | Enter wrong password | Error message appears | ❌ Failed |
| TC18 | Verify admin dashboard access restricted to admin users | Login as normal user, access `/admin` | Unauthorized access error shown | ❌ Failed |
| TC19 | Verify email notification sent on successful order | Place an order | Email received in inbox | ⏳ Pending |
| TC20 | Verify risk assessment log updates after each test cycle | Review risk log after testing | Log file updates with latest status | ⏳ Pending |
