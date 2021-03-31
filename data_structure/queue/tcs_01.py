def string_shift(s1):
    ls1 = list(s1)
    f_shift = ls1[1:] + ls1[:1]
    b_shift = f_shift[2:] + f_shift[:2]
    if f_shift == b_shift:
        print("1")
    else:
        print("0")

# Driver Code Starts
if __name__ == "__main__":
    s1 = input("Enter the String: ")
    string_shift(s1)
