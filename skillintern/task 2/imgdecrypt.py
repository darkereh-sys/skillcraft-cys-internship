from PIL import Image
import os
import sys

def print_header():
    print("==================================================================")
    print("                       Image Encryption Tool")
    print("==================================================================\n")

def print_menu():
    print("You can encrypt/decrypt images with:")
    print("  [1] Swap Pixels (Red/Blue channel swap)")
    print("  [2] XOR Pixels (Bitwise Value Scrambling)")
    print("  [3] Swap + XOR (Combination of both methods)")
    print("\nMenu:")
    print("  [1] Swap Pixels")
    print("  [2] XOR Pixels")
    print("  [3] Swap + XOR")
    print("  [4] Exit")

def process_image(mode, input_path, output_path, key=None):
    try:
        img = Image.open(input_path)
        img = img.convert("RGB")
        pixels = img.load()
        width, height = img.size

        print("Processing...", end="")

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                if mode == 1 or mode == 3:
                    r, b = b, r

                if mode == 2 or mode == 3:
                    if key is None:
                        key = 128 
                    r = r ^ key
                    g = g ^ key
                    b = b ^ key

                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print(f"\nSuccess! Image processed and saved to '{output_path}'")
        
    except FileNotFoundError:
        print(f"\nError: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def main():
    print_header()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '4':
            print("Exiting program...")
            print("==================================================================")
            print("             Thank you for using the tool!")
            print("==================================================================")
            sys.exit()

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.\n")
            continue

        input_path = input("Enter input image path (e.g., image.png): ").strip('"')
        
        filename, ext = os.path.splitext(input_path)
        default_output = f"{filename}_processed{ext}"
        
        output_path = input(f"Enter output image path (default: {default_output}): ").strip('"')
        if not output_path:
            output_path = default_output

        key = 0
        if choice in ['2', '3']:
            key_input = input("Enter XOR key (0-255) or press Enter for 128: ")
            if key_input == "":
                key = 128
            else:
                try:
                    key = int(key_input)
                except ValueError:
                    print("Invalid key! Using default 128.")
                    key = 128

        process_image(int(choice), input_path, output_path, key)
        print("-" * 60)

if __name__ == "__main__":
    main()