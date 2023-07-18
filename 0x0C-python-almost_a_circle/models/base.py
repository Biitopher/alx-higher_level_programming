#!/usr/bin/python3
"""Defines Base"""
import json
import csv
import turtle


class Base:
    """Represents base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Represents data sharing"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json string representation"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list that json string represents"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns all set attributes"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """List of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                data = file.read()
                obj_list = cls.from_json_string(data)
                instances = [cls.create(**obj) for obj in obj_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes json string representation"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """List of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method to open and draw windows"""
        pen = turtle.Turtle()
        pen.screen.bgcolor("blue")
        pen.pensize(3)
        pen.shape("turtle")

        pen.color("black")
        for rect in list_rectangles:
            pen.showturtle()
            pen.up()
            pen.goto(rect.x, rect.y)
            pen.down()
            for i in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)
            pen.hideturtle()

        pen.color("red")
        for sq in list_squares:
            pen.showturtle()
            pen.up()
            pen.goto(sq.x, sq.y)
            pen.down()
            for i in range(2):
                pen.forward(sq.width)
                pen.left(90)
                pen.forward(sq.height)
                pen.left(90)
            pen.hideturtle()

        turtle.exitonclick()

