import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import threading
from converter import convert


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class ConvertApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor MP3 <-> WAV")
        self.file_route = None
        self.output_folder = None
        self._buildUI()
        
        
    def _buildUI(self):
        self.label_file = ctk.CTkLabel(self.root, text="No file Selected")
        self.label_file.pack(pady = 10)
        
        ctk.CTkButton(self.root, text="Select File", command=self.select_file).pack(pady=5)
        self.label_folder = ctk.CTkLabel(self.root, text="Destination: same as file")
        self.label_folder.pack(pady=10)
        
        
        ctk.CTkButton(self.root, text="Select destination Folder", command=self.select_folder).pack(pady=5)
        
        self.convert_button = ctk.CTkButton(self.root, text="Convert", command=self.convert_file)
        self.convert_button.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self.root, mode="indeterminate")
        
        
        
    def select_file(self):
        route = filedialog.askopenfilename(filetypes=[("Audio", "*.mp3 *.wav")])
        if route:
            self.file_route = route
            self.label_file.configure(text=os.path.basename(route))
            
    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.label_folder.configure(text=f"Destination: {folder}")
            
            
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