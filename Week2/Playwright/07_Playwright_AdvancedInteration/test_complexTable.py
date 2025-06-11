import time
import re
from playwright.sync_api import Playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright. chromium.launch(headless=False)
    context = browser. new_context()
    page = context.new_page()
    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
    time.sleep(2)
    row = page.locator("#example tr")
    row.locator(":scope", has_text="Bradley Greer").locator(".dt-select-checkbox").click()
    print(row)

    time.sleep(5)