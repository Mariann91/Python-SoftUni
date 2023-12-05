from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):

        result = [f"{self.name} Main Service:"]
        second_line = f"Robots: {' '.join(robot.name for robot in self.robots)}" if self.robots else "Robots: none"

        result.append(second_line)

        return "\n".join(result)
