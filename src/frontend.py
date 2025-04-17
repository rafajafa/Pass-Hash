import tkinter as tk
from tkinter import ttk
import main as backend
import tkinter.font as tkfont

class Frontend:
    def __init__(self, root):
        self.root = root
        self.root.title("Passhash")
        self.root.geometry("350x400")
        self.root.resizable(True, True)
        self.root.minsize(300, 350)
        # self.root.maxsize(800, 800)
        self.root.configure(bg="#f4f4f4")
        
        self.base_font = tkfont.Font(family="Arial", size=12)
        self.title_font = tkfont.Font(family="Arial", size=24, weight="bold")
        self.button_font = tkfont.Font(family="Arial", size=12)
        self.root.bind("<Configure>", self.on_resize)

        self.root.password = tk.StringVar()
        self.use_upper = tk.BooleanVar()
        self.use_numbers = tk.BooleanVar()
        self.use_special = tk.BooleanVar()
        self.length = tk.IntVar(value=10)

        self.build_ui()

    def build_ui(self):
        # Use a single main frame
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky="NSEW")
        
        # Make the root window and main frame resizable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Set up styles
        style = ttk.Style()
        style.configure("TButton", font=self.button_font)
        style.configure("TCheckbutton", font=self.base_font)
        style.configure("TLabel", font=self.base_font)

        # Title
        ttk.Label(main_frame, text="Passhash", font=self.title_font).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Checkboxes
        ttk.Checkbutton(main_frame, text="Include uppercase letters?", variable=self.use_upper).grid(row=1, column=0, columnspan=2, sticky="W")
        ttk.Checkbutton(main_frame, text="Include numbers?", variable=self.use_numbers).grid(row=2, column=0, columnspan=2, sticky="W")
        ttk.Checkbutton(main_frame, text="Include special characters?", variable=self.use_special).grid(row=3, column=0, columnspan=2, sticky="W")

        # Length
        ttk.Label(main_frame, text="Password length:").grid(row=4, column=0, pady=(10, 0), sticky="W")
        ttk.Entry(main_frame, textvariable=self.length, width=10).grid(row=4, column=1, pady=(10, 0), sticky="EW")

        # Base password
        ttk.Label(main_frame, text="Base password:", font=self.base_font).grid(row=5, column=0, pady=(10, 0), sticky="W")
        self.password_entry = ttk.Entry(main_frame, textvariable=self.root.password, show="*")
        self.password_entry.grid(row=5, column=1, pady=(10, 0), sticky="EW")

        # Submit button
        self.submit_button = ttk.Button(main_frame, text="Submit", command=self.submit, style="TButton")
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=15)

        # Result label
        self.secure_password_label = ttk.Label(main_frame, text="", foreground="green", wraplength=360, font=self.base_font)
        self.secure_password_label.grid(row=7, column=0, columnspan=2, pady=(0, 10), sticky="EW")

        # Error label
        self.error_label = ttk.Label(main_frame, text="", foreground="red", wraplength=360, font=self.base_font)
        self.error_label.grid(row=8, column=0, columnspan=2, sticky="EW")

        # Copy button
        self.copy_button = ttk.Button(main_frame, text="Copy to clipboard", command=self.copy, style="TButton")
        self.copy_button.grid(row=9, column=0, columnspan=2, pady=(10, 0))

    def on_resize(self, event):
        width = event.width

        # Calculate dynamic font sizes
        title_size = max(16, int(width / 20))
        base_size = max(10, int(width / 40))
        button_size = max(10, int(width / 40))

        # Update the font sizes
        self.title_font.configure(size=title_size)
        self.base_font.configure(size=base_size)
        self.button_font.configure(size=button_size)
        
    
    def submit(self):
        password = self.root.password.get()
        try:
            secure_password = backend.hashpass(
                password,
                int(self.length.get()),
                self.use_upper.get(),
                self.use_numbers.get(),
                self.use_special.get()
            )

            self.error_label.config(text="")
            self.secure_password_label.config(text=secure_password)

        except ValueError as e:
            self.secure_password_label.config(text="")
            self.error_label.config(text="Error: " + str(e))

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.secure_password_label.cget("text"))
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = Frontend(root)
    root.mainloop()
