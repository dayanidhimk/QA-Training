import time

from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    # page.goto("https://www.amazon.in/")
    page.goto("https://demo.automationtesting.in/Register.html")

    btn_value = page.locator("form button", has_text=" Submit ").text_content()
    print(btn_value)
    page.locator("form button", has_text=" Submit ").click()

    # label_h1 = page.locator("Automation Demo Site").text_content()
    # label_h1 = page.locator("text = Automation Demo Site ").text_content()
    # print(label_h1)
    # webtable = page. locator ("text = WebTable")
    # webtable.hover()
    # webtable.click()
    # page.Locator("text = Sign in").last.click()
    time.sleep(5)