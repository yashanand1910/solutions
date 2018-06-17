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
 * newInterval : new Interval to be inserted
 * len : populate the length of returned array of intervals in len
 */
int max (int a, int b) {
    if (a > b) return a;
    return b;
}
int min (int a, int b) {
    if (a < b) return a;
    return b;
}
 
interval* insert(interval *intervals, int sz, interval newInterval, int *len) {
    interval* stack = (interval*)malloc(*len * sizeof(interval));
    int stackTop = -1;
    
    *len = sz;
    if (*len==0) {
        *len = 1;
        stack[++stackTop] = newInterval;
        return stack;
    }
    
    int i, pos = 1000;
    for (i = 0; i < sz; i++) {
        if (newInterval.start > intervals[i].start) {
            stack[i] = intervals[i];
            stackTop++;
            *len -= 1;
        } else {
            pos = i - 1;
            break;
        }
    }
    
    if (pos < 0) {
        stack[0] = newInterval;
        stackTop++;
    } else {
        intervals[pos] = newInterval;
        intervals += pos;
        *len += 1;
    }
    if (pos == 1000) {
        intervals[0] = newInterval;
        *len = 1;
    }
    
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
