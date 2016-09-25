#include <iostream>

using namespace std;

int main(void) {
  int s,v1,v2;

  cin >> s >> v1 >> v2;
  if (!cin)
    return 1;

  // s, v1 and v2 between 1 and 1000000
  if (s < 1 || s > 1000000)
    return 2;
  if (v1 < 1 || v1 > 1000000)
    return 3;
  if (v2 < 1 || v2 > 1000000)
    return 4;
  // v1 > v2
  if (v1 <= v2)
    return 5;

  // we win!
  return 42;
}

