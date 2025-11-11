🧪 Test Cases — Book Store App
1. Catalog & Search
ID	Title	Preconditions	Steps	Expected Result	Postconditions	Evidence
TC-CAT-01	Search books using catalog search bar	Catalog page loaded with books	1. Navigate to /catalog
2. Enter a keyword in catalog search
3. Press Enter	Filtered list of books matching keyword appears	Search results displayed dynamically	screenshot/catalog_search_pass.png
TC-CAT-02	Search books using Navbar search bar	App loaded, Navbar visible	1. Use the top Navbar search bar
2. Enter a valid book title
3. Press Enter	List of books matching title should appear	None	screenshot/navbar_search_fail.png
TC-CAT-03	Verify search is case-insensitive	Catalog page loaded	1. Type “HARRY POTTER”
2. Observe results	Books titled “Harry Potter” should appear regardless of case	N/A	screenshot/search_case_pass.png
2. Cart Functionality
ID	Title	Preconditions	Steps	Expected Result	Postconditions	Evidence
TC-CART-01	Add book to cart	Book catalog displayed	1. Click “Buy Now” on a book
2. Open /cart	The selected book appears in the cart with correct title and price	Cart updated in localStorage	screenshot/add_to_cart_pass.png
TC-CART-02	Update quantity in cart	Cart contains at least 1 item	1. Change quantity from 1 → 2
2. Observe subtotal	Subtotal updates correctly	Cart total recalculated	screenshot/cart_update_pass.png
TC-CART-03	Remove item from cart	Cart contains at least 1 item	1. Click “Remove” button
2. Confirm	Book is removed from cart	Cart item count decreases	screenshot/remove_cart_pass.png
3. Checkout
ID	Title	Preconditions	Steps	Expected Result	Postconditions	Evidence
TC-CHK-01	Proceed to checkout	Cart has items	1. Click “Checkout”
2. Observe navigation	Redirects to /checkout	Checkout page loads	screenshot/checkout_nav_pass.png
TC-CHK-02	Simulate Paystack test payment	Checkout form filled, test Paystack key configured	1. Click “Pay with Paystack”
2. Enter test card details	Mock payment success message	Order stored in localStorage	screenshot/paystack_mock_pass.png
4. Admin Access
ID	Title	Preconditions	Steps	Expected Result	Postconditions	Evidence
TC-AUTH-01	Access admin route as normal user	User logged in (non-admin)	1. Navigate to /admin	“Unauthorized Access” message displayed	None	screenshot/admin_unauthorized_pass.png
TC-AUTH-02	Access admin route with admin role	localStorage.app.user.role = admin	1. Navigate to /admin	Admin console loads successfully	Admin panel accessible	screenshot/admin_access_pass.png
5. Accessibility & Performance
ID	Title	Preconditions	Steps	Expected Result	Postconditions	Evidence
TC-A11Y-01	Check keyboard accessibility for Navbar	App running	1. Press Tab to navigate links
2. Press Enter on a menu item	Focus outline visible, navigation works	None	screenshot/a11y_tab_pass.png
TC-PERF-01	Measure LCP and TTI	App running locally	1. Open Lighthouse
2. Run audit	LCP ≤ 2.5s, TTI ≤ 1s	None	lighthouse_report.png

✅ Notes:
