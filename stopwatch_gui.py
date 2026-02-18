#Stopwatch GUI version:
import tkinter as tk
running = False
seconds = 0

def update_time():
    global seconds 
    if running:
        seconds += 1
        mins = seconds // 60
        secs = seconds % 60
        time_label.config(text=f"{mins:02}:{secs:02}")
    root.after(1000,update_time)

def start():
    global running
    running = True
def stop():
    global running
    running = False
def reset():
    global seconds, running
    running = False
    seconds = 0
    time_label.config(text="00:00")

root = tk.Tk()
root.title("Stopwatch")
root.geometry("250x200")

time_label = tk.Label(root, text="00:00", font=("Arial", 30))
time_label.pack(pady=20)

tk.Button(root, text="Start", command=start).pack()
tk.Button(root, text="Stop", command=stop).pack()
tk.Button(root, text="Reset", command=reset).pack()

update_time()
root.mainloop()