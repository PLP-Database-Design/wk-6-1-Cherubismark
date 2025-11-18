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
    search.send_keys("Gatsby")
    print("Search term 'Gatsby' entered")
    
    # Try pressing Enter to trigger search
    search.send_keys(Keys.RETURN)
    print("Enter key pressed")
    
    # Wait for results to load
    print("Waiting for results...")
    time.sleep(3)
    
    # Take screenshot after search
    driver.save_screenshot("debug_screenshot_after_search.png")
    print("Screenshot after search saved")
    
    # Try multiple selectors for book elements - FILTER FOR VISIBLE BOOKS ONLY
    book_selectors = [
        "[data-testid*='book-card']",  # More specific first
        ".BookCard[data-testid]",
        ".book-card[data-testid]", 
        "[data-testid*='book']",
        ".BookCard",
        ".book-card", 
        ".book",
        ".card",
        ".MuiCard-root"
    ]
    
    books = []
    for selector in book_selectors:
        all_elements = driver.find_elements(By.CSS_SELECTOR, selector)
        if all_elements:
            # Filter only visible books
            visible_books = [book for book in all_elements if book.is_displayed()]
            print(f"Found {len(all_elements)} total elements, {len(visible_books)} visible books using selector: {selector}")
            
            # DEBUG: Print details about visible books
            if visible_books:
                print(f"\n=== VISIBLE BOOKS DETAILS ===")
                for i, book in enumerate(visible_books):
                    try:
                        title_element = book.find_element(By.CSS_SELECTOR, "h2, h3, h4, .title, [data-testid*='title'], .book-title")
                        title_text = title_element.text
                        print(f"Visible Book {i+1}: '{title_text}'")
                    except:
                        try:
                            # If no specific title element, show the text content
                            book_text = book.text.replace('\n', ' ')[:100] if book.text else "No text content"
                            print(f"Visible Book {i+1}: {book_text}...")
                        except:
                            print(f"Visible Book {i+1}: Could not extract details")
            
            if visible_books:
                books = visible_books
                break
    
    if not books:
        print("No visible books found with any selector. Looking for any visible card-like elements...")
        # Look for any elements that might contain books (only visible ones)
        all_cards = driver.find_elements(By.CSS_SELECTOR, "div, article, section, li")
        visible_cards = [card for card in all_cards[:30] if card.is_displayed() and card.text.strip()]
        card_count = 0
        for card in visible_cards:
            text = card.text.strip()
            if text and len(text) > 10:  # If it has substantial text
                print(f"Potential visible book element: {text[:50]}...")
                card_count += 1
        print(f"Found {card_count} potential visible book containers")
    
    # Check if we're on a different page or if there's an error message
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error, .alert, .message, [role='alert']")
    if error_messages:
        for error in error_messages:
            if error.is_displayed():
                print(f"Visible error message: {error.text}")
    
    # Assertion based on VISIBLE books only
    print(f"\n=== FINAL TEST RESULTS ===")
    print(f"Visible books found: {len(books)}")
    
    assert len(books) > 0, f"Expected at least 1 visible book, but found {len(books)}"
    
    # Additional verification: Check if the visible book contains "Gatsby"
    book_titles = []
    for book in books:
        try:
            title_element = book.find_element(By.CSS_SELECTOR, "h2, h3, h4, .title, [data-testid*='title']")
            title_text = title_element.text.lower()
            book_titles.append(title_text)
            if "gatsby" in title_text:
                print(f"✅ SUCCESS: Found book containing 'Gatsby': {title_element.text}")
        except:
            continue
    
    if book_titles:
        print(f"All visible book titles: {book_titles}")
    
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