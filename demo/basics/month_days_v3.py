# Take month number and display no.of days in the month
month = int(input("Enter month number [1-12] :"))

match month:
    case 2:
        year = int(input("Enter year :"))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(29)
        else:
            print(28)
    case 4 | 6 | 9 | 11:
        print(30)
    case _:
        print(31)
