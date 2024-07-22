import subprocess
import os

# Define a function to run the external program to verify the token
def get_token_from_external_program():
    # Run the external program using subprocess
    process = subprocess.Popen(['python', 'token.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Check if the external program returned an error
    if error:
        raise Exception('Error running external program: {}'.format(error))

    # Return the token from the output
    return output.decode('utf-8').strip()

# Define a class to manage the token
class TokenManager:
    def __init__(self):
        self.token = None

    def get_token(self):
        # If the token is not set, get it from the external program
        if not self.token:
            self.token = get_token_from_external_program()
        return self.token

    def reset_token(self):
        self.token = None

# Create an instance of the TokenManager
token_manager = TokenManager()

# Example usage:
print(token_manager.get_token())  # Runs the external program to get the token
print(token_manager.get_token())  # Returns the cached token
token_manager.reset_token()  # Resets the token, so the next call will run the external program again
print(token_manager.get_token())  # Runs the external program to get the token again