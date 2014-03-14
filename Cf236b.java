import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Cf236b {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        solver.solve(1, in, out);
        out.close();
    }
}

class TaskA {
    static final int MAX = 1000001;

    private List<Integer> generatePrimes(int n) {
        List<Integer> primes = new ArrayList<Integer>();
        if (n < 2) return primes;
        primes.add(2);
        if (n < 3) return primes;
        int[] buffer = new int[MAX];
        buffer[2] = 1;
        n++;
        for (int i = 3; i < n; i += 2) {
            if (buffer[i] == 0) {
                primes.add(i);
                for (int j = i * 2; j < n; j += i) {
                    buffer[j] = 1;
                }
            }
        }
        return primes;
    }

    private int countDivisor(int n, List<Integer> primes) {
        int res = 1;
        for (int p : primes) {
            if (n < p) break;
            int counter = 1;
            while (n % p == 0) {
                counter++;
                n /= p;
            }
            res *= counter;
        }
        return res;
    }

    public void solve(int testNumber, InputReader in, PrintWriter out) {
        List<Integer> primes = generatePrimes(100);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int res = 0;
        int[] buffer = new int[MAX];

        buffer[1] = 1;

        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= b; j++) {
                for (int k = 1; k <= c; k++) {
                    int product = i * j * k;
                    if (buffer[product] == 0 && product > 1) {
                        buffer[product] = countDivisor(product, primes);
                    }
                    res += buffer[product];
                }
            }
        }

        out.println(res);
    }
}

class InputReader {
    private BufferedReader reader;
    private StringTokenizer tokenizer;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
        tokenizer = null;
    }

    public String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }
}
