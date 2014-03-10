#include <math.h>
#include <stdio.h>

#define MAX 1000001

int main(int argc, char ** argv) {
    int a, b, c, i, j, k, ans = 0;
    scanf("%d%d%d", &a, &b, &c);
    static int D[MAX] = {1, 1};
    for (i = 1; i < a + 1; i++) {
        for (j = 1; j < b + 1; j++) {
            for (k = 1; k < c + 1; k++) {
                int l = i * j * k;
                if (!D[l]) {
                    long double sqi = sqrtl(l);
                    int m, sum = 0;
                    for (m = 2; m < (int) sqi + 1; m++) {
                        if (!(l % m)) {
                            if (sqi == m) {
                                sum++;
                                continue;
                            }
                            sum += 2;
                        }
                    }
                    D[l] = sum + 2;
                }
                ans += D[l];
            }
        }
    }
    printf("%d\n", ans % (1 << 31));
    return 0;
}
