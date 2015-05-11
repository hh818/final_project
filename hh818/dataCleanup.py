'''
Created on Apr 30, 2015

@author: Ho Huang(hh818)
'''
import pandas as pd
import numpy as np
from datetime import datetime

def lowerComplaintType(series):
    '''take a series of complaint types, and convert each element to lowercase'''
    series = series.str.lower()
    return series


def changeComplaintTypeBuildingCondition(complaintType, series1, series2):
    '''categorize complaint types into five main categories, return a new series of complaint categories'''
    mask = series1.str.contains(complaintType)
    series2[mask] = 'building condition'
    return series2

def changeComplaintTypeNoise(complaintType, series1, series2):
    '''categorize complaint types into five main categories, return a new series of complaint categories'''
    mask = series1.str.contains(complaintType)
    series2[mask] = 'noise'
    return series2

def changeComplaintTypeStreetCondition(complaintType, series1, series2):
    '''categorize complaint types into five main categories, return a new series of complaint categories'''
    mask = series1.str.contains(complaintType)
    series2[mask] = 'street condition'
    return series2

def changeComplaintTypeSanitation(complaintType, series1, series2):
    '''categorize complaint types into five main categories, return a new series of complaint categories'''
    mask = series1.str.contains(complaintType)
    series2[mask] = 'sanitation'
    return series2
                
def makeComplaintCatList():
    '''make a list of lists of which complaint type belong to which complaint category'''
    building = ['building', 'water', 'sewer', 'paint', 'heat', 'radioactive', 'electric', 'fire', 'plumbing', 'sewage', 'maintenance', 'door', 'floor', 'elevator', 'lead', 'appliance', 'window', 'scrie']
    noise = ['noise', 'construction', 'drinking']
    street = ['street', 'parking', 'vehicle', 'bike', 'driveway', 'bus', 'tree', 'derelict', 'parking', 'graffiti', 'sign', 'sidewalk', 'snow', 'traffic', 'muni', 'taxi', 'litter', 'panhand', 'phone', 'safety', 'scaffold']
    sanitation = ['health', 'dirty', 'food', 'poison', 'recycl', 'rodent', 'sanita', 'animal', 'pigeon', 'smoking', 'sweep', 'dog', 'urinat', 'toilet']
    
    return building, noise, street, sanitation

def getMonth(dt):
    '''pass in a series of dates and return a series of just months'''
    dt = datetime.strptime(dt[:-3], '%m/%d/%Y %H:%M:%S').month
    return dt