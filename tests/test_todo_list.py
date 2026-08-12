from models.TodoList import TodoList

from tests.test_todo import create_todo_no_due_date

# ---------------------------------------------------------------------------- #
# ------------------------------ Initialization ------------------------------ #
# ---------------------------------------------------------------------------- #
def test_todo_list_initialization():
    todo_list = TodoList()

    assert todo_list.repo.get_all() == {}

# ---------------------------------------------------------------------------- #
# ------------------------------------ Add ----------------------------------- #
# ---------------------------------------------------------------------------- #
def test_add_todo_valid():
    todo_list = TodoList()
    todo = create_todo_no_due_date()

    result = todo_list.add(todo=todo)

    assert result == True
    assert len(todo_list.repo.get_all()) == 1

def test_add_todo_duplicate():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo=todo)

    result = todo_list.add(todo=todo)

    assert result == False
    assert len(todo_list.repo.get_all()) == 1

# ---------------------------------------------------------------------------- #
# ------------------------------ Get Todo By ID ------------------------------ #
# ---------------------------------------------------------------------------- #
def test_get_todo_by_id_valid():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo=todo)

    target = todo_list.get_todo_by_id(todo_id=todo.id)

    assert target == todo

def test_get_todo_by_id_empty_collection():
    todo_list = TodoList()

    result = todo_list.get_todo_by_id(todo_id=1)

    assert result == None
    assert len(todo_list.repo.get_all()) == 0

def test_get_todo_by_id_invalid_id():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo)

    result = todo_list.get_todo_by_id(4)

    assert result == None

# ---------------------------------------------------------------------------- #
# ---------------------------------- Remove ---------------------------------- #
# ---------------------------------------------------------------------------- #
def test_remove_todo_valid():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo=todo)

    result = todo_list.remove(todo_id=todo.id)

    assert result == True
    assert len(todo_list.repo.get_all()) == 0

def test_remove_todo_empty_collection():
    todo_list = TodoList()

    result = todo_list.remove(todo_id=1)

    assert result == False

def test_remove_todo_invalid_id():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo=todo)

    result = todo_list.remove(todo_id=2)

    assert result == False
    assert len(todo_list.repo.get_all()) == 1

# ---------------------------------------------------------------------------- #
# ---------------------------------- Get All --------------------------------- #
# ---------------------------------------------------------------------------- #
def test_get_all_empty():
    todo_list = TodoList()

    result = todo_list.get_all()

    assert len(result) == 0
    assert result == []

def test_get_all_single():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo)

    result = todo_list.get_all()

    assert len(result) == 1
    assert result == list(todo_list.repo.get_all().values())

def test_get_all_multiple():
    todo_list = TodoList()
    num_todos = 3

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todo_list.add(todo)

    result = todo_list.get_all()

    assert len(result) == num_todos

# ---------------------------------------------------------------------------- #
# ------------------------------- Get Completed ------------------------------ #
# ---------------------------------------------------------------------------- #
def test_get_completed_empty():
    todo_list = TodoList()

    result = todo_list.get_completed()

    assert len(result) == 0

def test_get_completed_single_completed():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo=todo)
    todo.complete()

    result = todo_list.get_completed()

    assert len(result) == 1
    assert result[0] == todo

def test_get_completed_single_incomplete():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo=todo)

    result = todo_list.get_completed()
    print(result)

    assert len(result) == 0

def test_get_completed_multiple_none_complete():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todo_list.add(todo=todo)

    result = todo_list.get_completed()

    assert len(result) == 0

def test_get_completed_multiple_single_completed():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1

        if i == 0:
            todo.complete()

        todo_list.add(todo=todo)

    result = todo_list.get_completed()

    assert len(result) == 1
    assert result[0] == todo_list.get_all()[0]

def test_get_completed_multiple_some_completed():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1

        if i in [0, 1]:
            todo.complete()

        todo_list.add(todo=todo)

    result = todo_list.get_completed()
    print(result)

    assert len(result) == 2
    assert result == todo_list.get_all()[:2]

def test_get_completed_multiple_all_completed():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todo.complete()
        todo_list.add(todo=todo)

    result = todo_list.get_completed()

    assert len(result) == num_todos
    assert result == todo_list.get_all()

# ---------------------------------------------------------------------------- #
# -------------------------------- Get Pending ------------------------------- #
# ---------------------------------------------------------------------------- #
def test_get_pending_empty():
    todo_list = TodoList()

    result = todo_list.get_pending()

    assert len(result) == 0

def test_get_pending_single_pending():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo_list.add(todo=todo)

    result = todo_list.get_pending()

    assert len(result) == 1
    assert result == todo_list.get_all()

def test_get_pending_single_completed():
    todo_list = TodoList()
    todo = create_todo_no_due_date()
    todo.complete()
    todo_list.add(todo=todo)

    result = todo_list.get_pending()

    assert len(result) == 0

def test_get_pending_multiple_none_pending():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todo.complete()
        todo_list.add(todo=todo)

    result = todo_list.get_pending()

    assert len(result) == 0

def test_get_pending_multiple_single_pending():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1

        if i != 0:
            todo.complete()

        todo_list.add(todo=todo)

    result = todo_list.get_pending()

    assert len(result) == 1
    assert result[0] == todo_list.get_all()[0]

def test_get_pending_multiple_some_pending():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1

        if i not in [0, 1]:
            todo.complete()

        todo_list.add(todo=todo)

    result = todo_list.get_pending()

    assert len(result) == 2
    assert result == todo_list.get_all()[:2]

def test_get_pending_multiple_all_pending():
    todo_list = TodoList()
    num_todos = 5

    for i in range(num_todos):
        todo = create_todo_no_due_date()
        todo.id = i + 1
        todo_list.add(todo=todo)

    result = todo_list.get_pending()

    assert len(result) == num_todos
    assert result == todo_list.get_all()