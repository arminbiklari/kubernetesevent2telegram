import requests

def send_message(message):
    TOKEN = "5663208423:AAFX5tS-SYIld-qnJyinz2H88B42VuV6EDg"
    chat_id = "-676355763"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())
