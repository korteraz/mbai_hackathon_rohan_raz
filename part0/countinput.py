#Raz Kurteran and Rohan Kumar
def countchar():
    input_string = str(input("Enter a string:"))
    input_string = input_string.replace(" ", "").replace(".","").replace("!", "").replace(",", "")
    char_count = len(input_string)
    return char_count

if __name__ == '__main__':
    print(countchar())
    #print(countchar("This, is Fun!"))
    #print(countchar("...."))
    #print(countchar("testtesttest"))
    #print(countchar("  "))
