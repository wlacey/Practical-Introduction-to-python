""""Write a class called Time whose only field is a time in seconds. It should have a method called
convert_to_minutes that returns a string of minutes and seconds formatted as in the following
example: if seconds is 230, the method should return '5:50'. It should also have
a method called convert_to_hours that returns a string of hours, minutes, and seconds
formatted analogously to the previous method."""

#NoteThe question has a slight mistake the Input of 230s should give an output of 3:50s and not 5:50s

from datetime import timedelta

class Time():
    
    def __init__(self, sec):
        self.sec = sec
        
    def convert(self):
        return timedelta(seconds = self.sec)
    
    def __str__(self):
        return f'The current amount of seconds is {self.sec}.'

def validate_sec(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input >= 0:
                valid = True
            else:
                print('\nPlease enter the amount in seconds.')
        except:
            print('\nPlease enter a valid integer.')
    return user_input

def main():
    print('Welcome to Time Conversion.')
    message = 'Enter the number of seconds you want to convert: '
    user_sec = validate_sec(message)
    user = Time(user_sec)
    print(f'\n{user}\n')
    print(f'The converted time is {user.convert()}')
    
if __name__ == '__main__':
    main()
