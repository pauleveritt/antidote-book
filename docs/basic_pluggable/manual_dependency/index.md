# Manual Dependency

You can work with dependencies without the magical "injection" process.
In this example our `Greeting` function doesn't have any parameters.
Instead, it internally grabs Antidote's `world` object to get what it wants:

```{literalinclude} __init__.py
```

## Analysis

The `world` object is a global that contains all the registrations for injectables.
It can be imported and used anywhere.

As noted in Antidote's {doc}`antidote:tutorial` tutorial, this syntax should be used as a backup.
Injection is faster and easier to test.


Full code: {download}`__init__.py` and {download}`test_manual_dependency.py`.