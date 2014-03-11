#include <iostream>

#define MAX 1000001

using namespace std;

int main(int argc, char ** argv) {
    int a, b, c, ans = 0;
    int D[MAX] = {0};
    for (int i = 1; i < MAX; i++) {
        for (int j = i; j < MAX; j += i) {
            D[j]++;
        }
    }
    cin >> a >> b >> c;
    for (int i = 1; i < a + 1; i++) {
        for (int j = 1; j < b + 1; j++) {
            for (int k = 1; k < c + 1; k++) {
                ans += D[i*j*k];
            }
        }
    }
    cout << ans << endl;
    return 0;
}
