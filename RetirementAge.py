import datetime
import calendar

def retirement(yearOfBirth, monthOfBirth):
    age=67
    month=0
    yearOfBirth, monthOfBirth=int(yearOfBirth), int(monthOfBirth)
    if yearOfBirth>=1900:

        if yearOfBirth<=1937:
            age=65
            month=0
        elif yearOfBirth==1938:
            age=65
            month=2
        elif yearOfBirth==1939:
            age=65
            month=4
        elif yearOfBirth==1940:
            age=65
            month=6
        elif yearOfBirth==1941:
            age=65
            month=8

        elif yearOfBirth==1942:
            age=65
            month=10
        
        elif yearOfBirth<=1954 and yearOfBirth>=1943 :
            age = 66
            month=0
        elif yearOfBirth==1955:
            age=66
            month =2
        elif yearOfBirth==1956:
            age = 66
            month = 4
        elif yearOfBirth==1957:
            age = 66
            month = 6
        elif  yearOfBirth==1958:
            age = 66
            month = 8
        elif yearOfBirth == 1959:
            age = 66
            month = 10
        elif yearOfBirth >= 1960:
            age = 67
            month = 0
    print("Your full retirement age is ", age," and ",month," months")
    sum=monthOfBirth+month
    month2=sum
    if month2>12:
        month2=sum-12
    plus=0
    if sum>=12:
        plus=1
    year2=yearOfBirth+age+plus
    print("this will be in ",calendar.month_name[month2]," of ",year2)
    
def main():
    print("Social Security Full Retirement Age Calculator")
    yearOfBirth=int(input("Enter the year of birth or enter to exit: "))
    monthOfBirth=0
    while monthOfBirth<=0 or monthOfBirth>12:
        monthOfBirth=int(input("Enter the month of birth or enter to exit: "))
    retirement(yearOfBirth,monthOfBirth)
if __name__ == '__main__': main() 
