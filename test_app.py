import todo_cli

def setup_function():
    todo_cli.tasks.clear()

def test_add_task():
    task = todo_cli.add_task("Buy milk")
    assert task["title"] == "Buy milk"
    assert task["completed"] is False
    assert task["id"] == 1

def test_list_tasks():
    todo_cli.add_task("Buy milk")
    tasks = todo_cli.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy milk"

def test_update_task():
    todo_cli.add_task("Buy milk")
    updated = todo_cli.update_task(1)
    assert updated is not None
    assert updated["completed"] is True

def test_update_invalid_task():
    updated = todo_cli.update_task(99)
    assert updated is None

def test_delete_task():
    todo_cli.add_task("Buy milk")
    result = todo_cli.delete_task(1)
    assert result is True
    assert len(todo_cli.tasks) == 0

def test_delete_invalid_task():
    result = todo_cli.delete_task(50)
    assert result is False
