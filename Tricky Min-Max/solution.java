public class Puzzle {
  public static int solve(int a, int b, char symbol) {
    int c = a - b;
    int k = (c >> 31) & 1;
    int max = a - k * c;
    int min = b + k * c;
    return ('>' - symbol) / 2 * min + (symbol - '<') / 2 * max;
  }
}
