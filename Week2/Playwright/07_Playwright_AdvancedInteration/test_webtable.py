import time

from playwright.sync_api import Playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    locator = page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]")
    expect(locator).to_contain_text("Learn Selenium")

    row_count = page.locator("//table[@name='BookTable']/tbody/tr").count()
    column_count = page.locator("//table[@name='BookTable']/tbody/tr/th").count()

    for r in range(2, row_count+1):
        for c in range(1, column_count+1):
            value = page.locator("//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text_content()
            print(value, end="    ")
        print()