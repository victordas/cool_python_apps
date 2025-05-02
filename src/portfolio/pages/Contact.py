from streamlit import form, form_submit_button, header, text_area, text_input
from re import match
from send_email import send_mail

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return match(pattern, email) is not None


header("Contact me")

with form(key='-CONTACT_FORM-'):
    user_email = text_input('Your email address', key='user_email')
    message = text_area('Your message', key='message')
    button = form_submit_button()

    if button and is_valid_email(user_email) and message.strip() != "":
        mail_body = f"Subject: Cool Python Apps\n{message}\nFrom: {user_email}"
        send_mail(message=mail_body)
