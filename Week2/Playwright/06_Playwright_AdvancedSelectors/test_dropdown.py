import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # inspecting Playwright selectors in Chrome Dev tools
    page = context.new_page()

    page.goto("https://demo.automationtesting.in/Register.html")
    time.sleep(2)

    # Selecting a skill from the dropdown
    page.locator("#Skills").select_option("Android")
    time.sleep(3)
    page.locator("#Skills").select_option("C")
    time.sleep(5)