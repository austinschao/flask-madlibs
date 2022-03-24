from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import STORY_LIST

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/questions")
def display_questions():
    """ Display each word from the prompt """
    user_choice = request.args
    print(user_choice)
    return render_template("questions.html", prompts = STORY_LIST[user_choice].prompts)


# @app.get("/story")
# def retrieve_answers():
#     """ Retrieve answers from form """

#     story = silly_story.generate(request.args)
#     return render_template("story.html", story = story)


@app.get("/choose")
def display_choice():
    "display user choice page"

    return render_template("choose.html", story_list = STORY_LIST)


