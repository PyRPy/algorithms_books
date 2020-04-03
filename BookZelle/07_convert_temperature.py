# 07_convert_temperature.py
# convert temperature from C unit to F unit
def main():
    celsius = float(input("what is the temperature in C ?"))
    fahrenheit = 9/5 * celsius + 32 
    print("the temperature is", fahrenheit, "deg in F")

    # print warnings for exreme temperatures
    if fahrenheit > 90:
        print("it is a really hot out here. Be Careful!")
    if fahrenheit < 30:
        print("it is realy cold!")

main()
