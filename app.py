from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

app = Flask(__name__)

# PERBAIKAN: Gunakan model Gemini 2.5 Flash (Recommended)
model = genai.GenerativeModel('gemini-2.5-flash')

# Simpan session chat per user (simplified)
chat_sessions = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        session_id = data.get('session_id', 'default')
        
        # Buat session baru jika belum ada
        if session_id not in chat_sessions:
            chat_sessions[session_id] = model.start_chat(history=[])
        
        # Kirim pesan dan dapatkan response
        response = chat_sessions[session_id].send_message(user_message)
        
        return jsonify({
            'response': response.text
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'response': f'Maaf, terjadi kesalahan: {str(e)}'
        }), 500

@app.route('/reset', methods=['POST'])
def reset():
    data = request.json
    session_id = data.get('session_id', 'default')
    
    # Reset session
    if session_id in chat_sessions:
        del chat_sessions[session_id]
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)