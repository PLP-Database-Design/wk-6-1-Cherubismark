# 📤 Submission Guidelines — Book Store App QA Project

## Team members and their roles    
| Name              | Role            |
| ----------------- | --------------- |
| **Dominic Kirui** | Project Manager |
| **Gilbert Keter** | Risk Analyst    |
| **Bismark Koskei**       | Test Executor   |



## 📦 Weekly Submissions
All groups submit the full repository weekly for continuous progress and feedback.

### Week 1: Initial Setup & Planning (Due: Wednesday, Nov 5, 2025)
- Repo runs locally (`npm install`, `npm start`)
- Project board (https://trello.com/invite/b/6909c8aede29d1fd8dca980b/ATTI5a567bb75b5e43570e5bd14960088f9881BA4206/bookstore-qa-project) created and shared.
- `tests/test-plan.md` (use template below)
- Team roles and communication plan
# Communication Plan
- WhatsApp group for daily updates
- Weekly Google Meet for progress review

### Week 2: Test Design & Early Execution (Due: Tuesday, Nov 11, 2025)
- Draft test cases/checklists in `tests/test-cases.md` (use template below)
- Early manual/automated scripts (optional)
- Initial defect log in `tests/defect-log.md` (use format below)

### Week 3: Test Execution & Reporting (Due: Tuesday, Nov 18, 2025)
- Executed results (manual/automated) with evidence
- Updated defect log with severity/priority and attachments
- Screenshots/videos/logs of key issues

## 🏁 Final Submission (Due: Tuesday, Nov 18, 2025)
- `tests/final-report.md` (executive summary, approach, environment, results, defect analysis, risks, recommendations)
- Jira/Project exports or screenshots (board, filters, dashboards)
- All code and documentation committed
- 5-minute video presentation link (see `docs/video-guide.md`)

## 🧩 Templates
### 📝 Test Plan (tests/test-plan.md)
- Objective and Scope
       1.  Ensure all core functionalities (catalog, user accounts, cart, checkout, inventory, order tracking) meet functional and non-functional requirements.
       2. Detect and resolve defects before release.
        3. Confirm usability, performance, and security under expected workloads.
- In-Scope Features (map to FR codes)

|Code        |Feature         |Description                        |
| ---------- | -------------- | --------------------------------- |
| FR-CAT-01  | Catalog        | Display, filter, search for books |
| FR-CART-02 | Cart           | Add/update/remove items; subtotal |
| FR-CHK-03  | Checkout       | Payment via Paystack              |
| FR-ORD-04  | Order Tracking | Persistent order history          |
| FR-AUTH-05 | Admin Access   | Guarded admin route               |


- Out-of-Scope
1. Backend API integration (mocked for testing)
2. Real Paystack verification server callback

- Environments (browsers/devices, throttling)
  
| Component     | Details                                              |
| ------------- | ---------------------------------------------------- |
| **OS**        | Windows 10 / Ubuntu 24.04                            |
| **Browser**   | Chrome 130+, Firefox 125+, Edge 130+                 |
| **Backend**   | Node.js 20.x                                         |
| **Database**  | Mock (localStorage)                                  |
| **Tools**     | Postman, Selenium, Jest, Lighthouse, Chrome DevTools |
| **Test Data** | 50 sample books, 3 test users, Paystack test cards   |

 
- Tools (extensions, screen readers)
1. Chrome DevTools
2. Lighthouse
3. Axe Accessibility plugin

- Risks and Mitigations
  
| Risk                      | Impact | Mitigation                                           |
| ------------------------- | ------ | ---------------------------------------------------- |
| Checkout payment failure  | High   | Validate `.env` Paystack key and use sandbox mode    |
| localStorage quota        | Medium | Graceful fallback test and error logging             |
| Unauthorized admin access | High   | Verify route guard and test invalid session behavior |
| Performance regression    | Medium | Monitor LCP & TTI via Lighthouse                     |
| A11y non-compliance       | Low    | Use keyboard + aria-label audit                      |


- Test Types (functional, a11y, perf, compatibility, hygiene)
 1. Functional
2. Accessibility
3. Performance
4. compatibility
5. UI validation

- Entry/Exit Criteria
1. Entry: App deploys locally; all major features reachable.
2. Exit: ≥ 90% test cases passed; all critical defects resolved.

### ✅ Test Case (tests/test-cases.md)
- ID: TC-<area>-<number>
- Title: Concise scenario name
- Pre-conditions: State, user role, data
- Steps:
  1. 
  2. …
- Expected Result: Observable outcomes (UI text, URL, ARIA, network where applicable)
- Post-conditions: State changes
- Evidence: Screenshot/gif paths

| ID             | Feature      | Test Case Title                        | Precondition                | Steps                                                                    | Expected Result                                           | Status                   |
| -------------- | ------------ | -------------------------------------- | --------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------- | ------------------------ |
| *TC-CAT-01*  | Catalog      | Verify catalog displays all books      | App is running, books exist | 1. Navigate to /catalog <br> 2. Observe book list                      | All 6 books visible with title, author, price           | ✅ Pass                   |
| *TC-CAT-02*  | Search       | Validate search returns relevant books | Catalog loaded              | 1. Search "kill"  2. Press Enter                                    | Books with "kill" in title/author appear                 | ✅ Pass                   |
| *TC-CART-02* | Cart         | Update quantity                        | Book added to cart          | 1. Increase quantity to 2 <br> 2. Verify subtotal                        | Subtotal updates correctly                                |  ✅ 
Pass                |


### 🐞 Bug Report (defect log entry)


| ID          | Summary                                          | Severity / Priority | Environment              | Affected FR(s) | Steps to Reproduce                                                                                      | Expected Result                                 | Actual Result                         |  
| ----------- | ------------------------------------------------ | ------------------- | ------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ------------------------------------- |

|BUG-CHK-01   | Checkout fails if Paystack key missing  | Critical / High | Chrome 130+, Windows 10  | FR-CHK-03      | 1. Go to `/checkout`  2. Attempt payment with empty `.env` key                                           | App shows error message and prevents submission |
|BUG-CAT-01  | Search finds partial matches                   | Minor / Medium      | Edge 130+, Windows 10    | FR-CAT-01      | 1. Go to `/catalog`  2. Enter partial title e.g., "kill"  3. Click search          | Partial match returns relevant books            | valid results found  |
|BUG-CAT-02 | Navbar search input not functioning, catalog search works | Major / High        | Chrome 130+, Windows 10 | FR-CAT-01      | 1. Use search input in Navbar  2. Type a book title  3. Press Enter | Should display matching books |


## 📚 Required Artifacts
- Test plan, test cases, defect logs
- Environment notes (browser versions, devices)
- Accessibility/performance findings with metrics (LCP, TTI) and tools used
- CSV exports or screenshots from management tool

## 🗂️ File Naming
- `team-<name>_final-report.md`, `team-<name>_presentation.(mp4|link)`, etc.
- Include team name and date on first page of all documents

## 🏆 Grading Rubric (Guidelines)
- Testing Thoroughness (35%): coverage, depth, negative paths, a11y/perf checks
- Documentation Quality (25%): clarity, structure, evidence, traceability to FR codes
- Video Presentation (20%): concise, insightful, well-evidenced
- Project Management (15%): organized board, statuses, filters/dashboards
- Team Collaboration (5%): roles, consistency, communication

## 📜 Policies
- Late submissions: per course policy (confirm with instructor)
- Academic integrity: cite sources; individual contributions documented
- Privacy: redact keys; do not expose production credentials

## 🎥 Presentation Checklist
- 5 minutes max; follow `video-guide.md`
- 2–3 top defects with evidence and impact
- Include a11y/perf highlights (metrics, tools)
- Recommendations aligned to risk







