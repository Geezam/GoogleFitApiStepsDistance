from dateutil.relativedelta import relativedelta #date and time stuff
from datetime import date

    
def PreMonthFirstLast(): #info about the previous month as example data
    today = date.today()
    d = today - relativedelta(months=1)
    first_day = date(d.year, d.month, 1)
    first = first_day.timetuple()
    humanFirst = first_day.strftime('%d %B %Y')
    #returns first date of the previous month - datetime.date(2019, 7, 1)

    last_day = date(today.year, today.month, 1) - relativedelta(days=1)
    last = last_day.timetuple()
    humanLast = last_day.strftime('%d %B %Y')
    #returns the last date of the previous month - datetime.date(2019, 7, 31)
    
#https://www.w3schools.com/python/python_datetime.asp
#https://stackoverflow.com/questions/57686399/how-to-consider-previous-month-first-day-and-previous-month-last-day-in-timestam
    
    lastMonth = first_day.strftime('%B %Y')
    firstDayNum = first_day.strftime('%d')
    lastDayNum = last_day.strftime('%d')
    monthNum = first_day.strftime('%m')
    yearNum = first_day.strftime('%Y')
    
    firstLast = [first,last,humanFirst,humanLast,lastMonth,firstDayNum,lastDayNum,monthNum,yearNum]
    return firstLast
