# Section 8 - Small Program

def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    if phrase.startswith(('how', 'what', 'why')):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

messages = []

"""
while message != r"\end":
    message = input("Say something: ")
    messages.append(message)
"""

while True:
    message = input("Say something: ")
    if message == r"\end":
        break
    else:
        messages.append(sentence_maker(message))

print(" ".join(messages))
