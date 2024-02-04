#include <iostream>
#include <cmath>

long long int compare_(long long int a, long long int b1, long long int b2);

using namespace std;

int main() {
    int people, capacity;
    cin >> people >> capacity;
    long long int a[people], DP[people + 1][capacity + 1][2];
    for (int i = 0; i < people; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < capacity + 1; i++) {
        DP[1][i][0] = 0;
        DP[1][i][1] = 0;
    }
    for (int i = 1; i < people + 1; i++) {
        for (int j = 0; j < capacity + 1; j++) {
            if (i == j) DP[i][j][0] = 9999999999;
            if (i < j + 1) {
                DP[i][j][1] = 9999999999;
                DP[i][j][0] = 9999999999;
            }

            if (j == 0) DP[i][j][0] = 9999999999;
            if (i == j) DP[i][j][1] = 9999999999;

            if (i > capacity + j) {
                DP[i][j][0] = 9999999999;
                DP[i][j][1] = 9999999999;
            }
        }
    }

    for (int i = 1; i < people + 1; i++) {
        for (int j = 0; j < capacity + 1; j++) {
            if (DP[i][j][1] != 9999999999 && i != 1) DP[i][j][1] = compare_(DP[i - 1][j][1], DP[i - 1][j][0], a[i - 1]);
            if (DP[i][j][0] != 9999999999 && i != 1)
                DP[i][j][0] = compare_(DP[i - 1][j - 1][0], DP[i - 1][j - 1][1], a[i - 1]);
//            cout << i << " " << j << " " << 0 << " " << DP[i][j][0] << endl;
//            cout << i << " " << j << " " << 1 << " " << DP[i][j][1] << endl;
        }
    }
    int res = 9999999999;
//    cout << "****************************************" << endl;
    for (int i = 0; i < capacity + 1; ++i) {
//        cout << people - 1 << " " << i << " " << 0 << " " << DP[people - 1][i][0] << endl;
//        cout << people - 1 << " " << i << " " << 1 << " " << DP[people - 1][i][1] << endl;
        res = res > DP[people][i][0] ? DP[people][i][0] : res;
        res = res > DP[people][i][1] ? DP[people][i][1] : res;
    }
    cout << res;
}


long long int compare_(long long int a, long long int b1, long long int b2) {
    if (b1 == 9999999999) return a;
    if (a == 9999999999) return b1 + b2;
    return a > (b1 + b2) ? (b1 + b2) : a;
}
