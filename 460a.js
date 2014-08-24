print(function(n, m) {
    ans = n
    while (n >= m) {
        var q = ~~(n / m);
        ans += q;
        n = q + n % m;
    }
    return ans;
}.apply(null, readline().split(' ').map(Number)));
