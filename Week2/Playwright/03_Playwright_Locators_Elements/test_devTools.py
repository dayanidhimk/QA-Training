import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # inspecting Playwright selectors in Chrome Dev tools
    page = context.new_page()
    page.goto("https://www.amazon.in/")

    list_a = page.locator("a:has-text('Amazon')").all_inner_texts()

    for lis in list_a:
        print(lis)

    time.sleep(2)