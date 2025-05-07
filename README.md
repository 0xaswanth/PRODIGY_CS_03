# PRODIGY_CS_03

# Password Complexity Checker

## Task Overview
The Password Complexity Checker is a tool that assesses the strength of a password based on specific criteria, including length, presence of uppercase and lowercase letters, numbers, and special characters. It provides feedback to users on the password's strength, estimates the time required to crack the password, and gives suggestions to improve its security.

## Features
- **Password Length**: The tool checks the length of the password.
- **Entropy Calculation**: It estimates the entropy of the password based on the character sets used.
- **Estimated Crack Time**: Provides an estimated time required to crack the password based on entropy.
- **Strength Evaluation**: Classifies the password strength as "Too Weak", "Acceptable", or "Secure".
- **Personal Information Detection**: Checks if the password contains the user's name or email.
- **Suggestions for Improvement**: Provides suggestions to enhance password security.

## Usage
1. **Input**: The user is prompted to input their name (optional), email (optional), and the password they want to evaluate.
2. **Output**: The tool displays a report on the password's strength, including:
   - Password Length
   - Entropy Estimate
   - Estimated Crack Time
   - Verdict (Too Weak, Acceptable, Secure)
   - Any warnings about personal information
   - Suggestions for improvement if the password is not secure.

## Code Breakdown

### `SmartPasswordChecker` class:
- **`__init__`**: Initializes the password, name, email, and defines the character sets.
- **`calculate_entropy`**: Calculates the entropy of the password to measure its strength.
- **`estimate_crack_time`**: Estimates the time to crack the password based on the entropy.
- **`contains_personal_info`**: Checks if the password contains the user's name or email.
- **`evaluate_strength`**: Evaluates the strength of the password based on entropy.
- **`suggest_improvements`**: Provides suggestions to improve the password's strength.
- **`evaluate`**: Evaluates and prints the password report.

### `main` function:
- Prompts the user for input.
- Creates an instance of `SmartPasswordChecker` and evaluates the password.

## Requirements
- Python 3.x
- `math` library (included in Python standard library)
- `string` library (included in Python standard library)

## Example Usage

```
Enter your name (optional): John Doe
Enter your email (optional): johndoe@example.com
Enter your password: P@ssw0rd123

🧠 Password Evaluation Report:
- Password Length     : 12 characters
- Entropy Estimate    : 48.0 bits
- Estimated Crack Time: 3 hours
- Verdict             : Secure

⚠️ Warning: Your password contains your name or email. Avoid using personal info!

🔧 Suggestions to Improve Your Password:
- Include special characters like !, @, #, etc.
```

## License
This tool is provided for educational and personal use. You are free to modify and use it as needed.

