import time

from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    # page.locator("//input[@placeholder='First Name']").fill("Dayanidhi")
    page.fill("//input[@placeholder='First Name']", "Dayanidhi")
    # link_text = page. locator ("text = SwitchTo")
    # link_text.hover()
    # page.Locator ("button", has_text=" Submit ").click()

    select_size = page.locator("select#country option")
    print("Size of Select dropdown", select_size.count())
    list_select = select_size.all_text_contents()
    print(list_select)
    time.sleep(5)