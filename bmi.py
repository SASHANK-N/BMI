def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be positive.")
    return weight / (height ** 2)
