# problem:
# https://leetcode.com/problems/design-parking-system/

# solution:
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.availableBig = big
        self.availableMedium = medium
        self.availableSmall = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.availableBig > 0:
            self.availableBig -= 1
            return True
        elif carType == 2 and self.availableMedium > 0:
            self.availableMedium -= 1
            return True
        elif carType == 3 and self.availableSmall > 0:
            self.availableSmall -= 1
            return True
        else:
            return False
