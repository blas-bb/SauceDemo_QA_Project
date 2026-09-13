BACKPACK = "sauce-labs-backpack"


def open_checkout(inventory_page, cart_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.open_cart()
    cart_page.start_checkout()


def test_checkout_page_opens(
    logged_in,
    inventory_page,
    cart_page,
    checkout_page
):
    open_checkout(inventory_page, cart_page)

    assert checkout_page.get_title() == (
        "Checkout: Your Information"
    )


def test_checkout_requires_first_name(
    logged_in,
    inventory_page,
    cart_page,
    checkout_page
):
    open_checkout(inventory_page, cart_page)

    checkout_page.fill_information(
        "",
        "Tester",
        "11000"
    )
    checkout_page.continue_checkout()

    # Korisnik mora ostati na istoj stranici
    # zato što First Name nije popunjen.
    assert checkout_page.get_title() == (
        "Checkout: Your Information"
    )


def test_checkout_requires_last_name(
    logged_in,
    inventory_page,
    cart_page,
    checkout_page
):
    open_checkout(inventory_page, cart_page)

    checkout_page.fill_information(
        "QA",
        "",
        "11000"
    )
    checkout_page.continue_checkout()

    # Korisnik mora ostati na istoj stranici
    # zato što Last Name nije popunjen.
    assert checkout_page.get_title() == (
        "Checkout: Your Information"
    )


def test_checkout_overview_contains_product(
    logged_in,
    inventory_page,
    cart_page,
    checkout_page
):
    open_checkout(inventory_page, cart_page)

    checkout_page.fill_information(
        "QA",
        "Tester",
        "11000"
    )
    checkout_page.continue_checkout()

    assert checkout_page.get_title() == (
        "Checkout: Overview"
    )

    assert checkout_page.get_summary_item_count() == 1


def test_complete_checkout(
    logged_in,
    inventory_page,
    cart_page,
    checkout_page
):
    open_checkout(inventory_page, cart_page)

    checkout_page.fill_information(
        "QA",
        "Tester",
        "11000"
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert checkout_page.get_complete_message() == (
        "Thank you for your order!"
    )