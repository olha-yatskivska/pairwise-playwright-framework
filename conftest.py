import pytest
import os
import platform
from pages.pantry_page import PantryPage

@pytest.fixture(scope="function")
def pantry_page(page):
    """
    Initializes the PantryPage object and navigates to either 
    the live staging URL or the local HTML file based on environment settings.
    """
    pantry = PantryPage(page)
    
    # Check if a 'USE_LOCAL' environment variable is set
    use_local = os.getenv("USE_LOCAL", "false").lower() == "true"
    
    if use_local:
        # Navigate to the local file path
        local_html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_app", "index.html"))
        pantry.navigate(f"file://{local_html_path}")
    else:
        # Default to the production/staging URL
        pantry.navigate("https://pairwise-testing.netlify.app/")
    
    # Yield hands control over to the test function
    yield pantry
    
    # Any teardown code would go here after the yield, 
    # but Playwright handles closing the page automatically!
    
    
def pytest_sessionfinish(session, exitstatus):
    """
    Hook that runs after the test session finishes.
    Dynamically captures runtime environment settings for Allure reporting.
    """
    allure_dir = "allure-results"
    
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)
        
    env_file = os.path.join(allure_dir, "environment.properties")
    
    # Read active browsers/devices from pytest configuration
    browsers = session.config.getoption("--browser", default=["chromium"])
    device = session.config.getoption("--device", default=None)
    
    with open(env_file, "w", encoding="utf-8") as f:
        f.write("Environment=QA\n")
        f.write(f"OS={platform.system()} {platform.release()}\n")
        f.write(f"Python_Version={platform.python_version()}\n")
        f.write(f"Browsers={', '.join(browsers)}\n")
        if device:
            f.write(f"Emulated_Device={device}\n")
        f.write("Test_Type=UI_Automation\n")
        f.write("Project=Pairwise_Recipes\n")