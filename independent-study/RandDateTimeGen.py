import random
import datetime
from datetime import time

# Generate a day within the given time frame
def random_date(start_date, end_date):   
    num_days = (end_date - start_date).days
    rand_days = random.randint(0, num_days)
    rand_date = start_date + datetime.timedelta(days = rand_days)
    
    return rand_date


# Generate a time frame (12 hr time) within the given hours (24 hr)
def random_timeframe(min_hr_24, max_hr_24, max_timeframe):
	start_hr = random.randint(min_hr_24, max_hr_24)
	start_min = random.randint(0, 59)
		
	end_hr = random.randint(min_hr_24, max_hr_24 + max_timeframe)
 
	while (end_hr <= start_hr) or (end_hr > start_hr + max_timeframe): # End should be after start, and not longer than the given max
		end_hr = random.randint(min_hr_24, max_hr_24 + max_timeframe) 
		if end_hr > start_hr and end_hr <= start_hr + max_timeframe:
			break


	end_min = random.randint(0, 59)
		
	rand_time_start = time(start_hr, start_min, 0).strftime('%I:%M %p')
	rand_time_end = time(end_hr, end_min, 0).strftime('%I:%M %p')
		
	return rand_time_start, rand_time_end
