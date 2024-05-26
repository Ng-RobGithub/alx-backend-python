0x03-Unittests_and_integration_tests

They help ensure that individual components and their interactions function correctly

Characteristics:

Isolated: Unit tests should not depend on external systems like databases, APIs, or the filesystem.
Fast: They run quickly since they test small pieces of code in isolation.
Repeatable: They produce the same results every time they run, given the same input.

A. Run pycodestyle on your files to check for style issues:
- pycodestyle your_script.py

Use the following command to run your tests:
- python -m unittest discover tests
