import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Konfigurasi API Key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Inisialisasi model
model = genai.GenerativeModel('gemini-2.5-flash')

def chat():
    print("=== Chatbot Gemini AI ===")
    print("Ketik 'keluar' untuk mengakhiri chat\n")
    
    while True:
        # Input dari user
        user_input = input("Anda: ")
        
        # Cek jika user ingin keluar
        if user_input.lower() in ['keluar', 'exit', 'quit']:
            print("Terima kasih telah menggunakan chatbot!")
            break
        
        # Generate response dari Gemini
        response = model.generate_content(user_input)
        
        # Tampilkan response
        print(f"Bot: {response.text}\n")

if __name__ == "__main__":
    chat()