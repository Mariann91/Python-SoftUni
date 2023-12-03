from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    @staticmethod
    def find_object(attribute, value, object_list):

        for obj in object_list:

            if getattr(obj, attribute) == value:
                return obj

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        user = self.find_object(
            attribute="driving_license_number",
            value=driving_license_number,
            object_list=self.users)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in ManagingApp.VALID_VEHICLE_TYPES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self.find_object(
            attribute="license_plate_number",
            value=license_plate_number,
            object_list=self.vehicles
        )

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(
            ManagingApp.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        )

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        route_to_add = Route(start_point, end_point, length, route_id)

        for route in self.routes:

            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        self.routes.append(route_to_add)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str,
                  license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = self.find_object("driving_license_number", driving_license_number, self.users)
        vehicle = self.find_object("license_plate_number", license_plate_number, self.vehicles)
        route = self.find_object("route_id", route_id, self.routes)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        status = "OK"

        if is_accident_happened:

            vehicle.is_damaged = True
            user.decrease_rating()
            status = "Damaged"

        else:
            user.increase_rating()

        return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} " \
               f"Battery: {vehicle.battery_level}% Status: {status}"

    def repair_vehicles(self, count: int):

        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))

        number_to_repair = min(count, len(sorted_damaged_vehicles))
        count_of_repaired_vehicles = 0

        for index in range(number_to_repair):
            current_vehicle = sorted_damaged_vehicles[index]

            current_vehicle.is_damaged = False
            current_vehicle.recharge()

            count_of_repaired_vehicles += 1

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):

        sorted_users = sorted(self.users, key=lambda x: -x.rating)

        result = ["*** E-Drive-Rent ***"]

        for user in sorted_users:
            result.append(str(user))

        return "\n".join(result)
