import time
from datetime import datetime

# Set your future event date and time here
EVENT_NAME = "Birthday"
EVENT_TIME = datetime(2025, 12, 8, 6, 1, 59)  # YYYY, MM, DD, HH, MM, SS

def countdown(target_time):
    while True:
        now = datetime.now()
        remaining = target_time - now

        if remaining.total_seconds() <= 0:
            print(f"\n🎉 {EVENT_NAME} is happening now!")
            break

        days = remaining.days
        hours, rem = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        print(f"\r⏳ Time until {EVENT_NAME}: {days}d {hours:02}h {minutes:02}m {seconds:02}s", end='')
        time.sleep(1)

# Run the countdown
countdown(EVENT_TIME)
