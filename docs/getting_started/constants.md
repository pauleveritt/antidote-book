# Configuration with Constants

# Constants

Your injectables almost always need some configuration.
Antidote provides an approach for such "constants" with extra touches for how development works.

The `Config` class has a special `provide_const` protocol for Antidote.
This lets values be _optionally_ retrieved from dynamic sources -- in this case, an environment variable.

The test example shows using monkeypatch to simulate putting a configuration value into the environment.

## Analysis

Your injectables will likely need configuration values from a variety of sources.
Antidote's idea of `Constants` is an interesting take on this:

- Preserves Antidote's emphasis on strong typing, with (limited) support for runtime checking
- Differentiates between a value coming from the constant's class vs. instance
- Lazy evaluation as needed

## Download
