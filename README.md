# Python Playground

This repo serves as a 6 week challenge to get up to speed learning Python.
The learning roadmap was developed using ChatGPT and the code was written by yours truly. The core resource for learning
Python concepts was [the Python tutorial](https://docs.python.org/3/tutorial/index.html).


## Week 1 - Python Core Syntax + OOP Basics

**Topics:**
- Data types, methods, classes, args/kwargs, errors
- `@classmethod`, `@property` decorators
- Package structure
- Unit testing
- Inheritance with abstract base classes
- Intro to entity persistence with SQLAlchemy

**Project:**
The Jamobank package provides the `BankAccount` class with robust deposit and withdraw methods.

## Week 2: More OOP + Dunder Methods

**Topics:**
- Dunder methods
- List comprehensions
- Refined package structure
- Linting with Black

**Project:**
The `jamolib` package provides the core functionality of a library's checkout system between books and users.
Once populated, a library's book catalog can be searched with the ability to sort by author or title.
Enter into a REPL session with `python -m jamolib` or run the tests with `pytest jamolib`

## Week 3: Decorators + Context Managers + Modules

**Topics:**
- Function and class decorators (@wraps, @classmethod)
- Mixins
- with blocks + enter and exit Dunder methods
- Strict type hint refactor with mypy
- Interdependent package module imports

**Project:**
Write a @logger decorator to log function calls and a context manager for timing code blocks.

**Resources:**
- [Typing Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Real Python – Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python Docs – Context Managers](https://docs.python.org/3/library/contextlib.html)

## Week 4: Files, JSON, Dataclasses

**Topics:**
- open(), file reading/writing
- json modules
- dataclasses vs classic classes
- transition from unittest to Pytest

**Project:**
Build a object formatting/writing service where a given object can be formatted and saved into different file types
(e.g. JSON, Markdown front matter). Wrap the service with a CLI meant for creating "Songs" which is a simple construct
used on personal site.

**Resources:**
- [Real Python – Dataclasses](https://realpython.com/python-data-classes/)
- [Pytest Docs](https://docs.pytest.org/en/stable/)

## Week 5: SQLAlchemy + Flask

**Topics:**
- Flask
- SQLAlchemy models + Pydantic schemas

**Project:**
Refactor above CLI to persist "Song" objects with secondary step of saving to file. CLI should also have
the ability to list and delete entities. Duplicate CLI functionality with API endpoints (/songs/create, /songs)

**Resources:**
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

## Week 6: TBD -- Previously AsyncIO + Real Project or Portfolio App

**Topics:**
- async def, await, async with
- FastAPI async routes + async SQLAlchemy
- Background tasks, error handling

**Project Ideas:**
REST API for a task manager
Personal bookmarks manager with tags + search
Public API that returns data from a JSON file or DB

**Resources:**
- [FastAPI Async Guide](https://fastapi.tiangolo.com/async/)
