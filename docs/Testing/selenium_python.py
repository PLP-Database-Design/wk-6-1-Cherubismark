
 # Document Name : Bookstore QA Project Team TNNP


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os

print("Script started...")
print("Python path:", sys.executable)

try:
    print("Setting up Chrome driver...")
    
    # Add Chrome options for better debugging
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    print("Chrome driver setup successful")
    
    print("Navigating to http://localhost:3000/catalog...")
    driver.get("http://localhost:3000/catalog")
    
    # Use explicit waits instead of fixed sleep
    wait = WebDriverWait(driver, 30)
    
    # Wait for page to load completely
    print("Waiting for page to load...")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    # Check current URL
    print(f"Current URL: {driver.current_url}")
    print(f"Page title: {driver.title}")
    
    # Take a screenshot to see what's visible
    driver.save_screenshot("debug_screenshot_initial.png")
    print("Initial screenshot saved as debug_screenshot_initial.png")
    
    # Debug: Print page source to see what's actually loaded
    print("Page source length:", len(driver.page_source))
    
    # Look for any input elements to understand the structure
    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"Found {len(all_inputs)} input elements on page")
    for i, input_elem in enumerate(all_inputs):
        print(f"Input {i}: id='{input_elem.get_attribute('id')}', "
              f"class='{input_elem.get_attribute('class')}', "
              f"type='{input_elem.get_attribute('type')}'")
    
    print("Looking for search element...")
    
    # Try multiple ways to find the search element
    search = None
    search_selectors = [
        "#search",
        "input[type='search']",
        "input[placeholder*='search' i]",
        "input[name*='search' i]",
        ".search",
        "[data-testid='search']"
    ]
    
    for selector in search_selectors:
        try:
            search = driver.find_element(By.CSS_SELECTOR, selector)
            print(f"Search element found using selector: {selector}")
            break
        except:
            continue
    
    if not search:
        print("Search element not found with any selector!")
        # Print all elements with 'search' in their attributes
        elements_with_search = driver.find_elements(By.XPATH, "//*[contains(@id, 'search') or contains(@class, 'search') or contains(@name, 'search')]")
        print(f"Elements with 'search' in attributes: {len(elements_with_search)}")
        for elem in elements_with_search:
            print(f"Tag: {elem.tag_name}, id: {elem.get_attribute('id')}, class: {elem.get_attribute('class')}")
        raise Exception("Search element not found")
    
    print("Search element found!")
    
    # Clear and type search term
    search.clear()
    search.send_keys("Mocking")
    print("Search term entered")
    
    # Try pressing Enter to trigger search
    search.send_keys(Keys.RETURN)
    print("Enter key pressed")
    
    # Wait for results to load
    print("Waiting for results...")
    time.sleep(3)
    
    # Take screenshot after search
    driver.save_screenshot("debug_screenshot_after_search.png")
    print("Screenshot after search saved")
    
    # Try multiple selectors for book elements
    book_selectors = [
        ".BookCard",
        ".book-card",
        ".book",
        ".card",
        "[data-testid*='book']",
        ".MuiCard-root"  # Material-UI card
    ]
    
    books = []
    for selector in book_selectors:
        books = driver.find_elements(By.CSS_SELECTOR, selector)
        if books:
            print(f"Found {len(books)} books using selector: {selector}")
            break
    
    if not books:
        print("No books found with any selector. Looking for any card-like elements...")
        # Look for any elements that might contain books
        all_cards = driver.find_elements(By.CSS_SELECTOR, "div, article, section, li")
        card_count = 0
        for card in all_cards[:20]:  # Check first 20 elements
            text = card.text.strip()
            if text and len(text) > 10:  # If it has substantial text
                print(f"Potential book element: {text[:50]}...")
                card_count += 1
        print(f"Found {card_count} potential book containers")
    
    # Check if we're on a different page or if there's an error message
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error, .alert, .message, [role='alert']")
    if error_messages:
        for error in error_messages:
            print(f"Error message found: {error.text}")
    
    assert len(books) > 0, f"Expected at least 1 book, but found {len(books)}"
    print("Search test passed!")
    
except Exception as e:
    print("Search test FAILED:", e)
    import traceback
    traceback.print_exc()
    
    # Save final page source for debugging
    if 'driver' in locals():
        with open("debug_page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Page source saved as debug_page_source.html")
finally:
    print("Closing browser...")
    if 'driver' in locals():
        driver.quit()
    print("Browser closed")