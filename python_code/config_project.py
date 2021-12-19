import tkinter as tk


def conf():
    def packItems(items: list, pady: int):
        for el in items:
            el.pack(pady=pady)

    def checkIn():
        if in_projectName.get() and '/' in in_projectPath.get():
            root.quit()
            return {'projectName': in_projectName.get(), 'projectPath': in_projectPath.get()}
        else:
            errorMessage = "[SyntaxError]: "
            if not in_projectName.get() and '/' not in in_projectPath.get():
                errorMessage += 'the input is empty'

            elif not in_projectName.get():
                errorMessage += 'project name is empty'

            elif '/' not in in_projectPath.get():
                errorMessage += "it missing '/' in project path"

            out_submitFormError.configure(text=errorMessage)


    backgroundPage = '#2F3136'

    root = tk.Tk()
    root.geometry('300x300')
    root.title('project config')
    root.configure(background=backgroundPage)

    out_projectName = tk.Label(text='project name', fg='#A4A6A9', bg=backgroundPage)
    in_projectName = tk.Entry(bg='#202225', fg='white', borderwidth='0px', highlightthickness='0px')

    out_projectPath = tk.Label(text='project path', fg='#A4A6A9', bg=backgroundPage)
    in_projectPath = tk.Entry(bg='#202225', fg='white', borderwidth='0px', highlightthickness='0px')

    out_submitFormError = tk.Label(text="", bg=backgroundPage, fg='red')
    in_submitForm = tk.Button(text='Submit', fg='#A4A6A9', bg='#2F3136', highlightthickness='2px', highlightbackground='#202225', borderwidth='0px', activebackground='#2F3136', activeforeground='white', command=checkIn)

    packItems([
        out_projectName, in_projectName, out_projectPath, in_projectPath, out_submitFormError, in_submitForm
    ], 13)

    root.mainloop()