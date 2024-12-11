import tkinter as tk
from tkinter import messagebox
import time
from collections import deque

class PasswordCrackerDetection:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Cracking Detection Tool")
        
        self.failed_attempts = deque(maxlen=5) 
        self.threshold_time = 60 
        
       
        self.label = tk.Label(root, text="Enter Password:")
        self.label.pack(pady=10)
        
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=5)
        
        self.login_button = tk.Button(root, text="Login", command=self.check_password)
        self.login_button.pack(pady=10)
        
        self.message = tk.Label(root, text="", fg="red")
        self.message.pack(pady=5)
        
    def check_password(self):
        entered_password = self.password_entry.get()
        if entered_password == "secret":
            self.message.config(text="Access Granted!", fg="green")
        else:
            self.message.config(text="Access Denied! Wrong password.", fg="red")
            self.log_failed_attempt()
        
    def log_failed_attempt(self):
        current_time = time.time()
        self.failed_attempts.append(current_time)
        
        if len(self.failed_attempts) == self.failed_attempts.maxlen:
            if (self.failed_attempts[-1] - self.failed_attempts[0]) < self.threshold_time:
                self.trigger_alert()
    
    def trigger_alert(self):
        messagebox.showwarning("Alert", "Multiple failed login attempts detected!")
        self.failed_attempts.clear()  

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCrackerDetection(root)
    root.mainloop()
