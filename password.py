import re

def check_password_complexity(password):
    """
    Evaluates password strength based on standard cybersecurity metrics.
    Returns a dictionary containing the score, strength rating, and suggestions.
    """
    score = 0
    feedback = []

    # 1. Test Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase total length to at least 8 characters.")

    # 2. Test Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 3. Test Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 4. Test Digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # 5. Test Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #).")

    # Map scores to qualitative tiers
    if score >= 5:
        rating = "Strong"
    elif 3 <= score <= 4:
        rating = "Medium"
    else:
        rating = "Weak"

    return {
        "score": score,
        "rating": rating,
        "suggestions": feedback
    }

# Interactive testing loop
if __name__ == "__main__":
    print("--- Password Complexity Checker ---")
    user_input = input("Enter a password to evaluate: ")
    
    result = check_password_complexity(user_input)
    
    print(f"\nStrength Rating: {result['rating']} ({result['score']}/6)")
    
    if result['suggestions']:
        print("Suggestions to improve your password:")
        for tip in result['suggestions']:
            print(f" - {tip}")
    else:
        print("Excellent! Your password meets all security baselines.")
