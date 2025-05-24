import tkinter as tk


class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("My Awesome Window")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        print("Window is now running and waiting for close...")
        self.root.mainloop()
        print("Window mainloop has exited.")

    def close(self):
        self.running = False
        print("Closing sequence initiated!")
        self.root.destroy()

    def draw_line(self, line_obj, fill_color="black"):
        line_obj.draw(self.canvas, fill_color)
