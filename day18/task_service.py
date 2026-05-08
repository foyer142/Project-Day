
class TaskService:
    def __init__(self):
        self.tasks = []

        
    def add_task(self, title: str) -> None:
        self.tasks.append({
            "title": title,
            "done": False
        })

    def get_all_tasks(self) -> list[dict]:
        return self.tasks.copy()

    def get_completed_tasks(self) -> list[dict]:
        return [task for task in self.tasks if task['done'] == True]

    def get_active_tasks(self) -> list[dict]:
        return [task for task in self.tasks if task['done'] == False]

    def mark_done(self, title: str) -> bool:
        for task in self.tasks:
            if task['title']==title:
                task['done'] = True
                return True
        return False

    def delete_task(self, title: str) -> bool:
        for task in self.tasks:
            if task['title']==title:
                self.tasks.remove(task)
                return True
        return False

def main():
    service = TaskService()

    service.add_task("Learn OOP")
    service.add_task("Build UserService")
    service.add_task("Review code")

    print(service.get_all_tasks())

    print(service.mark_done("Learn OOP"))
    print(service.get_completed_tasks())
    print(service.get_active_tasks())

    print(service.delete_task("Review code"))
    print(service.get_all_tasks())

    print(service.mark_done("Missing task"))
    print(service.delete_task("Missing task"))


if __name__=='__main__':
    main()