# 🤖 Gemini AI Chatbot

Chatbot berbasis Gemini AI dengan Flask dan interface web yang modern.

![Gemini Chatbot](https://img.shields.io/badge/Gemini-AI%20Chatbot-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Flask](https://img.shields.io/badge/Flask-3.0.0-orange)

## ✨ Fitur

- 💬 Chat interaktif dengan Gemini AI
- 🧠 Memori percakapan (context awareness)
- 🎨 UI modern dan responsive
- 🔄 Reset percakapan
- 🚀 Fast response dengan Gemini 2.5 Flash

## 🛠️ Teknologi

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini 2.5 Flash
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render / Railway / Vercel

## 📦 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/USERNAME/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Buat Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
```bash
# Copy .env.example menjadi .env
cp .env.example .env

# Edit .env dan tambahkan API key Anda
# GEMINI_API_KEY=your_api_key_here
```

### 5. Dapatkan API Key
1. Buka [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Login dengan akun Google
3. Klik "Create API Key"
4. Copy API key dan paste ke file `.env`

### 6. Jalankan Aplikasi
```bash
python app.py
```

Buka browser: `http://localhost:5000`

## 🚀 Deployment

### Deploy ke Render

1. Push code ke GitHub
2. Buka [Render](https://render.com)
3. Create New → Web Service
4. Connect repository Anda
5. Isi konfigurasi:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Tambahkan Environment Variable:
   - Key: `GEMINI_API_KEY`
   - Value: `your_api_key`
7. Deploy!

### Deploy ke Railway

1. Push code ke GitHub
2. Buka [Railway](https://railway.app)
3. New Project → Deploy from GitHub
4. Pilih repository
5. Tambahkan Environment Variable `GEMINI_API_KEY`
6. Deploy otomatis!

## 📁 Struktur Project

```
gemini-chatbot/
├── app.py                  # Main Flask application
├── templates/
│   └── index.html         # Frontend UI
├── .env                   # Environment variables (tidak di-commit)
├── .env.example           # Template environment variables
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
└── README.md            # Dokumentasi
```

## 🔧 Konfigurasi

### Ganti Model AI
Edit `app.py`:
```python
# Gunakan model lain jika diperlukan
model = genai.GenerativeModel('gemini-2.5-flash')  # Default
# model = genai.GenerativeModel('gemini-2.5-pro')  # Lebih pintar
# model = genai.GenerativeModel('gemini-2.0-flash') # Alternatif
```

### Ubah Port
Edit `.env`:
```
PORT=8000
```

## 📝 API Endpoints

- `GET /` - Halaman utama
- `POST /chat` - Kirim pesan ke chatbot
- `POST /reset` - Reset percakapan

## 🤝 Kontribusi

Kontribusi selalu welcome! Silakan:
1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 License

MIT License - bebas digunakan untuk project apapun!

## 👨‍💻 Author

Your Name - [GitHub](https://github.com/USERNAME)

## 🙏 Credits

- [Google Gemini AI](https://ai.google.dev/)
- [Flask Framework](https://flask.palletsprojects.com/)

---

⭐ Jika project ini membantu, berikan star ya!