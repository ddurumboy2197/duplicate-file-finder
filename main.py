class Task:
    def __init__(self, name):
        self.name = name
        self.dependencies = []
        self.resolved = False

class TaskDependencyResolver:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name):
        if name not in self.tasks:
            self.tasks[name] = Task(name)

    def add_dependency(self, task_name, dependency_name):
        if task_name in self.tasks and dependency_name in self.tasks:
            self.tasks[task_name].dependencies.append(dependency_name)

    def resolve_dependencies(self):
        resolved_tasks = []
        unresolved_tasks = list(self.tasks.keys())

        while unresolved_tasks:
            task_name = unresolved_tasks.pop(0)
            if not self.tasks[task_name].resolved:
                if not self.tasks[task_name].dependencies:
                    self.tasks[task_name].resolved = True
                    resolved_tasks.append(task_name)
                else:
                    for dependency_name in self.tasks[task_name].dependencies:
                        if dependency_name not in resolved_tasks:
                            unresolved_tasks.append(task_name)
                            break
                    else:
                        self.tasks[task_name].resolved = True
                        resolved_tasks.append(task_name)

        return resolved_tasks

resolver = TaskDependencyResolver()

resolver.add_task('A')
resolver.add_task('B')
resolver.add_task('C')
resolver.add_task('D')

resolver.add_dependency('A', 'B')
resolver.add_dependency('B', 'C')
resolver.add_dependency('C', 'D')

print(resolver.resolve_dependencies())
```

Kodda quyidagilar mavjud:

- `Task` classi: har bir vazifani ifodalaydi, uning nomi, bog'lanishlari va hal etilganligi mavjud.
- `TaskDependencyResolver` classi: vazifa bog'lanishlarini hal qiluvchi funksiyalarni ifodalaydi.
- `add_task` metodi: vazifani qo'shish uchun ishlatiladi.
- `add_dependency` metodi: vazifa bog'lanishini qo'shish uchun ishlatiladi.
- `resolve_dependencies` metodi: vazifa bog'lanishlarini hal qiladi va hal etilgan vazifalarni qaytaradi.
