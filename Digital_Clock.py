import tkinter as tk
from time import strftime

class CreativeClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon Cyber Clock")
        self.root.geometry("450x450")
        self.root.configure(bg="#0B0F19")
        self.root.resizable(False, False)

        # Canvas for custom graphics and progress rings
        self.canvas = tk.Canvas(
            root, width=450, height=450, bg="#0B0F19", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")

        cx, cy, r = 225, 225, 160  # Center position & radius

        # 1. Outer background track
        self.canvas.create_oval(
            cx - r, cy - r, cx + r, cy + r,
            outline="#1E293B", width=12
        )

        # Get current time metrics
        now_time = strftime("%I:%M:%S")
        am_pm = strftime("%p")
        day_str = strftime("%A")
        date_str = strftime("%b %d, %Y")
        sec = int(strftime("%S"))

        # 2. Dynamic seconds arc (Fills up as seconds progress)
        angle = (sec / 60) * 360
        if angle > 0:
            self.canvas.create_arc(
                cx - r, cy - r, cx + r, cy + r,
                start=90, extent=-angle,
                style="arc", outline="#00F0FF", width=12
            )

        # 3. Inner Card Background
        self.canvas.create_oval(
            cx - (r - 25), cy - (r - 25), cx + (r - 25), cy + (r - 25),
            fill="#111827", outline="#1F293D", width=2
        )

        # 4. Main Time Display
        self.canvas.create_text(
            cx - 15, cy - 20,
            text=now_time, fill="#F9FAFB",
            font=("Consolas", 34, "bold")
        )

        # 5. AM/PM Indicator
        self.canvas.create_text(
            cx + 120, cy - 20,
            text=am_pm, fill="#00F0FF",
            font=("Segoe UI", 12, "bold")
        )

        # 6. Day Badge
        self.canvas.create_text(
            cx, cy + 25,
            text=day_str.upper(), fill="#F43F5E",
            font=("Segoe UI", 12, "bold")
        )

        # 7. Date Stamp
        self.canvas.create_text(
            cx, cy + 50,
            text=date_str, fill="#9CA3AF",
            font=("Segoe UI", 11)
        )

        # Refresh every second
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = CreativeClock(root)
    root.mainloop()