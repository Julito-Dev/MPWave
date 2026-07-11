import customtkinter as ctk
from ui import ConvertApp

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("400x350")
    app = ConvertApp(root)
    root.mainloop()
    