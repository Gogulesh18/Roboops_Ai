from src.Backend.simulation.task_queue import task_queue


class TaskQueueService:

    @staticmethod
    def add(task):

        task_queue.append(task)

        priority_order = {
            "High": 0,
            "Normal": 1,
            "Low": 2
        }

        task_queue.sort(
            key=lambda task: priority_order.get(
                task.priority,
                1
            )
        )

    @staticmethod
    def get_all():
        return task_queue

    @staticmethod
    def pop():

        if task_queue:
            return task_queue.pop(0)

        return None