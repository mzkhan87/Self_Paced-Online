import io
import pytest

from mailroom_lesson_09 import *

def test_show_list(capsys):
    c = Donor()
    c.show_list()
    captured = capsys.readouterr()
    expected = '\nJosh Hoff\nTatsiana Kisel\n'
    assert captured.out == expected
    
def test_add_new_donor():
    c = Donor()
    c.add_donor('Andrew', 300)
    assert 'Andrew' in donors.keys()
    assert donors['Andrew'] == [300]
    
def test_show_list_after_adding_donor(capsys):
    c = Donor()
    c.show_list()
    captured = capsys.readouterr()
    expected = '\nJosh Hoff\nTatsiana Kisel\nAndrew\n'
    assert captured.out == expected
    
def test_add_donation_to_existing_donor():
    c = Donor()
    c.add_donor('Josh Hoff', 250)
    assert 'Josh Hoff' in donors.keys()
#NOTE: 25 and 75 are existing values for Josh Hoff
    assert donors['Josh Hoff'] == [25, 75, 250]
    
def test_create_report(capsys):
    c = Donor()
    c.report()
    expected = '\nDonor Name             | Total Given | Num Gifts | Average Gift\n\
---------------------------------------------------------------\n\
Josh Hoff               $      350.00           3      116.67\n\
Andrew                  $      300.00           1      300.00\n\
Tatsiana Kisel          $      140.55           2       70.28\n'
    captured = capsys.readouterr()
    assert captured.out == expected
    
def test_letters_to_everyone_files():
    c = Donor()
    c.letters()
    tab = '    '
    for i, val in donors.items():
        with open(f'{i}.txt', 'r') as outfile:
            donation = sum(val)
            check_text = f'Dear {i}, \n\n{tab}Thank you very much for your most recent donation \
of ${val[-1]:.2f}! \n\n{tab}You have now donated a total of ${donation:.2f}. \n\n{tab}Your support \
is essential to our success and will be well utilized. \n\n{tab*2}Sincerely, \n{tab*3}-The Company'
            expected = outfile.read()
            assert check_text == expected