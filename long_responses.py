import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "I can Do 3 main operatios like help you for leave application along with the CL pl and i can also raise tickets for certain things"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
