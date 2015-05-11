'''
Created on Apr 30, 2015

@author: Ho Huang(hh818)
'''
import pandas as pd
from errorHandling import *

def loadDataFrame():
    '''load csv file and return a DataFrame'''
    try:
        print 'Reading the 311 Service Requests csv file. This might take a minute or two...\n'
        columnsToInclude = ['Created Date', 'Complaint Type', 'Incident Zip', 'Borough']
        serviceRequests = pd.read_csv('311_Service_Requests_from_2010_to_Present.csv', usecols = columnsToInclude, low_memory = False)
    
    except:
        raise noDataError()
    
    else:
        return serviceRequests
        