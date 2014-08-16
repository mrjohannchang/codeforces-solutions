print(function(x1, y1, x2, y2) {
    if (x1 != x2 && y1 != y2) {
        if (Math.abs(x1 - x2) != Math.abs(y1 - y2)) {
            return -1;
        } else {
            return [x1, y2, x2, y1].join(" ");
        }
    } else {
        return [
            x1 == x2 ? x1 + Math.abs(y1 - y2) : x1,
            y1 == y2 ? y1 + Math.abs(x1 - x2) : y1,
            x1 == x2 ? x1 + Math.abs(y1 - y2) : x2,
            y1 == y2 ? y1 + Math.abs(x1 - x2) : y2,
        ].join(" ");
    }
}.apply(null, readline().split(" ").map(Number)));
