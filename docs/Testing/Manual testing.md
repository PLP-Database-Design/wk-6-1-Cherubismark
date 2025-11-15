# Test Report

## 🧪 A. FUNCTIONAL TEST CASES

| TC | Objective | Steps | Expected | Status |
|----|-----------|-------|----------|--------|
| TC01 | Validate user login with valid credentials | Enter email → password → Login | Dashboard loads successfully | ✔️ Pass |
| TC02 | Ensure API retrieves items | Visit Items page | List loads | ✔️ Pass |
| TC03 | Add item using form | Fill form and submit | Item saved & shown in list | ✔️ Pass |
| TC04 | Edit item and save | Modify item → Save | Item updated | ✔️ Pass |
| TC05 | Delete selected item | Select item → Delete | Removed from list | ✔️ Pass |
| TC06 | Verify search functionality (Secondary Search) | Enter keyword → Click SECOND search button | Results filtered | ✔️ Pass |
| TC07 | Validate main search button behavior | Type keyword → Click MAIN search button | Search results display | ⚠️ FAIL |

**TC07 Details:**

- **Actual Result:** Nothing happens (no API call, no UI update)  
- **Severity:** Medium  
- **Priority:** High  
- **Evidence:** Console shows no event triggered  

---

## 🧿 B. ACCESSIBILITY TEST CASES

| TC | Objective | Expected | Status |
|----|-----------|----------|--------|
| TC08 | Keyboard Navigation | User can navigate with Tab | ✔️ Pass |
| TC09 | ARIA Labels | All interactive elements have ARIA | ✔️ Pass |

---

## 📊 C. PERFORMANCE TEST CASES

| TC | Objective | Expected | Status |
|----|-----------|----------|--------|
| TC10 | Page Load | Loads < 3s | ✔️ Pass |
| TC11 | Search Response | Response < 2s (secondary search) | ✔️ Pass |

---

## 🌐 D. COMPATIBILITY TEST CASES

| TC | Browser | Expected | Status |
|----|--------|----------|--------|
| TC12 | Chrome | Works | ✔️ Pass |
| TC13 | Firefox | Works | ✔️ Pass |
| TC14 | Edge | Works | ✔️ Pass |

---

## 🎨 E. UI VALIDATION TEST CASES

| TC | Objective | Expected | Status |
|----|-----------|----------|--------|
| TC15 | UI Alignment | Buttons, inputs aligned correctly | ✔️ Pass |
| TC16 | Visual Consistency | Colors & fonts uniform | ✔️ Pass |

---

## 🚨 SUMMARY OF STATUS

| Area | Pass | Fail |
|------|------|------|
| Functional | 6 | 1 |
| Accessibility | 2 | 0 |
| Performance | 2 | 0 |
| Compatibility | 3 | 0 |
| UI | 2 | 0 |

---

### ✅ Notes

- Only the **Main Search Button (TC07)** failed.  
- Evidence is available in console logs.  
- Next steps: Full defect report or developer assignment recommended.
