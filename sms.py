import requests

def send_sms(phone_number, message):
    response = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': message,
        'key': 'textbelt',
    })
    return response.json()

if __name__ == "__main__":
    phone_number = input("أدخل رقم الهاتف: ")
    message = input("أدخل الرسالة: ")
    result = send_sms(phone_number, message)
    print(result)
