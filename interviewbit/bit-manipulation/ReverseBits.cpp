unsigned int Solution::reverse(unsigned int A) {
    int i = 0; unsigned int output = 0;
    
    while (A > 0) { // Run loop for all significant bits of A
        output += (A % 2) * pow(2, 31 - i); // Using remainders to convert binary directly to decimal of its reverse (ith bit => n - ith bit)
        A /= 2; // Move to next significant bit
        i++;
    }
    
    return output;
}
