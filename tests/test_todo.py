from datetime import datetime, timedelta

from models.Todo import Todo

def create_todo_no_due_date():
    # Due date defaults to None
    return Todo(id=1, title="Test", description="Testing", priority="Low")

def create_todo_with_due_date(due_date: datetime):
    return Todo(id=1, title="Test", description="Testing", priority="Low", due_date=due_date)

# ---------------------------------------------------------------------------- #
# ------------------------------ Initialization ------------------------------ #
# ---------------------------------------------------------------------------- #
def test_initialize_no_due_date():
    todo = create_todo_no_due_date()

    assert todo.id == 1
    assert todo.title == "Test"
    assert todo.description == "Testing"
    assert todo.priority == "Low"
    assert todo.due_date == None
    assert todo.completed == False
    assert todo.created_date < datetime.now()

def test_initialize_with_due_date():
    todo = create_todo_with_due_date(due_date=datetime.now() + timedelta(days=1))

    assert todo.id == 1
    assert todo.title == "Test"
    assert todo.description == "Testing"
    assert todo.priority == "Low"
    assert todo.due_date is not None
    assert todo.due_date > datetime.now()
    assert todo.completed == False
    assert todo.created_date < datetime.now()

# ---------------------------------------------------------------------------- #
# --------------------------------- Complete --------------------------------- #
# ---------------------------------------------------------------------------- #
def test_complete_incompleted_todo():
    todo = create_todo_no_due_date()
    result = todo.complete()

    assert result == True
    assert todo.completed == True

def test_complete_completed_todo():
    todo = create_todo_no_due_date()
    todo.complete()

    result = todo.complete()

    assert result == False
    assert todo.completed == True

# ---------------------------------------------------------------------------- #
# -------------------------------- Uncomplete -------------------------------- #
# ---------------------------------------------------------------------------- #
def test_uncomplete_completed_todo():
    todo = create_todo_no_due_date()
    todo.complete()

    result = todo.uncomplete()

    assert result == True
    assert todo.completed == False

def test_uncomplete_uncompleted_todo():
    todo = create_todo_no_due_date()

    result = todo.uncomplete()

    assert result == False
    assert todo.completed == False

# ---------------------------------------------------------------------------- #
# -------------------------------- Is Overdue -------------------------------- #
# ---------------------------------------------------------------------------- #
def test_is_overdue_no_due_date():
    todo = create_todo_no_due_date()
    result = todo.is_overdue()

    assert result == False

def test_is_overdue_not_overdue():
    todo = create_todo_with_due_date(due_date = datetime.now() + timedelta(days=1))

    result = todo.is_overdue()

    assert result == False

def test_is_overdue_overdue():
    todo = create_todo_with_due_date(due_date=datetime.now() - timedelta(days=1))

    result = todo.is_overdue()

    assert result == True