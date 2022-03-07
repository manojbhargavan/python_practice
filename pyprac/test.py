import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(':')
goal = input_list[0]
deadline = input_list[1].split('.')
deadline_year = int(deadline[2])
deadline_month = int(deadline[1])
deadline_day = int(deadline[0])

date_of_deadline = datetime.date(deadline_year, deadline_month, deadline_day)
current_date = datetime.date.today()
timespan = date_of_deadline - current_date
print(timespan)
