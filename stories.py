"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

silly_story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story(
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

pizza_story = Story(
    ["adjective_1", "nationality","person", "noun_1", "adjective_2", "noun_2", "adjective_3", "adjective_4", "plural_noun",
    "noun_3", "number_1", "shapes","food_1", "food_2", "number_2"],
    """Pizza was invented by a {adjective_1} {nationality} chef named {person}.
    To make pizza you need to take a lump of {noun_1}, and make a thin, round {adjective_2} {noun_2}.
    Then you cover it with {adjective_3} sauce , {adjective_4} cheese, and fresh chopped {plural_noun}.
    Next you have to bake it in a very hot {noun_3}. When it is done, cut it into {number_1}
    {shapes}. Some kids like {food_1} pizza the best, but my favorite is the {food_2} pizza.
    If i could, I would eat pizza {number_2} times a day!"""
)

STORY_LIST = {"silly" : silly_story, "exicted" : excited_story, "pizza" : pizza_story}