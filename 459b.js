print(function(n) {
    d = {};
    var bMin = 1E9, bMax = 1;
    readline().split(" ").map(function(v) {
        d[v] = d[v] ? d[v] + 1 : 1;
        v = Number(v);
        if (v < bMin)
            bMin = v
        if (v > bMax)
            bMax = v
    });
    return [bMax - bMin, bMin == bMax ? n * (n - 1) / 2
            : d[bMin] * d[bMax]].join(" ");
}.apply(null, readline().split(" ").map(Number)));
