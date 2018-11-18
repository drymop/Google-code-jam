__Problem A:__
https://codejam.withgoogle.com/codejam/contest/3324486/dashboard \
Without any forbidden prefixes, there are 2^N sequences. Each forbidden prefix of length k will removes 2^(N-k) sequences.\
However, if we simply subtracting the removed sequences for each forbidden prefix, there might be overlap. E.g any sequence with prefix RBRBB also has prefix RBR, and thus RBRBB is "redundant". The solution is to not consider any forbidden prefix that starts with another forbidden prefixes. This can be done in O(Np^2) time, which is sufficient for the problem. A prefix tree can cut this down to O(Np).\
After all "redundant" prefixes have been discarded, we simply subtract 2^(N-k) from the total number of sequences for each prefix of length k.\

__Problem B:__
https://codejam.withgoogle.com/codejam/contest/3324486/dashboard#s=p1 \
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
Now, wall 1 collapses, but Thanh has time to paint 2.
