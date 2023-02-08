# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



    # Use a breakpoint in the code line below to debug your script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day = int(input("Enter day of birth:"))
    month = int(input("Month of birth:"))
    year = int(input("Year of birth:"))
    print(day, month, year)

    number = 0
    while day > 0:
        number += day % 10
        day = int(day / 10)

    while month > 0:
        number += month % 10
        month = int(month / 10)

    while year > 0:
        number += year % 10
        year = int(year / 10)
    print(number)
    tmp = 0
    while number >= 10:
        tmp = 0

        while number > 0:
            tmp += number % 10
            number = int(number / 10)
        number = tmp

    print(number)

    if (number == 1):
        print(
            "Да се научим да поемаме отговорност и преодоляваме трудностите чрез разум Самостоятелен бизнес, търговски представител, програмист.")
    elif (number == 2):
        print(
            "Да се научим да работим в колектив. Професии в областта на медицината, биологията, химията, археологията.")
    elif (number == 3):
        print(
            "Да се научим да ценим и малките успехи в живота. Професии свързани с пътуване, туризъм, усъвършенстване на технологии, търговия.")
    elif (number == 4):
        print(
            "Да се научим на прецизност в професията. Професии свързани с конструиране, техника, строг ред и дисциплина, спорт.")
    elif (number == 5):
        print(
            "Да се научим да комуникираме с другите. Професии свързани с преподаване, научна и административна дейност, журналистика и реклама.")
    elif (number == 6):
        print(
            "Да се научим на безкористност, човеколюбие, безпристрастност. Професии свързани с изкуство, дизайн, художествена гимнастика, поезия, психология.")
    elif (number == 7):
        print("Да се научим да анализираме. Професии свързани с точна изработка – гравьор, скулптор, градинар, хирург.")
    elif (number == 8):
        print(
            "Да се научим на взискателност, целеустременост, постоянство.Професии свързани с риск – криминалист, съдебен медик, траурен агент, банкер, медиум.")
    elif (number == 9):
        print(
            "Да се научим на състрадание, толерантност, благотворителност. Професии свързани с нетрадиционно мислене чрез духовно израстване – пионери във всяка една област, хора, които променят разбиранията ни за света и човечеството.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
