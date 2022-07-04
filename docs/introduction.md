# Introduction

Not every problem has a 5 line "Hello World" solution.

Building an application is usually great for the first five minutes.
But the next 5 years?
If you made your choices based on the first five minutes with a framework, you might have five years of hacks and fighting the framework ahead of you.
What if there was a way to build modular, extensible -- pluggable! -- applications from the start?

This usually means a lot of ceremony.
We're not here to write Java!
But as new frameworks such as FastAPI have shown, you *can* get people to do type hinting and dependency injection, if:

- The barrier is low
- The payoff is high

What if there was a general-purpose framework that helped you write your own pluggable application?
One that also had a low barrier and high payoff, but also -- some *very* interesting possibilities.

Welcome to Antidote, a modern, fast, well-supported package for dependency injection and more.

## About Pluggable Apps

What is a "pluggable app" and why should I care?
It's a topic I have a long interest in (Zope, Plone, Pyramid), so let's make the case.

Sometimes you have a "library"...a package where *you* call *it*.
For example, `urllib3` "is a powerful, user-friendly HTTP client for Python."

Sometimes you have a "framework"...a package that calls you.
Most web development packages -- Django, Flask, FastAPI -- are frameworks.
You write a view, register it, and run their app.
A request comes in, and they call your view, passing in the request data.

Neither of these -- library or framework -- is ready-to-go, "out of the box" (OOTB.)
You have write your "app".
But you don't distribute it as a PyPI package for others -- it's just meant for your needs.
At most, you publish your repo, with a `requirements.txt` that helps install the app.

But what if you *could* ship something that worked OOTB, but was extensible enough to turn from "their app" into "your app"?
This is the history I come from with Zope and Plone.
A ready-to-use app with well-defined plug-points, providing a rich ecosystem of quality plugins.
It's also true that Django, with its admin UI, has some of this OOTB experience as well.

But what if you wanted to make your own Django?
You need a framework-framework.
This is what Pyramid provided -- a *magnificent* web framework that was extensible in very, very rich ways.
In fact, this book looks at Antidote largely as a Pyramid old-timer.
Seeing the same patterns, but outside a web-only usage, and teleported into a modern Python context. 

## Benefits of Pluggable Apps

That's the history and positioning.
What specifically do I get from approaching my app as a "pluggable app"?

### OOTB

First, unlike a library or framework, you can ship an actual, working application.
Out-of-the-box.
Sane defaults, a UI, logging...the works.

It just so happens that you've written all of that ready-to-go functionality as well-defined, enforceable plug points that can be replaced downstream.

### Add/Replace Functionality

Let's look at pluggability.
The first and simplest way: *adding* something to the app.

You've seen this: adding a view to Flask, adding a model to Django, adding a template to Sphinx, adding a plugin in pytest.
Pretty straightforward.

The second kind of pluggability is tougher: replacing something that's built-in.
It's tougher: the framework needs to anticipate that a different implementation will be used by anything calling that feature.
And this replacement implementation is *unknown to the framework author* until runtime in somebody's site.

When this is supported, it can be kind of clunky, for several reasons:

- The replaceability was added after-the-fact
- You probably replace the original implementation (monkeypatch) and can no longer reach it
- The mechanism of replacement is magical ("leave a special file in this special directory")
- Debugging is..ahem...problematic

Thus, it's tough.
And we haven't gotten to the powerful one yet.

### Vary Functionality

"I want to replace the logo but only when looking at an Invoice."
That one sentence uncovers a LOT of power, but also complexity.

You might have seen this in web frameworks.
Flask lets you register [different views for HTTP methods](https://flask.palletsprojects.com/en/2.1.x/quickstart/#http-methods).
Meaning, you get a few limited, built-in ways to vary a few built-in things.

But what if you wanted more ways -- and more *powerful ways -- to vary?
What if you wanted register your *own* ways to vary?
Pyramid really pioneered this with its {term}`pyramid:predicate` concept.
In Pyramid, predicates apply to many places where you want to go find something -- a view, a route, a subscriber, etc.
This is part of what makes Pyramid shine as a framework-framework.

But there's a step beyond even this.
What if you want to register your *own kinds of things*?
Maybe your pluggable app has nothing to do with views, routes, and subscribers.
It doesn't even deal with the web.

You'll need a powerful framework-framework that is independent of an existing pluggable app.

### Small Core

We've all admired over the years those packages that advertise "a small core with lots of plugins."
And for good reasons.
It's good for both the consumer of the package and the author of the package.

Of course, that benefit comes at a cost: it's hard to get the plug-points right.
It's even harder to make a pluggability architecture that gives extensibility without being too magical.

### Static Analysis

TODO Finish

- Static analysis vs. "magic string" of convention over configuration

- Broad quality ecosystem via contracts
- Caller-callee decoupling
- Smaller surface area
- Tracking, caching, rebuild
  
## Setup
  - 
Python version

## About This Book

- How to use this book
  - Install
  - Run

- Executable install
- 
## Sample App: `MegaStore`

Let's learn Antidote by gradually writing a pluggable application.
This app shows itself in several ways:

- A book...this book!
- Example code in the book which is:
  - Fully-runnable
  - With tests
  - And passes other quality tools (mypy, black, flake8, etc.)
- An installable package which you can then:
  - Invoke the examples and run them
  - Make your own "site" to extend the pluggable app

For the sample app's scenario, imagine a `MegaStore` chain of stores.
Each store greets customers as they come in.
`MegaStore` provides a system for doing so, with defaults at the corporate level.
But each store can change some defaults, to make it more local to the area -- including installing plugins.

- `App` is what `MegaStore` provides to each store
- `Site` is what each individual store deploys
- `Plugin` is optional software that a `Site` can add to the `App`
- `Customer` is someone who walks in
- `Greeter` is someone who meets the `Customer`
- `greeting` is what they say to the `Customer`
- `Config` provides common settings such as the punctuation on the `greeting`

Clever readers might spot that this parallels web applications:

- `App` is a framework
- `Site` is an installation that uses that framework
- `Customer` is an HTTP request
- `Greeter` is a view
- `Greeting` is a response

We'll use this scenario in the first two sections of the book.

- About this project
  - Test first
  - typing

## My Interest: Sphinx
