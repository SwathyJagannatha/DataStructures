def print_char(char):
    char_upper = char.upper()
    if char_upper == "A":
        print("..######..\n..#....#..\n..######..", end=" ")
         
    elif char_upper == "B":
        print("..######..\n..#....#..\n..#####...", end=" ")
        
    elif char_upper == "C":
        print("..######..\n..#.......\n..#.......", end = " ")
        
        
    elif char_upper == "D":
        print("..#####...\n..#....#..\n..#....#..", end = " ")
        
        
    elif char_upper == "E":
        print("..######..\n..#.......\n..#####...", end = " ")
       
        
    elif char_upper == "F":
        print("..######..\n..#.......\n..#####...", end = " ")
        
    elif char_upper == "G":
        print("..######..\n..#.......\n..#.####..", end = " ")
        
        
    elif char_upper == "H":
        print("..#....#..\n..#....#..\n..######..", end = " ")
        
    # Add more characters...

name = "GEEK"

for char in name:
    print_char(char)
    print()  # Print a newline after each character's ASCII art