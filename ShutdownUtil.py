import time
import os
import webbrowser

def is_okay_check():
    is_okay = input("")
    
    if is_okay.lower() ==  "n":
        return ask_for_time()
    elif is_okay.lower() != "y":
        print("Invalid answer, please try again. (Y/N)")
        is_okay_check()

def ask_for_time():
    tim = input("Enter the time until shutdown in hh,mm,ss: ").split(',')

    if len(tim) == 3:
        tim = [int(num) for num in tim]
    elif tim[0] == "freak you":
        print("i hate you too bub")
        exit()
    elif tim[0] == "goon":
        print("if you insist")
        time.sleep(1)
        webbrowser.open_new_tab("https://tinyurl.com/icemanleakreal")
        exit()
    else:
        print("Invalid input. Please try again.")
        return ask_for_time()

    print()

    print("You chose:", tim[0], "hours,", tim[1], "minutes, and", tim[2], "seconds, correct? [Y/N]")

    new_tim = is_okay_check()

    if new_tim:
            return new_tim
    
    return tim

print ("Shutdown Utility")

print()

tim = ask_for_time()

hrs = tim[0]
mins = tim[1]
secs = tim[2]
total_time = (hrs * 3600) + (mins * 60) + secs

for i in range(total_time):
    if hrs == 0 and mins == 0 and secs != 0:
        print(f"{total_time} seconds remaining                                                        ", end="\r", flush=True)
        time.sleep(1)
        total_time = total_time - 1
    elif hrs == 0 and mins != 0:
        if secs == 0:
            print(f"{mins} minutes and 0 seconds remaining                                            ", end="\r", flush=True)
            time.sleep(1)
            mins = mins - 1
            secs = 59
            total_time = total_time - 1
        else:
            print(f"{mins} minutes and {secs} seconds remaining                                       ", end="\r", flush=True)
            time.sleep(1)
            secs = secs - 1
            total_time = total_time - 1
    elif hrs != 0:
        if mins == 0 and secs == 0:
            print(f"{hrs} hours, 0 minutes and 0 seconds remaining                                    ", end="\r", flush=True)
            time.sleep(1)
            hrs = hrs - 1
            mins = 59
            secs = 59
            total_time = total_time - 1
        elif secs == 0:
            print(f"{hrs} hours, {mins} minutes and 0 seconds remaining                               ", end="\r", flush=True)
            time.sleep(1)
            mins = mins - 1
            secs = 59
            total_time = total_time - 1
        else:
            print(f"{hrs} hours, {mins} minutes and {secs} seconds remaining                          ", end="\r", flush=True)
            time.sleep(1)
            secs = secs - 1
            total_time = total_time - 1
print("0 seconds remaining")
time.sleep(1)
print("Complete! Shutting down now...")
time.sleep(2)
os.system("poweroff")


        









