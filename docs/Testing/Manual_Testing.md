# Manual Testing – TNNP Bookstore App

## A. Functional Tests

| TC | Objective | Steps | Expected | Status |
|----|-----------|-------|---------|--------|
| TC01 | Login | Enter email & password | Dashboard loads | Pass |
| TC02 | API retrieves items | Open Items page | List loads | Pass |
| TC03 | Add item | Fill form | Item saved & visible | Pass |
| TC04 | Edit item | Modify → Save | Updated | Pass |
| TC05 | Delete item | Select → Delete | Removed | Pass |
| TC06 | Search (secondary) | Enter keyword | Results filtered | Pass |
| TC07 | Main search button | Type → click | Results display | Fail |

**Notes:** Only TC07 failed. Evidence in console.

## B. Accessibility Tests

| TC | Objective | Expected | Status |
|----|-----------|---------|--------|
| TC08 | Keyboard nav | Navigate via Tab | Pass |
| TC09 | ARIA labels | All interactive elements labeled | Pass |

## C. Performance Tests

| TC | Objective | Expected | Status |
|----|-----------|---------|--------|
| TC10 | Page load | < 3s | Pass |
| TC11 | Search response | < 2s | Pass |

## D. Compatibility Tests

| TC | Browser | Expected | Status |
|----|--------|---------|--------|
| TC12 | Chrome | Works | Pass |
| TC13 | Firefox | Works | Pass |
| TC14 | Edge | Works | Pass |

## E. UI Validation

| TC | Objective | Expected | Status |
|----|-----------|---------|--------|
| TC15 | Alignment | Buttons, inputs aligned | Pass |
| TC16 | Visual consistency | Colors & fonts uniform | Pass |
