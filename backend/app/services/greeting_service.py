import random


GREETINGS = [
    "Hello from FastAPI!",
    "Hey there! Welcome back.",
    "Greetings, traveler.",
    "What's up? The API is alive and well.",
]


def get_greeting(name: str | None = None) -> str:
    greeting = random.choice(GREETINGS)
    if name:
        greeting = f"{greeting} Nice to meet you, {name}."
    return greeting
