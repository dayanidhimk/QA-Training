import time
from playwright.sync_api import Playwright

def handle_dialog(dialog) :
    assert dialog. type == 'beforeunload'
    dialog. dismiss()

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context. new_page ()

    # page. goto("https://demo.automationtesting.in/Register.html")
    # time.sleep(2)
    # page.hover ("//a[text ()='SwitchTo' ]")
    # time.sleep(2)
    # page.hover("//a[text ()='Frames' ]")
    # time.sleep(2)

    page. goto("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    page.dblclick("//button[text()='Copy Text']")
    time.sleep(1)

    page.drag_and_drop(source="#draggable", target="#droppable")
    time.sleep(5)