'''
Created on Apr 30, 2015

@author: Ho Huang(hh818)
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fileLoading import *
from dataCleanup import *
from userInput import *
from graphDataClass import *
import sys
    
if __name__ == '__main__':
    
    serviceRequests = loadDataFrame()
    
    serviceRequests = serviceRequests.rename(columns = {'Complaint Type':'Complaints'} )
    
    serviceRequests['Complaints'] = lowerComplaintType(serviceRequests['Complaints'])
    
    building, noise, street, sanitation = makeComplaintCatList()
    
    serviceRequests['Complaint Type'] = np.NaN
    
    for complaintType in building:
        serviceRequests['Complaint Type'] = changeComplaintTypeBuildingCondition(complaintType, serviceRequests['Complaints'], serviceRequests['Complaint Type'])
    
    for complaintType in noise:
        serviceRequests['Complaint Type'] = changeComplaintTypeNoise(complaintType, serviceRequests['Complaints'], serviceRequests['Complaint Type'])
        
    for complaintType in street:
        serviceRequests['Complaint Type'] = changeComplaintTypeStreetCondition(complaintType, serviceRequests['Complaints'], serviceRequests['Complaint Type'])
        
    for complaintType in sanitation:
        serviceRequests['Complaint Type'] = changeComplaintTypeSanitation(complaintType, serviceRequests['Complaints'], serviceRequests['Complaint Type'])
    
    #drop all missing values and reset index to start at 0
    serviceRequests = serviceRequests.dropna().reset_index(drop = True)
    
    serviceRequests['Created Date'] = map(getMonth, serviceRequests['Created Date'])
            
    print "File successfully loaded\n"
    
    while True:
        #take user inputs
        location = inputLocation(serviceRequests)
        if location.upper() == 'QUIT':
            sys.exit('Bye')
        else:
            print 'Location to look at: ' + location + '\n'
                
            complaintType = inputType()
            print 'Complaint type to look at: ' + complaintType.upper() + '\n'
            
                
            graph = graphClass(location, complaintType, serviceRequests)
                
            if complaintType == 'all':
                dfToPlot = graph.constructDataFrameToPlotAll()
            else:
                dfToPlot = graph.constructDataFrameToPlotType()
                
            graph.plotFrequency()
            print 'graph saved\n'
        
    
    

