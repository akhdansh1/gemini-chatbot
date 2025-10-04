import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Konfigurasi API Key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Inisialisasi model
model = genai.GenerativeModel('gemini-2.5-flash')

def chat_with_history():
    print("=== Chatbot Gemini AI dengan Memori ===")
    print("Ketik 'keluar' untuk mengakhiri chat")
    print("Ketik 'reset' untuk memulai percakapan baru\n")
    
    # Mulai chat session
    chat_session = model.start_chat(history=[])
    
    while True:
        # Input dari user
        user_input = input("Anda: ")
        
        # Cek perintah khusus
        if user_input.lower() in ['keluar', 'exit', 'quit']:
            print("Terima kasih telah menggunakan chatbot!")
            break
        
        if user_input.lower() == 'reset':
            chat_session = model.start_chat(history=[])
            print("Percakapan telah direset!\n")
            continue
        
        # Kirim pesan dan dapatkan response
        response = chat_session.send_message(user_input)
        
        # Tampilkan response
        print(f"Bot: {response.text}\n")

if __name__ == "__main__":
    chat_with_history()