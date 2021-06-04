import tkinter as tk


def return_cDNA():
    DNA = entry1.get()
    cDNA = ''
    for n in DNA:
        if n == 'A':
            cDNA = cDNA + 'T'
        elif n == 'T':
            cDNA = cDNA + 'A'
        elif n == 'G':
            cDNA = cDNA + 'C'
        elif n == 'C':
            cDNA = cDNA + 'G'

    print(cDNA)


def return_mRNA():
    DNA = entry1.get()
    mRNA = ''
    for n in DNA:
        if n == 'A':
            mRNA = mRNA + 'U'
        elif n == 'T':
            mRNA = mRNA + 'A'
        elif n == 'G':
            mRNA = mRNA + 'C'
        elif n == 'C':
            mRNA = mRNA + 'G'

    print(mRNA)


w = tk.Tk()
w.title('Find cDNA/mRNA')
w.geometry('300x150')

entry1 = tk.Entry(w, width=30)
entry1.pack()

tk.Button(w, text='find cDNA', command=return_cDNA).pack()
tk.Button(w, text='find mRNA', command=return_mRNA).pack()

w.mainloop()
