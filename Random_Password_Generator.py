import tkinter as tk
from tkinter import messagebox
import string
import secrets
import math
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SecurePass Generator")
        self.root.geometry("400x450")
        self.lfrem = tk.Frame(root)
       
        tk.Label(self.lfrem, text="Password Length:").pack(side='left',padx=10)
        self.length_var = tk.IntVar(value=12)
        self.length_spinbox = tk.Spinbox(self.lfrem, from_=4, to=64, textvariable=self.length_var, width=5)
        self.length_spinbox.pack()
        self.lfrem.pack()

        
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        frame_opts = tk.Frame(root)
        frame_opts.pack(pady=10)
        tk.Checkbutton(frame_opts, text="A-Z", variable=self.use_upper).grid(row=0, column=0)
        tk.Checkbutton(frame_opts, text="a-z", variable=self.use_lower).grid(row=0, column=1)
        tk.Checkbutton(frame_opts, text="0-9", variable=self.use_digits).grid(row=1, column=0)
        tk.Checkbutton(frame_opts, text="!@#", variable=self.use_symbols).grid(row=1, column=1)

        self.frem = tk.Frame(root)
        tk.Label(self.frem, text="Exclude Characters (e.g. 'l1O0'):").pack(side='left',padx=5)
        self.exclude_entry = tk.Entry(self.frem)
        self.exclude_entry.pack()
        self.frem.pack()
   
        tk.Button(root,width=40, text="GENERATE PASSWORD", bg="lightgreen", command=self.generate_password).pack(pady=15)

        self.frm = tk.Frame(root)
        self.password_entry = tk.Entry(self.frm, font=("Courier", 14), justify='center')
        self.password_entry.pack(pady=5,side='left' ,padx=20)

        
        tk.Button(self.frm, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)
        self.frm.pack()
       
        self.strength_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
        self.strength_label.pack(pady=10)

    def generate_password(self):

        chars = ""
        mandatory_chars = []
        
        exclusions = set(self.exclude_entry.get())
        
   
        def get_filtered_set(character_set):
            return [c for c in character_set if c not in exclusions]

        if self.use_upper.get():
            pool = get_filtered_set(string.ascii_uppercase)
            if pool: 
                chars += "".join(pool)
                mandatory_chars.append(secrets.choice(pool))
        
        if self.use_lower.get():
            pool = get_filtered_set(string.ascii_lowercase)
            if pool: 
                chars += "".join(pool)
                mandatory_chars.append(secrets.choice(pool))

        if self.use_digits.get():
            pool = get_filtered_set(string.digits)
            if pool: 
                chars += "".join(pool)
                mandatory_chars.append(secrets.choice(pool))

        if self.use_symbols.get():
            pool = get_filtered_set(string.punctuation)
            if pool: 
                chars += "".join(pool)
                mandatory_chars.append(secrets.choice(pool))

    
        length = self.length_var.get()
        if not chars:
            messagebox.showwarning("Error", "Please select at least one character type.")
            return
        if length < len(mandatory_chars):
            messagebox.showwarning("Error", f"Length must be at least {len(mandatory_chars)} to satisfy rules.")
            return

     
 
        remaining_length = length - len(mandatory_chars)
        password_list = mandatory_chars + [secrets.choice(chars) for _ in range(remaining_length)]
        
      
        shuffled_password = ''.join(secrets.SystemRandom().sample(password_list, len(password_list)))

        
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, shuffled_password)
        self.assess_strength(length, len(chars))

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

    def assess_strength(self, length, pool_size):
        
        
        if pool_size == 0: return
        entropy = length * math.log2(pool_size)
        
        if entropy < 50:
            self.strength_label.config(text="Weak", fg="red")
        elif entropy < 80:
            self.strength_label.config(text="Moderate", fg="orange")
        else:
            self.strength_label.config(text="Strong", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
