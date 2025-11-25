from app import tasks, add_task, list_tasks, update_task, delete_task

def setup_function():
    tasks.clear()

def test_add_task():
    task = add_task("Buy milk")
    assert task["id"] == 1
    assert task["title"] == "Buy milk"
    assert task["completed"] is False

def test_list_tasks():
    add_task("Buy milk")
    all_tasks = list_tasks()
    assert len(all_tasks) == 1

def test_update_task():
    add_task("Buy milk")
    updated = update_task(1, completed=True)
    assert updated is not None
    assert updated["completed"] is True

def test_delete_task():
    add_task("Buy milk")
    result = delete_task(1)
    assert result is True

def test_delete_nonexistent_task():
    result = delete_task(99)
    assert result is False
