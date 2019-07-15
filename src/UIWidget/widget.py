import tkinter


class UserInterface:
    def __init__(self, data):
        self.window = tkinter.Tk()
        self.window.title("Twitter Sentiment Analysis Tool (TSAT)")
        self.text_var = tkinter.StringVar()
        frame = tkinter.Frame(self.window, background="#ebeef3")
        frame.pack(fill="both")
        self.count = 1
        self.apple = data

    def classify(self):
        self.widget()
        self.window.mainloop()

    def callback(self):
        self.count += 1
        try:
            print("works")
            self.text_var.set(self.apple.get_tweet(self.count).text)
        except:
            print("exception")
            pass

    def widget(self):
        self.text_var.set(self.apple.get_tweet(self.count))
        w = tkinter.Label(self.window, wraplength='500', justify='center', textvariable=self.text_var, relief="groove", fg='#3e4247', borderwidth=2, highlightcolor='#326690', font=('Helvetica'), bg='#d6effc')
        w.pack(expand=True)
        btnMyButton = tkinter.Button(self.window, text="Im Button", command=self.callback)
        btnMyButton.pack()
