from tkinter import *
from tkinter import messagebox
import json   #Reading file module
import random #Getting question in a random order

#This class for Info page
class Info:
    def __init__(self, master):
        self.master = master
        self.master.title("Info")
        self.master.geometry("600x110")
        self.label1 = Label(master, text="This project is created by Ramazan TOKAY \nfor Programming Language II course. \n Copyright 2019", font=("Helvetica",20), fg="red")
        self.label1.place(height=100,relx=0.5,y=50,anchor=CENTER)
#This class for Help page
class Help:
    def __init__(self, master):
        self.master = master
        self.master.title("Help")
        self.master.geometry("750x110")
        self.label1 = Label(master, text="Email: ramazan.tokay@metu.edu.tr.\n You can send a message to me in case of having a problem.", font=("Helvetica",20), fg="red")
        self.label1.place(height=100,relx=0.5,y=50,anchor=CENTER)


#This class for Main page
class CAI:

    def __init__(self, master):
        # This is the constructor of the class.
        # In this part, user interface is creating and questions that are in questions.txt are reading

        #User Interface is loading
        self.master = master
        master.title("Questions")
        master.geometry("400x300")
        frame = Frame(master)
        frame.pack()
        #Reading the questions from *.txt file.
        #Checking if there is file or not
        try:
            with open('questions.txt', 'r') as data_file:
                self.data = json.load(data_file)
        except:
            print("We could not find questions file, Please find your questions file")
            master.destroy()
            return


        self.usr_point = 0
        self.wrong_questions = 0
        self.correct_questions = 0
        self.instance = 0
        self.level_value = 0
	#Loading the quiz page interface
        self.welcome=Label(frame, text="Welcome to Math Questions",font="Helvetica 18 bold")
        self.welcome.grid(row=0, padx=50)

        self.question = Label(frame, fg="red", font="Helvetica 18 bold")
        self.question.grid(row=2, padx=20, pady=30)

        self.question_entry = Entry(frame, width=30)
        self.question_entry.grid(row=3)

        self.button = Button(frame, text="Next", command=self.Check_Answer)
        self.button.grid(row=4, column=0, pady=10)

        self.question_status = Label(frame)
        self.question_status.grid(row=5, columnspan=2, padx=20, pady=10)

        self.Load_Ques()

    def Load_Ques(self):
        #In this part, the questions are loading in the User Interface (UI)

        self.question_entry.focus_set()
        if self.instance == 0:
            self.current_question_set = random.sample(self.data, 10)

        question = random.choice(self.current_question_set)

        self.current_question = question['question']
        self.level_value = int(question['level'])

        self.question.config(text=self.current_question)
        self.question_status.config(
            text="T: %s / %s questions answered correctly" % (self.correct_questions, self.wrong_questions))
        self.question_answer = question['answer']

        self.current_question_set.remove(question)

        print(self.current_question_set)

    def Check_Answer(self):
        #In this part, the answers are checking whether they are correct or not

        self.wrong_questions += 1
        if type(self.question_entry.get()) == str:
            user_answer = str(self.question_entry.get()).lower()
        else:
            user_answer = self.question_entry.get()

        if user_answer in self.question_answer:
            self.correct_questions += 1
            self.usr_point += self.level_value * 2
            messagebox.showinfo("Correct", "You are correct!")
        else:
            messagebox.showerror("Incorrect", "Sorry,that was incorrect!")

        print('ques', self.wrong_questions)
        if self.wrong_questions == 10:
            print('yo:', self.wrong_questions)
            messagebox.showinfo("Final Score","\n Final Score: %s \n\n Thanks for playing" % (self.usr_point))
            self.master.destroy()
        else:
            self.instance += 1
            self.question_entry.delete(0, 'end')
            self.Load_Ques()


