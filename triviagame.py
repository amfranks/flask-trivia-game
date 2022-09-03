import requests, triviaquestion, uuid

class TriviaGame():
    def __init__(self):
        self.triviaQuestions = []

    def getAllQuestions(self): 
        return self.triviaQuestions

    def retrieveMultipleChoice(self, categoryID, numOfQuestions): # Retrieves multiple choice trivia questions from the API.
        URL = f"https://opentdb.com/api.php?amount={numOfQuestions}&category={categoryID}&difficulty=easy&type=multiple"

        try:
            response = requests.get(URL, timeout=5)
            response.raise_for_status()

            # If request is successful.
            response_JSON = response.json()
            return response_JSON

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def storeResultingQuestions(self, listOfQuestions):
        self.resetData()

        # Loop through all returned questions.
        for question in listOfQuestions["results"]:
            id = uuid.uuid1()

            newQuestion = triviaquestion.TriviaQuestion(
                question["category"],
                question["difficulty"],
                question["question"],
                question["correct_answer"],
                question["incorrect_answers"],
                id
            )

            self.triviaQuestions.append(newQuestion)

    def resetData(self):
        self.triviaQuestions.clear()