# Decorator reporting an exception
def input_error(func):

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "This record is not exist"
        except ValueError:
            return "This record is not correct!"
        except IndexError:
            return "This command is wrong"

    return wrapper