
def get_days_later_string(days_later:int)->str:

    if days_later == 1:
        return ' (next day)'
    if days_later > 1:
        return f' ({days_later} days later)'

    return ''

def number(week: dict, day:str, days_later:int)->str:

    for key in week:
        if key.lower() == day:
            number_of_day = week[key] + days_later

            if number_of_day < 7:
                for key in week:
                    if week[key] == number_of_day:
                        return(week[key])   
            else:
                for key in week:
                    if week[key] == number_of_day % 7:
                        return(week[key])


def semana(week, num):
    for key in week:
        if week[key] == num:
            return(key)

def get_ampm(total_hours:int) -> str:
    if total_hours < 12:
        return 'AM'
    if total_hours >= 12:
        return 'PM'

def add_time(start_time:str, time_add:str, weekday:str = None) -> str:

    # add_time('8:16 PM', '466:02','tuesday')

    time_ampm = start_time.split()
    time = time_ampm[0]
    ampm = time_ampm[1]

    time_list = [time, time_add]

    total_minutes = 0
    total_hours = 0

    for item in time_list:

        time_parts = item.split(':')
        hour = int(time_parts[0])
        total_hours += hour
        minutes = int(time_parts[1])
        total_minutes += minutes
  
    if ampm == 'PM':
        total_hours +=  12
    
    if total_minutes >= 60:
        add_hours = int(total_minutes / 60)
        total_minutes = total_minutes % 60
        total_hours = add_hours + total_hours


    days_later = int(total_hours/24)
    total_hours = total_hours - 24 * days_later
    
    new_ampm = get_ampm(total_hours)

    if total_hours == 0:
        total_hours = total_hours + 12
        
    elif total_hours > 12:
        total_hours = total_hours - 12

    answer = f'{total_hours:02d}:{total_minutes:02d} {new_ampm}'

    if weekday:

        week = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
        day = weekday.lower()
        num = number(week, day, days_later)
        day = semana(week, num)

        answer +=  f', {day}'

    days_later_string = get_days_later_string(days_later)
    answer += days_later_string

    return answer


new = add_time('11:59 AM', '50:05')

print(new)