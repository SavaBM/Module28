import os
from dotenv import load_dotenv

load_dotenv()

name_user = os.getenv('name_user')
last_name_user = os.getenv('last_name_user')

valid_login = os.getenv('valid_login')
invalid_login = os.getenv('invalid_login')

valid_email = os.getenv('valid_email')
invalid_email = os.getenv('invalid_email')

valid_password = os.getenv('valid_password')
invalid_password = os.getenv('invalid_password')

valid_phone_number = os.getenv('valid_phone_number')
invalid_phone_number = os.getenv('invalid_phone_number')

mail_passw = os.getenv('mail_passw')
