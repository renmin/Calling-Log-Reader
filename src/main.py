import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os

class LogAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Log Analyzer")
        self.call_id = tk.StringVar()
        
        # 创建拖拽区域
        self.create_drag_drop_area()

        # 创建Call ID输入框和提交按钮
        self.create_call_id_input()

    def create_drag_drop_area(self):
        drag_drop_label = tk.Label(self.root, text="拖拽日志文件到这里")
        drag_drop_label.pack(pady=20)

        # 绑定拖拽事件
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.handle_drop)

    def create_call_id_input(self):
        call_id_label = tk.Label(self.root, text="请输入Call ID:")
        call_id_label.pack()

        call_id_entry = tk.Entry(self.root, textvariable=self.call_id)
        call_id_entry.pack(pady=10)

        submit_button = tk.Button(self.root, text="提交", command=self.submit)
        submit_button.pack(pady=10)

    def handle_drop(self, event):
        # 获取拖拽的文件路径
        file_path = event.data

        # 检查文件是否存在
        if os.path.isfile(file_path):
            print(f"拖拽的文件路径: {file_path}")
        else:
            print("无效的文件路径")

    def submit(self):
        # 获取输入的Call ID
        entered_call_id = self.call_id.get()

        # 检查Call ID的格式
        if self.is_valid_call_id(entered_call_id):
            print(f"提交成功！Call ID: {entered_call_id}")
        else:
            print("无效的Call ID格式")

    def is_valid_call_id(self, call_id):
        # 在实际应用中，可以根据需要进行更严格的Call ID验证
        # 这里简单地检查长度是否为36（GUID字符串的长度）
        return len(call_id) == 36

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = LogAnalyzerApp(root)
    root.mainloop()
