/*
 * Shamith Louis Saldanha
 * */

/*
 * Function definition for functions in swing_function.h
 * */

#include "swing_functions.h"

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <stdbool.h>

/*
 * searchContinuityAboveValue:
 * 
 * Naive implementation
 * 
 * Function to traverse a single data column.
 * Returns an index in which the data is above a threshold,
 *  for win_length values.
 * Requires that data array pointer not point to null
 * Works correctly only if beginning index and ending index not point beyond the array length
 * Works well if only index_end be either equal to or greater than index_beginning
 * 
 * Function is not complete
 * */
index_t searchContinuityAboveValue(
    data_t* data,
    index_t index_begin,
    index_t index_end,
    data_t threshold,
    index_t win_length
)
{
    assert(data != NULL);
    
    index_t i = 0;
    index_t start = -1;
    index_t end = -1;
    
    for (i = index_begin; i <= index_end ; i++)
    {
        // Remaining length not enough for win_length
        if (i > (index_end + win_length))
        {
            break;
        }
        // CHecking if first element in win_length size is above threshold
        // Then will check for other elements
        if (data[i] > threshold)
        {
            start = i;
            end = start + win_length;
            if (if_all_above_threshold(data, threshold, start, end))
            {
                return start;
            }
        }
    }
    return start;
}

/*
 * Helper function
 * Checks to see if all array elements are above threshold*/
bool if_all_above_threshold(data_t *data, data_t threshold, index_t start, index_t end)
{
    index_t i = 0;
    for (i = start; i < end ; i++)
    {
        if(data[i] < threshold)
        {
            return false;
        }
    }
    // by this point, all data in array are greater than threshold
    return true;
}