import numpy as np
import csv

class errorDefinitions():
    ERROR_TOO_SMALL = -1
    ERROR_NO_DATA = -2
    ERROR_NOT_FOUND = -3
    ERROR_OUT_OF_BOUNDS = -4

errd = errorDefinitions()

"""
Sliding window method:
Common to the 4 functions below.
Two loops used.

First loop:
Initialises the window at indexStart.
For that window, gets a count for suitable values

Second loop:
After that, move window by 1, there will be a departing and incoming element
check departing and incoming element if they are suitable.
If former, decrement by 1; if latter, increment by 1.
Check every loop in case the count matches the block size, and store/return the index
"""

"""
searchContinuityAboveThreshold:
Function to search if all elements of a certain length are above the threshold
Checks using a "sliding window method".
Returns an error value if there is one.
Else returns the first index which matches criterion.
"""
def searchContinuityAboveThreshold(data, indexBegin, indexEnd, threshold, winLength):
    count_above_thres = 0

    # preliminary error checking
    if (indexEnd - indexBegin + 1) < winLength:
        return errd.ERROR_TOO_SMALL
    if (data is None):
        return errd.ERROR_NO_DATA
    
    #initial work - starting the sliding window
    for i in range(indexBegin, indexBegin + winLength, 1):
        try:
            data[i] = data[i]
        except IndexError:
            return errd.ERROR_OUT_OF_BOUNDS
        if (data[i] > threshold):
            count_above_thres += 1
    if (count_above_thres == winLength):
        return indexBegin
    
    # moving the sliding window
    for i in range(indexBegin + 1, indexEnd + 1, 1):
        try:
            data[i + winLength - 1] = data[i + winLength - 1]
        except IndexError:
            return errd.ERROR_OUT_OF_BOUNDS
        if (data[i - 1] > threshold):
            count_above_thres -= 1
        if (data[i + winLength - 1] > threshold):
            count_above_thres += 1
        if (count_above_thres == winLength):
            return i-1
    return errd.ERROR_NOT_FOUND
    #end of function


"""
backSearchContinuityWithinRange:
Function to "back-search" a window of data within a threshold
Uses sliding window technique.
Returns an error value if found.
Else returns the index value as per criterion.
"""
def backSearchContinuityWithinRange(data, indexBegin, indexEnd, thresholdLo, thresholdHi, winLength):
    count_within_range = 0

    # preliminary checking for errors
    if (indexBegin - indexEnd + 1) < winLength:
        return errd.ERROR_TOO_SMALL
    if (data is None):
        return errd.ERROR_NO_DATA

    # initial work, starting the sliding window
    for i in range(indexBegin, indexBegin - winLength, -1):
        try:
            data[i] = data[i]
        except IndexError:
            return errd.ERROR_OUT_OF_BOUNDS
        if ((data[i] > thresholdLo) and (data[i] < thresholdHi)):
            count_within_range += 1
    if (count_within_range == winLength):
        return indexBegin
    
    # moving the sliding window
    for i in range(indexBegin - 1, indexEnd -1 , -1):
        if (i - winLength + 1)<0:
            return errd.ERROR_OUT_OF_BOUNDS
        if ((data[i + 1] > thresholdLo) and (data[i + 1] < thresholdHi)):
            count_within_range -= 1
        if ((data[i - winLength + 1] > thresholdLo) and (data[i - winLength + 1] < thresholdHi)):
            count_within_range += 1
        if (count_within_range == winLength):
            return i+1
    return errd.ERROR_NOT_FOUND


"""
searchContinuityAboveValueTwoSignals:
Function to search for continuous values above threshold for two separate signals.
Uses the same sliding window technique as earlier.
Returns the index (a positive value) if found, else returns an error constant
"""
def searchContinuityAboveValueTwoSignals(
    data1, data2, indexBegin, indexEnd, threshold1, threshold2, winLength):
    
    count_above_thres_1 = 0
    count_above_thres_2 = 0

    # preliminary error checking
    if (indexEnd - indexBegin + 1) < winLength:
        return errd.ERROR_TOO_SMALL
    if ((data1 is None) or (data2 is None)):
        return errd.ERROR_NO_DATA
    
    #initial work - starting the sliding window
    for i in range(indexBegin, indexBegin + winLength, 1):
        
        try:
            data1[i] = data1[i]
            data2[i] = data2[i]
        except IndexError:
            return errd.ERROR_OUT_OF_BOUNDS
        
        if (data1[i] > threshold1):
            count_above_thres_1 += 1
        if (data2[i] > threshold2):
            count_above_thres_2 += 1
    
    if ((count_above_thres_1 == winLength) and (count_above_thres_2 == winLength)):
        return indexBegin
    
    # moving the sliding window
    for i in range(indexBegin + 1, indexEnd + 1, 1):
        
        try:
            data1[i + winLength - 1] = data1[i + winLength - 1]
            data2[i + winLength - 1] = data2[i + winLength - 1]
        except IndexError:
            return errd.ERROR_OUT_OF_BOUNDS
        
        if (data1[i - 1] > threshold1):
            count_above_thres_1 -= 1
        if (data2[i - 1] > threshold2):
            count_above_thres_2 -= 1
        
        if (data1[i + winLength - 1] > threshold1):
            count_above_thres_1 += 1
        if (data2[i + winLength - 1] > threshold2):
            count_above_thres_2 += 1
        
        if ((count_above_thres_1 == winLength) and (count_above_thres_2 == winLength)):
            return i-1
        
    return errd.ERROR_NOT_FOUND
    #end of function

"""
searchMultiContinuityWithinRange
Function that returns all indices at which there is a continuous block of data within a range
Follows the sliding window idea of previous functions as well
Returns a list of all indices that match criterion
"""
def searchMultiContinuityWithinRange(data, indexBegin, indexEnd, thresholdLo, thresholdHi, winLength):
    count_within_range = 0
    suitable_indices = []

    # preliminary error checking
    if (indexEnd - indexBegin + 1) < winLength:
        return errd.ERROR_TOO_SMALL
    if (data is None):
        return errd.ERROR_NO_DATA
    
    #initial work - starting the sliding window
    for i in range(indexBegin, indexBegin + winLength, 1):
        try:
            data[i] = data[i]
        except IndexError:
            return errd.ERROR_OUT_OF_BOUNDS
        if ((data[i] > thresholdLo) and (data[i] < thresholdHi)):
            count_within_range += 1
    if (count_within_range == winLength):
        suitable_indices.append(indexBegin)
    
    # moving the sliding window
    for i in range(indexBegin + 1, indexEnd + 1, 1):
        try:
            data[i + winLength - 1] = data[i + winLength - 1]
        except IndexError:
            return errd.ERROR_OUT_OF_BOUNDS
        if ((data[i - 1] > thresholdLo) and (data[i - 1] < thresholdHi)):
            count_within_range -= 1
        if ((data[i + winLength - 1] > thresholdLo) and (data[i + winLength - 1] < thresholdHi)):
            count_within_range += 1
        if (count_within_range == winLength):
            suitable_indices.append(i-1)
    
    return suitable_indices
    #end of function
