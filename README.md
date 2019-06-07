# Computer Aided Instruction
###### for 5.th grade students

**Description:** 
This project contains 10 math questions for 5.grade students. 
During the quiz, students can see their wrong and correct answers. At the end of the quiz, they will their final points. 

------
**Usage:**
The questions are in the *questions.txt* file, and you can add more questions in it. After adding questions, you have to 
edit code in specific lines. In 76.th line change the second parameters.

'''
self.current_question_set = random.sample(self.data, 10)
'''
Also, 109.th line, change the number in terms of number of questions.

'''
if self.wrong_questions == 10:
'''


**This project is created for Programming Language II course(CEIT211).**
