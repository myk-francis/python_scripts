
from datetime import datetime

rep_time = '4'

display_time = rep_time if (rep_time != '15') else 3

display_am_pm = 'AM' if (rep_time != '15') else 'PM'

dest_filename = f'Route Report ({datetime.now().strftime("%d-%m-%Y")}) {display_time} {display_am_pm}.xlsx'

print(dest_filename)