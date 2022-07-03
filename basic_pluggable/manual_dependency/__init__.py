from antidote import world, injectable


@injectable
class Greeter:
    salutation: str = "Hello"


# No longer uses injection.
def greeting() -> str:
    """Get a `Greeter` and return a greeting."""
    greeter = world.get(Greeter)
    return f'{greeter.salutation}!'


def main():
    return greeting()
