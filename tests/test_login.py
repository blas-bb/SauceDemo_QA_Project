def test_valid_login(driver, login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.get_title() == "Products"


def test_locked_user(driver, login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_message() == (
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_empty_username(driver, login_page):
    login_page.login("", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Username is required"


def test_empty_password_intentional_fail(driver, login_page):
    login_page.login("standard_user", "")
    # NAMERNO POGREŠNO očekivanje radi prikaza FAIL-a i screenshota.
    assert login_page.get_error_message() == "Epic sadface: WRONG PASSWORD MESSAGE"


def test_wrong_password_intentional_fail(driver, login_page):
    login_page.login("standard_user", "wrong_password")
    # NAMERNO POGREŠNO očekivanje radi prikaza drugog FAIL-a.
    assert login_page.get_error_message() == "Epic sadface: Login successful"
