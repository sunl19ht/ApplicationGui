import requests
import tkinter as tk
# from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
headers = {"Content-Type": "application/json"}
root = tk.Tk()  # 创建一个窗口
def login():
    root.title("登录") # 设置窗口标题
    root.geometry("250x470") # 设置窗口大小

    nickname = tk.Label(root, text="账号", font=("Microsoft YaHei", 20), fg="black") # 添加标签控件
    nickname.grid() # 定位

    password = tk.Label(root, text="密码", font=("Microsoft YaHei", 20), fg="black") # 添加标签控件
    password.grid()

    nicknameText = tk.Entry(root, font=("Microsoft YaHei", 10), fg="black") # 添加输入框
    nicknameText.grid(row=0, column=1) # row行, column列

    passwordText = tk.Entry(root, font=("Microsoft YaHei", 10), fg="black", show="*") # 添加输入框
    passwordText.grid(row=1, column=1)

    button = tk.Button(root, text="登录", font=("Microsoft YaHei", 15), fg="black", command=lambda: loginButton(nicknameText.get(), passwordText.get())) # 添加按钮
    button.grid()

    root.mainloop() # 循环显示该窗口

def loginButton(nickname, password):
    data = {
        "nickname": nickname,
        "password": password
    }
    response = requests.post(url = "http://localhost:8080/user/login", json=data, headers=headers).json()
    # private Integer code; //编码：1成功，0和其它数字为失败
    # private String msg; //错误信息
    # private T data; //数据
    code = response.get("code")
    msg = response.get("msg")
    data = response.get("data")
    if code != 1: # 请求失败
        messagebox.showerror("Error！", msg)
    else:
        mainMenu()
        root.withdraw() # 隐藏登录窗口

def mainMenu():
    chatMenu = tk.Toplevel(root)
    chatMenu.title("聊天室")
    chatMenu.geometry("380x470")

    # 创建发送消息的文本框
    sent_text = scrolledtext.ScrolledText(chatMenu, width=40, height=5, state=tk.DISABLED)
    sent_text.grid(row=0, column=1)

    # 创建输入框
    input_entry = tk.Entry(chatMenu, width=40)
    input_entry.grid(row=3, column=1)

    # 创建发送按钮
    send_button = tk.Button(chatMenu, text="发送", font=("Microsoft YaHei", 15), command=lambda: sendMessageButton(input_entry, sent_text))
    send_button.grid()

def sendMessageButton(input_entry, sent_text):
    message = input_entry.get()
    
    sent_text.config(state=tk.NORMAL)
    sent_text.insert(tk.END, f"你： {message}\n")
    sent_text.config(state=tk.DISABLED)

    input_entry.delete(0, tk.END)



if __name__ == "__main__":
    login()
    # mainMenu()