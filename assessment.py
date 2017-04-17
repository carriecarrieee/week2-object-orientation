"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Three main design advantages that object orientation can provide are:
   a. Encapsulation - where data is close to its functionality
   b. Abstraction - no need to know internal info of a method
   c. Polymorphism - easy to make methods different or customized; flexibility
      of types without conditionals  

2. What is a class?

   A class is a way of organizing and producing objects with similar attributes
   and methods; it is a type of thing.

3. What is an instance attribute?

   An instance attribute is a variable that lives inside a particular instance
   and is not relevant to other instances unless set.

4. What is a method?

   A method is like a function that is defined inside a class. 

5. What is an instance in object orientation?

   An instance is a copy of the class; it is an individual occurrence of a
   class. "Instance" and "object" are equivalent.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attributes are defined in the class and any instances of that class
   will have access to these attributions, while instance attributes only
   pertain to that particular instance. However, if a class attribute was
   changed on the instance, then the instance will no longer be able to access
   any changes to the class attribute.

   For example, let's set a class attribute of hunger = 50 in a class "Animal"
   and create an instance of "Animal" called "cat". Currently,
   >>> cat.hunger
   50
   
   But if we then make a change to the class attribute:
   >>> cat.hunger = 25
   >>> Animal.hunger = 0

   Now, the instance "cat" will not capture the "hunger" attribute change to the
   class "Animal" to 0:
   >>> cat.hunger
   25  

   An example of an instance attribute would be either "name" or "species",
   where each animal will have, but each instance will be different. 

   We can use class attributes with variables that won't change across all
   instances of the class, and we should use instance attributes with variables
   that we do expect to be different from instance to instance.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ Stores student first and last names, and addresses."""

    def __init__(self, first_name, last_name, address):
        """ Initializes the class variables to store data"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        """ Returns student name and address stored in dictionary."""

        return "first name: {}, \nlast name: {}, \naddress: {}".format(
            self.first_name, self.last_name, self.address)

class Question(object):
    """ Stores a question and a correct answer."""

    def __init__(self, question, correct_answer):
        """ Initializes the class variables to store data."""

        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        """ Returns dictionary of (question: correct_answer)."""

        return "question: {}, \ncorrect_answer: {}".format(self.question,
            self.correct_answer)

    def ask_and_evaluate(self):
        """ Prints question, prompts user for answer, then evaluates answer."""

        print question
        answer = raw_input("> ")
        if answer == correct_answer:
            return True
        else:
            return False

class Exam(object):
    """Stores data that is a dictionary of (question: correct answers)."""

    def __init__(self, name):
        """ Initializes the class variables and attribute."""

        self.name = name
        self.questions_list = [] # list of Question objects

    def __repr__(self):
        """ Returns a dictionary containting values point to lists of questions
            and answers."""

            return "name: {}, list of questions: [{}]".format(self.name, 
                self.questions_list)

    def add_question(self, question, correct_answer):
        """Adds question and correct_answer to questions list"""

        question_instance = Question(question, correct_answer) # create instance
        self.questions_list.append(question_instance)

    def administer(self):
        """ Administers all questions and returns user score. """

        score = 0.00

        num_corr_response = self.ask_and_evaluate()
        for question in questions_list:
            if num_corr_response == True,
                score += 1

        return self.score / len(self.questions_list)