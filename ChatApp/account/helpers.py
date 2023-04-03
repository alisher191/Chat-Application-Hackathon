import requests
import random

API_KEY = '674e4aab-f5f6-45f3-8d1a-ef9c21f7ec76'


def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(1000, 9999)
        url = f'https://2factor.in/API/V1/{API_KEY}/SMS/{phone_number}/{otp}'
        response = requests.get(url)
        return otp
    except Exception:
        return None
