"""Use the Antidote `world` to get a dependency manually."""
from antidote import world, injectable


@injectable
class Greeter:
    salutation: str = "Hello"


def greeting() -> str:
    """Get a `Greeter` and return a greeting."""
    greeter = world.get(Greeter)
    return f'{greeter.salutation}!'


def main():
    return greeting()


def test() -> tuple[str, str]:
    return main(), "Hello!"
