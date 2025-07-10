
def sort(width, height, length, mass):
    # NOTE: the problem statement does not specify what to do if the input is invalid.
    # I'm assuming that the input is invalid if it is not a positive integer.
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("Width, height, length, and mass must be positive")

    bulky_edge = width >= 150 or height >= 150 or length >= 150
    bulky_volume = width * height * length >= 1000000
    bulky = bulky_edge or bulky_volume
    heavy = mass >= 20
    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
