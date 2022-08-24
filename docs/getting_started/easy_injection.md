# Easy Lookup with Injection

Our `greeting` function was able to ask the `world` for a `Greeter`.
That lookup is simple, but we can do better.

Let's take this lookup _out_ of our function body.
Instead, let's get Antidote to _inject_ our `Greeter`.

Injection!
Yeh baby!

## Using `world` Directly is a Code Smell

In our previous example, we used `world.get` within our function to grab the `Greeter`:

```{literalinclude} ../../src/antidote_book/manual_lookup/__init__.py
---
start-at: def greeting
end-at: return "No
emphasize-lines: 3
---
```

It works but let's see if _injection_ is a better fit.
As Antidote covers in its {doc}`Tutorial Introduction <antidote:tutorial/1_introduction>`:

:::{note} Use Injection

Prefer using `inject()` to `world.get`.
`greeting` does not rely on dependency injection making it harder to test!
`.inject` is also considerably faster thanks to heavily tuned cython code.
:::

Easier to test, faster, and it will also tap into some superpowers.
It also eases our later goal of replaceability: the signature tells us its "surface area" with the outside world.

## Inject My `Greeter`

Big words!
Let's ask Antidote's _injector_ to do the work of `world.get(Greeter)`:

```{literalinclude} ../../src/antidote_book/easy_injection/__init__.py
---
start-at: def greeting
end-at: return "N
emphasize-lines: 1
---
```

Here, `greeting` stated its _dependencies_ in its _function parameters_.
Wanna know what it needs?
It tells you waht it needs -- right there between the `()`.
It needs a `Greeter` and asked "the system" to go get one.

Nothing changes with the `Greeter` or its "registration" as an injectable:

```{literalinclude} ../../src/antidote_book/easy_injection/__init__.py
---
start-at: "@injectable"
end-at: "self.salutation"
---
```

When our code runs the `greeting` function:

```{literalinclude} ../../src/antidote_book/easy_injection/__init__.py
---
start-at: "def main"
end-at: "return greeting"
---
```

...the "system" steps in:

- In the `main` call to `greeting()`, we don't pass an argument
- The `@injectable` decorator looks for the default value for the `greeter` parameter
- `inject.me()` is the default value
- When it runs, it looks at the type hint on that parameter to find `Greeter`
- That type is what is used for the injection lookup
- Therefore, it does a `world.get(Greeter)`

This whole process is called "injection", in which the Antidote system:

- Looks up something that needs to run
- Finds its parameters and their definitions
- Performs some works to find values to pass in
- Call that target with the arguments
- Return the result value

We can see in `test_easy_injection.py` another basic "does it match?" test, same as the previous chapter:

```{literalinclude} ../../tests/test_easy_injection.py
---
start-at: "test_shallow"
end-at: "assert actual"
---
```

For the unit test, though...remember back to our Django view example in the previous chapter?

```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

In this view function, `Question` is _inside_ the function.
This means it has to be mocked in some way.

In the previous chapter, we had to do that also, with `world.test.new` and `overrides`.
But thanks to injection, we can just _pass in_ our dependency, which makes the test code super simple:

```{literalinclude} ../../tests/test_easy_injection.py
---
start-at: "test_greeting"
end-at: 'assert actual == "From Test!"'
---
```

Test writing is now _really_ easy, as my test just passed in a `Greeter`.

In summary: our function had a dependency, and we asked for it to be injected.
The caller (our test) was decoupled from the callee (`greeting`.)
You can thus _extend_ a system without forking either side.

And quite possibly, gain some superpowers along the way.

## Download Files

- {download}`easy_injection/__init__.py <../../src/antidote_book/easy_injection/__init__.py>`
- {download}`tests/test_easy_injection.py <../../tests/test_easy_injection.py>`
