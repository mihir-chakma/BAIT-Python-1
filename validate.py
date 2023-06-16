import sys
def validate_data(a, b, c):
    valid = a!= 0 and b!=0 and c!=0 and a!=b and b!=c and c!=a
    if not valid:
        print("Invalid data - Quitting...!")
        sys.exit()
    else:
        return a, b, c 

