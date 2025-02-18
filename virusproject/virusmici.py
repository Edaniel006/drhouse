import tkinter as tk
import pyautogui
import keyboard
import threading
import random
import time
import os
import pynput.mouse
import math

class AnimatedCursor:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Hide window frame
        self.root.attributes("-topmost", True)  # Keep on top
        self.root.attributes("-transparentcolor", "white")  # Make white transparent

        # Load animation frames
        self.frames = [
            tk.PhotoImage(file="New Piskel-1.png.png"),
            tk.PhotoImage(file="New Piskel-2.png.png"),
            tk.PhotoImage(file="New Piskel-3.png.png"),
            tk.PhotoImage(file="New Piskel-4.png.png"),
        ]
        self.current_frame = 0

        # Load images
        self.kakakep = tk.PhotoImage(file="szar.png")

        self.current_kaka = 0
        self.warning_images = [
            tk.PhotoImage(file="sprite_1.png"),
            tk.PhotoImage(file="sprite_2.png"),
            tk.PhotoImage(file="sprite_3.png"),
            tk.PhotoImage(file="sprite_4.png"),
        ]

        # Variables
        self.shitcount = 0
        self.animation_running = True
        self.position = (100, 100)
        self.last_activity_time = time.time()
        self.shitwarning_kep = False

        # Create label for animation
        self.label = tk.Label(root, image=self.frames[0], bg="white")
        self.label.pack()

        # Make window draggable
        self.make_draggable(self.label)

        # Start threads
        threading.Thread(target=self.animate, daemon=True).start()
        threading.Thread(target=self.stealing, daemon=True).start()
        threading.Thread(target=self.szar_xd, daemon=True).start()
        threading.Thread(target=self.listen_for_quit, daemon=True).start()
        threading.Thread(target=self.check_activity, daemon=True).start()

    def animate(self):
        """Animates the cursor image if animation is running."""
        while True:
            if self.animation_running:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.label.config(image=self.frames[self.current_frame])
            time.sleep(0.5)

    def make_draggable(self, widget):
        """Makes the window draggable."""
        def start_drag(event):
            self._drag_start_x = event.x
            self._drag_start_y = event.y

        def drag_motion(event):
            x = self.root.winfo_x() + event.x - self._drag_start_x
            y = self.root.winfo_y() + event.y - self._drag_start_y
            self.root.geometry(f"+{x}+{y}")
            self.position = (x, y)
            self.last_activity_time = time.time()

        widget.bind("<Button-1>", start_drag)
        widget.bind("<B1-Motion>", drag_motion)

    def check_activity(self):
        """Checks if the cursor has been inactive for 10 seconds and shuts down the PC."""
        while True:
            elapsed_time = time.time() - self.last_activity_time
            print(f"Shutdown in {10 - math.floor(elapsed_time)} sec")
            if elapsed_time > 10:
                print("Initiating shutdown!")
                self.shutdown_angy()
                break
            time.sleep(1)

    def shutdown_angy(self):
        """Shuts down the PC in 10 seconds."""
        os.system("shutdown -s -t 10")
        keyboard.block_key()
        mouse = pynput.mouse.Controller()
        print("Shutdown started!")

    def stealing(self):
        """Randomly moves the mouse every few seconds."""
        screen_width, screen_height = pyautogui.size()
        delay = 5

        def check_key():
            nonlocal delay
            keyboard.wait("esc")
            delay = 1  # Reduce delay if ESC is pressed

        threading.Thread(target=check_key, daemon=True).start()

        while True:
            KEP1 = random.randint(1, screen_width)
            KEP2 = random.randint(1, screen_height)
            pyautogui.moveTo(KEP1, KEP2)
            print(f"Mouse moved: ({KEP1}, {KEP2}), Delay: {delay}s")
            self.root.geometry(f"+{KEP1 - 55}+{KEP2 - 55}")

            time.sleep(delay)

    def szar_xd(self):
        """Displays a poop image periodically."""
        while self.shitcount < 1000:
            time.sleep(10)

            # Show warning
            self.shitms()
            print("Warning appeared!")

            time.sleep(3)  # Keep warning visible

            # Show poop image
            gif_x, gif_y = self.root.winfo_x(), self.root.winfo_y()
            szar_window = tk.Toplevel(self.root)
            szar_window.overrideredirect(True)
            szar_window.attributes("-topmost", True)
            szar_window.geometry(f"+{gif_x}+{gif_y}")

            szar_label = tk.Label(szar_window, image=self.kakakep, bg="white")
            szar_label.pack()

            self.shitcount += 1
            print(f"Poop image shown! Count: {self.shitcount}")

            # Remove poop image on click
            def remove_image(event):
                szar_window.destroy()
                self.reset_shitms()
                print("Warning removed!")

            szar_label.bind("<Button-1>", remove_image)

    def shitms(self):
        """Displays a warning animation and stops normal animation."""
        self.animation_running = False
        self.shitwarning_kep = True

        def warning_animation():
            while self.shitwarning_kep:
                self.current_kaka = (self.current_kaka + 1) % len(self.warning_images)
                self.label.config(image=self.warning_images[self.current_kaka])
                time.sleep(0.5)

        threading.Thread(target=warning_animation, daemon=True).start()

    def reset_shitms(self):
        """Resets the animation back to normal."""
        self.shitwarning_kep = False
        self.animation_running = True
        self.label.config(image=self.frames[self.current_frame])

    def listen_for_quit(self):
        """Listens for 'q' key press to exit."""
        keyboard.wait("q")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedCursor(root)
    root.mainloop()
