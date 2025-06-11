import time
from playwright. sync_api import Playwright

def handle_dialog(dialog) :
    assert dialog.type == 'beforeunload'
    dialog.dismiss()

def test_run(playwright: Playwright) -> None:
    browser = playwright. chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(2)
    page.on("dialog", lambda dialog: dialog.accept("Daya"))
    page.locator("//button[text()='Click for JS Prompt' ]").click()

    # page.on("dialog", lambda dialog: dialog.dismiss())
    # page.on("dialog", lambda dialog: print(dialog.message))
    # page.locator("//button[text()='Click for JS Confirm' ]").click()

    # Accept
    # page.on("dialog", lambda dialog: dialog.accept())
    # page.locator("//button[text()='Click for JS Alert' ]").click()
    # mesg = page.locator ("#result").text_content()
    # assert mesg == "You successfully clicked an alert"
    time.sleep(5)