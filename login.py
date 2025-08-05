import os

def run_command():
    user_input = input("Enter a command: ")
    os.system(user_input)  # 🚨 Vulnerable: command injection 

if __name__ == "__main__":
    run_command()
