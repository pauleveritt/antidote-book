# Varying Injection with Qualifiers

- Not just french in a Quebec store, speak French to FrenchCustomer
- So FrenchGreeting when it is a FrenchCustomer, DefaultGreeting when DefaultCustomer
- In next step, we can move this to injection
- Failing test, adding 4 possibilities in test_main
- Add a test_french_greeting, change other to test_default_greeting
- Drop salutation, to get a simpler example

- Add customer.FrenchCustomer
  - Note that we're not making it injectable yet
- Change get_greeeting to accept a Customer, with a default of DefaultCustomer
  - No longer inject greeting
  - It then does inject.me(qualified_by)
- FrenchGreeting
  - Don't subclass from DefaultGreeting, as it will also match that
- Customer can't yet vary, as it is the QualifiedBy
-
- Handle site.py FrenchSalutation
