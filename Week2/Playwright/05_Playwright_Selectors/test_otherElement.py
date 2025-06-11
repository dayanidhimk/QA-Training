import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # inspecting Playwright selectors in Chrome Dev tools
    page = context.new_page()

    page.goto("https://demo.automationtesting.in/Register.html")

    list_element = page.locator ("#Skills").all_inner_texts()

    for lis in list_element:
        print(lis)

    # page.locator("#Skills").click()
    page.locator("#Skills").select_option("C")

    time.sleep(10)