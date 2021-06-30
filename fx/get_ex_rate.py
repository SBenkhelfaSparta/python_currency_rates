import json

class GetExRate:
    def getRate(self, code):
        f = open('fx/exchange_rates.json')
        data = json.load(f)
        try:
            return data['rates'][code]
        except:
            print("You must have typed in a code we do not have. Try again or look elsewhere for that currency pair")
