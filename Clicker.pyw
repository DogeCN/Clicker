import pyautogui,threading,keyboard
import tkinter as tk

count = 0

Form = tk.Tk()
Form.title('Clicker')
Form.geometry('300x200')
Form.resizable(False, False)
Form.iconbitmap('Mouse.ico')
Form.configure(bg='#A8B8C6')

TextLabel = tk.Label(Form, font=('Microsoft YaHei UI', 16), bg='#A8B8C6')
TextLabel.pack()
WarnLable = tk.Label(Form, font=('Microsoft YaHei UI', 16), text='Invalid input.', fg='red', bg='#A8B8C6')
Entry = tk.Entry(Form, width=10, font=('Microsoft YaHei UI', 16), justify=tk.CENTER)

def QClick():
    global count
    while ThreadRunning:
        if ThreadRunning:
            pyautogui.click(button='right')
            count += 1
        else:
            break

def End():
    global ThreadRunning
    keyboard.wait('F8')
    ThreadRunning = False

def Main():
    Entry.pack()
    TextLabel.configure(text='\nEnter the number of threads\nThen press F8 to start.\n')
    while True:
        keyboard.wait('F8')
        try:
            n = int(Entry.get())
        except:
            WarnLable.pack()
        else:
            WarnLable.pack_forget()
            Entry.pack_forget()
            QCthreads = [threading.Thread(target=QClick, daemon=True) for i in range(n)]
            Endthread = threading.Thread(target=End, daemon=True)
            Endthread.start()
            TextLabel.configure(text='\nPress F8 to stop.\n')
            for t in QCthreads:
                t.start()
            QClick()
            TextLabel.configure(text=TextLabel.cget('text') + 'Theoretical click count: ' + str(count) + '\n')
            Reset.pack()
            break

def reset():
    global ThreadRunning
    Reset.pack_forget()
    Mainthread = threading.Thread(target=Main, daemon=True)
    Mainthread.start()
    ThreadRunning = True
Reset = tk.Button(Form, text='Reset', font=('Helvetica', 16), command=reset)
reset()

Form.mainloop()