
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
import tkinter.font
from tkinter import filedialog

import sys
temp = sys.path
sys.path.append('../Jordan/Services/')
from services import searchMessages # This code gets the method for making API request
sys.path.append(temp)

class emaildisplay():
    def __init__(self, parent, emailObject):
        self.gui(parent, emailObject)
        

    def gui(self, parent, emailObject):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#e2e2e2')
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#e2e2e2')
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.messagelabel = Label(self.w1, text = emailObject.message, anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.messagelabel.place(x = 0, y = 160, width = 500, height = 292)
        self.senderlabel = Label(self.w1, text = "From: " + emailObject.sender, anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.senderlabel.place(x = 0, y = 0, width = 500, height = 32)
        self.subjectlabel = Label(self.w1, text = "Subject: " + emailObject.subject, anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.subjectlabel.place(x = 0, y = 30, width = 500, height = 32)
        self.tolabel = Label(self.w1, text = "Recipients:" + emailObject.receiver, anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.tolabel.place(x = 0, y = 70, width = 500, height = 32)

class Widget1():
    def __init__(self, parent):
        self.gui(parent)
        self.button_list = []

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#414141')
            self.w1.geometry('1280x720')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#414141')
            self.w1.place(x = 0, y = 0, width = 1280, height = 720)
        self.button1 = Button(self.w1, text = "Search Email", font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.button1.place(x = 800, y = 50, width = 200, height = 40)
        self.button1['command'] = self.search_email
        self.resultbox = Text(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.resultbox.place(x = 300, y = 230, width = 400, height = 470)
        self.ltext1 = Entry(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), state = "normal")
        self.ltext1.place(x = 170, y = 50, width = 200, height = 40)
        self.label1 = Label(self.w1, text = "Keyword:", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label1.place(x = 50, y = 50, width = 120, height = 40)
        self.button2 = Button(self.w1, text = "Directory Selector", font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.button2.place(x = 500, y = 50, width = 200, height = 40)
        self.button2['command'] = self.browse_folder
        self.label2 = Label(self.w1, text = "Search Type", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label2.place(x = 50, y = 160, width = 150, height = 22)
        self.combo1 = Combobox(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.combo1.place(x = 50, y = 210, width = 160, height = 30)
        self.combo1['values'] = ("Disk & Gmail", "Disk Only", "Gmail only")
        self.combo1.current(0)
        self.label3 = Label(self.w1, text = "Selected Option", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label3.place(x = 800, y = 170, width = 200, height = 22)
        self.label4 = Label(self.w1, text = "Search Results", anchor='w', font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.label4.place(x = 300, y = 170, width = 200, height = 22)
        self.text3 = Text(self.w1, font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.text3.place(x = 800, y = 230, width = 400, height = 470)
        self.button1_copy = Button(self.w1, text = "Get Emails", font = tkinter.font.Font(family = "Verdana", size = 12), cursor = "arrow", state = "normal")
        self.button1_copy.place(x = 1030, y = 50, width = 200, height = 40)
        self.button1_copy['command'] = self.search_email
        self.vslider1 = Scale(self.w1, from_ = 0, to = 100, resolution = 1, orient = VERTICAL, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.vslider1.place(x = 680, y = 240, width = 22, height = 453)

    def print_test(self):
        input = self.ltext1.get()
        print(input)

    def browse_folder(self):
        # Ask for text input from the user
        root = Tk()
        root.withdraw()  # Remove or comment out this line to keep the window visible
        folder_selected = filedialog.askdirectory()
        root.destroy()  # Close the Tkinter window after selecting the directory

    def search_email(self):
        input = self.ltext1.get()
        global entrylist
        entrylist = searchMessages(input)
        offSet = 0
        
        for email in entrylist:
            print(email)
            button = Button(self.w1, text = "Subject: " + email.subject + " Sender: " + email.sender, bg = "#e6e6e6", font = tkinter.font.Font(family = "Bahnschrift Light", size = 8), cursor = "arrow", state = "normal",)
            button.place(x = 300, y = (230 + offSet), width = 400, height = 62)
            button['command'] = lambda b = button: self.show_message(b)
            button._name = email.id
            print(offSet)
            offSet += 68
            self.button_list.append(button)

    def show_message(self, button):
        print(button)
        for email in entrylist: #Find a better way to get the button we need
            if button._name == email.id:
                window = emaildisplay(0, email)
                break
                    
            
                
        
        
        

    
        
             
        
             

if __name__ == '__main__':
    a = Widget1(0)
    a.w1.mainloop()



