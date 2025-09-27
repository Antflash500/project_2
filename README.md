# Project Two by: Antflash005 / 4l9ynX__X
memakai fitur dari [wwebjs](https://wwebjs.dev/), code ini mampu menerima pesan dan menampilkan nya dalam bentuk notif window layak nya wa pada umum nya. Namun, ini tidak memakai Whatsapp Official yang harus install di desktop dahulu. Namun, hanya sekali scan Code QR maka code akan berjalan otomatis seperti menerima pesan, nama kontak pengirim, dan isi pesan yang dikirim


## Cara Penginstallan 
1. download file github dengan lakukan
   ```
   git clone https://github.com/Antflash500/project_2
   ```
   
2. Jika sudah install juga `requirments.txt` nya, dengan perintah :
   ```
   pip install -r requirments.txt
   ```
   
3. lalu masuk ke folder `sounds/` dan tambahkan sound yang diinginkan sesuai format berikut
   ```
   group.mp3
   personal.mp3
   priority.mp3
   ```
4. Lalu Edit `config.json` untuk tambahkan nomor priority `(format: 6281234567890@c.us)`, contoh :
   ```
       "priority_contacts": [
        "6283122085487@c.us",      > ganti nomer nya
        "6282315550135@c.us"       > ganti nomer nya
    ],
   ```
5. masukkan perintah `npm install` untuk menginstall `library .js` nya
6. jalankan perintah berikut :
   ```
   # Terminal 1 - WhatsApp Bot
   node whatsapp-bot.js

   # Terminal 2 - Python Notifier  
   python main.py
   ```
7. Scan `Code QR` dengan `Whatsapp Mobile`, dan code siap di gunakan



## Feature in Project :
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
###  In Development :
- Message Quick Replies: Send predefined replies directly from notification
- Notification History: View missed notifications history
- Custom Theme Support: Dark/Light mode toggle


### Planned Features :
- Advanced Filtering: Filter notifications by keywords, contacts, or groups
- Scheduled Muting: Auto-mute during specific hours (sleep/work mode)
- Multiple WhatsApp Accounts: Support for managing multiple numbers
- Message Statistics: Analytics for message frequency and patterns
- Backup Integration: Auto-backup important conversations
- Mobile Companion App: Sync with mobile app for enhanced features


### UI/UX Improvements :
- Animated Notifications: Smooth entrance/exit animations
- Interactive Notifications: Mark as read/reply directly from popup
- Custom Position Settings: Choose notification screen position
- Size Customization: Adjustable notification size


### Security & Privacy :
- End-to-End Encryption: Secure local data storage
- Privacy Mode: Hide message content in notifications
- Auto-Cleanup: Automatic deletion of old logs


### Special Thanks To :
`Deepseek`
`wwebjs`
`python - thinker`
`javascript edition`
`my brain :3`
