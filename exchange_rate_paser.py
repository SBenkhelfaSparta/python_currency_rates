from fx import get_ex_rate

ger = get_ex_rate.GetExRate()

code = input("Input the currency code you would like to compare to the EUR: ")
print("EUR/" + code + " = " + str(ger.getRate(code)))
