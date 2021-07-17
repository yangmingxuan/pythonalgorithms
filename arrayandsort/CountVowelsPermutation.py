"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
Output: 68


Constraints:

1 <= n <= 2 * 10^4
"""

class CountVowelsPermutation:
    """
     * Explanation: aDP[i] 表示以a为首长度为i+1有几个字符串，eDP,iDP等也相同；
     *      a元音之后只能跟随e元音，那么a首长度为i+1的字符串个数就是以e为首长度为i的字符串个数；
     *      同理，e之后只能跟a和i，那么e首长度为i+1的个数就是a为首长度为i和i为首长度为i的个数之和；
     *      以此类推，最终总的字符串就是aDP[n-1]+eDP[n-1]+iDP[n-1]+oDP[n-1]+uDP[n-1].
     * Explanation: aDP[i] indicates the number of strings starting with a and having a length of i+1, eDP, iDP, etc. are also the same;
     *     A vowel can only be followed by e, then the number of strings with length i+1 at the beginning of a is the number of strings with length i at the beginning of e;
     *     In the same way, e can only be followed by a and i, then the number of e with length i+1 is the sum of the number with a leading length of i and i leading with length i;
     *     By analogy, the final total string is aDP[n-1]+eDP[n-1]+iDP[n-1]+oDP[n-1]+uDP[n-1].
    """
    def countVowelPermutation(self, n: int) -> int:
        modulo = 1000000007
        adp,edp,idp,odp,udp = [0] * n,[0] * n,[0] * n,[0] * n,[0] * n
        adp[0] = edp[0] = idp[0] = odp[0] = udp[0] = 1

        for i in range(1, n):
            #Each vowel 'a' may only be followed by an 'e'.
            #So, the number of strings with length i+1 at the beginning of a is the number of strings with length i at the beginning of e
            adp[i] = edp[i-1]

            #Each vowel 'e' may only be followed by an 'a' or an 'i'
            edp[i] = (adp[i - 1] + idp[i - 1]) % modulo

            #Each vowel 'i' may not be followed by another 'i'
            idp[i] = (adp[i - 1] + edp[i - 1] + odp[i - 1] + udp[i - 1]) % modulo

            #Each vowel 'o' may only be followed by an 'i' or a 'u'.
            odp[i] = (idp[i - 1] + udp[i - 1]) % modulo

            #Each vowel 'u' may only be followed by an 'a'
            udp[i] = adp[i - 1]

        return (adp[n-1] + edp[n-1] + idp[n-1] + odp[n-1] + udp[n-1]) % modulo

cvp = CountVowelsPermutation()
ans = cvp.countVowelPermutation(2)

