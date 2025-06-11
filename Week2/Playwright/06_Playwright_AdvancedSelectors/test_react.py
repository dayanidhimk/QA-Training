import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.netflix.com/in/")
    time.sleep(2)
    page.locator("_react=[label='Email address'] >> input").first.fill("dayanidhi@gmail.com")
    time.sleep(5)