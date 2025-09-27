# Project One by: Antflash005 / 4l9ynX__X
memakai fitur app password bawaan dari google (gmail) dan tujuan untuk mengambil(graph) yang masuk ke gmail untuk di tampilkan dalam bentuk notif ke windows desktop pojok kanan bawah, dan code tersebut mampu mendefinisikan apa saja email yang pentin, sedang, dan tidak dan menyortir nya di notif


### Cara Penginstallan 
1. download file github dengan lakukan
   ```
   git clone https://github.com/Antflash500/project_1
   ```
   
2. Jika sudah install juga `requirments.txt` nya, dengan perintah :
   ```
   pip install -r requirments.txt
   ```
   
4. lalu masuk ke code `config.py` dan ubah code nya, seperti berikut :
   ```
   GMAIL_CONFIG = {
       'email': 'contoh@gmail.com',         # Ganti dengan emailmu
       'app_password': '16 code nya',       # Ganti dengan app password
   ```
   
5. jika sudah jalankan `main.py` dengan perintah :
   ```
   python main.py
   ```


### Current Feature :
- Real-time Notifications: Instant desktop alerts for new WhatsApp messages
- Custom Sound System: Different sounds for personal chats, groups, and priority contacts
- Clean Minimalist UI: Modern notification design without clutter
- Priority Contacts: Special notifications for important contacts
- One-Click Access: Click notification to open WhatsApp Web directly
- Lightweight: Low resource consumption, runs in background
- Auto-Reconnect: Automatic recovery from connection issues


### Technical Feature :
- WebSocket Integration: Real-time communication between components
- Multi-threading: Non-blocking notification system
- Cross-platform Ready: Designed for Windows (easily adaptable to Mac/Linux)
- Configurable Settings: Easy customization via config file


## Fitur yang akan datang (Incoming) adalah :
- System tray icon dengan menu
- Sound notifications
- Different popup colors berdasarkan priority
- Quick actions (mark as read, archive)
- Email history log
- Custom themes (light/dark mode)

