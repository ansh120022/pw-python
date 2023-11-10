from pytest import fixture
from playwright.sync_api import sync_playwright
from pages.registration import Registration


@fixture
def app():
    with sync_playwright() as playwright:
        app = playwright.chromium.launch(channel="chrome", headless=True)
        page = app.new_page()
        yield page
        app.close()


@fixture
def login(app):
    Registration(app).login()
