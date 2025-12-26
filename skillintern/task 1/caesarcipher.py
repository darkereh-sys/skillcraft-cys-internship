def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher.
    
    Args:
        text (str): The input message to process.
        shift (int): The number of positions to shift.
        mode (str): 'encrypt' or 'decrypt'.
    """
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    shift = shift % 26

    for char in text:
       
        if char.isalpha():
          
            base = ord('A') if char.isupper() else ord('a')
            
            new_ord = (ord(char) - base + shift) % 26 + base
            
            result += chr(new_ord)
        else:
            result += char
            
    return result

#  Main part of the program that interacts with the user 
if __name__ == "__main__":
    print("Caesar Cipher Program")
    print("---------------------")

    # Get user input
    try:
        message = input("Enter your message: ")
        
        while True:
            shift_input = input("Enter the shift value (a number): ")
            if shift_input.isdigit():
                shift_key = int(shift_input)
                break
            else:
                print("Invalid input. Please enter a whole number.")

        while True:
            choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
            if choice in ['e', 'encrypt', 'd', 'decrypt']:
                mode = 'encrypt' if choice.startswith('e') else 'decrypt'
                break
            else:
                print("Invalid choice. Please enter 'e' or 'd'.")

        # Perform the operation and print the result
        output = caesar_cipher(message, shift_key, mode)
        
        print("\n--- Result ---")
        print(f"Original Message:  {message}")
        print(f"Shift by:     {shift_key}")
        print(f"Mode:      {mode}")
        print(f"Result:    {output}")

    except Exception as e:
        print(f"An error occurred: {e}")