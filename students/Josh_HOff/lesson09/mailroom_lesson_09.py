import sys
import copy
import pathlib

donors = {'Josh Hoff': [25, 75], 'Tatsiana Kisel': [35, 105.55]}

#This class handles all input from the user
class Input(object):
    def __init__(self=None):
        pass
    
    def thank_you(self=None):
        while True:
            donor_name = input('\nWhat is the name of the donor?: ')
            if donor_name == 'list':
                Donor().show_list()
                continue
            elif donor_name == 'quit':
                break
            while True:
                try:
                    donation = float(input('\nWhat is the donation amount?: '))
                except ValueError:
                    print('\nPlease give a number instead.')
                    continue
                break
            Donor().add_donor(donor_name, donation)
            break

#this class handles all donor management
class Donor(object):
    def __init__(self=None):
        pass
                    
    @staticmethod
    def report():
        global donors
        y = '|'
        rows = ''
        top = f'Donor Name{y:>14} Total Given {y} Num Gifts {y} Average Gift\n'
        top += ('-' * 63)
        sorted_donors = sorted(donors.items(), key=lambda k: sum(k[1]), reverse=True)
        for name, donations in sorted_donors:
            gift = len(donations)
            average = (sum(donations) / gift)
            rows += f'\n{name:<23} $ {sum(donations):>11.2f} {gift:>11} {average:>11.2f}'
        top += rows
        print(f'\n{top}')
        
    @staticmethod
    def letters():
        tab = '    '
        global donors
        for i, val in donors.items():
            with open(f'{i}.txt', 'w') as outfile:
                donation = sum(val)
                outfile.write(f'Dear {i}, \n\n{tab}Thank you very much for your most recent donation \
of ${val[-1]:.2f}! \n\n{tab}You have now donated a total of ${donation:.2f}. \n\n{tab}Your support \
is essential to our success and will be well utilized. \n\n{tab*2}Sincerely, \n{tab*3}-The Company')
        
    def quitting(self):
        sys.exit()
        
    @staticmethod
    def show_list():
        print('')
        global donors
        for i in donors:
            print(i)
            
    def continuing(self):
        print('Try Again.\n')
        
    @staticmethod
    def add_donor(donor_name='Jacob', donation=30):
        global donors
        if donor_name in donors:
            donors[donor_name] += [donation]
        else:
            donors[donor_name] = [donation]
        
        
switch_func_dict = {'1':Input().thank_you, '2':Donor().report, '3':Donor().letters, '4':Donor().quitting, 'quit':Donor().quitting, 'list':Donor().show_list}

#main function: adjusted to use classes
if __name__ == '__main__':
    while True:
        choice = input('\n1: Send a Thank You \n2: Create a Report \n3: Send Letters to Everyone \n4: Quit \nChoose an Option: ')
        c = switch_func_dict.get(choice, Donor().continuing)()