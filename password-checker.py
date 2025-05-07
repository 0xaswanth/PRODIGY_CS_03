import math
import string

class SmartPasswordChecker:
    def __init__(self, password, name="", email=""):
        self.password = password
        self.name = name.lower()
        self.email = email.lower()
        self.length = len(password)
        self.character_sets = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'digits': string.digits,
            'symbols': string.punctuation
        }

    def calculate_entropy(self):
        used_sets = set()
        for c in self.password:
            for category, charset in self.character_sets.items():
                if c in charset:
                    used_sets.add(category)

        charset_size = sum(len(self.character_sets[cat]) for cat in used_sets)
        if charset_size == 0:
            return 0

        entropy = math.log2(charset_size) * self.length
        return round(entropy, 2)

    def estimate_crack_time(self, entropy):
        guesses_per_second = 1_000_000_000  # 1 billion guesses per second
        total_guesses = 2 ** entropy
        seconds = total_guesses / guesses_per_second
        if seconds < 60:
            return f"{round(seconds)} seconds"
        elif seconds < 3600:
            return f"{round(seconds / 60)} minutes"
        elif seconds < 86400:
            return f"{round(seconds / 3600)} hours"
        elif seconds < 31536000:
            return f"{round(seconds / 86400)} days"
        else:
            return f"{round(seconds / 31536000)} years"

    def contains_personal_info(self):
        lower_pass = self.password.lower()
        return self.name in lower_pass or self.email in lower_pass

    def evaluate_strength(self, entropy):
        if entropy < 28:
            return "Too Weak"
        elif entropy < 50:
            return "Acceptable"
        else:
            return "Secure"

    def suggest_improvements(self):
        suggestions = []
        if self.length < 12:
            suggestions.append("- Use at least 12 characters.")
        if not any(c in string.ascii_uppercase for c in self.password):
            suggestions.append("- Add uppercase letters.")
        if not any(c in string.ascii_lowercase for c in self.password):
            suggestions.append("- Add lowercase letters.")
        if not any(c in string.digits for c in self.password):
            suggestions.append("- Add some numbers.")
        if not any(c in string.punctuation for c in self.password):
            suggestions.append("- Include special characters like !, @, #, etc.")
        return suggestions

    def evaluate(self):
        entropy = self.calculate_entropy()
        crack_time = self.estimate_crack_time(entropy)
        verdict = self.evaluate_strength(entropy)

        print("\n🧠 Password Evaluation Report:")
        print(f"- Password Length     : {self.length} characters")
        print(f"- Entropy Estimate    : {entropy} bits")
        print(f"- Estimated Crack Time: {crack_time}")
        print(f"- Verdict             : {verdict}")

        if self.contains_personal_info():
            print("⚠️ Warning: Your password contains your name or email. Avoid using personal info!")

        if verdict != "Secure":
            print("\n🔧 Suggestions to Improve Your Password:")
            for suggestion in self.suggest_improvements():
                print(suggestion)

def main():
    print("🔐 Smart Password Strength Checker 🔐")
    try:
        name = input("Enter your name (optional): ").strip()
        email = input("Enter your email (optional): ").strip()
        password = input("Enter your password: ").strip()

        if not password:
            print("❌ Password cannot be empty!")
            return

        checker = SmartPasswordChecker(password, name, email)
        checker.evaluate()
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user.")

    input("\nPress Enter to exit...")  # Keeps the window open after evaluation

if __name__ == "__main__":
    main()
