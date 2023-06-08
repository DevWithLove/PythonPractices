import time

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function
def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return  wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you")

#or we can use decorator in this way
decorated_greeting = delay_decorator(say_greeting)

# say_hello()
# decorated_greeting()

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticatied_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@is_authenticatied_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Tony")
create_blog_post(new_user)