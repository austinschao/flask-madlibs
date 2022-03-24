from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import STORY_LIST

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

current_story = []

@app.get("/questions")
def display_questions():
    """ Display each word from the prompt """
    story = request.args["story"]
    current_story.append(STORY_LIST[story])
    return render_template("questions.html", prompts = STORY_LIST[story].prompts)


@app.get("/story")
def retrieve_answers():
    """ Retrieve answers from form """

    story = current_story[-1].generate(request.args)
    return render_template("story.html", story = story)


@app.get("/choose")
def display_choice():
    "display user choice page"
    return render_template("choose.html", story_list = STORY_LIST)


