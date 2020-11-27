class Student:
  def __init__(self, age, fName, lName):
    """Defines a new class to store student information.

    Args:
        age ([int]): [Student's current age.]
        fName ([str]): [Student's given name.]
        lName ([str]): [Student's last name.]
    """
    self.age = age
    self.firstName = fName
    self.lastName = lName


class CollegeStudent(Student):
  def __init__(self, degreeProgram, age, fName, lName):
    """Class for College students, use the student class for grades =< 12.

    Args:
        degreeProgram ([str]): [Student's degree program of choice.]
        age ([int]): [Student's current age.]
        fName ([str]): [Student's given name.]
        lName ([str]): [Student's last name.]
    """
    super().__init__(age, fName, lName)
    self.degreeProgram = degreeProgram

if __name__ == "__main__":
  Santiago = CollegeStudent("Skateboarding", 22, "Santiago", "Dunlap")
  print("{} {} {} {}".format(Santiago.age, Santiago.firstName,
                             Santiago.firstName, Santiago.lastName))

  Lynsey = CollegeStudent("Psychology", 25, "Lynsey", "Lambert")
  print("{} {} {} {}".format(Lynsey.age, Lynsey.firstName,
                             Lynsey.firstName, Lynsey.lastName))

  Jensen = CollegeStudent("Buisness", 25, "Jensen", "Moon")
  print("{} {} {} {}".format(Jensen.age, Jensen.firstName,
                             Jensen.firstName, Jensen.lastName))
