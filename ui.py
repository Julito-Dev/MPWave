import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from converter import convert


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class ConvertApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor MP3 <-> WAV")
        self.file_route = None
        self._buildUI()
        
        
    def _buildUI(self):
        self.label_file = ctk.CTkLabel(self.root, text="No file Selected")
        self.label_file.pack(pady = 20)
        
        ctk.CTkButton(self.root, text="Select File", command=self.select_file).pack(pady=5)
        ctk.CTkButton(self.root, text="Convert", command=self.convert_file).pack(pady=5)
        
        
    def select_file(self):
        route = filedialog.askopenfilename(filetypes=[("Audio", "*.mp3 *.wav")])
        if route:
            self.file_route = route
            self.label_file.configure(text=os.path.basename(route))
            
    def convert_file(self):
        if not self.file_route:
            messagebox.showwarning("Atention", "First, Select a File.")
            return

        exit = os.path.splitext(self.file_route)[1].lower()
        exit_format = "wav" if exit == ".mp3" else "mp3"
            
        try:
            result_route = convert(self.file_route, exit_format)
            messagebox.showinfo("Finished", f"Converted: {result_route}")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))