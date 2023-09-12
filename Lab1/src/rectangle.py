"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""


class Shape:
    @abstractmethod
    def set_values(self, width, height):
        pass

    def area(self):
        pass


class Rectangle(Shape):
    def set_values(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
