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
        self.root.title("Multimedia Conversor")
        self.file_route = None
        self.output_folder = None
        self._buildUI()
        
        
    def _buildUI(self):
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1, weight=1)
        
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)
        self.root.rowconfigure(2, weight = 0)
    
        
        
        #LEFT FRAME: INPUT
        
        self.left_frame = ctk.CTkFrame(self.root)
        self.left_frame.grid(row= 0, column= 0, padx= 10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.left_frame, text= "Input", font=("", 16, "bold")).pack(pady=10)
        self.label_file = ctk.CTkLabel(self.left_frame, text="No file Selected")
        self.label_file.pack(pady = 10)
        ctk.CTkButton(self.left_frame, text="Select File", command=self.select_file).pack(pady=5)
        
        
        
        #RIGHT FRAME: OUTPUT
        self.right_frame = ctk.CTkFrame(self.root)
        self.right_frame.grid(row=0, column = 1, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.right_frame, text= "Output", font=("", 16, "bold")).pack(pady=(15,5))
        
        self.label_folder = ctk.CTkLabel(self.right_frame, text="Destination: same as input file")
        self.label_folder.pack(pady=10)
        
        
        
        ctk.CTkButton(self.right_frame, text="Select destination Folder", command=self.select_folder).pack(pady=5)
        
        self.format_menu = ctk.CTkOptionMenu(self.right_frame, values=["wav","mp3"])
        self.format_menu.pack()
        
        #Convert button and loading bar
        
        self.convert_button = ctk.CTkButton(self.root, text="Convert", command=self.convert_file)
        self.convert_button.grid(row=1, column=0, columnspan= 2, pady=10, padx=(5,10), sticky="ew")
        
        self.progress_bar = ctk.CTkProgressBar(self.root, mode="indeterminate")
        self.progress_bar.grid(row = 2, column = 0, columnspan=2, padx=10, pady=(0,10), sticky="ew")
        self.progress_bar.grid_remove()
        
    def select_file(self):
        route = filedialog.askopenfilename(filetypes=[("Audio", "*.mp3 *.wav"), ("Video", "*.mp4")])
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
        exit_format = self.format_menu.get()
        
        self._set_loading_state(True)
        
        thread = threading.Thread(target=self._run_conversion, args=(exit_format,))
        thread.start()
           
           
    def _run_conversion(self, exit_format):
        try:
            result_route = convert(self.file_route, exit_format, self.output_folder)
            self.root.after(0, self._on_success, result_route)
        except Exception as e:
            self.root.after(0, self._on_error, str(e))

    def _on_success(self, result_route):
        self._set_loading_state(False)
        messagebox.showinfo("Finished", f"Converted: {result_route}")
            
    def _on_error(self, error_msg):
        self._set_loading_state(False)
        messagebox.showerror("Error", error_msg)
        
    def _set_loading_state(self, loading):
        if loading:
            self.convert_button.configure(state="disabled", text="Converting...")
            self.progress_bar.grid()
            self.progress_bar.start()
            
        else:
            self.progress_bar.stop()
            self.progress_bar.grid_remove()
            self.convert_button.configure(state="normal", text="Convert")