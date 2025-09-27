const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const WebSocket = require('ws');

// WebSocket server untuk komunikasi dengan Python
const wss = new WebSocket.Server({ port: 8765 });

const client = new Client({
    authStrategy: new LocalAuth({
        clientId: "wa-notifier-client"
    }),
    puppeteer: {
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
});

client.on('qr', (qr) => {
    console.log('📱 Scan QR code ini dengan WhatsApp:');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('✅ WhatsApp client ready!');
});

client.on('message', async (message) => {
    // Skip pesan dari status broadcast
    if (message.from === 'status@broadcast') return;
    
    const contact = await message.getContact();
    const chat = await message.getChat();
    
    const messageData = {
        sender: contact.name || contact.pushname || 'Unknown',
        message: message.body,
        isGroup: chat.isGroup,
        chatId: chat.id._serialized,
        timestamp: new Date().toISOString(),
        type: chat.isGroup ? 'group' : 'personal'
    };
    
    console.log('📨 Pesan baru:', messageData.sender, '-', messageData.message.substring(0, 50));
    
    // Kirim ke semua connected Python clients
    wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(messageData));
        }
    });
});

client.on('disconnected', (reason) => {
    console.log('❌ Client disconnected:', reason);
});

// Start WebSocket server dan WhatsApp client
wss.on('listening', () => {
    console.log('🔌 WebSocket server running on port 8765');
    client.initialize();
});