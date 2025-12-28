def sort(width, height, length, mass):
    # Check if the package is bulky
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150

    # Check if the package is heavy
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


print(sort(50, 40, 30, 10))   # STANDARD
print(sort(200, 40, 30, 10)) # SPECIAL (bulky)
print(sort(50, 40, 30, 25))  # SPECIAL (heavy)
print(sort(200, 40, 30, 25)) # REJECTED (bulky and heavy)
