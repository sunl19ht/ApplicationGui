import tkinter as tk
from tkinter import scrolledtext

def send_message():
    message = input_entry.get()
    
    sent_text.config(state=tk.NORMAL)
    sent_text.insert(tk.END, f"你： {message}\n")
    sent_text.config(state=tk.DISABLED)

    input_entry.delete(0, tk.END)

# 创建主窗口
root = tk.Tk()
root.title("聊天室")

# 创建发送消息的文本框
sent_text = scrolledtext.ScrolledText(root, width=40, height=5, state=tk.DISABLED)
sent_text.pack(pady=10)

# 创建输入框
input_entry = tk.Entry(root, width=40)
input_entry.pack(pady=10)

# 创建发送按钮
send_button = tk.Button(root, text="发送", command=send_message)
send_button.pack()

# 启动 Tkinter 事件循环
root.mainloop()
