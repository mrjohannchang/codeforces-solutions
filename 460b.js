(function(a, b, c) {
    var count = 0;
    var answers = [];

    for (var s = 1; s <= 9 * 9; s++) {
        var x = b * Math.pow(s, a) + c;

        if (x >= 1E9)
            continue;

        var xString = x.toString();
        var sum = 0;
        for (var j = 0; j < xString.length; j++) {
            sum += Number(xString[j]);
        }

        if (s == sum) {
            count += 1;
            answers.push(x);
        }
    }

    print(count);
    if (count > 0)
        print(answers.join(' '));
}).apply(null, readline().split(' ').map(Number));
