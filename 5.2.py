class LockedDoorException(Exception):
    pass

class Door:
    def __init__(self, locked=True):
        self.locked = locked

    def open(self):
        if self.locked:
            raise LockedDoorException
        else:
            print("The door is open.")


d = Door(locked=True)
try:
    d.open()
    print("I have passed through the door.")
except LockedDoorException:
    print("The door is locked, you can't open it.")
