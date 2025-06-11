import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.spicejet.com/")
    time.sleep(2)
    page.fill(".css-1cwyjr8", "mu")

    page.locator(".r-knv0ih .r-cqee49", has=page.locator("//div[text()=' Mumbai']").click())

    # page. locator(".r-knv0ih .r-cqee49", has_text="Mumbai").click()
