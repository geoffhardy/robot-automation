
def sort(width, height, length, mass):
    bulky_edge = width >= 150 or height >= 150 or length >= 150
    bulky_volume = width * height * length >= 1000000
    bulky = bulky_edge or bulky_volume
    heavy = mass >= 20
    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
