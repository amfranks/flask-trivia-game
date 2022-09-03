import random

class TriviaQuestion():
    def __init__(self, category, difficulty, question, correctAnswer, incorrectAnswers, id):
        self.question = question
        self.category = category
        self.difficulty = difficulty
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers
        self.id = id

    def getQuestion(self):
        return self.question

    def getCategory(self):
        return self.category

    def getdifficulty(self):
        return self.difficulty

    def getCorrectAnswer(self):
        return self.correctAnswer

    def getIncorrectAnswers(self):
        return self.incorrectAnswers

    def getID(self):
        return self.id


    def getShuffledAnswers(self):
        answers = self.incorrectAnswers
        answers.append(self.correctAnswer)
        
        random.shuffle(answers)

        return answers