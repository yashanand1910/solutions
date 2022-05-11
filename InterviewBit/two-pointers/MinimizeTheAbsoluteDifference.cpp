int maxIndex (vector<int> &a) {
    int index = -1, max = INT_MIN;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] > max) {
            max = a[i];
            index = i;
        }
    }
    return index;
}

int Solution::solve(vector<int> &A, vector<int> &B, vector<int> &C) {
    vector<int> maxTriplet; int range;
    int i = A.size() - 1, j = B.size() - 1, k = C.size() - 1;
    
    maxTriplet.push_back(A[i]);
    maxTriplet.push_back(B[j]);
    maxTriplet.push_back(C[k]);
    range = abs(max(maxTriplet[0], max(maxTriplet[1], maxTriplet[2])) - min(maxTriplet[0], min(maxTriplet[1], maxTriplet[2])));
    while (i >= 0 && j >= 0 && k >= 0) {
        if (maxIndex(maxTriplet) == 0) {
            maxTriplet[0] = A[--i];
        } else if (maxIndex(maxTriplet) == 1) {
            maxTriplet[1] = B[--j];
        } else {
            maxTriplet[2] = C[--k];
        }
        range = min (range, abs(max(maxTriplet[0], max(maxTriplet[1], maxTriplet[2])) - min(maxTriplet[0], min(maxTriplet[1], maxTriplet[2]))));
    }
    
    return range;
}