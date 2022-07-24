# Extend

Adding a new thing.

- Test-first
- Instead of salutation on Greeting, we want to get it from a service in a *new* plugin
- This service looks at the time of day and gives a salutation
- Singleton is ok, since the time lookup is in the __call__
- Add the test for salutation, second for lookup
- Change the greeting test to str the salutation and check if in the two choices
- Same for test_main