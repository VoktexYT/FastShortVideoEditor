import tkinter as tk


def conf():
    def packItems(items: list, pady: int):
        for el in items:
            el.pack(pady=pady)

    def checkIn():
        if in_projectName.get() and '/' in in_projectPath.get() and in_videoName.get() and in_videoFps.get():
            out_submitFormError.configure(text='true', fg='green')
            root.quit()
            return {
                'projectName': in_projectName.get().replace(" ", "_"),
                'projectPath': in_projectPath.get().replace(" ", ""),
                'videoName': in_videoName.get().replace(" ", "_"),
                'videoFps': in_videoFps.get().replace(" ", "")
            }
        else:
            errorMessage = "[SyntaxError]: "
            if not in_projectName.get() and not in_videoName.get() and not in_videoFps.get() and '/' not in in_projectPath.get():
                errorMessage += ' All input is empty'

            elif not in_projectName.get():
                errorMessage += 'Project name is empty'

            elif '/' not in in_projectPath.get():
                errorMessage += "It missing '/' in project path"

            elif not in_videoName.get():
                errorMessage += 'Video name is empty'

            elif not in_videoFps.get():
                errorMessage += 'Video FPS is empty'

            else:
                errorMessage += 'Unidentified error'

            out_submitFormError.configure(text=errorMessage)

    backgroundPage = '#2F3136'

    root = tk.Tk()
    root.geometry('300x600')
    root.title('project config')
    root.configure(background=backgroundPage)

    out_projectName = tk.Label(root, text='project name', fg='#A4A6A9', bg=backgroundPage, font=('monospace', 13))
    in_projectName = tk.Entry(root, bg='#202225', fg='white', borderwidth='0px', highlightthickness='0px', font=1)

    out_projectPath = tk.Label(root, text='project path', fg='#A4A6A9', bg=backgroundPage, font=('monospace', 13))
    in_projectPath = tk.Entry(root, bg='#202225', fg='white', borderwidth='0px', highlightthickness='0px', font=1)

    out_videoName = tk.Label(root, text='name of the final video', fg='#A4A6A9', bg=backgroundPage, font=('monospace', 13))
    in_videoName = tk.Entry(root, bg='#202225', fg='white', borderwidth='0px', highlightthickness='0px', font=1)

    out_videoFps = tk.Label(root, text='video fps', fg='#A4A6A9', bg=backgroundPage, font=('monospace', 13))
    in_videoFps = tk.Entry(root, bg='#202225', fg='white', borderwidth='0px', highlightthickness='0px', font=1)

    out_submitFormError = tk.Label(root, text="", bg=backgroundPage, fg='#FF466B')
    in_submitForm = tk.Button(root, text='Submit', fg='#A4A6A9', bg='#2F3136', highlightthickness='2px', highlightbackground='#202225', borderwidth='0px', activebackground='#2F3136', activeforeground='white', command=checkIn)

    packItems([
        out_projectName, in_projectName, out_projectPath, in_projectPath,
        out_videoName, in_videoName, out_videoFps, in_videoFps,
        out_submitFormError, in_submitForm
    ], 15)

    root.mainloop()

    a = True
    while a:
        if out_submitFormError.cget('text') == 'true':
            return True, checkIn()