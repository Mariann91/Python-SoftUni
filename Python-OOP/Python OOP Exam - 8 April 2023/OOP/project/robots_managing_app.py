from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICES_AND_ROBOTS = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,

    }

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    @staticmethod
    def find_object(name, object_list):

        for obj in object_list:

            if obj.name == name:
                return obj

    def add_service(self, service_type: str, name: str):

        if service_type not in RobotsManagingApp.VALID_SERVICES_AND_ROBOTS.keys():
            raise Exception("Invalid service type!")

        self.services.append(
            RobotsManagingApp.VALID_SERVICES_AND_ROBOTS[service_type](name)
        )

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in RobotsManagingApp.VALID_SERVICES_AND_ROBOTS.keys():
            raise Exception("Invalid robot type!")

        self.robots.append(
            RobotsManagingApp.VALID_SERVICES_AND_ROBOTS[robot_type](
                name,
                kind,
                price,
            )
        )

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):

        unsuitable_robot_service_matches = {
            "FemaleRobot": "MainService",
            "MaleRobot": "SecondaryService",
        }

        robot = self.find_object(robot_name, self.robots)
        service = self.find_object(service_name, self.services)

        if unsuitable_robot_service_matches[robot.__class__.__name__] == service.__class__.__name__:
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)

        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = self.find_object(service_name, self.services)
        robot = self.find_object(robot_name, service.robots)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)

        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):

        service = self.find_object(service_name, self.services)

        number_of_robots_fed = 0

        for robot in service.robots:
            robot.eating()

            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):

        service = self.find_object(service_name, self.services)
        total_price = sum(robot.price for robot in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []

        for service in self.services:

            result.append(service.details())

        return "\n".join(result)
      
