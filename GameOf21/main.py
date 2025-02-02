import card_calculations

spelare = card_calculations.new_card()
dator = card_calculations.new_card()
choice = True
print(f"Dator har nu {dator} poäng.")
print(f"Du har nu {spelare} poäng.")

while True:
    if choice:
        print("Meny")
        print("1. Ta ett nytt kort")
        print("2. Inget nytt kort")
        print("3. Avsluta")
        alternativ = input("Välj ett alternativ: ")
        try:
            alternativ = int(alternativ)
            if alternativ == 1:
                spelare += card_calculations.new_card()
                if spelare <= 21:
                    print(f"Du har nu {spelare} poäng och dator: {dator}")
                    dator = card_calculations.dator_new_card(dator, spelare, False)
                    if dator > 21:
                        print(f"Du vann. Spelare: {spelare}, dator: {dator}.")
                        choice = False
                else:
                    print(f"Du blev tjock. Du fick {spelare} poäng.")
                    choice = False
            elif alternativ == 2:
                dator = card_calculations.dator_new_card(dator, spelare, True)
                if dator > 21:
                    print(f"Du vann. Spelare: {spelare}, dator: {dator}.")
                    choice = False
                elif dator < spelare:
                    print(f"Du vann. Spelare: {spelare}, dator: {dator}.")
                    choice = False
                elif dator == spelare:
                    print(f"Det blev oavgjort. Spelare: {spelare}, dator: {dator}.")
                    choice = False
                else:
                    print(f"Du förlorade. Spelare: {spelare}, dator: {dator}.")
                    choice = False
            elif alternativ == 3:
                break;
            else:
                print("Ogiltigt värde, försök igen.")
        except ValueError:
            print("Det är inget giltigt alternativ, försök igen")
    else:
        print("Meny")
        print("1. Börja om")
        print("2. Avsluta")
        alternativ = input("Välj ett alternativ: ")
        try:
            alternativ = int(alternativ)
            if alternativ == 1:
                choice = True
                spelare = card_calculations.new_card()
                dator = card_calculations.new_card()
                print(f"Dator har nu {dator} poäng.")
                print(f"Du har nu {spelare} poäng.")
            elif alternativ == 2:
                break;
            else:
                print("Ogiltigt värde, försök igen.")
        except ValueError:
            print("Det är inget giltigt alternativ, försök igen")