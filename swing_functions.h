/*
 * Shamith Louis Saldanha
 * */

/*
 * Program to store the declarations of functions and data structures
 * */


#ifndef SWING_FNS_H
#define SWING_FNS_H

typedef long index_t;
typedef long time_t;
typedef double data_t;

typedef struct swing_data_struct
{
    index_t *index;
    time_t *timestamp;
    data_t *acc_x;
    data_t *acc_y;
    data_t *acc_z;
    data_t *gyro_x;
    data_t *gyro_y;
    data_t *gyro_z;
} swing_t;

index_t searchContinuityAboveValue(
    data_t*, 
    index_t, 
    index_t, 
    data_t, 
    index_t);

index_t backSearchContinuityWithinRange(
    data_t*, 
    index_t, 
    index_t, 
    data_t, 
    data_t, 
    index_t);

index_t searchContinuityAboveValueTwoSignals(
    data_t*, 
    data_t*, 
    index_t, 
    index_t, 
    data_t, 
    data_t, 
    index_t);

index_t searchMultiContinuityWithinRange(
    data_t*, 
    data_t*, 
    index_t, 
    index_t, 
    data_t, 
    data_t, 
    index_t);

#endif