# the GSD in this scenario has been considered at 3.5% whereas the service charges has been considered at 5%


n=int(input("Dear coustomer please select from the given options for the desired menu :\n"
            "1) Espresso and Mocha chillers\n"
            "2) Over Ice \n"
            "3) Choclate chiller \n"
            "4) Fusion \n"))
if n==1:
    menu = {"11": 361, "12": 409,
            "21": 361, "22": 409,
            "31": 361, "32": 409,
            "41": 396, "42": 461,
            "51": 396, "52": 461,
            "61": 396, "62": 461,
            "71": 396, "72": 461,
            "81": 399, "82": 509
            }
    print(""
          "Espresso and Mocha chillers \n"
          "                                       Small     Regular\n"
          "1) VERY VANILLA CHILLER                 361       409\n"
          "2) COCOA LOCO                           361       409\n"
          "3) COOKIES N CREAM                      361       409\n"
          "4) HAZELNUT MOCHA CHILLER               396       461\n"
          "5) CHOCLATE MACHADIMA CHILLER           396       461\n"
          "6) ITALIAN  DOLCE CHILLER  CHILLER      396       461\n"
          "7) CARAMEL  NUT CHILLER                 396       461\n"
          "8) TIRAMISU CHILLER                     399       509\n")
    total_cost = 0
    break_condition = ["N", "no"]

    while True:
        choice0 = input("Dear costumer enter your choice from the above menu(N or no for exit:")
        if choice0 in break_condition:
            print("Your bill without tax is                        :", total_cost, " PKR-")
            total_cost1 = total_cost + (3.5 * (total_cost / 100))
            print("Your bill after 3.5 % GSD is                    :", round(total_cost1, 2), " PKR-")
            print("Your  Final bill after 5 % service charges is   :",
                  round(total_cost1 + (5 * (total_cost1 / 100)), 2), " PKR-")
            final_cost=round(total_cost1 + (5 * (total_cost1 / 100)), 2)
            file = open("bill.txt","w")
            file.writelines("Dear coustomer your final bill after 3.5 % GSD and 5% service charges is "+str(final_cost))

            break
        else:
            choice = int(choice0)
        choice1 = int(input("Enter 1 for small and Enter 2 for regular size : "))
        choice2 = int(input("Enter the desired quantity : "))
        result = str(choice) + str(choice1)
        total_cost += int(menu[result]) * choice2
        print("Your updated bill is", total_cost)
elif n==2:
    menu = {"11": 300, "12": 374,
            "21": 300, "22": 361,
            "31": 378, "32": 430,
            "41": 252, "42": 274,
            "51": 250, "52": 291,
            "61": 250, "62": 291,
            "71": 250, "72": 291,
            "81": 250, "82": 291,
            "91": 335, "92": 340,
            "101": 335, "102": 361,
            "111": 239, "112": 291,

            }
    print(""
          "Over Ice  \n"
          "                                       Small     Regular\n"
          "1) SIGNATURE ICED COFFEE                300       374\n"
          "2) ICED MOCHA                           300       361\n"
          "3) ICED CARAMEL LATTE                   378       430\n"
          "4) ICED AMERICANO                       252       274\n"
          "5) BLUEBERRY LEMONADE                   250       291\n"
          "6) LYCHEE LEMONADE                      250       291\n"
          "7) GREEN APPLE LEMONADE                 250       291\n"
          "8) PEACH LEMONADE                       250       291\n"
          "9) APPLE SODA                           335       348\n"
          "10) LIME SODA                           335       361\n"
          "11) ICED TEAS(PEACH/LEMON LYCHEE)       239       291\n")
    total_cost = 0
    break_condition = ["N", "no"]

    while True:
        choice0 = input("Dear costumer enter your choice from the above menu(N or no for exit:")
        if choice0 in break_condition:
            print("Your bill without tax is                        :", total_cost, " PKR-")
            total_cost1 = total_cost + (3.5 * (total_cost / 100))
            print("Your bill after 3.5 % GSD is                    :", round(total_cost1, 2), " PKR-")
            print("Your  Final bill after 5 % service charges is   :",
                  round(total_cost1 + (5 * (total_cost1 / 100)), 2), " PKR-")
            final_cost=round(total_cost1 + (5 * (total_cost1 / 100)), 2)
            file = open("bill.txt","w")
            file.writelines("Dear coustomer your final  bill after 3.5 % GSD and 5% service charges is "+str(final_cost))

            break
        else:
            choice = int(choice0)
        choice1 = int(input("Enter 1 for small and Enter 2 for regular size : "))
        choice2 = int(input("Enter the desired quantity : "))
        result = str(choice) + str(choice1)
        total_cost += int(menu[result]) * choice2
        print("Your updated bill is", total_cost)
elif n==3:
    menu = {"11": 348, "12": 365,
            "21": 348, "22": 365,
            "31": 348, "32": 400
            }
    print(""
          "Menu for Chocolate Chillers   \n"
          "                                       Small     Regular\n"
          "1) ORIGINAL ICED CHOCOLATE              348       365\n"
          "2) WHITE ICED CHOCLATE                  348       365\n"
          "3) CHOCOLATE DELIGHT                    348       400\n")
    total_cost = 0
    break_condition = ["N", "no"]

    while True:
        choice0 = input("Dear costumer enter your choice from the above menu(N or no for exit:")
        if choice0 in break_condition:
            print("Your bill without tax is                        :", total_cost, " PKR-")
            total_cost1 = total_cost + (3.5 * (total_cost / 100))
            print("Your bill after 3.5 % GSD is                    :", round(total_cost1, 2), " PKR-")
            print("Your  Final bill after 5 % service charges is   :",
                  round(total_cost1 + (5 * (total_cost1 / 100)), 2), " PKR-")
            final_cost=round(total_cost1 + (5 * (total_cost1 / 100)), 2)
            file = open("bill.txt","w")
            file.writelines("Dear coustomer your final bill after 3.5% GSD and 5% service charges  is "+str(final_cost))

            break
        else:
            choice = int(choice0)
        choice1 = int(input("Enter 1 for small and Enter 2 for regular size : "))
        choice2 = int(input("Enter the desired quantity : "))
        result = str(choice) + str(choice1)
        total_cost += int(menu[result]) * choice2
        print("Your updated bill is", total_cost)

elif n==4:
    menu = {"11": 335, "12": 365,
            "21": 335, "22": 365,
            "31": 348, "32": 400,
            "41": 348, "42": 400,
            }
    print(""
          "Menu for Fusion   \n"
          "                                       Small     Regular\n"
          "1) Iced lime                            335       365\n"
          "2) Appler Chiller                       335       365\n"
          "3) Chai chiller                         348       400\n"
          "4) Green Tea chiller                    348       400\n")
    total_cost = 0
    break_condition = ["N", "no"]

    while True:
        choice0 = input("Dear costumer enter your choice from the above menu(N or no for exit:")
        if choice0 in break_condition:
            print("Your bill without tax is                        :", total_cost, " PKR-")
            total_cost1 = total_cost + (3.5 * (total_cost / 100))
            print("Your bill after 3.5 % GSD is                    :", round(total_cost1, 2), " PKR-")
            print("Your  Final bill after 5 % service charges is   :",
                  round(total_cost1 + (5 * (total_cost1 / 100)), 2), " PKR-")
            final_cost=round(total_cost1 + (5 * (total_cost1 / 100)), 2)
            file = open("bill.txt","w")
            file.writelines("Dear coustomer your final bill after 3.5% GSD and 5% Service charges is  is "+str(final_cost))

            break
        else:
            choice = int(choice0)
        choice1 = int(input("Enter 1 for small and Enter 2 for regular size : "))
        choice2 = int(input("Enter the desired quantity : "))
        result = str(choice) + str(choice1)
        total_cost += int(menu[result]) * choice2
        print("Your updated bill is", total_cost)


