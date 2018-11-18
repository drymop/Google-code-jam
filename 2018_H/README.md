__OK so turn out I pretty much just repeated the [Contest analysis](https://codejam.withgoogle.com/codejam/contest/3324486/dashboard#s=a), not sure if that's a good thing or not.__

## [Problem A](https://codejam.withgoogle.com/codejam/contest/3324486/dashboard):
Without any forbidden prefixes, there are 2^N sequences. Each forbidden prefix of length k will removes 2^(N-k) sequences.\
However, if we simply subtracting the removed sequences for each forbidden prefix, there might be overlap. E.g any sequence with prefix RBRBB also has prefix RBR, and thus RBRBB is "redundant". The solution is to not consider any forbidden prefix that starts with another forbidden prefixes. This can be done in O(Np^2) time, which is sufficient for the problem. A prefix tree can cut this down to O(Np).\
After all "redundant" prefixes have been discarded, we simply subtract 2^(N-k) from the total number of sequences for each prefix of length k.\

## [Problem B](https://codejam.withgoogle.com/codejam/contest/3324486/dashboard#s=p1):
Thanh always paint a continuos segment of ceil(N/2) walls. Thus the problem reduces to finding the maximum sum of continuous sub-array of length k, where k = ceil(N/2). This can be done in O(N) time. \
_Note_: Given any sub-array of length k = ceil(N/2), Thanh has a strategy that guarantees painting the whole sub-array. The trick is to start painting at a specific wall, such that both ends of the sub-array is closer to a painted wall than the end of the array. For example, if N = 7, and Thanh wants to paint the walls in bracket:\
_ _ [ _ _ _ _] _ \
0 1   2 3 4 5  6 \
He has to start at 4, such that if either wall 0 or 6 is destroyed, he still has time to rush to that side. Says wall 0 is destroyed:\
x _ [ _ _ o _] _ \
0 1   2 3 4 5  6 \
Thanh has to rush toward 2, before the collasp reaches. Thus Thanh paints 3. Says the next destroyed wall is 6.\
x _ [ _ o o _] x \
0 1   2 3 4 5  6 \
Thanh has to paint 5. He still has the leeway to reach 2 before the collapsing.\
x _ [ _ o o o] x \
0 1   2 3 4 5  6 \
Now, wall 1 collapses, but Thanh has time to paint 2.\

## [Problem C](https://codejam.withgoogle.com/codejam/contest/3324486/dashboard#s=p2):
### Naive algorithm (which I used the first time orz): DP
The subproblem is S(i, j), where i is the total number of people (also is number of seats on the boat), and j is the number of _newlywed couples_ (that we don't want sitting next to each other). Condition: i >= 2j. Consider choosing a person to sit in the next seat. If we choose a non-newlywed person (there are i-2j ways), the problem reduces to S(i-1, j). If we choose a person P that is newly-wed (there are 2j ways), the problem reduces to S(i-1, j-1), aka 1 less couple. But not exactly! - since the next person after this cannot be P's spouse. This elmininates S(i-2, j-1) arrangements. Thus the final recursion is:\
S(i, j) = (i-2j) * S(i-1, j-1) + 2j * S(i-1, j-1) - 2j * S(i-2, j-1)\
Now, this is O(nm), which is good enough for the small problem. However, the large problem has n = m = 100000, so this is not good enough.\

### Combinatoric algorithm
I then (belatedly) relized that _simple combinatoric_ is the key! Let n be the total number of people, and m be the number of newlywed couples. Without constraints, there are n! (n factorial) arrangements. However, those includes arrangement where a couple sits next to each other. For each couple, there are 2(n-1)! arrangements where they sit next to each other. The (n-1)! part comes from considering the couple as 1 person, and 2 comes from interchanging the couple (Aa - aA). Since there are m couples, the # of arrangements should be n! - m*2(n-1)!\
But we now undercount things, as all cases of __2__ couples (says Aa and Bb) are counted twice (1 for Aa and 1 for Bb). We need to _add_ those cases back. Now we have:\
n! - m*2*(n-1)! + (mC2)*2^2*(n-2)!\
Where mC2 (m choose 2) comes from choosing 2 couples, 2^2 comes from interchanging the 2 people in each couple, and (n-2)! comes from the number of arrangement if we consider each of the 2 couples as just 1 person.\
All cases of __3__ couples are now counted twice, so we have to subtract them. Then we needs to add all cases of 4 couples, substract all cases of 5 couples, and so on, according to the _Inclusion-Exclusion Principle_.\ 
The final number of arrangements looks like this:\
n! - mC1 * 2^1 * (n-1)! + mC2 * 2^2 * (n-2)! - ... + (-1)^k * mCk * 2^k * (n-k)! + ... \
for k ranges from 0 to m.
