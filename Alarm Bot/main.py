from tkinter import *
from datetime import datetime
import time
import winsound
from threading import Thread
import os  

# ========== Main GUI Setup ==========
root = Tk()
root.title("⏰ PyNexus Alarm Clock")
root.geometry("500x300")
root.config(bg="#1f1f2e")

# ========== Global Variables ==========
alarm_time = None
alarm_triggered = False

# ========== Alarm Logic ==========
def set_alarm():
    global alarm_time, alarm_triggered
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm_triggered = False
    status_label.config(text=f"Alarm set for {alarm_time}", fg="#00FFAA")

def alarm():
    global alarm_triggered
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        clock_label.config(text=f"⏳ {current_time}")
        if alarm_time == current_time and not alarm_triggered:
            alarm_triggered = True
            status_label.config(text="🚨 Wake Up!", fg="red")
            try:
                if os.path.exists("sound.wav"):
                    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                else:
                    status_label.config(text="Sound file not found!", fg="yellow")
            except Exception as e:
                status_label.config(text=f"Error: {str(e)}", fg="orange")
        time.sleep(1)

def start_thread():
    t = Thread(target=alarm)
    t.daemon = True
    t.start()

# ========== GUI Elements ==========

Label(root, text="PyNexus Alarm Clock", font=("Helvetica", 20, "bold"),
      fg="#FF3CAC", bg="#1f1f2e").pack(pady=10)

clock_label = Label(root, text="", font=("Courier", 18), fg="#00FFAA", bg="#1f1f2e")
clock_label.pack()

Label(root, text="Set Alarm Time (HH:MM:SS)", font=("Helvetica", 14),
      fg="#ffffff", bg="#1f1f2e").pack(pady=5)

frame = Frame(root, bg="#1f1f2e")
frame.pack()

# Time Selection
hour = StringVar(value="00")
minute = StringVar(value="00")
second = StringVar(value="00")

hrs = OptionMenu(frame, hour, *["{:02}".format(i) for i in range(24)])
hrs.config(bg="#333", fg="white", width=5)
hrs.pack(side=LEFT, padx=5)

mins = OptionMenu(frame, minute, *["{:02}".format(i) for i in range(60)])
mins.config(bg="#333", fg="white", width=5)
mins.pack(side=LEFT, padx=5)

secs = OptionMenu(frame, second, *["{:02}".format(i) for i in range(60)])
secs.config(bg="#333", fg="white", width=5)
secs.pack(side=LEFT, padx=5)

# Set Button
Button(root, text="🔔 Set Alarm", font=("Helvetica", 14, "bold"),
       bg="#007BFF", fg="white", command=set_alarm).pack(pady=10)

# Status Display
status_label = Label(root, text="No alarm set", font=("Helvetica", 12),
                     fg="gray", bg="#1f1f2e")
status_label.pack(pady=5)

# Start alarm thread on launch
start_thread()

root.mainloop()
