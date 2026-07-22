import customtkinter as ctk
from ui import ConvertApp
import sys
import os


def get_assets_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("600x400")
    root.iconbitmap(get_assets_path("assets/favicon.ico"))
    app = ConvertApp(root)
    root.mainloop()
    
    