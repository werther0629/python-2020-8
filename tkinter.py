import tkinter as tk

werther = tk.Tk()
werther.title('python')
werther.geometry('600x400')

def addname():
    savename = entName.get()
    if savename != '':
        display = tk.Label(werther,text = savename,width = 50)
        display.place(x=100,y=40,width=100,height=20)
    entName.delete(0,'end')

labName = tk.Label(werther, text = '名字：', width=50)
labName.place(x=10, y=10, width=100, height=20)

entName = tk.Entry(werther, width = 120)
entName.place(x=110, y=10, width=120, height=20)

btn = tk.Button(werther, text='加入', width=40,command=addname)
btn.place(x=250, y=10, width=60, height=20)

werther.mainloop()