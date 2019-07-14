import tkinter


class UserInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Twitter Sentiment Analysis Tool (TSAT)")

    def classify(self, text):
        frame = tkinter.Frame(self.window, background="#ebeef3")
        frame.pack(fill="both")
        w = tkinter.Label(self.window, wraplength='500', justify='center', text=text, relief="groove", fg='#3e4247', borderwidth=2, highlightcolor='#326690', font=('Helvetica'), bg='#d6effc')
        w.pack(expand=True)

    def __del__(self):
        self.window.mainloop()