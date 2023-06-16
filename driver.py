import inputs
import validate
import process
import output

def main():
    a, b, c = inputs.input_data()
    x, y, z = validate.validate_data(a, b, c)
    hi = process.find_highest(x, y, z)
    lo = process.find_lowest(x, y, z)
    mi = x + y + z - (hi+lo)
    output.display_ascend(lo, mi, hi)

if __name__=="__main__":
    main()
