# Priya Companion Server

This folder contains a local companion server that allows Priya (the web app) to control your local laptop (mouse, keyboard, opening apps). 

Because a web browser cannot directly control your computer for security reasons, you need to run this small script on your laptop. 

## Python Server (Recommended & Easiest)

We recommend using the Python server because it's very easy to install and run.

### 1. Install Python Dependencies
Open your terminal or command prompt and run:
```bash
pip install flask flask-cors pyautogui
```

### 2. Run the Server
```bash
python server.py
```

You should see: `Starting Local Companion Server on port 8080...`

### 3. Talk to Priya
Now go back to the Priya web app and say:
- "Open Spotify"
- "Type hello world"
- "Click"

Priya will send the command to your local server, which will execute it on your machine!

## How it works

1. You run `server.py` on your laptop. It listens on `http://localhost:8080/api/command`.
2. When you tell Priya to "open Spotify", the web app sends a `POST` request to `http://localhost:8080/api/command`.
3. The local server uses `pyautogui` and `os.system` to control your mouse, keyboard, or launch the app.
