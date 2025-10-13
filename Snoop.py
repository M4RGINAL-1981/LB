import snoop

@snoop
def add(a: float, b: float):
    result = a + b
    return result

add(2, 3)