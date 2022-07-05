# A Pluggable App

- Software layout: site.py, framework/_, plugins/_/\*
- Re-organize into thin core with plugins for built-ins as framework/plugins/_/_
- Custom creation with factory callables
- Replaceable parts with `@interface`
- Replacing a built-in with `@override`
- Providing a fallback with `.by_default`
  - And `implements.overriding`
- Varying lookup with qualifiers
- Replaceable specs with protocols
- Per-transaction data from scopes
- Injection from scope
- Convenient plugs with decorators
- Best-match with predicates
