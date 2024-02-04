#include <iostream>

using namespace std;

unsigned long long balancing(unsigned long long inp) {
    unsigned long long pow = 1000000009 - 2;
    unsigned long long res = 1;
    while (1) {
        if (pow == 0) break;
        if (pow % 2) res = (res * inp) % 1000000009;
        inp = (inp * inp) % 1000000009;
        pow /= 2;
    }
    return res;
}

void preprocess(const string &input,
                unsigned long long powers[],
                unsigned long long prefix[],
                unsigned long long suffix[]) {

    powers[0] = 11;
//    cout << powers[0] << " ";
    for (int i = 1; i < input.length(); i++) {
        powers[i] = (powers[i - 1] * 11) % 1000000009;
//        cout << powers[i] << " ";
    }
//    cout << endl;

    prefix[0] = input[0];
//    cout << prefix[0] << " ";
    for (int i = 1; i < input.length(); i++) {
        prefix[i] = (prefix[i - 1] + (input[i - 1] * powers[i - 1]) % 1000000009) % 1000000009;
//        cout << prefix[i] << " ";

    }
//    cout << endl;

    suffix[0] = input[input.length() - 1];
//    cout << suffix[0] << " ";
    for (int i = 1; i < input.length(); i++) {
        suffix[i] = (suffix[i - 1] + (input[input.length() - i] * powers[i - 1]) % 1000000009) % 1000000009;
//        cout << suffix[i] << " ";
    }
//    cout << endl;
}


int calculate(int start, int end, int len,
              unsigned long long powers[],
              unsigned long long prefix[],
              unsigned long long suffix[]) {

    int count = 0;
    while (1) {
        if (start > end) break;
        unsigned long long forward =
                (prefix[end] - prefix[start] + 1000000009) % 1000000009 * balancing(powers[start]) % 1000000009;
        unsigned long long backward =
                (suffix[len - 1 - start] - suffix[len - end - 1] + 1000000009) % 1000000009 *
                balancing(powers[len - end - 1]) % 1000000009;
//        cout << forward << endl;
//        cout << backward << endl;
        if (forward == backward) {
            count++;
            if (start == end) break;
            end = start + (end - start + 1) / 2 - 1;
//            cout << start << endl;
//            cout << end << endl;
        } else {
            break;
        }
    }
    return count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int count;
    string input;
    cin >> input >> count;

    unsigned long long powers[input.length()];
    unsigned long long prefix[input.length()];
    unsigned long long suffix[input.length()];

    preprocess(input, powers, prefix, suffix);

    int s, e;
    for (int i = 0; i < count; ++i) {
        cin >> s >> e;
        cout << calculate(s - 1, e - 1, input.length(), powers, prefix, suffix) << endl;
    }

    return 0;
}