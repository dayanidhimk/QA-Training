import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    time.sleep(2)
    first_tagName = page.locator(".navAccessibility li a >> nth=0").text_content()
    print(first_tagName)

    last_tagName = page.locator(".navAccessibility li a >> nth=-1").text_content()
    print(last_tagName)

    page.locator(".navAccessibility li a >> nth=-1").click()