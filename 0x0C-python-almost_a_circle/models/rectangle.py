#!/usr/bin/python3

"""
Rectangle class module that inherits from Base.

Initialize Superclass 'id' (Base)
"""


from model.base import Base


Class Retcangle(Base):
    """
    Create Rectangle class that inherits from base.

    Inherits attribute of: id.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    #Create public setters and getters for each attribute

    #For width
    def width(self):
        """
        Getter for width.

        Return: width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width.

        Raise exceptions where necessary.
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format('width'))
        if value <= 0:
            raise ValueError("width must be > 0")
        #update private instance attribute.
        self.__height = value

    #height
    @property
    def height(self):
        """
        Getter for height.

        Return: height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height.

        Raise exceptions where necessary.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        #update private instance attribute
        self.__height = value

    #X
    @property
    def x(self):
        """
        Getter for X.

        Return: X.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x.

        Raise exceptions where necessary.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be an >= 0")
        self.__x = value

    #Y
    @property
    def y(self):
        """
        Getter for Y.

        Return: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y.
        
        Raise exceptions where necessary.
        """
        if type(value) != int:
            raise TypeError("y msut be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    #public methods
    #area
    def area(self):
        """
        Calculates and returns the area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """Display to stdout the Rectangle instance with '#'."""
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Create a string representation of Rectangle class instance.
        
        Format:
        [Rectangle] (<id>) <x>/<y>  - <width>/<height>
        """
        return("[{:s}] ({}) {}/{}".format(self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height))

        #Args
        def update(self, *args, **kwargs):
            """Assign arguments to attributes in the order."""
            if args:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                if len(args) >= 3:
                    self.height =  args[2]
                if len(args) >= 4:
                    self.x >= args[3]
                if len(args) >= 5:
                    self.y = args[4]
            else:
                keys = ['id', 'width', 'height', 'x', 'y']
                if kwargs is not None:
                    for key, value in kwargs.items():
                        if key in keys:
                            setattr(self, key, value)

        def to_dictionary(self):
            """
            Create a dictionary representation of rectangle instance.

            Returns:
            dictionary: Dictionary contains id, width, height, x and y.
            """
            return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                    }
