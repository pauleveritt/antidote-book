"""Use the Antidote `world` to get a dependency manually.

We have a `greeting` function that needs a `Greeter`.
"""
from antidote import world, injectable


@injectable
class Greeter:
    salutation: str = "Hello"


def greeting() -> str:
    """Get a `Greeter` and return a greeting."""
    greeter = world.get(Greeter)
    return f'{greeter.salutation}!'


def main() -> str:
    return greeting()


def test() -> tuple[str, str]:
    return main(), "Hello!"
