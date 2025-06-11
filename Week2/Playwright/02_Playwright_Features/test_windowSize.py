import time

from playwright.sync_api import Playwright
import tkinter as tk

def test_run(playwright: Playwright) -> None:
    root = tk.Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()

    browser = playwright.chromium.launch (headless=False)
    context = browser.new_context(
        viewport={'width':screenwidth, 'height': screenheight}
    )

    page = context.new_page()
    # page.set_viewport_size({'width': screenwidth, 'height': screenheight})
    page.goto("https://www.netflix.com/in/")
    time.sleep(5)