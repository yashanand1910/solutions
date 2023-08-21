class Solution {
public:
  /**
   * Build graph for courses by filling indegrees & children maps.
   */
  void buildGraph(int numCourses, unordered_set<int> &remCourses,
                  unordered_map<int, int> &indegree,
                  unordered_map<int, vector<int>> &children,
                  vector<vector<int>> &prerequisites) {
    for (int courseNum=0; courseNum < numCourses; courseNum++) {
      remCourses.emplace(courseNum);
      indegree[courseNum] = 0;
      children[courseNum] = {};
    }

    for (auto& prereq : prerequisites) {
      int source = prereq[0];
      int target = prereq[1];
      indegree[target]++;
      children[source].emplace_back(target);
    }
  }

  bool canFinish(int numCourses, vector<vector<int>> &prerequisites) {
    unordered_set<int> remCourses;    // set of courses not taken so far
    queue<int> q;                     // queue of courses to take in order
    unordered_map<int, int> indegree; // map of in-degrees of all courses
    unordered_map<int, vector<int>> children; // map of courses to its children

    buildGraph(numCourses, remCourses, indegree, children, prerequisites);

    // push all 0 indegrees to queue
    for (int courseNum = 0; courseNum < numCourses; courseNum++) {
      if (indegree[courseNum] == 0) q.push(courseNum);
    }

    // access courses topologically
    while (q.size()) {
      int currCourse = q.front();
      q.pop();
      remCourses.erase(currCourse);

      // update children
      for (auto& child : children[currCourse]) {
        int degree = --indegree[child];
        if (degree == 0) q.push(child);
      }
    }

    // check if any courses remain
    if (remCourses.size()) return false;
    else return true;
  }
};
