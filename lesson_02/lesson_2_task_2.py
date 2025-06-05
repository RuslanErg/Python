def is_year_leap(year):
    if (year % 4 == 0):
        print("Year: " + str(year) + " True")
    else:
        print("Year: " + str(year) + " False")


is_year_leap(int(input("Введите год: ")))
