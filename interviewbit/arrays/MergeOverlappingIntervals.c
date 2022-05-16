/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 * };
 *
 * typedef struct Interval interval;
 */
/*
 * intervals : the array of interval
 * sz : number of entries in intervals
 * len : populate the length of returned array of intervals in len
 */
int min (int a, int b) {
    if (a < b) return a;
    return b;
}
int max (int a, int b) {
    if (a > b) return a;
    return b;
} 
int compareIntervals(const void* a, const void* b) {
    interval value1 = *((interval *)a);
    interval value2 = *((interval *)b);
    if (value1.start > value2.start) {
        return 1;
    }
    return 0;
}

interval* merge(interval *intervals, int sz, int *len) {
    *len = sz;
    
    qsort(intervals, sz, sizeof(interval), compareIntervals);
    
    interval* stack = (interval*)malloc(*len * sizeof(interval));
    int stackTop = -1;
    
    stack[++stackTop] = intervals[0];
    intervals += 1;
    *len -= 1;
    
    while (*len > 0) {
        if (stack[stackTop].end >= intervals[0].start) {
            stack[stackTop].start = min(stack[stackTop].start, intervals[0].start);
            stack[stackTop].end = max(stack[stackTop].end, intervals[0].end);
        } else {
            stack[++stackTop] = intervals[0];
        }
        intervals += 1;
        *len -= 1;
    }
    
    *len = stackTop + 1;
    return stack;
}
