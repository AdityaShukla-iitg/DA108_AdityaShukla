#Below code calculate the age and days left for next birthday topics are import of datetime, function and logical building






from datetime import date


def calc_age_and_next_birthday(birth_year, birth_month, birth_day ):                                   #function jiska naam hai calc_age which has 3 parameters year, month, day
    today = date.today()                                                                               #aaj ka din
    birth_date = date(birth_year, birth_month , birth_day)                                             #changing inputs into date format


    #calc age of Aditya Shukla

    age= today.year - birth_date.year                                                                  #subtract today - dob to get age

    if (today.month, today.day) < (birth_month , birth_day):                                           #suppose your birthday is not happened yet so we minus 1
        age-=1                                                                                         # Example : if your dob is in 2000 and current is 2025 it will get age = 25
                                                                                                                   #but your birthdayis yet to come so minus 1

    #calc next birthday of Aditya Shukla
    next_birthday = date(today.year, birth_month , birth_day)                                          
    if next_birthday < today :
        next_birthday = date(today.year+1 , birth_month , birth_day)                                   


    days_to_birthday =(next_birthday -today).days

    return age, days_to_birthday




birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

age, days_until_next_birthday = calc_age_and_next_birthday(birth_year, birth_month, birth_day)         #function call and arguments are here
print(f"You are {age} years old.")                                                                     #print using f string
print(f"Your next birthday is in {days_until_next_birthday} days.")