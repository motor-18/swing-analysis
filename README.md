# swing-analysis
An small project to obtain higher level information from data generated from a swing. The information obtained here can be used by itself or for even higher level insights.

# Credits
Thanks to Diamond Kinetics of Pittsburgh PA.

# Important dates
Started November 2019

# Tech used
Standard C libraries in 64 bit Linux
Developed on Ubuntu 18 Bionic

# Requirements to use
Standard C libraries in Linux
Ubuntu 18 Bionic

# Data Structure Used
The datastructure contains pointers (to arrays) to the following items:
1. Index
(integer or variant thereof)
2. Timestamp
(integer or variant thereof)
3. Values for accelerometer data each for X, Y, Z axes - 3 total
(floating point or variant thereof)
4. Values for gyroscope data each about X, Y, Z axes - 3 total
(floating point or variant thereof)

The functions present here are to operate on a single (or two) datasets. Hence, the data structure is actually simply a list of pointers to all the elements. All elements in this datastructure are pointers in the array sense.