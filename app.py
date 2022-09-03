import os
from flask import Flask, render_template, request, send_from_directory
import triviaquestion, triviagame

app = Flask(__name__)
trivia_game = triviagame.TriviaGame()
trivia_game_questions = trivia_game.getAllQuestions()

@app.route("/")
def home():
    trivia_questions = trivia_game.retrieveMultipleChoice(9, 5)
    trivia_game.storeResultingQuestions(trivia_questions)
    all_questions = trivia_game_questions
    print(all_questions)
    print(all_questions[0].id)
    return render_template('questions.html', results=all_questions)

@app.route("/score", methods=['POST'])
def scoreGame():
    if request.method == 'POST':
        correctlyAnsweredQuestions = [] 
        incorrectlyAnsweredQuestions = []
        for question in trivia_game_questions:
            if (request.form[str(question.getID())] == question.getCorrectAnswer()): # If question id (from form) is equal to a correct answer.
                correctlyAnsweredQuestions.append(question)
            else:
                incorrectlyAnsweredQuestions.append(question)
        return render_template('results.html', results=[correctlyAnsweredQuestions, incorrectlyAnsweredQuestions])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run()