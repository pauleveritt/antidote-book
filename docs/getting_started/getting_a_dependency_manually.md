# Getting a Dependency Manually

Our applications frequently have functions which need to get data from "the system".
Let's see how to use Antidote's {doc}`antidote:reference/world` to go fetch an object and get some data from it.

## It's Like Views

Here's a classic pattern Python web pattern: register a view function which, in its body, queries the database.
The results are then packed into view data and rendered through a template.
From [the Django tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial03/#a-shortcut-render):

```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

In this view function, `Question` is an object which the framework injected with superpowers.
It knows how to get us the data we want. 

Fortunately Antidote has one of those too: the {doc}`World <antidote:reference/world>` object.
Let's see how we can use it in our function to *pull* in the object we need.

## The Greeting Gets the Greeter

We have a simple `greeting` function.
It needs to get the `Greeter` class and make an instance:

```{literalinclude} ../../src/antidote_book/manual_lookup/__init__.py
---
start-at: def greeting
end-at: return f
---
```

Two lines but lots going on. 
First, what is `world`?
Think of it both as registry and a tool that can create instances.
It's a module with functions like `get`, but it's also stateful.

We need a `Greeter`, so we ask the `world` to go get us one.
Actually, we're saying:

- I'm looking for something that matches the `Greeter` symbol
- If you have already made one, return it (the "singleton" pattern, when there can only be one of something)
- Otherwise, find the "factory" that can make something that matches a `Greeter`
- Get the arguments that factory wants
- Pass those arguments into to the factory
- Return the result
- Oh, and remember that result for next time

That's our "view".
Instead of grabbing `Question`, we had to do `world.get(Greeter)` but the concept is similar.

## Wherefore Art Thou, `Greeter`?

But how did Antidote find the right `Greeter` and know how to make it?
The answer is simple, but deeper than you think.

We defined a `Greeter` class, and importantly, we decorated it with `@injectable`:

```{literalinclude} ../../src/antidote_book/manual_lookup/__init__.py
---
start-at: "@injectable"
end-at: "self.salutation"
---
```

What does `@injectable` do?
It registers that symbol -- `Greeter` -- in the registry.
In this case, it also says that the Python class is able to "construct" an instance of that symbol when asked.
In computer terms, it registers a "factory": something that can make a `Greeter`.

The `world` will do one more thing, though.
By default, Antidote registers injectables as "singletons".
This means the `world` will remember the constructed instance.
The next time something asks the `world` for a `Greeter`, it will *skip* construction and return the instance.

If you're using a smart editor, you'll get autocomplete all the way through.
If you're using a type checker, you'll get no warnings -- all is good in the `world`.

## Let's Run It

Not much to it...just call `greeting`:

```{literalinclude} ../../src/antidote_book/manual_lookup/__init__.py
---
start-at: "def main"
end-at: "return greeting"
---
```

We can see in `test_manual_lookup.py` a basic "does it match?" test:

```{literalinclude} ../../tests/test_manual_lookup.py
---
start-at: "test_shallow"
end-at: "assert actual"
---
```

The unit test for the `greeter` function though is different.
It has to get an *isolated* `world`.
Fortunately Antidote makes it easy with `world.test.clone` and `world.test.override.singleton`:

```{literalinclude} ../../tests/test_manual_lookup.py
---
start-at: "test_greeting"
end-at: 'assert actual == "Fake Hello!"'
---
```

If you suspect this test example is leading somewhere, well, you'd be right.
We're going to tackle that in the next chapter.

## That's a Whole Lotta Nothingburger

"Big deal. The class is right there...a few lines up! I could construct it myself!"

Yes. But.

As we'll see in the coming chapters, you don't always want *that* `Greeter`.
You might need "the system" to select the "best" `Greeter`.
You might want "the system" to help construct the `Greeter`, using other information it knows about.
In fact, you might want "the system" to call your `greeting` function.
And of course, you might like the idea that "the system" will manage the lifetime of the result.

Let's take a look and see where this leads us.
Hopefully, to a pluggable app.

## Download Files

- {download}`manual_lookup/__init__.py <../../src/antidote_book/manual_lookup/__init__.py>`
- {download}`tests/test_manual_lookup.py <../../tests/test_manual_lookup.py>`
