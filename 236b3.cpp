#include <iostream>
#include <vector>

#define MAX 1000001

void gen_primes(int n, std::vector<int> &primes) {
    if (n < 2) return;
    primes.push_back(2);
    if (n < 3) return;
    int buf[MAX] = {0, 0, 1};
    n++;
    for (int i = 3; i < n; i += 2) {
        if (buf[i] == 0) {
            primes.push_back(i);
            for (int j = 2 * i; j < n; j += i) {
                buf[j] = 1;
            }
        }
    }
}
int count_divisor(int n, std::vector<int> primes) {
    int ret = 1;
    for (std::vector<int>::iterator it = primes.begin(); it < primes.end(); it++) {
        if (n < *it) break;
        int cnt = 1;
        while (!(n % *it)) {
            cnt++;
            n /= *it;
        }
        ret *= cnt;
    }
    return ret;
}
int main(int argc, char ** argv) {
    std::vector<int> primes;
    gen_primes(100, primes);
    int a, b, c, ans = 0;
    std::cin >> a >> b >> c;
    a++; b++; c++;
    int buf[MAX] = {0, 1};
    for (int i = 1; i < a; i++) {
        for (int j = 1; j < b; j++) {
            for (int k = 1; k < c; k++) {
                int prdct = i * j * k;
                if (buf[prdct] == 0 and prdct > 1) {
                    buf[prdct] = count_divisor(prdct, primes);
                }
                ans += buf[prdct];
            }
        }
    }
    std::cout << ans << std::endl;
    return 0;
}
