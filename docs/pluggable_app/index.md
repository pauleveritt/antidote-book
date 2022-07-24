# A Pluggable App

Now that we've learned the basics of Antidote, let's learn the basics of _pluggable apps_.
In this section, we'll:

- Change our directory layout to the "app", "plugin", "site" structure

Along the way, we'll start to "make the case" for pluggable apps: the "why" as much as the "what" and the "how".
We'll then use this understanding in later sections, where we start building real-world useful software.

As you go through these sections, keep in mind some of the tenets we're advocating for pluggable apps:

- Pluggability: extend, replace, vary
- Fail faster with strong typing
- Decoupling the caller and callee
- Clearly expressing your callable's dependencies

Next

- Varying lookup with qualifiers
- debugging_antidote_apps
- (new) Smaller surface areas with operators
- Per-transaction data from scopes with injection from scope
- Convenient plugs with decorators
- Best-match with predicates
- (MAYBE) Start refactoring as generic view/resource/request/response system

```{toctree}
---
hidden:
maxdepth: 1
---

app_layout
interfaces
protocols
extend
replace
debugging_antidote_apps
```
