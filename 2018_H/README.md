__Problem A:__
https://codejam.withgoogle.com/codejam/contest/3324486/dashboard \
Without any forbidden prefixes, there are 2^N sequences.\
1 forbidden prefix of length k will removes 2^(N-k) sequences. However, if we simply subtracting the removed sequences for each forbidden prefix, there might be overlap. E.g any sequence with prefix RBRBB also has prefix RBR, and thus RBRBB is "redundant". The solution is to not consider any forbidden prefix that starts with another forbidden prefixes. This can be done in O(Np^2) time, which is sufficient for the problem. A prefix tree can cut this down to O(Np).
After all "redundant" prefixes have been discarded, we simply subtract 2^(N-k) from the total number of sequences for each prefix of length k.
