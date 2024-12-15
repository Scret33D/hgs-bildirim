#Scret Bu Bir HGS Uygulaması için bildirim yollayıcıdır
#her an fixlenebilir
#scretontop

import requests
import json


def send_onesignal_notification(app_id, rest_api_key, heading, content):
    """
    OneSignal ile tüm kullanıcılara bildirim gönderir.

    :param app_id: OneSignal Uygulama ID'si.
    :param rest_api_key: OneSignal REST API anahtarı.
    :param heading: Bildirimin başlığı.
    :param content: Bildirimin içeriği.
    :return: API yanıtı.
    """
    url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {rest_api_key}"
    }

    payload = {
        "app_id": app_id,
        "headings": {"en": heading},
        "contents": {"en": content},
        "included_segments": ["All"]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("Bildirim başarıyla gönderildi.")
    else:
        print(f"Bir hata oluştu: {response.status_code}, {response.text}")

    return response.json()

# Kullanım örneği
if __name__ == "__main__":
    ONE_SIGNAL_APP_ID = "3a812cd9-40fd-44ba-a581-9215ad0314f5"
    ONE_SIGNAL_REST_API_KEY = "MjE3Zjk1YWQtOTlhZS00NDc4LTgyNzktMDkxOTZiZWM1ZWYz"

    heading = "Scret" #Bildirim'in başlığı
    content = "Scret" #Bildirim'in mesajı

    send_onesignal_notification(
        app_id=ONE_SIGNAL_APP_ID,
        rest_api_key=ONE_SIGNAL_REST_API_KEY,
        heading=heading,
        content=content
    )