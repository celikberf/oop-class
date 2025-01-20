class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer



class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print('-' + q)
        
        answer = input('cevap : ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:

            self.displayProgress()
            self.displayQuestion()
    
    def shoeScorre(self):
        print('score : ', self.score)

    def displayProgress(self):
        totalQuestions = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestions:
            print('Quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestions}'.center(100,'*'))


q1 = Question('en iyi programlama dili hangisidir ? ', ['C#','python','javascript','java'],'python')
q2 = Question('en iyi popüler dili hangisidir ? ', ['C#','javascript','python','java'],'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ? ', ['python','javascript','java','C#'],'python')
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()
