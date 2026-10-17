"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.


class ParentClass:
    """Represent a network device monitored by a home server."""

    device_category = "Network device"

    def __init__(self, name, status):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Device name must be a nonempty string.")

        if status not in ("online", "offline", "degraded"):
            raise ValueError(
                "Device status must be online, offline, or degraded."
            )

        self.name = name.strip()
        self.status = status

    def get_info(self):
        return f"{self.name} ({self.device_category}): {self.status}"

    def __str__(self):
        return self.get_info()



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.


class ChildClass(ParentClass):
    """Represent a storage server with multiple hard drives."""

    device_type = "Storage server"
    valid_drive_states = {"healthy", "degraded", "failed"}

    def __init__(self, name, status, capacity_tb, drives):
        # Initialize the attributes inherited from ParentClass.
        super().__init__(name, status)

        # Validate the storage capacity.
        if (
            isinstance(capacity_tb, bool)
            or not isinstance(capacity_tb, (int, float))
            or not (0 < capacity_tb < float("inf"))
        ):
            raise ValueError("Capacity must be a positive finite number.")

        # Validate the list of hard drives.
        if not isinstance(drives, list):
            raise ValueError("Drives must be provided as a list.")

        drive_bays = set()

        for drive in drives:
            if not isinstance(drive, dict):
                raise ValueError("Each drive must be a dictionary.")

            if "bay" not in drive or "health" not in drive:
                raise ValueError(
                    "Each drive must contain bay and health information."
                )

            bay = drive["bay"]
            health = drive["health"]

            if (
                not isinstance(bay, str)
                or not bay.strip()
                or bay in drive_bays
            ):
                raise ValueError("Drive bays must have unique valid names.")

            if (
                not isinstance(health, str)
                or health not in self.valid_drive_states
            ):
                raise ValueError("Invalid drive health status.")

            drive_bays.add(bay)

        # Child-specific instance variables.
        self.capacity_tb = capacity_tb
        self.drives = deepcopy(drives)

    def get_info(self):
        """Override the parent method with storage information."""
        parent_info = super().get_info()

        return (
            f"{parent_info} | "
            f"{self.device_type} | "
            f"{self.capacity_tb} TB | "
            f"{len(self.drives)} drive(s)"
        )

    def health_summary(self):
        """Count healthy drives and drives needing attention."""
        healthy = sum(
            drive["health"] == "healthy"
            for drive in self.drives
        )

        problems = len(self.drives) - healthy

        return (
            f"{healthy} healthy drive(s), "
            f"{problems} drive(s) needing attention"
        )


    # STUDENT-CREATED EXTENSION:
    # Update the status of an existing drive, validating all inputs.
    # Raise clear errors instead of silently ignoring invalid operations.
    def update_drive_status(self, bay, health):
        """Update the health of a drive identified by its bay."""
        if not isinstance(bay, str) or not bay.strip():
            raise ValueError("Drive bay must be a nonempty string.")

        if not isinstance(health, str) or health not in self.valid_drive_states:
            raise ValueError("Invalid drive health status.")

        for drive in self.drives:
            if drive["bay"] == bay:
                drive["health"] = health
                return

        raise KeyError(f"Drive bay {bay!r} was not found.")



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.


def demonstrate_namespaces():
    """Demonstrate class and instance namespaces."""

    print("\n=== Namespace Demonstration ===")

    # Create two objects from the child class.
    server1 = ChildClass(
        "Storage-A",
        "online",
        12,
        [{"bay": "A1", "health": "healthy"}]
    )

    server2 = ChildClass(
        "Storage-B",
        "degraded",
        16,
        [{"bay": "B1", "health": "degraded"}]
    )

    # Access the same class variable in two different ways.
    print("Class variable through class:", ChildClass.device_type)
    print("Class variable through object:", server1.device_type)

    # Add a new attribute to only the first object.
    server1.rack_location = "Rack 1"

    # Display each object's instance namespace.
    print("\nServer 1 instance namespace:")
    print(server1.__dict__)

    print("\nServer 2 instance namespace:")
    print(server2.__dict__)

    # Display information about the child class namespace.
    print("\nChild class namespace:")
    print(sorted(ChildClass.__dict__.keys()))

    # Verify that the new attribute belongs only to server1.
    print(
        "\nOnly Server 1 has rack_location:",
        "rack_location" in server1.__dict__
        and "rack_location" not in server2.__dict__
    )



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.


def demonstrate_copying():
    """Demonstrate shallow and deep copying with nested drive data."""

    print("\n=== Copy Demonstration ===")

    # Create an object containing a list of drive dictionaries.
    original = ChildClass(
        "Storage-C",
        "online",
        24,
        [
            {"bay": "C1", "health": "healthy"},
            {"bay": "C2", "health": "healthy"}
        ]
    )

    # A shallow copy creates a new outer object but shares
    # references to nested mutable data with the original.
    shallow = copy(original)

    # A deep copy creates a new outer object and independently
    # copies its nested mutable data.
    deep = deepcopy(original)

    # Modify a nested dictionary inside the original object.
    original.drives[0]["health"] = "failed"

    # Compare the original object and its two copies.
    print("\nOriginal object:")
    print(original.drives)

    print("\nShallow copy:")
    print(shallow.drives)

    print("\nDeep copy:")
    print(deep.drives)

    # Verify whether the nested drive lists share references.
    print(
        "\nOriginal shares drive list with shallow copy:",
        original.drives is shallow.drives
    )

    print(
        "Original shares drive list with deep copy:",
        original.drives is deep.drives
    )



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.


def main():
    """Run all Unit 1 object-oriented programming demonstrations."""

    print("=== Unit 1 OOP Assignment ===")

    # Create and test an object from the parent class.
    print("\n=== Parent Object ===")

    router = ParentClass("Router-01", "online")

    print("Parent information:")
    print(router.get_info())

    # Create and test an object from the child class.
    print("\n=== Child Object and Inheritance ===")

    server = ChildClass(
        "Storage-01",
        "degraded",
        32,
        [
            {"bay": "1", "health": "healthy"},
            {"bay": "2", "health": "degraded"}
        ]
    )

    # Demonstrate the child's overridden method.
    print("Child information:")
    print(server.get_info())

    # Demonstrate inheritance from the parent class.
    print("Inherited category:", server.device_category)

    print(
        "Child inherits from ParentClass:",
        isinstance(server, ParentClass)
    )

    # Call the child's additional method.
    print("Drive health summary:", server.health_summary())

    # Demonstrate the student-created extension with a successful update.
    print("\n=== Student-Created Extension ===")
    print("Before update:", server.health_summary())
    server.update_drive_status("2", "healthy")
    print("After update:", server.health_summary())

    # Handle a missing bay without stopping the program.
    try:
        server.update_drive_status("99", "failed")
    except KeyError as error:
        print("Invalid drive bay handled:", error)

    # Run the required namespace demonstration.
    demonstrate_namespaces()

    # Run the required shallow and deep copying demonstration.
    demonstrate_copying()



if __name__ == "__main__":
    main()
