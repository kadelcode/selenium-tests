from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_google_title():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print("Test passed: Google title is correct!")
    driver.quit()

if __name__ == "__main__":
    test_google_title()
