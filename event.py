from datetime import datetime

class Event():
	
    name = "default"
    start_time = None
    end_time = None
    
    # name (string) - name of event
    def __init__(self, name):
        self.name = name

    # start(end)_time -beggining(ending) of occured event in hh:mm-hh:mm 
    def set_time(self, time_string):
        time_format = "%H:%M" 
        try:
            self.start_time = datetime.strptime(time_string[:5], 
                              time_format).time() 
            self.end_time = datetime.strptime(time_string[6:], 
                            time_format).time() 
        except ValueError:
            return False
        return True
    
    def get_event_string(self):
        result = self.start_time.strftime("%H:%M-") \
        + self.end_time.strftime("%H:%M - ") \
        + self.name
        return result

