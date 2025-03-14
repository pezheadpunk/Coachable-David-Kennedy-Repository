'''
1. Write a class called Counter. This should take in an integer as the
constructor for the starting value.
'''
class Counter:
    def __init__(self, starting_value):
        self.count = starting_value

    def get_cout(self):
        '''
        a. Implement functions get_count which returns the current count.
        '''
        return self.count

    def increment(self):
        '''
        And increment which increments the count by 1.
        '''
        self.count += 1

    def reset_count(self):
        '''
        b. Implement a function that resets the counter to 0.
        '''
        self.count = 0

class MaxThresholdError(Exception):
    pass

class LimitCounter(Counter):
    '''
    c. Implement a class LimitCounter, which should inherit from Counter, with a new
    constructor that prevents the count from exceeding a certain max threshold. The
    default max threshold is 100.
    '''
    def __init__(self, starting_value, max_threshold =100):
        super().__init__(starting_value)
        self.max_threshold = max_threshold

    def increment(self):
        '''
        If you try to increment past 100, there should raise an error.
        '''
        if self.count + 1 > self.max_threshold:
            raise MaxThresholdError("Incrementing will exeed max threshold")
        self.count += 1

class BankAccount:
    '''
    2. Make a BankAccount class where balance is private. Use getters/setters to add
    methods to deposit money and get the balance.
    '''
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        '''Setter'''
        self.__balance += amount

    def get_balance(self):
        '''Getter'''
        return self.__balance

class Employee:
    '''
    3. Create a class Employee with a get_salary() method that returns a base salary
    of 50,000.
    '''
    def __init__(self):
        self.base_salary = "50,000"

    def get_salary(self):
        '''Returns class base salary'''
        return self.base_salary

class Manager(Employee):
    '''
    Create a subclass Manager that overrides get_salary() to return 80,000.
    '''
    def __init__(self):
        super().__init__()
        # This override of the base_salary attribute will also override the call
        # in get_salary that is inherited from Employee class.
        self.base_salary = "80,000"

class Book:
    '''
    4. Modify the Book class so that printing an instance returns “Book: BookTitle”
    instead of <__main__.Book object at 0x…>.
    '''
    def __init__(self, book_title):
        self.book_title = book_title

    def __str__(self):
        return f"Book: {self.book_title}"

class Task:
    '''
    5. Implement a Task class that represents a basic to-do task, along with a
    RecurringTask subclass for tasks that reset daily.
    a. For the Task Class:
    '''
    def __init__(self, title):
        '''
        i. Takes in a title (string) when initialized.
        ii. Has a completed attribute that defaults to False.
        '''
        self.title = title
        self.completed = False

    def mark_completed(self):
        '''
        iii. Implements a mark_completed() method that sets completed = True.
        '''
        self.completed = True

    def __str__(self):
        '''
        iv. Implements __str__() to return “Task: <title> - Completed: <True/False>“.
        v. Raises an error if title is empty or not a string.
        '''
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Invalid Title")
        return f"Task: {self.title} - Completed: {self.completed}"

class RecurringTask(Task):
    '''
    b. For the RecurringTask Subclass:
    i. Inherits from Task.
    '''
    def mark_completed(self):
        '''
        ii. Overrides mark_completed() so that when called, it resets completed back
        to False.
        '''
        self.completed = False

    def __str__(self):
        '''
        iii. Overrides __str__() to indicate that the task is recurring.
        '''
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Invalid Title")
        return f"Task: {self.title} - is a recurring task"
