print(function(n, m, a) {
    return ~~((n + a - 1) / a) * ~~((m + a - 1) / a);
}.apply(null, readline().split(" ").map(Number)));
