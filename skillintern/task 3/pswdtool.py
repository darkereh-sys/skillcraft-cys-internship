import re

def assess_password(password: str):
    score = 0
    feedback = []

    # Length checks
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 1

    # Character checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength label
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, feedback


def main():
    print("Password Strength Checker")
    print("-" * 30)

    password = input("Enter your password: ")

    score, strength, feedback = assess_password(password)

    print("\nResults")
    print("-" * 30)
    print(f"Score: {score} / 7")
    print(f"Strength: {strength}")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nExcellent password!")


if __name__ == "__main__":
    main()
