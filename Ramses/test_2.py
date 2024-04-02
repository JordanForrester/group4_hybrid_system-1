
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
    
    listIndex = 0
    entrylist = []
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
        self.resultbox = Listbox(self.w1, font = tkinter.font.Font(family = "Segoe UI", size = 9), cursor = "arrow", state = "normal")
        self.resultbox.place(x = 320, y = 230, width = 420, height = 430)
        self.prevButton = Button(self.w1, text = "Previous", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.prevButton.place(x = 320, y = 670, width = 120, height = 42)
        self.prevButton['command'] = self.list_previous
        self.prevButton_copy = Button(self.w1, text = "Next", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.prevButton_copy.place(x = 620, y = 670, width = 120, height = 42)
        self.prevButton_copy['command'] = self.list_next
        self.text5 = Text(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal")
        self.text5.place(x = 1030, y = 110, width = 200, height = 30)
        self.text5.insert(INSERT, "Enter number of emails to get")

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
        count = self.text5.get("1.0",'end-1c')
        if count == "Enter number of emails to get":
            count = 100

        #count = self.button1_copy
        
        self.entrylist = searchMessages(input, count)
        self.listIndex = 0
        self.displayResults()

    def show_message(self, button):
        print(button)
        for email in self.entrylist: #Find a better way to get the button we need
            if button._name == email.id:
                window = emaildisplay(0, email)
                break

    def list_previous(self):
        if self.listIndex >= 10:
            
            
            self.listIndex = self.listIndex - 10
            self.displayResults()

    def list_next(self):
            
            if self.listIndex <= len(self.entrylist):
                
                self.displayResults()

    def list_clear(self):
        for x in self.button_list:
            x.destroy()
            
    def displayResults(self):  
        self.list_clear()                       
        offSet = 0
        for email in range(self.listIndex, self.listIndex + 6):
            print(email)
            button =   Button(self.resultbox, text = "Subject: " + self.entrylist[email].subject + " Sender: " + self.entrylist[email].sender, bg = "#e6e6e6",font =tkinter.font.Font(family = "Bahnschrift Light", size = 8), cursor = "arrow", state = "normal",)
            button.place(x = 5, y = (20 + offSet), width = 400, height = 62)
            button['command'] = lambda b = button: self.show_message(b)
            button._name = self.entrylist[email].id
            print(offSet) 
            offSet += 68
            self.button_list.append(button)
            self.listIndex = self.listIndex + 1
        
            
        
                    
            
                
        
        
        

    
        
             
        
             

if __name__ == '__main__':
    a = Widget1(0)
    a.w1.mainloop()



