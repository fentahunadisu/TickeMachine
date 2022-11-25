print("********** will come to drug store ********")
cosmetics = 0
medicine = 0
perfume = 0
def drug_stor():
    if order == "cosmetics":
        global cosmetics
        cosmetics += 1
        print(f"c - {cosmetics}")
    if order == "medicine":
        global medicine
        medicine += 1
        print(f"p - {medicine}")
    if order == "perfume":
        global perfume
        perfume += 1
        print(f"m - {perfume}")
order = input("please choose your product area: ")