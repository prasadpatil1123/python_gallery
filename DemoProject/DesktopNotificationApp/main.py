import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="** Please Drink Water Now !!",
            message="The National Academies of Science, Engineering, and Medicine determined that an adequate daily "
                    "fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) "
                    "of fluids a day for women.",
            # app_icon="Hello",
            app_icon ='../DesktopNotificationApp/drink.ico',
            timeout=15,
        )
        print("Hello")
        # time.sleep(6)
        time.sleep(60*60)
# pythonw .\main.py