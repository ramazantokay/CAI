# Computer Aided Instruction for 5.th grade students

**Description:** 
This project contains 10 math questions for 5.grade students. The purpose of this project, make students practice more in math questions.
During the quiz, students can see their wrong and correct answers. At the end of the quiz, they will see their final points. 

------
**Installation:**
The questions are in the *questions.txt* file. You can add more questions in it. 
After adding questions, you have to edit code in specific lines. 

In 76.th line change the second parameters in terms of the number of questions.
```
self.current_question_set = random.sample(self.data, 10)
```
Also, 109.th line, change the number in terms of the number of questions.

```
if self.wrong_questions == 10:
```
------

**This project is created for Programming Language II course(CEIT211). Python**
