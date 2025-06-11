import time

from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://petstore.octoperf.com/actions/Catalog.action")
    link_list = page.locator("a")
    print(link_list.count())

    lis = link_list.all_inner_texts()

    for lin in lis:
        print(lin)
        if "DOGS" == lin:
            page.locator("text = "+lin +"").first.click()

    time.sleep(5)