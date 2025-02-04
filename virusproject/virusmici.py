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

        # Load animation frames
        self.frames = [
            tk.PhotoImage(file="dr-house-house.gif"),
            tk.PhotoImage(file="frame_00_delay-0.03s.gif"),
            tk.PhotoImage(file="frame_01_delay-0.04s.gif"),
            tk.PhotoImage(file="frame_02_delay-0.03s.gif"),
            tk.PhotoImage(file="frame_04_delay-0.07s.gif"),
            tk.PhotoImage(file="frame_05_delay-0.03s.gif"),
            tk.PhotoImage(file="frame_50_delay-0.04s.gif"),
        ]
        self.current_frame = 0

        # Load additional images
        self.kakakep = tk.PhotoImage(file="szar.png")
        self.warning_images = [
            tk.PhotoImage(file="drhousebeszarok.png")
        ]

        # Initialize shitcount
        self.shitcount = 0
        self.animation_running = True  # Flag to control animation

        # Create a label to display the animation
        self.label = tk.Label(root, image=self.frames[0], bg="white")
        self.label.pack()

        # Make the label draggable
        self.make_draggable(self.label)

        # Start animation
        threading.Thread(target=self.animate, daemon=True).start()

        # Start threads
        threading.Thread(target=self.stealing, daemon=True).start()
        threading.Thread(target=self.szar_xd, daemon=True).start()
        threading.Thread(target=self.listen_for_quit, daemon=True).start()

    def animate(self):
        """Animates the cursor image if animation is running."""
        while True:
            if self.animation_running:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.label.config(image=self.frames[self.current_frame])
            time.sleep(0.2)  # 200ms delay

    def shitms(self):
        """Shows a warning image and stops animation."""
        self.animation_running = False  # Stop animation
        self.label.config(image=random.choice(self.warning_images))

    def reset_shitms(self):
        """Restores the original animation and restarts animation."""
        self.animation_running = True

    def make_draggable(self, widget):
        """Allows dragging the widget."""
        def start_drag(event):
            self._drag_start_x = event.x
            self._drag_start_y = event.y

        def drag_motion(event):
            x = self.root.winfo_x() + event.x - self._drag_start_x
            y = self.root.winfo_y() + event.y - self._drag_start_y
            self.root.geometry(f"+{x}+{y}")

        widget.bind("<Button-1>", start_drag)
        widget.bind("<B1-Motion>", drag_motion)

    def listen_for_quit(self):
        """Listen for 'q' key press to quit the program."""
        keyboard.wait("q")
        self.root.quit()
        
    def stealing(self):
        """Moves the cursor to a random position every few seconds."""
        screen_width, screen_height = pyautogui.size()
        delay = 5  # Default delay

        def check_key():
            nonlocal delay
            keyboard.wait("esc")  # Vár, amíg az 'esc'-et lenyomják
            delay = 1  # Ha lenyomják, véglegesen 1 lesz

        threading.Thread(target=check_key, daemon=True).start()

        while True:
            # Move the cursor to a random position
            KEP1 = random.randint(1, screen_width)
            KEP2 = random.randint(1, screen_height)
            pyautogui.moveTo(KEP1, KEP2)
            print(f"Moved to: ({KEP1}, {KEP2}), Delay: {delay}s")

            # Move the GIF window to follow the cursor
            self.root.geometry(f"+{KEP1}+{KEP2}")

            time.sleep(delay)



    def szar_xd(self):
        """Temporarily changes the cursor image before displaying szar.png."""
        while self.shitcount < 1000:
            time.sleep(10)  # Wait 10 seconds

            #  Show warning image (shitms) and stop animation
            self.shitms()
            print("shitms megjelent!")

            time.sleep(3)  # Wait so it's visible

            # Show szar.png
            gif_x, gif_y = self.root.winfo_x(), self.root.winfo_y()
            szar_window = tk.Toplevel(self.root)
            szar_window.overrideredirect(True)
            szar_window.attributes("-topmost", True)
            szar_window.geometry(f"+{gif_x}+{gif_y}")

            szar_label = tk.Label(szar_window, image=self.kakakep, bg="white")
            szar_label.pack()

            self.shitcount += 1
            print(f"szar.png megjelent! Jelenlegi shitcount: {self.shitcount}")

            #  Remove szar.png when clicked and restore animation
            def remove_image(event):
                szar_window.destroy()
                self.reset_shitms()  # Restore animation
                print("shitms eltűnt!")

            szar_label.bind("<Button-1>", remove_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedCursor(root)
    root.mainloop()
