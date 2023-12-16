def calculate_average(*args):
    try:
        summ = 0
        for i in args:
            summ += i
        return summ / len(args)
    except TypeError:
        return None
    except ZeroDivisionError:
        return None