#include <stdio.h>

#define MAX 1000001

int main(int argc, char ** argv) {
    int a, b, c, i, j, k, ans = 0;
    static int D[MAX];
    for (i = 1; i < MAX; i++) {
        for (j = i; j < MAX; j += i) {
            D[j]++;
        }
    }
    scanf("%d%d%d", &a, &b, &c);
    for (i = 1; i < a + 1; i++) {
        for (j = 1; j < b + 1; j++) {
            for (k = 1; k < c + 1; k++) {
                ans += D[i*j*k];
            }
        }
    }
    printf("%d\n", ans % (1 << 31));
    return 0;
}
