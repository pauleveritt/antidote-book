# Pluggable App Layout

This is a book about pluggable apps, using a "MegaStore" sample application.
MegaStore is a pluggable app with independent plugins that get installed into a particular site.
In this chapter, let's re-organize our software to simulate Python packages that get installed for each.

## Pluggable App

The application itself is `MegaStore`, a chain of stores where customers receive a greeting from a greeter when they enter.
`MegaStore` is an actual application: you can install it, run it, and get something.
We call this "OOTB": out-of-the-box, it provides something useful.

But it is a _pluggable_ app.
The useful things that `MegaStore` does can be plugged into: Extended, Replaced, or Varied.
We'll approach `MegaStore` as a _thin core_ with common code that pulls everything together.
This thin core then ships with plugins for the out-of-the-box part.
That way, the built-in stuff isn't "more equal" than an replacement parts.

We'll start with a package at `megastore/__init__.py`:

```{literalinclude} ../../src/antidote_book/app_layout/megastore/__init__.py
---
start-at: "@inject"
---
```

This is indeed a thin core.
It provides the web framework equivalent of processing an HTTP request: find a view, call it, and return the result.
In this case: find a `Greeting`, call it, and return a string.
Since `get_greeting` has the `@inject` decorator, everything it needs is provided by plugins.

Again, for this example, `megastore` is in a _subdirectory_.
In practice, it would be its own Python package, installed by `pip`.

Let's look at the simulated-packages for each plugin.

## `Greeting` Plugin

We just said the `MegaStore` core was thin, and -- yep -- it's _really_ thin.
All the work comes from plugins which the core looks up via Antidote.

These plugins would normally be separate pip-installed packages.
We'll put them in the `megastore_plugins` directory to simulate this.
The first plugin we saw was used by the core, at `megastore_plugins/greeting/__init__.py`:

```{literalinclude} ../../src/antidote_book/app_layout/megastore_plugins/greeting/__init__.py
---
start-at: "from ..customer"
---
```

This `Greeting` plugin defines an "injectable".
When this module is imported, the `@injectable` decorator registers the symbol `Greeting` with the current Antidote "world".

The `Greeting` is like a view in a web system.
It pulls in everything needed for a request -- a "greeting" to a customer, in this case -- and returns a result.
The "everything needed" part is the "dependencies" which we clearly state in dataclass fields.
A `Greeting` needs:

- A `Customer`
- A `Greeter`
- The site configuration, which can provide `punctuation`
- A `salutation` which is a property of the `Greeting` itself

The `MegaStore` core's `get_greeting` injects an instance of this class.
It then has all the inputs it needs to do its work.
The work is in the `__call__`: an f-string that assembles the text of the greeting.
It has a simple workflow:

:::{note} Why not a plain function?

The use of a dataclass with a single method has a certain "code smell".
Why not just use a function with parameters for each dataclass field?

Main reason: to provide a type that can be injected.
If it was just a `@lazy` function, we'd need the return type to be something more than a string, which we could then inject.
Typing and "fail faster" are an important part of the Antidote ethos.

Also, it's easy to replace this `Greeting` with a subclass that keeps the same contract, without repeating the function signature.
We could then provide a different `__call__` to give a different greeting.
:::

As usual for test-first development, we have a test for `Greeting`:

```{literalinclude} ../../tests/test_app_layout.py
---
start-at: "def test_greeting"
end-at: "assert greeting.salutation"
---
```

## `Customer` Plugin

As you can see, the `Greeting` plugin depends on two other plugins.
First, the `Customer` plugin at `megastore_plugins/customer/__init__py`:

```{literalinclude} ../../src/antidote_book/app_layout/megastore_plugins/customer/__init__.py
---
start-at: "@injectable"
---
```

As you can see, `Customer` at this point is all data.
And again, for test-first development, we have a test for `Customer`:

```{literalinclude} ../../tests/test_app_layout.py
---
start-at: "def test_customer"
end-at: "assert customer.name"
---
```

## `Greeter` Plugin

Same is true for the second dependency of `Greeting`, the `Greeter`:

```{literalinclude} ../../src/antidote_book/app_layout/megastore_plugins/greeter/__init__.py
---
start-at: "@injectable"
---
```

As usual for test-first development, we have a test for `Greeting`:

```{literalinclude} ../../tests/test_app_layout.py
---
start-at: "def test_greeter"
end-at: "assert greeter.name"
---
```

## `Config` Plugin

The `MegaStore` configuration system is the final plugin.
It provides knobs with default values, such as what punctuation to use in the greeting.
These defaults can be overridden by a plugin or by the site:

```{literalinclude} ../../src/antidote_book/app_layout/megastore_plugins/config/__init__.py
---
start-at: "class MegaStoreConfig"
---
```

For the config test, we just ensure that punctuation can be injected:

As usual for test-first development, we have a test for `Greeting`:

```{literalinclude} ../../tests/test_app_layout.py
---
start-at: "def test_config"
end-at: "assert this_punctuation"
---
```

We thus have four plugins:

- The `Greeting`
- The `Customer`
- The `Greeter`
- The configuration system

This constitutes the OOTB functionality for the `MegaStore` pluggable app.

## Site

Our last piece of the puzzle: an actual store.
Or to use more general jargon: a "site" that pulls in the needed software, provides any customization, and is run by a server.

It's important to note: the site is in full control.
It could choose to ignore `get_greeting` and just return `Down for maintenance.`

Here is the code for our site in `site.py`:

```{literalinclude} ../../src/antidote_book/app_layout/site.py
---
start-at: "from .megastore import get_greeting"
---
```

## Recap

Since this will be our pattern for the rest of the book, let's state again the package layout:

- The code for the pluggable app's (tiny) core goes in `megastore`
- All the plugin packages are in `megastore_plugins`
- A particular store is in `site.py`

## Download Files

- {download}`app_layout/megastore/__init__.py <../../src/antidote_book/app_layout/megastore/__init__.py>`
- {download}`app_layout/megastore_plugins/config/__init__.py <../../src/antidote_book/app_layout/megastore_plugins/config/__init__.py>`
- {download}`app_layout/megastore_plugins/customer/__init__.py <../../src/antidote_book/app_layout/megastore_plugins/customer/__init__.py>`
- {download}`app_layout/megastore_plugins/greeter/__init__.py <../../src/antidote_book/app_layout/megastore_plugins/greeter/__init__.py>`
- {download}`app_layout/megastore_plugins/greeting/__init__.py <../../src/antidote_book/app_layout/megastore_plugins/greeting/__init__.py>`
- {download}`tests/test_app_layout.py <../../tests/test_app_layout.py>`
