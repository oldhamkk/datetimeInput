from datetime import datetime
import time
yearin = ""
monthin = ""
dayin = ""
hourin = ""
minutein = ""
secondin = ""
datetime = ""
expectedinput = "%Y-%m-%d %H:%M:%S"
while True:
    yearin = input("Enter a year:\n")
    try:
        yeari = int(yearin)
    except:
        pass
    if yeari is not None:
        if yeari < 1900:
            print("Year must be greater than 1900")
        elif yeari > 2020:
            print("Year must be less than 2020")
        else:
            print("Year is Valid")
            break
    else:
        print("Year "+yearin+" is invalid")
while True:
    monthin = input("Enter a month:\n")
    try:
        monthi = int(monthin)
    except:
        pass
    if monthi is not None:
        if monthi < 1:
            print("Month must be greater than or equal to 1.")
        elif monthi > 12:
            print("Month must be less than or equal to 12")
        else:
            print("Month is valid.")
            break
    else:
        print("Month "+monthin+" is invalid")
        monthswith30days = [4, 6, 9, 11]
while True:
    dayin = input("Enter a day:\n")
    try:
        dayi = int(dayin)
    except:
        pass
    if dayi is not None:
        if dayi < 1:
            print("Day must be at least 1.")
        elif monthi == 2 and yeari % 4 == 0 and dayi > 29:
            print("Day must be no more than 29")
        elif monthi == 2 and yeari % 4 != 0 and dayi > 28:
            print("Day must be no more than 28")
        elif dayi > 30 and monthi in monthswith30days:
            print("Day must be no more than 30")
        elif dayi > 31:
            print("Day must be no more than 31")
        else:
            print("Day is valid.")
            break
    else:
        print("Month "+dayin+" is invalid")
while True:
    hourin = input("Enter an hour:\n")
    try:
        houri = int(hourin)
    except:
        pass
    if houri is not None:
        if houri < 0:
            print("Hour must be at least 00")
        if houri > 24:
            print("Hour must be less than 24")
        else:
            print("Hour is valid")
            break
    else:
        print("Hour "+hourin+" is invalid")
while True:
    minutein = input("Enter an minute:\n")
    try:
        minutei = int(minutein)
    except:
        pass
    if minutei is not None:
        if minutei < 0:
            print("Minute must be at least 00")
        if minutei > 60:
            print ("Minute must be less than 60")
        else:
            print("Minute is valid")
            break
    else:
        print("Minute "+minutein+" is invalid")
while True:
    secondin = input("Enter an second:\n")
    try:
        secondi = int(secondin)
    except:
        pass
    if secondi is not None:
        if secondi > 59:
            print("Second must be less than 60")
        else:
            print("Minute is valid")
            break
    else:
        print("Second "+secondin+" is invalid")
while True:
    print(yearin + "-" + monthin + "-" + dayin + " " + hourin + ":" + minutein + ":" + secondin)
    dt = datetime.datetime(yearin, monthin, dayin, hourin, minutein, secondin)
    time.mktime(dt.timetuple())
    break
