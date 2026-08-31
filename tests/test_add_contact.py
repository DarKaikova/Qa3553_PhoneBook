from models.contact import Contact
from pages.add_contact_page import ContactPage


def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        "Anna",
        "Test",
        "0501234567",
        "anna_test@gmail.com",
        "Tel Aviv",
        "QA lesson contact"
    )


    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)