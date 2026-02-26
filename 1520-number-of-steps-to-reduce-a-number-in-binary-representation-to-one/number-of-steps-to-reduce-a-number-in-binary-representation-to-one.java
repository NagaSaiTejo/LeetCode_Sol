import java.math.BigInteger;
class Solution {
    public int numSteps(String s) {
          BigInteger ss = new BigInteger(s, 2);
        int c = 0;
        while (!ss.equals(BigInteger.ONE)) {
            if (ss.mod(BigInteger.valueOf(2)).equals(BigInteger.ONE)) {
                ss = ss.add(BigInteger.ONE);
            } else {
                ss = ss.divide(BigInteger.valueOf(2));
            }
            c++;
        }
        return c;
    }
}