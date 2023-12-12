import requests
from tkinter import *
from tkinter import messagebox
headers = {"Content-Type": "application/json"}
def login():
    root = Tk()  # 创建一个窗口
    root.geometry("250x470") # 设置窗口大小
    root.title("登录") # 设置窗口标题

    nickname = Label(root, text="账号", font=("Microsoft YaHei", 20), fg="black") # 添加标签控件
    nickname.grid() # 定位

    password = Label(root, text="密码", font=("Microsoft YaHei", 20), fg="black") # 添加标签控件
    password.grid()

    nicknameText = Entry(root, font=("Microsoft YaHei", 10), fg="black") # 添加输入框
    nicknameText.grid(row=0, column=1) # row行, column列

    passwordText = Entry(root, font=("Microsoft YaHei", 10), fg="black", show="*") # 添加输入框
    passwordText.grid(row=1, column=1)

    button = Button(root, text="登录", font=("Microsoft YaHei", 15), fg="black", command=lambda: loginButton(nicknameText.get(), passwordText.get())) # 添加按钮
    button.grid()

    root.mainloop() # 循环显示该窗口

def loginButton(nickname, password):
    print(nickname, password)
    data = {
        "nickname": "sunl19ht",
        "password": "123456"
    }
    response = requests.post(url = "http://localhost:8080/user/login", json=data, headers=headers)
    print(response.json)
if __name__ == "__main__":
    login()