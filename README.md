# Automated UI Testing Framework


A robust, scalable UI test automation framework built using **Python, Playwright, and Pytest**. Designed following industry best practices, it implements the Page Object Model (POM) design pattern and Data-Driven Testing (DDT) to maximize test coverage while minimizing code duplication and maintenance overhead.

---

## Architecture & Design Patterns

* **Page Object Model (POM)**: Separates test logic from UI element locators. If the application interface changes, updates are localized to a single page class.

* **Data-Driven Testing (DDT):** Externalizes test datasets into CSV files, allowing the suite to iterate through mathematically optimized input combinations dynamically without hardcoding values.

* **Robust Fixture Management:** Centralizes browser initialization, context setup, and teardown cleanly using Pytest fixtures.

---

## Project Structure

* `data/:` Stores external test datasets (e.g., pairwise_data.csv) for optimized input testing.

* `pages/:` Houses Page Object classes (base_page.py, pantry_page.py) to centralize locators and interactions.

* `tests/:` Contains execution scripts that ingest CSV data and perform assertions using page methods.

* `conftest.py:` Manages Pytest hooks and fixtures for seamless session management.

* `pytest.ini & requirements.txt:` Define core execution parameters and project dependencies.

---

## Execution & CI/CD

#### Run via GitHub Actions

1. Navigate to Actions -> Playwright Tests -> Run workflow.

2. Check the box for use local if applicable, then click Run workflow.

3. View [test execution logs](https://prnt.sc/wdgl37KZHLpq) directly on GitHub or download the Allure Results Artifact to generate and view local reports.


#### Run Locally

Clone the repository, set up your virtual environment, and install dependencies:

Example local Allure history and outputs can be inspected in the [./allure-history](./allure-history) directory.

---

## VS Code Command Cheat Sheet 

| Command | When  |
| :-- | :-- |
| venv\Scripts\activate | Activate virtual environment |
| pytest or pytest --headed |  Run tests against live Netlify site (Production/Staging mode)|
| pytest --lf (which stands for --last-failed) | Run only the tests that failed in the last run |
| pytest -k TC-P-01 | Run a specific test case  | 
| $env:USE_LOCAL="true"; pytest --alluredir=allure-results --clean-alluredir | Run test cases locally |
| pytest --tracing=on (or off, or retain-on-failure) | Record the trace for each test (don't record, record, but remove all traces from successful test runs), check the trace.zip file |
| playwright show-trace trace.zip or use browser trace.playwright.dev | Open the trace |
| --alluredir=allure-results | Сollect the data for reports |
| allure serve allure-results   | Serve the report |
| --clean-alluredir | Clean the folder allure-results |
| allure generate allure-results --clean -o allure-report | Create allure-report dir with results |
| allure open allure-report | Open the report from allure-report/index.html |
| pip freeze > requirements.txt  | Export and lock all current package dependencies into your requirements file | 






