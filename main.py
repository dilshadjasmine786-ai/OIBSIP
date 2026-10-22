

def calculate_bmi():
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in metres: "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Error: Please enter valid numbers.")


calculate_bmi()
