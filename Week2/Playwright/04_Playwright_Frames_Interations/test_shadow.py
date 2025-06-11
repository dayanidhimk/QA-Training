import time

from playwright.sync_api import Playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://selectorshub.com/iframe-in-shadow-dom/")
    page.frame_locator("#pact1").locator("#glaf").fill("Testing")
    # page.goto("https://books-pwakit.appspot.com/")
    # page. locator("#input").fill("Testing")
    # page.Locator ("book-app[apptitle='BOOKS'] #input").fill("Testing")
    # text = page. Locator ("book-app [apptitle='BOOKS'] .books-desc").text_content()
    # print(text)
    time.sleep(5)