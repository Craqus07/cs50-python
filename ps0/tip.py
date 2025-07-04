def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # $##.##
    dd = float(d.replace("$",""))
    return dd


def percent_to_float(p):
    # ##%
    pp = float(p.replace("%",""))
    return pp

main()