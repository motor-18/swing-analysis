# swing-analysis
An small project to obtain higher level information from data generated from a swing. The information obtained here can be used by itself or for even higher level insights.

# Important dates
Started November 2019

# Requirements to use
- Python 2.7 Linux
- Ubuntu 18.04 Bionic

# Function commonalities
- It is assumed that the index is an integer greater than or equal to zero.

- Hence, there is a return value of either a positive or 0 value, which relates to index; or a negative value which relates to a possible error.

- There is error-checking for various errors in each function.

- It is assumed that the value sent as "data" is a single dimensional array; If not, the out-of-bounds error checking will kick-in.

- Unit testing of each function has been done, using different simple test cases. This is by no means complete, nor is it a formal verification.


# Error constants used
Currently, there are 4 constants used for denoting different types of errors.
They are:

1. ERROR_TOO_SMALL = -1
This constant is returned when the index begin and end are too small versus the length of continuity required.

2. ERROR_NO_DATA = -2
This constant is returned when at least one of the data is missing (None in Python)

3. ERROR_NOT_FOUND = -3
This constant is returned when there are no problems otherwise, but no suitable answer as been found

4. ERROR_OUT_OF_BOUNDS = -4
This constant is returned when there is a data access which is out of bounds


# Data Structure Used - in C, not in Python
The project was initially started in C, and then moved to Python early on.
Hence, the data structures were initially made in C.
For reasons of history, the C file of the data structures and function definitions are being kept.

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

# Future Work
- To possibly combine the commonality of each function - sliding window, among other things - into one function.
- To make functions more modular and more amenable to future modification/upgrades
