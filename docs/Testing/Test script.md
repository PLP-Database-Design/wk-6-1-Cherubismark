# 🧪 Combined Manual & Automated Testing Guide – TNNP Bookstore App

## 📖 1. Introduction
This document describes how both **manual** and **automated testing** are performed for the **TNNP Bookstore App** to ensure functionality, reliability, and user experience quality.

Testing focuses on validating key user flows: browsing books, adding to cart, performing checkout, and verifying accessibility.

---

## 🧠 2. Testing Objectives
- Verify that all features function as expected.  
- Detect and log functional, UI, and accessibility defects early.  
- Use automation for repetitive and regression test cases.  
- Improve app quality before deployment.

---

## 🧩 3. Manual Testing Process

### 🥇 Step 1: Review Requirements
Understand expected system behavior:
- Homepage loads book catalog
- User can log in / sign up
- Add to Cart and Checkout function correctly
- Paystack sandbox integration works
- Responsive layout and accessibility compliance

---

### 🧾 Step 2: Prepare and Execute Test Cases

| **Test Case ID** | **Scenario** | **Steps** | **Expected Result** | **Status** |
|------------------|--------------|------------|----------------------|-------------|
| TC01 | Verify homepage loads book catalog | 1. Open app in Chrome<br>2. Observe book list | All book cards display correctly | ✅ Pass |
| TC02 | Verify Add to Cart functionality | 1. Click “Add to Cart” on any book<br>2. Check subtotal | Cart count and subtotal update instantly | ❌ Fail (Subtotal updates after refresh) |
| TC03 | Verify checkout with sandbox Paystack key | 1. Add item to cart<br>2. Proceed to checkout<br>3. Enter dummy payment info | Payment confirmation message displays | ⏳ Pending |
| TC04 | Verify login with valid credentials | 1. Enter valid email & password<br>2. Click Login | Redirects to dashboard | ✅ Pass |
| TC05 | Verify mobile responsiveness | 1. Open in Chrome DevTools (iPhone X)<br>2. Check layout | Layout adjusts, no overlap | ❌ Fail (Overlapping text) |

---

### 🧾 Step 3: Log and Track Defects

| **Defect ID** | **Summary** | **Steps to Reproduce** | **Expected Result** | **Actual Result** | **Severity** | **Status** |
|----------------|-------------|------------------------|---------------------|-------------------|---------------|-------------|
| BUG-01 | Cart subtotal updates only after refresh | 1. Add book to cart<br>2. Check subtotal | Subtotal updates instantly | Updates after refresh | Medium | Open |
| BUG-02 | “Add to Cart” missing ARIA label | Run accessibility scan | Button has label | Label missing | Low | Open |
| BUG-03 | Text overlaps on mobile view | Resize window | Layout adjusts | Overlap occurs | Medium | Open |

---

### 🧰 Step 4: Retesting and Reporting
- Re-run failed cases after fixes.  
- Update **Defect Log** in Jira or Excel.  
- Prepare a **Test Execution Report** summarizing results.

**Sample Summary:**
| **Metric** | **Count** |
|-------------|-----------|
| Total Test Cases | 20 |
| Passed | 15 |
| Failed | 3 |
| Pending | 2 |

---

## 🤖 5. Automated Testing Process (Selenium)

### 🧪 Tools Used
- **Framework:** Selenium WebDriver  
- **Language:** Python / Java (depending on project)  
- **Accessibility Testing:** axe-core, Lighthouse  
- **Execution Environment:** Localhost server or dev server  

---

### 💻 Sample Selenium Automated Test Scripts

#### **Script 1: Verify Login Flow (Python)**
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
driver = webdriver.Chrome()
driver.get("http://localhost:3000")

driver.find_element(By.ID, "search").send_keys("React")
driver.find_element(By.ID, "searchBtn").click()
assert "React" in driver.page_source
driver.quit()
| **Category**       | **Type**          | **Tools Used**       | **Status**     | **Remarks**          |
| ------------------ | ----------------- | -------------------- | -------------- | -------------------- |
| Functional Testing | Manual + Selenium | Selenium, Chrome     | 🟡 In Progress | Some bugs open       |
| Accessibility      | Automated         | axe-core, Lighthouse | ❌ Fail         | Missing ARIA label   |
| Performance        | Automated         | Lighthouse           | ✅ Pass         | Avg load time 2.5s   |
| Compatibility      | Manual            | Chrome, Android      | ⏳ Pending      | Awaiting mobile test |
| UI Validation      | Manual            | Visual check         | ✅ Pass         | Matches design       |
