import tkinter as tk
from tkinter import ttk
import threading
import webbrowser
import json
import os
import queue
import time

class WhatsAppNotifier:
    def __init__(self, timeout=5000):
        self.timeout = timeout
        self.notification_queue = queue.Queue()
        self.current_notification = None
        
        # Font configuration - clean dan minimal
        self.title_font = ('Arial', 8)           # Sangat kecil, regular
        self.sender_font = ('Arial', 9, 'bold') # Nama kontak bold
        self.message_font = ('Arial', 9)        # Pesan normal
        
        # Start notification handler
        self.start_notification_handler()
    
    def start_notification_handler(self):
        """Start handling notifications in a separate thread"""
        def handler():
            while True:
                try:
                    notification_data = self.notification_queue.get(timeout=1)
                    if notification_data:
                        self._show_notification_main_thread(notification_data)
                        time.sleep(0.3)
                except queue.Empty:
                    continue
                except Exception as e:
                    print(f"Notification handler error: {e}")
        
        handler_thread = threading.Thread(target=handler, daemon=True)
        handler_thread.start()
    
    def _show_notification_main_thread(self, data):
        """Show notification in main thread"""
        try:
            root = tk.Tk()
            root.title("WhatsApp Notifier")
            root.geometry("280x100")
            root.configure(bg='#ffffff')
            root.overrideredirect(True)
            
            # Position window at top-right corner
            screen_width = root.winfo_screenwidth()
            root.geometry(f"+{screen_width-300}+20")
            root.attributes('-topmost', True)
            
            # Main container
            main_frame = tk.Frame(root, bg='#ffffff')
            main_frame.pack(fill='both', expand=True, padx=8, pady=8)
            
            # Title - "Pesan Dari Whatsapp"
            title_label = tk.Label(
                main_frame,
                text="Pesan Dari Whatsapp",
                fg='#666666',
                bg='#ffffff',
                font=self.title_font
            )
            title_label.pack(anchor='w', pady=(0, 2))
            
            # Sender name
            sender_label = tk.Label(
                main_frame,
                text=data['sender'],
                fg='#128C7E',
                bg='#ffffff',
                font=self.sender_font
            )
            sender_label.pack(anchor='w', pady=(0, 5))
            
            # Message content
            message_text = data['message']
            if len(message_text) > 80:
                message_text = message_text[:77] + "..."
            
            message_frame = tk.Frame(main_frame, bg='#ffffff')
            message_frame.pack(fill='both', expand=True)
            
            message_label = tk.Label(
                message_frame,
                text=message_text,
                fg='#000000',
                bg='#ffffff',
                font=self.message_font,
                wraplength=260,
                justify='left',
                anchor='w'
            )
            message_label.pack(fill='both', expand=True)
            
            # Auto-close
            def close_notification():
                root.destroy()
            
            root.after(self.timeout, close_notification)
            
            # Click to open WhatsApp
            def open_whatsapp(event):
                webbrowser.open("https://web.whatsapp.com")
                close_notification()
            
            main_frame.bind("<Button-1>", open_whatsapp)
            message_frame.bind("<Button-1>", open_whatsapp)
            
            # Hover effect
            def on_enter(event):
                main_frame.configure(bg='#f5f5f5')
                message_frame.configure(bg='#f5f5f5')
                title_label.configure(bg='#f5f5f5')
                sender_label.configure(bg='#f5f5f5')
                message_label.configure(bg='#f5f5f5')
            
            def on_leave(event):
                main_frame.configure(bg='#ffffff')
                message_frame.configure(bg='#ffffff')
                title_label.configure(bg='#ffffff')
                sender_label.configure(bg='#ffffff')
                message_label.configure(bg='#ffffff')
            
            main_frame.bind("<Enter>", on_enter)
            main_frame.bind("<Leave>", on_leave)
            
            # Smooth fade in
            root.attributes('-alpha', 0.0)
            for i in range(1, 11):
                root.attributes('-alpha', i * 0.1)
                root.update()
                time.sleep(0.01)
            
            self.current_notification = root
            root.mainloop()
            
        except Exception as e:
            print(f"Error showing notification: {e}")
    
    def show_notification(self, sender, message, chat_id):
        """Add notification to queue"""
        self.notification_queue.put({
            'sender': sender,
            'message': message,
            'chat_id': chat_id
        })

def test_notification():
    """Test the final design"""
    notifier = WhatsAppNotifier()
    notifier.show_notification(
        sender="Ibuke Ghifari", 
        message="Hhh",
        chat_id="123456"
    )
    time.sleep(5)

if __name__ == "__main__":
    test_notification()