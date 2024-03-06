from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\33[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")

minutes = input("Please insert how many minutes to wait: ")
while True:
    if minutes.isdigit():
        minutes = int(minutes)
        break
seconds = input("Please insert how many seconds to wait: ")
while True:
    if seconds.isdigit():
        seconds = int(seconds)
        break

total_seconds = minutes * 60 + seconds

alarm(total_seconds)