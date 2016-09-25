#include <iostream>
using namespace std;

int main()
{
	int s, v1, v2;

	cin >> s >> v1 >> v2;
		int t1 = (s/v1)*v1;
		while (t1 >= 0 && (s-t1)%v2 != 0)
			t1 -= v1;
		if (t1 >= 0)
			cout << t1/v1 << ' ' << (s-t1)/v2 << endl;
		else if (s%v2 == 0)
			cout << 0 << ' ' << s/v2 << endl;
		else
			cout << "Impossible" << endl;
return 0;
}
