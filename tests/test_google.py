from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_title():
    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Automatically download and use the correct Chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to Google
    driver.get("https://www.google.com")

    # Simple assertion
    assert "Google" in driver.title
    print("Test passed: Google title is correct!")

    # Quit the driver
    driver.quit()

if __name__ == "__main__":
    test_google_title()
