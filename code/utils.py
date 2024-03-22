
def assign_if_exists(value):
    return value if value is not None else ""

def process_date(date):
    return str(date.replace("-", ""))
    
def process_time(time):
    return str(time.replace(":", ""))

def pad_age(age):
    return str(age).zfill(3) + "Y"
