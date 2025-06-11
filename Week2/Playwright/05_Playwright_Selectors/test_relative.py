import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")
    page.locator("input[type='checkbox']:left-of(:text('John.Smith'))").first.click()
    text = page.locator("td:right-of(a:has-text('John.Smith'))").first.text_content()
    print(text)
    text1 = page.locator("a:below(a:has-text('John.Smith'))").first.text_content()
    print(text1)
    text2 = page.locator("a:above(a:has-text('John.Smith'))").first.text_content()
    print(text2)
    list_a = page. locator("a:near(:text('John.Smith'))").all_inner_texts()
    for lis in list_a:
        print(lis)
    time.sleep(5)