import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Start Tracing
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("python 3")
    page.goto("https://www.google.com/search?q=python+3&sca_esv=292513031035339b&sxsrf=AE3TifOG5p--byEaQBpct2FzX7gRU9bdhw%3A1749661862054&source=hp&ei=prhJaPKJAcievr0P8_6B0AY&iflsig=AOw8s4IAAAAAaEnGts_Uny5zsJVCOdUTOtdh0gk3D4GA&ved=0ahUKEwjy9Iyu7umNAxVIj68BHXN_AGoQ4dUDCBk&uact=5&oq=python+3&gs_lp=Egdnd3Mtd2l6IghweXRob24gMzIIEAAYgAQYsQMyCBAAGIAEGLEDMgsQABiABBixAxiDATIFEAAYgAQyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQNI_RdQAFjZFXAAeACQAQCYAZsBoAGGCKoBAzAuOLgBA8gBAPgBAZgCCKACnwjCAgoQIxiABBgnGIoFwgIIEC4YgAQYsQPCAg4QLhiABBixAxjHARivAcICDhAAGIAEGLEDGIMBGIoFmAMAkgcDMC44oAekOLIHAzAuOLgHnwjCBwUwLjYuMsgHFQ&sclient=gws-wiz")
    page.get_by_role("link", name="Download Python Python.org").click()

    #Stop Tracing
    page.context.tracing.stop(path="trace.zip")

# ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
