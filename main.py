import customtkinter as ctk
from ui import ConvertApp

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("600x400")
    app = ConvertApp(root)
    root.mainloop()
    
    