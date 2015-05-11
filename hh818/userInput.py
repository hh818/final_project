'''
Created on May 4, 2015

@author: Ho Huang(hh818)
'''
from errorHandling import *
import sys

def inputLocation(df):
    while True:
        try:
            location = raw_input('Enter a location to look at. It could be a Zipcode, the name of a NYC Borough, or all for the whole of NYC.\nOr enter Quit to quit:\n')
            if location.isdigit() == True:
                if int(location) > 10000 and int(location) <= 19999:
                    inDataSet = location in df['Incident Zip'].values
                    if inDataSet == True:
                        return location
                    else:
                        raise NonExistError
                elif location <= 10000 or location > 19999:
                    raise ValueError
            elif location.replace(' ', '').isalpha() == True:
                if location.upper() ==  'BROOKLYN' or location.upper() == 'BRONX' or location.upper() == 'MANHATTAN' or location.upper() == 'QUEENS' or location.upper() == 'STATEN ISLAND' or location.upper() == 'ALL' or location.upper() == 'QUIT':
                    return location.upper()
                else:
                    raise ValueError
            else:
                raise SyntaxError

        except ValueError:
            print '\nPlease enter a valid zip, borough, or simply \'all\'. A zip code should be 5 digits and start with a 1. A borough should be either Brooklyn, Bronx, Manhattan, Queens, or Staten Island.\n'
        except SyntaxError:
            print '\nPlease enter a valid input. either a integer or a string.\n'
        except NonExistError:
            print '\nSorry, there is no data on the zip you entered in this dataset.\n'
        except KeyboardInterrupt:
            print '\nKeyboardInterrupt. Exiting program now.'
            sys.exit('Bye')
            
def inputType():
    while True:
        try:
            complaintType = raw_input('Enter a type of complaints to look at, building condition, noise, street condition, sanitation, or all to include all:\n')
            if complaintType.replace(' ', '').isalpha() == True:
                complaintType = complaintType.lower()
                if complaintType == 'building condition' or complaintType == 'noise' or complaintType == 'street condition' or complaintType == 'sanitation' or complaintType =='all':
                    return complaintType
                else:
                    raise ValueError
            else:
                raise SyntaxError
        except ValueError:
            print '\nPlease enter a valid complaint type. building condition, noise, street condition, sanitation, or all.\n'
        except SyntaxError:
            print '\nPlease enter a valid type of input, complaint types can only be strings.\n'
        except KeyboardInterrupt:
            print '\nKeyboardInterrupt. Exiting program now.'
            sys.exit('Bye')
    


            