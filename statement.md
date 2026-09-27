PROJECT STATEMENT: PASSGEN
==========================

PROBLEM STATEMENT
-----------------
Everyday users and students frequently use predictable, low-complexity passwords (such as common names, sequential numbers, or personal details) to avoid the friction of remembering complex strings. Furthermore, novice developers attempting to automate password generation often rely on standard pseudo-random number generators like Python's built-in "random" module. This module uses the deterministic Mersenne Twister algorithm, which can be reverse-engineered and is fundamentally unsafe for cryptographic security.


SCOPE OF THE PROJECT
--------------------
PassGen is developed as a lightweight, zero-dependency command-line utility built entirely with the Python standard library. The scope of this project encompasses:

* Providing cryptographically sound password generation powered directly by operating system entropy (/dev/urandom on Linux systems via the Python "secrets" module).
* Evaluating existing or newly generated passwords across multiple complexity vectors to encourage strong security habits.
* Delivering a portable, cross-platform terminal interface that runs out of the box on Python 3 without requiring virtual environments or external package installations.


TARGET USERS
------------
* Students and General Users: Individuals looking for a fast, offline tool to generate unguessable passwords without trusting third-party web services.
* Developers and System Administrators: Technical users who need a quick, scriptable CLI tool to produce high-entropy strings for local testing, API keys, or temporary credentials.
* Academic Evaluators: Reviewers assessing practical applications of cryptographic randomness, string algorithms, and modular software testing.


HIGH-LEVEL FEATURES
-------------------
* Cryptographic Randomness: Leverages CSPRNG via secrets.choice to eliminate predictable output patterns.
* Customizable Credential Length: Permits custom string lengths (defaulting to 12) while balancing uppercase, lowercase, numerical, and special characters.
* Multi-Vector Strength Evaluation: Assesses credentials against length thresholds, casing diversity, digits, and punctuation to provide qualitative feedback (Weak, Medium, Strong).
* Interactive Terminal Workflow: Simple text menu loop for generation, strength testing, and exit operations.
* Automated Unit Testing: Includes a standardized test suite using the unittest library to verify generation length and evaluation scoring.