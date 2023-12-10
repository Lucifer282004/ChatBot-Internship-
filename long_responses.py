import random

R_ADVICE = "I can Do 2 main operations like help you for leave application along with the CL pl and i can also raise tickets for certain things"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
