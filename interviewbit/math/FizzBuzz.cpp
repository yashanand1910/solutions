vector<string> Solution::fizzBuzz(int A) {
    vector<string> output;
    
    for (int i = 1; i <= A; i++) {
        if (i % 3 == 0 && i % 5 != 0) {
            output.push_back("Fizz");
        }
        else if (i % 5 == 0 && i % 3 != 0) {
            output.push_back("Buzz");
        }
        else if (i % 15 == 0) {
            output.push_back("FizzBuzz");
        }
        else {
            output.push_back(to_string(i));
        }
    }
    
    return output;
}
