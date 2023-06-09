from flask import Blueprint, render_template
import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

timer_bp = Blueprint('timer', __name__)
class PomodoroTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Let's go fishing!")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="app/static/iconified/logo.png"))

        self.s = ttk.Style()
        self.s.configure("TNotebook.tab", font=('Ubuntu', 16))
        self.s.configure("TButton.tab", font=('Ubuntu', 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)

        self.fishing_timer_label = ttk.Label(self.tab1, text='25:00', font=('Ubuntu', 50))
        self.fishing_timer_label.pack(pady=20)

        self.reel_in_timer_label = ttk.Label(self.tab2, text='05:00', font=('Ubuntu', 50))
        self.reel_in_timer_label.pack(pady=20)

        self.tabs.add(self.tab1, text="Cast Line")
        self.tabs.add(self.tab2, text="Reel In")

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.reset_button = ttk.Button(self.grid_layout, text='Reset', command=self.reset_clock)
        self.reset_button.grid(row=0, column=1)

        self.Chill_Fish_counter_label = ttk.Label(self.grid_layout,text="Fish Caught: 0", font= ("Ubuntu", 16)) 
        self.Chill_Fish_counter_label.grid(row=1,column=0,columnspan=3, pady=10)   

        self.chill_fish = 0
        self.stopped=False
        self.running = False

        self.root.mainloop()


    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds =divmod(full_seconds,60)
                self.fishing_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1

            if not self.stopped:
                self.chill_fish += 1
                self.Chill_Fish_counter_label.config(text=f"Fish caught: {self.chill_fish}")
                if self.chill_fish % 4 == 0:
                    self.tabs.select(1)
                    self.start_timer()
                else:
                    self.tabs.select(1)
                self.start_timer()


        elif timer_id ==2:
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds =divmod(full_seconds,60)
                self.reel_in_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1  
            if not self.stopped:
                self.tabs.select(0)
                self.start_timer()

    def reset_clock(self):
        self.stopped = True
        self.chill_fish= 0
        self.Chill_Fish_counter_label.config(text="25:00")
        self.reel_in_timer_label.config(text="05:00")
        self.Chill_Fish_counter_label.config(text="Caught Fish: 0")
        self.running = False 

PomodoroTimer()
