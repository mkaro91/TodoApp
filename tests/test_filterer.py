from datetime import datetime, timedelta

from models.Todo import Priority
from services.todo_filterer import TodoFilterer

from tests.test_todo import create_todo_no_due_date, create_todo_with_due_date

FILTERER = TodoFilterer()

# ---------------------------------------------------------------------------- #
# ------------------------------- By Completed ------------------------------- #
# ---------------------------------------------------------------------------- #
def test_filter_by_completed_complete_empty_todos():
    todos = []

    results = FILTERER.by_completed(todo_list=todos, is_completed=True)

    assert len(todos) == 0
    assert len(results) == 0

def test_filter_by_completed_incompleted_empty_todos():
    todos = []

    results = FILTERER.by_completed(todo_list=todos, is_completed=False)

    assert len(todos) == 0
    assert len(results) == 0

def test_filter_by_completed_complete_no_result():
    todos = []

    for i in range(6):
        todo = create_todo_no_due_date()

        id = i + 1
        todo.id = id

        todos.append(todo)

    results = FILTERER.by_completed(todo_list=todos, is_completed=True)

    assert len(todos) == 6
    assert len(results) == 0

def test_filter_by_completed_incomplete_no_result():
    todos = []

    for i in range(6):
        todo = create_todo_no_due_date()

        id = i + 1
        todo.id = id
        todo.complete()
        todos.append(todo)

    results = FILTERER.by_completed(todo_list=todos, is_completed=False)

    assert len(todos) == 6
    assert len(results) == 0

def test_filter_by_completed_complete():
    todos = []

    for i in range(6):
        todo = create_todo_no_due_date()

        id = i + 1
        todo.id = id

        if id % 2 == 0:
            todo.complete()

        todos.append(todo)

    results = FILTERER.by_completed(todo_list=todos, is_completed=True)

    assert len(todos) == 6
    assert len(results) == 3

def test_filter_by_completed_incomplete():
    todos = []

    for i in range(6):
        todo = create_todo_no_due_date()

        id = i + 1
        todo.id = i

        if id % 2 == 0:
            todo.complete()

        todos.append(todo)

    results = FILTERER.by_completed(todo_list=todos, is_completed=False)

    assert len(todos) == 6
    assert len(results) == 3

# ---------------------------------------------------------------------------- #
# -------------------------------- By Priority ------------------------------- #
# ---------------------------------------------------------------------------- #
def test_by_priority_critical_empty_todos():
    todos = []
    results = FILTERER.by_priority(todo_list=todos, priority=Priority.CRITICAL)

    assert len(todos) == 0
    assert len(results) == 0

def test_by_priority_high_empty_todos():
    todos = []
    results = FILTERER.by_priority(todo_list=todos, priority=Priority.HIGH)

    assert len(todos) == 0
    assert len(results) == 0

def test_by_priority_medium_empty_todos():
    todos = []
    results = FILTERER.by_priority(todo_list=todos, priority=Priority.MEDIUM)

    assert len(todos) == 0
    assert len(results) == 0

def test_by_priority_low_empty_todos():
    todos = []
    results = FILTERER.by_priority(todo_list=todos, priority=Priority.LOW)

    assert len(todos) == 0
    assert len(results) == 0

def test_by_priority_critical_no_results():
    todos = []

    for i, priority in enumerate([Priority.HIGH, Priority.MEDIUM, Priority.LOW], start=1):
        todo = create_todo_no_due_date()
        todo.id = i
        todo.priority = priority

        todos.append(todo)

    results = FILTERER.by_priority(todo_list=todos, priority=Priority.CRITICAL)

    assert len(todos) == 3
    assert len(results) == 0

def test_by_priority_high_no_results():
    todos = []

    for i, priority in enumerate([Priority.CRITICAL, Priority.MEDIUM, Priority.LOW], start=1):
        todo = create_todo_no_due_date()
        todo.id = i
        todo.priority = priority
        todos.append(todo)

    results = FILTERER.by_priority(todo_list=todos, priority=Priority.HIGH)

    assert len(todos) == 3
    assert len(results) == 0

def test_by_priority_medium_no_results():
    todos = []

    for i, priority in enumerate([Priority.CRITICAL, Priority.HIGH, Priority.LOW], start=1):
        todo = create_todo_no_due_date()
        todo.id = i
        todo.priority = priority
        todos.append(todo)

    results = FILTERER.by_priority(todo_list=todos, priority=Priority.MEDIUM)

    assert len(todos) == 3
    assert len(results) == 0

def test_by_priority_low_no_results():
    todos = []

    for i, priority in enumerate([Priority.CRITICAL, Priority.HIGH, Priority.MEDIUM], start=1):
        todo = create_todo_no_due_date()
        todo.id = i
        todo.priority = priority
        todos.append(todo)

    results = FILTERER.by_priority(todo_list=todos, priority=Priority.LOW)

    assert len(todos) == 3
    assert len(results) == 0

# ---------------------------------------------------------------------------- #
# -------------------------------- By Due Date ------------------------------- #
# ---------------------------------------------------------------------------- #
def test_by_due_date_empty_todos():
    todos = []
    results = FILTERER.by_due_date(todo_list=todos, due_date=datetime.now())

    assert len(todos) == 0
    assert len(results) == 0

def test_by_due_date_no_results():
    todos = []

    for i in range(5):
        todo = create_todo_with_due_date(due_date=datetime.now())
        todo.id = i + 1
        todos.append(todo)

    results = FILTERER.by_due_date(todo_list=todos, due_date=datetime.now() - timedelta(days=1))

    assert len(todos) == 5
    assert len(results) == 0

def test_by_due_date_results():
    todos = []

    for i in range(5):
        todo = create_todo_with_due_date(due_date=datetime.now())
        todo.id = i + 1
        todos.append(todo)

    results = FILTERER.by_due_date(todo_list=todos, due_date=datetime.now() + timedelta(days=1))

    assert len(todos) == 5
    assert len(results) == 5

# ---------------------------------------------------------------------------- #
# -------------------------------- By Keyword -------------------------------- #
# ---------------------------------------------------------------------------- #
def test_by_keyword_empty_todos():
    todos = []
    results = FILTERER.by_keyword(todo_list=todos, keyword='a')

    assert len(todos) == 0
    assert len(results) == 0

def test_by_keyword_no_results():
    todos = []

    for i in range(5):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todos.append(todo)

    results = FILTERER.by_keyword(todo_list=todos, keyword='elephant')

    assert len(todos) == 5
    assert len(results) == 0

def test_by_keyword_results_in_title():
    todos = []

    for i in range(5):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todo.description = "description"
        todos.append(todo)

    results = FILTERER.by_keyword(todo_list=todos, keyword="test")

    assert len(todos) == 5
    assert len(results) == 5

def test_by_keyword_results_in_description():
    todos = []

    for i in range(5):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todo.description = "description"
        todos.append(todo)

    results = FILTERER.by_keyword(todo_list=todos, keyword="description")

    assert len(todos) == 5
    assert len(results) == 5