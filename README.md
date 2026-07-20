# pydo

a tiny, zero-dependency todo list for your terminal

## install
```bash
git clone https://github.com/nvimueller/pydo.git
cd pydo
pip install -e .
```

## usage
```bash
pydo add "write README"
pydo list
pydo done 1
pydo rename 2 "update README with examples"
```

## commands

`pydo add "<task>"`              add a new task  
`pydo list`                      show all tasks with indexes  
`pydo done <index>`              mark a task as complete  
`pydo rename <index> "<task>"`   edit a task  
