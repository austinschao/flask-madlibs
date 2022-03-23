from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/questions")
def display_questions():
    """ Display each word from the prompt """

    return render_template("questions.html", prompts = silly_story.prompts)


@app.get("/story")
def retrieve_answers():
    """ Retrieve answers from form """

    story = silly_story.generate(request.args)
    return render_template("story.html", story = story)

