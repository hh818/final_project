'''
Created on May 5, 2015

@author: Ho Huang
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class graphClass():
    def __init__(self, location, complaintType, df):
        self.location = location
        self.complaintType = complaintType
        self.df = df
        
    def constructDataFrameToPlotAll(self):
        '''construct a dataframe for plotting when complaint type is all'''
        if self.location.replace(' ', '').isalpha() == True:
            if self.location == 'ALL':
                grouped = self.df.groupby('Complaint Type')
                self.dfToPlot = pd.DataFrame()
                for complaintType, group in grouped:
                    self.dfToPlot[complaintType] = group['Created Date'].value_counts()
            else:
                mask = self.df['Borough'] == self.location
                self.df = self.df[mask]
                grouped = self.df.groupby('Complaint Type')
                self.dfToPlot = pd.DataFrame()
                for complaintType, group in grouped:
                    self.dfToPlot[complaintType] = group['Created Date'].value_counts()
                        
        if self.location.isdigit() == True:
            mask = self.df['Incident Zip'] == self.location
            self.df = self.df[mask]
            grouped = self.df.groupby('Complaint Type')
            self.dfToPlot = pd.DataFrame()
            for complaintType, group in grouped:
                self.dfToPlot[complaintType] = group['Created Date'].value_counts()
        
        return self.dfToPlot.sort_index(inplace=True)
    
    def constructDataFrameToPlotType(self):
        '''construct dataframe fo plotting when complaint type is specified'''
        if self.location.replace(' ', '').isalpha() == True:
            if self.location == 'ALL':
                grouped = self.df.groupby('Complaint Type')
                self.dfToPlot = pd.DataFrame()
                self.dfToPlot[self.complaintType] = grouped.get_group(self.complaintType)['Created Date'].value_counts()
            else:
                mask = self.df['Borough'] == self.location
                self.df = self.df[mask]
                grouped = self.df.groupby('Complaint Type')
                self.dfToPlot = pd.DataFrame()
                self.dfToPlot[self.complaintType] = grouped.get_group(self.complaintType)['Created Date'].value_counts()
                        
        if self.location.isdigit() == True:
            mask = self.df['Incident Zip'] == self.location
            self.df = self.df[mask]
            grouped = self.df.groupby('Complaint Type')
            self.dfToPlot = pd.DataFrame()
            self.dfToPlot[self.complaintType] = grouped.get_group(self.complaintType)['Created Date'].value_counts()
                    
        return self.dfToPlot.sort_index(inplace=True)
            
        
    def plotFrequency(self):
        '''plot the frequency trend over month with the dataframe constructed'''
        self.dfToPlot.plot(xticks = self.dfToPlot.index)
        plt.title('Number of complaints in ' + self.location + '\nComplaint type: ' + self.complaintType.lower())
        plt.xlabel('Month')
        plt.ylabel('Number of Complaints')
        plt.savefig(self.complaintType + '_complaints_' + self.location + '.pdf')
        plt.clf()
        
        
