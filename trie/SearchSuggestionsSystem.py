"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]


Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 10^4
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
"""
from typing import List


class SearchSuggestionsSystem:
    #For trie idea, see the Jave algorithm
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort();
        fromto = [0, len(products)]
        ans = []

        def suggestion(idx: int):
            eachwords = []
            newstart, k = -1, fromto[0]
            while k < fromto[1]:
                if idx < len(products[k]) and products[k][idx] == searchWord[idx]:
                    if newstart == -1:
                        newstart = k
                    if len(eachwords) < 3:
                        eachwords.append(products[k])
                else:
                    if newstart != -1:
                        break
                k += 1
            ans.append(eachwords)
            if newstart == -1:
                newstart = k
            fromto[0] = newstart
            fromto[1] = k

            return

        for i in range(len(searchWord)):
            suggestion(i)

        return ans
