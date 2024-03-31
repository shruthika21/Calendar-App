import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

# Input year and month
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Display calendar
display_calendar(year, month)
