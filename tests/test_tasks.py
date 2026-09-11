import pytest
from tasks import add_task, complete_task, remove_task, list_tasks


def test_add_task_without_tags():
    """Confirma que tags de tarefas diferentes não partilham a mesma lista
    quando 'tags' não é passado explicitamente (regressão para o bug
    do valor padrão mutável)."""
    tasks = []
    tasks = add_task(tasks, "Tarefa 1")   # sem tags
    tasks = add_task(tasks, "Tarefa 2")   # sem tags

    tasks[0]["tags"].append("urgente")    # mutar só a primeira

    assert tasks[0]["tags"] == ["urgente"]
    assert tasks[1]["tags"] == []         # a segunda NÃO deve ser afetada

    
def test_complete_task_valid_index():
    """Verifica que complete_task completa uma tarefa com um índice válido."""
    tasks = []
    tasks = add_task(tasks, "Tarefa 1")
    tasks = complete_task(tasks, 0)

    assert tasks[0]["done"] == True

def test_complete_task_invalid_index():
    """Verifica que complete_task não altera a lista com índice inválido."""
    tasks = []
    tasks = add_task(tasks, "Tarefa 1")

    result = complete_task(tasks, 1)  # índice 1 não existe, só há o 0

    assert result == tasks              # lista devolvida sem alterações
    assert result[0]["done"] is False   # tarefa continua por completar


#def test_complete_task_invalid_index():
#    """Verifica que complete_task não lança IndexError com um índice inválido."""
#    tasks = []
#    tasks = add_task(tasks, "Tarefa 1")
#    try:
#        complete_task(tasks, 1)
#        assert False, "Não deve chegar aqui se o índice for inválido"
#    except IndexError:
#        pass


def test_remove_task_valid_index():
    """Verifica que remove_task remove uma tarefa com um índice válido."""
    tasks = []
    tasks = add_task(tasks, "Tarefa 1")
    tasks = remove_task(tasks, 0)

    assert len(tasks) == 0

def test_remove_task_invalid_index():
    """Verifica que remove_task não altera a lista com índice inválido."""
    tasks = []
    tasks = add_task(tasks, "Tarefa 1")

    result = remove_task(tasks, 1)

    assert result == tasks
    assert len(result) == 1

#def test_remove_task_invalid_index():
#    """Verifica que remove_task não lança IndexError com um índice inválido."""
#    tasks = []
#    tasks = add_task(tasks, "Tarefa 1")
#    try:
#        remove_task(tasks, 1)
#        assert False, "Não deve chegar aqui se o índice for inválido"
#    except IndexError:
#        pass