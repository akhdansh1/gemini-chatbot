import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Konfigurasi API Key
api_key = os.getenv('GEMINI_API_KEY')
print(f"API Key loaded: {api_key[:10]}..." if api_key else "API Key tidak ditemukan!")

genai.configure(api_key=api_key)

# Cek model yang tersedia
print("\n=== Model yang Tersedia ===")
try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"✓ {model.name}")
            print(f"  Display Name: {model.display_name}")
            print(f"  Description: {model.description}")
            print()
except Exception as e:
    print(f"Error: {e}")

# Test generate content dengan model yang tersedia
print("\n=== Test Generate Content ===")
model_names_to_try = [
    'gemini-1.5-flash',
    'gemini-1.5-pro', 
    'gemini-pro',
    'gemini-1.5-flash-latest',
    'gemini-1.5-pro-latest'
]

for model_name in model_names_to_try:
    try:
        print(f"\nMencoba model: {model_name}")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Halo, apa kabar?")
        print(f"✓ BERHASIL! Model {model_name} bekerja!")
        print(f"Response: {response.text[:100]}...")
        break
    except Exception as e:
        print(f"✗ Gagal: {str(e)[:100]}")