# TNNP Bookstore App – Test Scripts (Manual & Automated)

## 1. Manual Testing Steps
- Run React dev server: `npm start` or `yarn start`
- Verify key flows:
  - Homepage loads
  - Add/Remove cart items
  - Checkout form validation
  - Paystack sandbox payment
  - Search & filtering
  - Responsive layout

**Logging Defects:** Track in `Defect_Log.md` and Jira.

---

## 2. Automated Testing (Selenium / Jest)

**Tools:** Selenium WebDriver, React Testing Library, Jest

### Sample Selenium Test (Python)
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:3000/login")
driver.find_element(By.ID, "email").send_keys("test@tnnp.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
assert "dashboard" in driver.current_url
driver.quit()
