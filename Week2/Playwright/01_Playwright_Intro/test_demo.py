import re
from playwright.sync_api import Page, expect

def test_verifyGoogleTitle(page: Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title(re.compile("Google"))