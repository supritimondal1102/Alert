from plyer import notification
import time

if __name__== '__main__':
    while True:
     notification.notify(
        title="*** Take Rest ***",
        message="Rest is vital for better mental health, improved mood and even a better metabolism. ",
        app_icon="C:/Users/supri/Desktop/icon.ico",
        timeout=5)
     time.sleep(10)