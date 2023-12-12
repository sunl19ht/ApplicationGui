import tkinter as tk
from tkinter import scrolledtext
import threading
import websocket

def on_message(ws, message):
    print(f"OnMessage: {message}")
def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("WebSocket connection opened")
    ws.send("Hello, server!")

def start_websocket():
    ws_url = "ws://your-server-url/websocket"
    ws = websocket.WebSocketApp(ws_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
# 启动 WebSocket 连接的线程
websocket_thread = threading.Thread(target=start_websocket)
websocket_thread.start()