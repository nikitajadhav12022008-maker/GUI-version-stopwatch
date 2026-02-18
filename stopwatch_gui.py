##python based Stopwatch GUI version:
# Import tkinter for GUI creation
import tkinter as tk


# -----------------------------
# Global Variables
# -----------------------------

# Indicates whether stopwatch is running or paused
running = False

# Stores total elapsed time in seconds
seconds = 0


# -----------------------------
# Function: Update Time
# -----------------------------
def update_time():
    """
    This function runs repeatedly every 1 second.
    If stopwatch is running → increase time
    Then update label on screen
    """
    global seconds

    if running:
        # Increase total seconds
        seconds += 1

        # Convert seconds into minutes and seconds
        mins = seconds // 60
        secs = seconds % 60

        # Display formatted time (MM:SS)
        time_label.config(text=f"{mins:02}:{secs:02}")

    # Schedule this function again after 1000 milliseconds (1 second)
    root.after(1000, update_time)


# -----------------------------
# Start Button Function
# -----------------------------
def start():
    """Starts the stopwatch"""
    global running
    running = True


# -----------------------------
# Stop Button Function
# -----------------------------
def stop():
    """Pauses the stopwatch"""
    global running
    running = False


# -----------------------------
# Reset Button Function
# -----------------------------
def reset():
    """Stops and resets the stopwatch to 00:00"""
    global seconds, running

    running = False
    seconds = 0

    # Update display immediately
    time_label.config(text="00:00")


# -----------------------------
# Create Main Window
# -----------------------------
root = tk.Tk()
root.title("Stopwatch")
root.geometry("250x220")
root.resizable(False, False)   # Prevent resizing


# -----------------------------
# Time Display Label
# -----------------------------
time_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 30, "bold")
)
time_label.pack(pady=20)


# -----------------------------
# Buttons
# -----------------------------
tk.Button(root, text="Start", width=10, command=start).pack(pady=3)
tk.Button(root, text="Stop", width=10, command=stop).pack(pady=3)
tk.Button(root, text="Reset", width=10, command=reset).pack(pady=3)


# Start update loop (runs forever every 1 second)
update_time()

# Keeps the window running
root.mainloop()
