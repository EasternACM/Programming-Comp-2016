#include <iostream>

using namespace std;


bool Solve(int s, int v1, int v2, int& v1_taken, int& v2_taken){
  int i = 0;
  v1_taken = s;
  v2_taken = s;
  bool found_answer = false;
  while(i*v1 <= s){
    int temp_s = s-i*v1;
    if(temp_s % v2 == 0){
      int j = temp_s / v2;
      found_answer = true;
      if(i+j < v1_taken + v2_taken){
	v1_taken = i;
	v2_taken = j;
      }
    }
    i++;
  }
  return found_answer;
}

int main(){
  int s, v1, v2;
  cin >> s >> v1 >> v2;
    int v1_taken, v2_taken;
    if(Solve(s,v1, v2, v1_taken, v2_taken))
      cout << v1_taken << " " << v2_taken << endl;
    else
      cout << "Impossible" << endl;
  return 0;
}
