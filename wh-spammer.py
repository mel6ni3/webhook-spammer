import time
import requests
import pyfiglet
banner = pyfiglet.figlet_format("KINGMAN")
print(banner)
msg = input("Please Insert WebHook Spam Message: ")
webhook = input("Porfavor inserte el link de la webhook: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
kingman_top = 1
while kingman_top == 1:
    spam(msg, webhook)
