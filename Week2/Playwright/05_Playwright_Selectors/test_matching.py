import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demo.automationtesting.in/Register.html")

    list_element = page.locator("button:has-text('Register'), button:has-text('Sign In'), button:has-text('Submit')").all_inner_texts()

    for lis in list_element:
        print(lis)

    time.sleep(5)