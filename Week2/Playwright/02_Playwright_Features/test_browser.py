import time

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://www.google.com/")
    # Click [aria-label="Search"]
    page.locator ("[aria-label=\"Search\"]").click()
    # Fill [aria-label="Search"]
    page.locator("[aria-label=\"Search\"]").fill("testing")
    time.sleep(5)

    browser1 = playwright.chromium.launch(headless=False)
    context1 = browser1.new_context()
    # Open new page
    page1 = context1.new_page()
    page1.goto("https://www.google.com/")
    # Click [aria-label="Search"]
    page1.locator("[aria-label=\"Search\"]").click()
    # Fill [aria-label="Search"]
    page1.locator("[aria-label=\"Search\"]").fill("testing")
    time.sleep(5)

with sync_playwright() as Playwright:
    run(Playwright)