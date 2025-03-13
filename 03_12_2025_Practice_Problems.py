'''
1. Write a class called Counter. This should take in an integer as the
constructor for the starting value.
'''
class Counter:
    def __init__(self, starting_value):
        self.count = starting_value

    '''
    a. Implement functions get_count which returns the current count.
    '''
    def get_cout(self):
        return self.count

    '''
    And increment which increments the count by 1.
    '''
    def increment(self):
        self.count += 1

    '''
    b. Implement a function that resets the counter to 0.
    '''
    def reset_count(self):
        self.count = 0

'''
c. Implement a class LimitCounter, which should inherit from Counter, with a new
constructor that prevents the count from exceeding a certain max threshold. The
default max threshold is 100.
'''
class LimitCounter(Counter):
    def __init__(self, starting_value, max_threshold =100):
        super().__init__(starting_value)
        self.max_threshold = max_threshold

    '''
    If you try to increment past 100, there should raise an error.
    '''
    def increment(self):
        if self.count + 1 > max_threshold:
            print("Error: Incrementing will exeed max threshold")
        else:
            self.count += 1


'''
2. Make a BankAccount class where balance is private. Use getters/setters to add
methods to deposit money and get the balance.
'''
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


'''
3. Create a class Employee with a get_salary() method that returns a base salary
of 50,000.
'''
class Employee:
    def __init__(self):
        self.base_salary = "50,000"

    def get_salary(self):
        return self.base_salary

'''
Create a subclass Manager that overrides get_salary() to return 80,000.
'''
class Manager(Employee):
    def __init__(self):
        # This override of the base_salary attribute will also override the call
        # in get_salary that is inherited from Employee class.
        self.base_salary = "80,000"


'''
4. Modify the Book class so that printing an instance returns “Book: BookTitle”
instead of <__main__.Book object at 0x…>.
'''
class Book:
    def __init__(self, book_title):
        self.book_title = book_title

    def __str__(self):
        return f"Book: {self.book_title}"


'''
5. Implement a Task class that represents a basic to-do task, along with a
RecurringTask subclass for tasks that reset daily.
a. For the Task Class:
'''
class Task:
    '''
    i. Takes in a title (string) when initialized.
    ii. Has a completed attribute that defaults to False.
    '''
    def __init__(self, title):
        self.title = title
        self.completed = False

    '''
    iii. Implements a mark_completed() method that sets completed = True.
    '''
    def mark_completed(self):
        self.completed = True

    '''
    iv. Implements __str__() to return “Task: <title> - Completed: <True/False>“.
    v. Raises an error if title is empty or not a string.
    '''
    def __str__(self):
        if not self.title or not isinstance(self.title, str):
            print("Error: Invalid Title")
        else:
            return f"Task: {self.title} - Completed: {self.completed}"

'''
b. For the RecurringTask Subclass:
i. Inherits from Task.
'''
class RecurringTask(Task):
    def __init__(self, title):
        super().__init__(title)

    '''
    ii. Overrides mark_completed() so that when called, it resets completed back
    to False.
    '''
    def mark_completed(self):
        self.completed = False

    '''
    iii. Overrides __str__() to indicate that the task is recurring.
    '''
    def __str__(self):
        if not self.title or not isinstance(self.title, str):
            print("Error: Invalid Title")
        else:
            return f"Task: {self.title} - is recurring"
