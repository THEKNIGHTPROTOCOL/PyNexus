import tkinter as tk
from tkinter import Frame, StringVar, Entry, Button, Label, LEFT, TOP, messagebox

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self._alarm_id = None
        self._paused = False
        self._remaining_time = 0
        self.create_widgets()
        self.master.geometry("300x250")

    def create_widgets(self):
        # Time input
        self.time_var = StringVar()
        self.input_time = Entry(self, width=25, font=('Calibri', 12), textvariable=self.time_var)
        self.input_time.insert(0, "Enter Time in seconds")
        self.input_time.bind("<Button-1>", self.clear_placeholder)
        self.input_time.pack(padx=10, pady=(30, 10))

        # Button panel
        button_frame = Frame(self)
        button_frame.pack(pady=10)

        Button(button_frame, text="Start", font=('Helvetica', 12), bg='green', fg='white',
               command=self.start_timer).pack(side=LEFT, padx=5)

        Button(button_frame, text="Pause", font=('Helvetica', 12), bg='orange',
               command=self.pause_timer).pack(side=LEFT, padx=5)

        Button(button_frame, text="Reset", font=('Helvetica', 12), bg='blue', fg='white',
               command=self.reset_timer).pack(side=LEFT, padx=5)

        Button(button_frame, text="Close", font=('Helvetica', 12), bg='red', fg='white',
               command=self.master.destroy).pack(side=LEFT, padx=5)

        # Timer display
        self.label_var = StringVar()
        self.label_var.set("0")
        self.timer_display = Label(self, textvariable=self.label_var, font=('Helvetica', 48))
        self.timer_display.pack(pady=10)

    def clear_placeholder(self, event):
        if self.input_time.get() == "Enter Time in seconds":
            self.input_time.delete(0, 'end')

    def start_timer(self):
        if self._alarm_id is not None:
            return  # Timer already running
        try:
            self._remaining_time = int(self.time_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number in seconds.")
            return
        self._paused = False
        self.update_timer()

    def pause_timer(self):
        self._paused = True
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
            self._alarm_id = None

    def reset_timer(self):
        self._paused = True
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
            self._alarm_id = None
        self._remaining_time = 0
        self.label_var.set("0")

    def update_timer(self):
        if self._paused:
            return
        self.label_var.set(str(self._remaining_time))
        if self._remaining_time > 0:
            self._remaining_time -= 1
            self._alarm_id = self.master.after(1000, self.update_timer)
        else:
            self._alarm_id = None
            messagebox.showinfo("Timer", "Time's up!")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("PyNexus Countdown Timer")
    app = Application(root)
    root.mainloop()
