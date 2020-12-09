def print_border():
    print("_" * 100)


def repr_int(x):
    try:
        x = int(x)
        return True
    except:
        return False