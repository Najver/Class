class LockedDoorException(Exception):
    pass

class Door:
    def __init__(self, locked=True):
        self.locked = locked
        self.passed_through = False

    def open(self):
        if self.locked:
            raise LockedDoorException
        else:
            print("The door is open.")
            self.passed_through = True

d = Door(locked=False)
try:
    d.open()
    print("I have passed through the door.")
except LockedDoorException:
    print("The door is locked, you can't open it.")
finally:
    if d.passed_through:
        print("You have passed through the door.")
    else:
        print("You have not passed through the door.")
