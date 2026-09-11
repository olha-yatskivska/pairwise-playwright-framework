This project utilizes Python, Playwright, and Pytest to execute automated UI tests. The framework is built using the Page Object Model (POM) design pattern and implements Data-Driven Testing (DDT) to maximize test coverage while maintaining clean, scalable code.

data/: Stores external test data sets. The pairwise_data.csv file allows the test suite to iterate through mathematically optimized input combinations without hardcoding values into the scripts.

pages/: Houses the Page Object classes (base_page.py, pantry_page.py). This centralizes UI locators and page interactions, ensuring that if the application's UI changes, maintenance is restricted to a single file.

tests/: Contains the Pytest execution scripts. The test files ingest the CSV data and assert the expected outcomes using the page methods.

conftest.py: Manages Pytest fixtures to handle browser initialization, context setup, and teardown seamlessly before and after test runs.

pytest.ini & requirements.txt: Manages core execution parameters and project dependencies for easy environment setup.



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






