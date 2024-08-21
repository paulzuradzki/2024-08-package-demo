def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

if __name__=="__main__":
    c = 0
    f = celsius_to_fahrenheit(c)

    print(f"c: {c}, f: {f}")