import time

from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://demo.automationtesting.in/Frames.html")
    page.frame_locator("iframe[name=SingleFrame]").locator("input").fill("testing")
    time.sleep(5)