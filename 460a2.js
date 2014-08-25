print(function(n, m) {
    return ~~((n * m - 1) / (m - 1));
}.apply(null, readline().split(' ').map(Number)));
