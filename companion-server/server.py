from flask import Flask, request, jsonify
from flask_cors import CORS
import pyautogui
import os
import platform

app = Flask(__name__)
CORS(app) # Allow cross-origin requests from the web app

@app.route('/api/command', methods=['POST'])
def handle_command():
    data = request.json
    action = data.get('action')
    payload = data.get('payload')
    
    print(f"Received command: {action} with payload: {payload}")
    
    try:
        if action == 'type':
            pyautogui.typewrite(payload)
        elif action == 'click':
            pyautogui.click()
        elif action == 'move':
            x, y = payload.get('x', 0), payload.get('y', 0)
            pyautogui.moveRel(x, y)
        elif action == 'open_app':
            app_name = payload
            system = platform.system()
            if system == 'Windows':
                os.system(f"start {app_name}")
            elif system == 'Darwin': # macOS
                os.system(f"open -a {app_name}")
            else: # Linux
                os.system(f"{app_name} &")
        return jsonify({"status": "success", "message": f"Executed {action}"})
    except Exception as e:
        print(f"Error executing command: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("Starting Local Companion Server on port 8080...")
    print("Priya can now control your computer! Say 'Open Spotify' or 'Type hello world'.")
    app.run(host='0.0.0.0', port=8080)
