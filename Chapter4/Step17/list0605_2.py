# 단계2: GUI 배치

import tkinter
root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)   # resizable: 윈도우 크기 변경 여부를 의미
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
pic = tkinter.PhotoImage(file="image/miko.png")
canvas.create_image(400, 300, image=pic)

label = tkinter.Label(root, text="??", font=("한컴산뜻돋움", 120), bg="white")
label.place(x=380, y=60)

button = tkinter.Button(root, text="제비뽑기", font=("한컴산뜻돋움", 36), fg="skyblue")
button.place(x=380, y=400)

root.mainloop()