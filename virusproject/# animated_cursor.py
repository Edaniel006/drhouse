# animated_cursor.py
import tkinter as tk
import pyautogui
import keyboard
import threading
import random
import time


class AnimatedCursor:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes("-topmost", True)  # Keep window on top
        self.root.attributes("-transparentcolor", "white")  # Make white transparent

        # Load animal frames (replace with your own images)
        self.frames = [
            tk.PhotoImage(file="dr-house-house.gif"),
            tk.PhotoImage(file="dr-house-house.gif"),
            tk.PhotoImage(file="frame_00_delay-0.03s.gif"),
            tk.PhotoImage(file="frame_01_delay-0.04s.gif"),
            tk.PhotoImage(file="frame_02_delay-0.03s.gif"),
            tk.PhotoImage(file="frame_04_delay-0.07s.gif"),
            tk.PhotoImage(file="frame_05_delay-0.03s.gif"),
            tk.PhotoImage(file="frame_50_delay-0.04s.gif"),
        ]
        self.current_frame = 0

        # Create a label to display the animation
        self.label = tk.Label(root, image=self.frames[0], bg="white")
        self.label.pack()

        # Start animation and cursor tracking
        self.animate()
        self.track_cursor()

        # Start the "stealing" functionality in a separate thread
        self.stealing_thread = threading.Thread(target=self.stealing)
        self.stealing_thread.daemon = True
        self.stealing_thread.start()

        # Start a thread to listen for the quit key
        self.quit_thread = threading.Thread(target=self.listen_for_quit)
        self.quit_thread.daemon = True
        self.quit_thread.start()

    def animate(self):
        # Cycle through frames
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.label.config(image=self.frames[self.current_frame])
        self.root.after(100, self.animate)  # Update every 100ms

    def track_cursor(self):
        # Get cursor position and move the window
        x, y = pyautogui.position()
        self.root.geometry(f"+{x-100}+{y-50}")  # Offset to avoid covering the cursor
        self.root.after(10, self.track_cursor)  # Update every 10ms

    def listen_for_quit(self):
        # Listen for the 'q' key to quit the script
        keyboard.wait("q")
        self.root.quit()

   
    def stealing(self):
        screen_width, screen_height = pyautogui.size()  # Get the screen resolution dynamically
        delay = 5  # Default delay is 5 seconds

        while True:
            KEP1 = random.randint(1, screen_width)  # Random X-coordinate
            KEP2 = random.randint(1, screen_height)  # Random Y-coordinate
            pyautogui.moveTo(KEP1, KEP2)  # Move the cursor to the random position
            print(f"Moved to: ({KEP1}, {KEP2})")  # Optional: Print the position for debugging

            # Check if 'esc' is pressed to adjust the delay
            if keyboard.is_pressed('x'):
                delay = 1 # Reduce delay to 1 second
            else:
                delay = 5  # Default delay is 5 seconds

            time.sleep(delay)  # Wait for the specified delay before the next move

            


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedCursor(root)
    root.mainloop()
