to_seconds = 24 * 60 * 60
to_hours = 24 * 60
unit_seconds = "seconds"
unit_hours = "hours"

def calculate_seconds(user_input):
    return (f" {user_input} days are { user_input * to_seconds } {unit_seconds}")

    

user_input = input("Enter a value for number of days and I will convert to seconds : \n")
user_input_num = int(user_input)
calculated_value = calculate_seconds(user_input_num)
print(calculated_value)


my_var = calculate_seconds(user_input_num)
print(my_var)
