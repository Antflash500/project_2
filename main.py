import websocket
import json
import time
import threading
import queue
from notification import WhatsAppNotifier
from sound_player import SoundPlayer
import os

class WANotifier:
    def __init__(self):
        self.config = self.load_config()
        self.notifier = WhatsAppNotifier(self.config.get('notification_timeout', 5000))
        self.sound_player = SoundPlayer()
        self.is_connected = False
        
        # Message queue untuk handle notifikasi secara sequential
        self.message_queue = queue.Queue()
        self.processing = False
        
    def load_config(self):
        """Load configuration from config.json"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "priority_contacts": [],
                "notification_timeout": 5000,
                "cooldown_period": 30
            }
    
    def determine_sound_type(self, message_data):
        """Determine which sound to play based on message type"""
        chat_id = message_data.get('chatId', '')
        
        # Check if it's a priority contact
        if chat_id in self.config.get('priority_contacts', []):
            return 'priority'
        
        # Check if it's a group message
        if message_data.get('isGroup', False):
            return 'group'
        
        # Default to personal
        return 'personal'
    
    def process_message_queue(self):
        """Process messages from queue one by one"""
        while not self.message_queue.empty():
            try:
                message_data = self.message_queue.get_nowait()
                
                print(f"📨 Processing message from: {message_data.get('sender', 'Unknown')}")
                
                # Determine sound type
                sound_type = self.determine_sound_type(message_data)
                
                # Play sound
                self.sound_player.play_sound(sound_type)
                
                # Show notification (dalam main thread)
                self.notifier.show_notification(
                    message_data.get('sender', 'Unknown'),
                    message_data.get('message', ''),
                    message_data.get('chatId', '')
                )
                
                # Cooldown antara notifikasi
                time.sleep(0.5)
                
                self.message_queue.task_done()
                
            except queue.Empty:
                break
        
        self.processing = False
    
    def on_message(self, ws, message):
        """Handle incoming messages from WebSocket"""
        try:
            message_data = json.loads(message)
            print(f"📨 Received message from: {message_data.get('sender', 'Unknown')}")
            
            # Add message to queue
            self.message_queue.put(message_data)
            
            # Process queue if not already processing
            if not self.processing:
                self.processing = True
                # Gunakan timer untuk process queue di main thread
                threading.Timer(0.1, self.process_message_queue).start()
            
        except json.JSONDecodeError as e:
            print(f"Error decoding message: {e}")
    
    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")
        self.is_connected = False
    
    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")
        self.is_connected = False
    
    def on_open(self, ws):
        print("✅ Connected to WhatsApp bot")
        self.is_connected = True
    
    def start(self):
        """Start the WebSocket client"""
        print("🚀 Starting WhatsApp Notifier...")
        print("📋 Configuration loaded:")
        print(f"   - Priority contacts: {len(self.config.get('priority_contacts', []))}")
        print(f"   - Notification timeout: {self.config.get('notification_timeout', 5000)}ms")
        print(f"   - Cooldown period: {self.config.get('cooldown_period', 30)}s")
        print("\n💡 Tips: Notifikasi akan muncul secara sequential untuk menghindari conflict")
        
        # WebSocket connection
        ws = websocket.WebSocketApp(
            "ws://localhost:8765",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        
        # Connection retry logic
        while True:
            try:
                ws.run_forever()
            except Exception as e:
                print(f"Connection error: {e}. Retrying in 10 seconds...")
                time.sleep(10)
            
            print("Reconnecting...")
            time.sleep(10)

if __name__ == "__main__":
    # Check if sounds folder exists
    if not os.path.exists('sounds'):
        os.makedirs('sounds')
        print("📁 Created sounds folder - please add your MP3 files:")
        print("   - personal.mp3")
        print("   - group.mp3") 
        print("   - priority.mp3")
        print("\n⚠️  Please add your sound files and restart the application")
    
    # Check if sound files exist
    sound_files = ['personal.mp3', 'group.mp3', 'priority.mp3']
    missing_files = [f for f in sound_files if not os.path.exists(os.path.join('sounds', f))]
    
    if missing_files:
        print(f"⚠️  Missing sound files: {missing_files}")
        print("💡 You can use temporary sound files or record your own")
    
    notifier = WANotifier()
    notifier.start()