'''
Created on May 1, 2015

@author: Ho Huang(hh818)
'''
class noDataError(Exception):
    '''exception thrown when csv file cannot be retrieved'''
    def __str__(self):
        return 'Unable to locate file, plase make sure the file is successfully downloaded and extracted before running the program'

class NonExistError(Exception):
    '''exception thrown a valid zip code cannot be found in dataframe'''
    pass
