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

- Replaceable parts with `@interface`
- Replacing a built-in with `@override`
- debugging_antidote_apps
- Providing a fallback with `.by_default`
  - And `implements.overriding`
- Varying lookup with qualifiers
- Replaceable specs with protocols
- (new) Smaller surface areas with operators
- Per-transaction data from scopes
- Injection from scope
- Convenient plugs with decorators
- Best-match with predicates

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
