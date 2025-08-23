# Python Playground

This repo houses a 6 week challenge to get up to speed learning Python.
The learning roadmap was initially developed using ChatGPT, but was heavily tweaked week-to-week
to suit topics I was interested in exploring. All code was written by yours truly.
The core resource for learning Python concepts was [the Python tutorial](https://docs.python.org/3/tutorial/index.html)
with judicious use of ChatGPT to learn best practices.


## Week 1: Python Core Syntax + OOP Basics

**Topics:**
- Data types, methods, classes, args/kwargs, errors
- `@classmethod`, `@property` decorators
- Package structure
- Unit testing
- Inheritance with abstract base classes
- Intro to entity persistence with SQLAlchemy

**Project:**
The Jamobank package provides the `BankAccount` class with robust deposit and withdraw methods.

## Week 2: More OOP + Dunder Methods + Linting

**Topics:**
- Dunder methods
- List comprehensions
- Refined package structure
- Linting with Black

**Project:**
The `jamolib` package provides the core functionality of a library's checkout system between books and users.
Once populated, a library's book catalog can be searched with the ability to sort by author or title.
Enter into a REPL session with `python -m jamolib` or run the tests with `pytest jamolib`

## Week 3: Decorators + Context Managers + Typing

**Topics:**
- Functool decorators (@wraps)
- Context managers
- Logging module
- Intro to OS library
- Strict type hint refactor with mypy

**Project:**
The `utilities` package contains @log and @profile decorators alongside a ChangeDirectory context manager

## Week 4 and 5: Files, stdlib modules, packages

**Topics:**
- File reading/writing, open()
- Mixins
- Dataclasses
- Dict comprehensions
- ABC class, `@abstractmethod`
- Warnings, Regex and Json modules
- Refactor out functionality to make PyPI package
- Python package best practices
- Docstring best practices (PEP 257)
- Virtual environments
- Release parsing package on PyPI
- Implement parsing package back in CLI project
- Python does not have null-safe method chaining :(

**Project:**
Build a CLI program to read and list Markdown files and parse their front matter. CLI can also edit the front matter
content of a given file and then write that content back to the file. Refactors out parsing functionality to create a standalone
[PyPI package](https://github.com/jamogriff/markup-front-matter-parser).

## Week 5 and 6: SQLAlchemy + CSV module

**Topics:**
- CSV module
- SQLAlchemy models + Pydantic schemas
- Python package dependency and virtual environment hell

**Project:**
Build a module to parse a large CSV, a service to persist data to a database with SQLAlchemy
and a repo to select data from said database with model hydration. This project has been migrated to
[a new repo](https://github.com/jamogriff/narababy-export-analyzer) because messing with pyenv, pipenv and uv
simultaneously has broken git commits.

**Resources:**
- [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial)

## Week 7 and Beyond: Capstone Project

**Project:**
TODO: post a link to dedicated repo
