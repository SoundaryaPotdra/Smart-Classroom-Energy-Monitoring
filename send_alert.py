import requests

BOT_TOKEN = "7794166567:AAETcJpteVMnELRskrnNLJrIXhNk6ll_A_k"
CHAT_ID = "1520847150"

def send_alert_telegram():
    MESSAGE = "⚠️ Alert! No human detected in the classroom, but lights are ON."
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": MESSAGE}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("✅ Telegram alert sent!")
    else:
        print("❌ Failed to send alert. Error:", response.text)

# Test the function
if __name__ == "__main__":
    send_alert_telegram()
