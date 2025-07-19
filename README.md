# Python Playground

This repo serves as a 6 week challenge to get up to speed learning Python.
The learning roadmap and weekly code challenges were developed using ChatGPT and implemented by yours truly. The core resource for learning
Python concepts was [the Python tutorial](https://docs.python.org/3/tutorial/index.html).

*Note the code isn't necessary friendly towards beginner developers.* This challenge was done in the context of a seasoned
backend developer applying OOP patterns and package best-practices in Python.

## Week 1 - Python Core Syntax + OOP Basics

**Topics:**
- Data types, methods, classes, args/kwargs, errors
- `@classmethod`, `@property` decorators
- Package structure
- Unit testing
- Intro to inheritance
- Intro to entity persistence with SQLAlchemy

**Project:**
The Jamobank package provides the `BankAccount` class with robust deposit and withdraw methods.

## Week 2: Advanced OOP + Dunder Methods + Type Hints

**Topics:**
- __init__, __str__, __eq__, __repr__, etc.
- List comprehensions
- Inheritance, mixins, abstract base classes
- Type hints (typing) + mypy

**Project:**
Build a small library system: Book, Library, User classes with __eq__, custom sorting, and type annotations.

**Resources:**
[Typing Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Week 3: Decorators + Context Managers + Modules

**Topics:**
- Function and class decorators (@wraps, @classmethod)
- with blocks + __enter__ / __exit__
- Linters (`ruff`, `flake8`, `black`)

**Project:**
Write a @logger decorator to log function calls and a context manager for timing code blocks.

**Resources:**
- [Real Python – Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python Docs – Context Managers](https://docs.python.org/3/library/contextlib.html)

## Week 4: Files, JSON, Dataclasses, Unit Testing

**Topics:**
- open(), file reading/writing
- json and csv modules
- dataclasses vs classic classes
- unittest or pytest

**Practice:**
Build a small CLI note app with file-based persistence covered by unit tests.

**Resources:**
- [Real Python – Dataclasses](https://realpython.com/python-data-classes/)
- [Pytest Docs](https://docs.pytest.org/en/stable/)

## Week 5: SQLAlchemy + FastAPI

**Topics:**
- FastAPI
- SQLAlchemy models + Pydantic schemas

**Project:**
Build a mini blog API (/users, /posts, etc.) with entity persistence.

**Resources:**
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

## Week 6: AsyncIO + Real Project or Portfolio App

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
