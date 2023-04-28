import tkinter as tk
import tkinter.ttk
import mysql.connector
class question_generator:
    
    #main application window
    def application_window(cls):
        #Establishing connection with mysql.connector.connect
        mydb = mysql.connector.connect(
        host="localhost", #host on which database is present
        user="root", #name of the user
        password="Tanmay@09;", #password for the user
        database="qgen" #database to access
        )
        mycursor = mydb.cursor() 
        mycursor.execute("SELECT course FROM programs")

        data = mycursor.fetchall()
        
        values = [item for tpl in data for item in tpl]

        #creating window
        window=tkinter.Tk()
    
        #title for thw window
        window.title("Question Paper Generator")
    
        #creating frame in window
        frame=tkinter.Frame(window)
        frame.pack()
        #creating frame within frame
        question_paper_detail_frame=tkinter.LabelFrame(frame, text="Question Paper Details")
        question_paper_detail_frame.grid(row=0, column=0, padx=50, pady=50) #position on first row & column
    
        #creating label 1 in frame 
        course_Label=tkinter.Label(question_paper_detail_frame,text="Course Name")
        course_Label.grid(row=0,column=0) #label position 
    
         #creating label 2 in the frame
        programme_code_Label=tkinter.Label(question_paper_detail_frame,text="Programme Code")
        programme_code_Label.grid(row=0,column=1)
    
        #creating label 3
        programme_label=tkinter.Label(question_paper_detail_frame,text="Programme")
        programme_label.grid(row=0,column=2)#setting position of label 3

        #creating combox 1
        course_combox=tkinter.ttk.Combobox(question_paper_detail_frame,values=values,width=30)
        course_combox.grid(row=1,column=0)#setting combobox postion below label 1
    
        #creating combobox 2 
        programme_code_combox=tkinter.ttk.Combobox(question_paper_detail_frame)
        programme_code_combox.grid(row=1,column=1)# setting postion of combobox below label 2 

        #creating combobox 3
        programme_combobox=tkinter.ttk.Combobox(question_paper_detail_frame)
        programme_combobox.grid(row=1,column=2)#setting position of combobox below label 3

        #creating label 4
        college_name_label=tkinter.Label(question_paper_detail_frame,text="Name of Constituent College")
        college_name_label.grid(row=2,column=1)#setting position of label 4

        #creating cobobox for label 4
        college_name_combobox=tkinter.ttk.Combobox(question_paper_detail_frame)
        college_name_combobox.grid(row=3,column=1)#setting position of combobox below label 4

        #creating label 5
        Subject_label=tkinter.Label(question_paper_detail_frame,text="Subject")
        Subject_label.grid(row=2,column=0)

        #creating combobox for lable 5
        Subject_combobox=tkinter.ttk.Combobox(question_paper_detail_frame,width=30)
        Subject_combobox.grid(row=3,column=0)

        
        #creating button 
        set_button=tkinter.Button(question_paper_detail_frame,text="Set Question Paper")
        set_button.grid(row=10,column=1)#setting position of button

        window.mainloop()

test=question_generator()
test.application_window()