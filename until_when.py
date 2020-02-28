import tkinter
import datetime


def on_click():
    label = tkinter.Label(root, text=AD_MATAI)
    label.pack()


TODAY = datetime.date.today()
FINAL_DAY = datetime.datetime.strptime('19/04/2022', r'%d/%m/%Y').date()
AD_MATAI = str(FINAL_DAY - TODAY)[:-9]


root = tkinter.Tk()
top_frame = tkinter.Frame(root)
top_frame.pack(side=tkinter.TOP)
button = tkinter.Button(top_frame, text="?עד מתי", fg="green", command=on_click)
button.pack()
root.mainloop()