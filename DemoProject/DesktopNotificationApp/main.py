import time  # Importing time module for handling time-related operations
from plyer import notification  # Importing notification module from plyer package

if __name__ == "__main__":
    # Run indefinitely until manually stopped
    # while True:
        # Display a notification reminding to drink water
        notification.notify(
            title="** Please Drink Water Now !!",  # Title of the notification
            message="The National Academies of Science, Engineering, and Medicine determined that an adequate daily "
                    "fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) "
                    "of fluids a day for women.",  # Message body of the notification
            app_icon='../DesktopNotificationApp/drink.ico',  # Path to the icon for the notification
            timeout=30,  # Time after which the notification disappears automatically (in seconds)
        )
        # Print a message to the console reminding to drink water
        print("Please Drink Water Now !!")
        # Wait for an hour before displaying the notification again
        # time.sleep(60*60)
