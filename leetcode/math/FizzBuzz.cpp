class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        
        for (int i=0; i<n; i++) {
            string s;
            
            if (((i+1)%3) == 0) {
                s = "Fizz";
                
                if (((i+1)%5) == 0) {
                    s = "FizzBuzz";
                }
                answer.push_back(s);
                continue;

            }
            if (((i+1)%5) == 0) {
                s = "Buzz";
                
                if (((i+1)%3) == 0) {
                    s = "FizzBuzz";
                }
                answer.push_back(s);
                continue;
            }
            
            s = to_string(i+1);
            answer.push_back(s);
        }
        
        return answer;
    }
};
