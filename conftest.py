from datetime import datetime
from pathlib import Path

import pytest
from pytest_html import extras

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Pokreni Chrome bez prikazivanja prozora.",
    )


@pytest.fixture
def driver(request):
    options = Options()

    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1440,1000")

    # Iskljucujemo Chrome Password Manager tokom testiranja
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    browser.get("https://www.saucedemo.com/")

    yield browser

    browser.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)


@pytest.fixture
def logged_in(driver, login_page):
    login_page.login("standard_user", "secret_sauce")
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    browser = item.funcargs.get("driver")

    if browser is None:
        return

    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = screenshots_dir / f"{item.name}_{timestamp}.png"

    browser.save_screenshot(str(screenshot_path))

    screenshot_base64 = browser.get_screenshot_as_base64()

    report.extras = getattr(report, "extras", [])

    report.extras.append(
        extras.png(
            screenshot_base64,
            name=f"Screenshot - {item.name}"
        )
    )