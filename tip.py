def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
   dollar_removed=float(d[1:]) #slicing the int part only
   return dollar_removed

  
def percent_to_float(p):
    percentage_without_sign=int(p[:-1]) #removing the percent sign
    return percentage_without_sign/100


main()