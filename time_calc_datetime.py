from datetime import datetime, timedelta

def add_time(start_time:str, time_add:str, weekday:str = None) -> str:

    start_time = datetime.strptime(start_time, "%I:%M %p")
    hours_add, minutes_add = time_add.split(':')
    time_to_add = timedelta(hours=int(hours_add), minutes=int(minutes_add))

    end_time = start_time + time_to_add

    days_later = end_time.day - start_time.day
    
    end_time_str = end_time.strftime('%I:%M %p')
    
    if weekday:
        end_time_str += end_time.strftime(' %A')

    if days_later == 1:
        end_time_str += ' (Next Day)'

    if days_later > 1:
        end_time_str += (f' ({days_later} Days Later)')

    return end_time_str

def main():
    new = add_time('11:59 PM', '48:05', 'tueSday')
    print(new)

if __name__ == '__main__':
    main()