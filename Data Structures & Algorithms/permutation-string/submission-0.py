class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}

        # Count characters in the first window
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        matches = 0

        # Count how many characters have matching frequencies
        for c in s1Count:
            if s1Count[c] == s2Count.get(c, 0):
                matches += 1

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == len(s1Count):
                return True

            # Add s2[r]
            c = s2[r]
            s2Count[c] = s2Count.get(c, 0) + 1

            if c in s1Count:
                if s1Count[c] == s2Count[c]:
                    matches += 1
                elif s1Count[c] + 1 == s2Count[c]:
                    matches -= 1

            # Remove s2[l]
            c = s2[l]
            s2Count[c] -= 1

            if c in s1Count:
                if s1Count[c] == s2Count[c]:
                    matches += 1
                elif s1Count[c] - 1 == s2Count[c]:
                    matches -= 1

            l += 1

        return matches == len(s1Count)