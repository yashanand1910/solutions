string Solution::findDigitsInBinary(int A) {
    string binForm = "";
    
    if (A == 0) {
        return "0";
    }
    
    int temp = A;
    while ( temp > 0 ) {
        binForm = to_string(temp % 2) + binForm;
        temp /= 2;
    }
    
    return binForm;
}