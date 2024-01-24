
def TreeChar(): 
    print(" *** Draw pyramid (0-9) ***")
    input_str = input("Enter height : ")
    num = int(input_str)
    n = 0
    for row in range(num):
        line = ' '*(num-row-1)
        for ch in range(2*row+1):
            line += chr(ord("Z")-n%26)
            n += 1
        print(line)
    print("===== End of program =====")

if __name__ == '__main__':
    TreeChar()