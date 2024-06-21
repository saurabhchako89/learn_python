to_seconds = 24 * 60 * 60
to_hours = 24 * 60
unit_seconds = "seconds"
unit_hours = "hours"

def calculate_seconds(days,custom_msg):
    print(f" {days} days are { days * to_seconds } {unit_seconds}")
    print(custom_msg)
    
def calculate_hours(days):
    print(f" {days} days are { days * to_hours } {unit_hours}")
    
def scope_check():
    my_var = "my internal variable"
    print(unit_hours)
    print(to_hours)
    print(my_var)
    
calculate_seconds(1,"Awesome")
calculate_seconds(10,"Looks Good")
calculate_seconds(25,"Hello World")

calculate_hours(1)
calculate_hours(10)
calculate_hours(25)

scope_check()