print("This is a modified version with updated logic")
def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be positive.")
    return weight / (height ** 2)

if __name__ == "__main__":
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
