import numpy as np
import csv

"""
searchContinuityAboveThreshold:
Function to search if all elements of a certain length are above the threshold
Checks using a "sliding window method".
Initialises the window at indexStart.
For that window, gets a count for the suitable (suitable = above threshold)
After that, move window by 1, there will be a departing and incoming element
check departing and incoming element if above threshold.
If former, decrement by 1; if latter, increment by 1.
Check every loop in case the count matches the winLength, return the index of start
Else return None
None also returned in case of missing data, small data etc.
"""
def searchContinuityAboveThreshold(data, indexBegin, indexEnd, threshold, winLength):
    count_above_thres = 0
    if (indexEnd - indexBegin) > winLength:
        return None
    if (data is None):
        return None
    for i in range(indexBegin, indexBegin + winLength, 1):
        if (data[i] > threshold):
            count_above_thres += 1
    if (count_above_thres == winLength):
        return indexBegin
    # by this point, we need to search more
    for i in range(indexBegin + 1, indexEnd, 1):
        try:
            data[i + winLength - 1] = data[i + winLength - 1]
        except IndexError:
            return None
        if (data[i - 1] > threshold):
            count_above_thres -= 1
        if (data[i + winLength - 1] > threshold):
            count_above_thres += 1
        if (count_above_thres == winLength):
            return i
    return None

def backSearchContinuityWithinRange(data, indexBegin, indexEnd, thresholdLo, thresholdHi, winLength):
    count_within_range = 0
    if (indexBegin - indexEnd) > winLength:
        return None
    if (data is None):
        return None
    for i in range(indexBegin, indexBegin + winLength, 1):
        if ((data[i] > thresholdLo) and (data[i] < thresholdHi)):
            count_within_range += 1
    if (count_within_range == winLength):
        return indexBegin
    # by this point, we need to search more
    for i in range(indexBegin + 1, indexEnd, 1):
        try:
            data[i + winLength - 1] = data[i + winLength - 1]
        except IndexError:
            return None
        if ((data[i - 1] > thresholdLo) and (data[i - 1] < thresholdHi)):
            count_within_range -= 1
        if ((data[i + winLength - 1] > thresholdLo) and (data[i + winLength - 1] < thresholdHi)):
            count_within_range += 1
        if (count_within_range == winLength):
            return i
    return None