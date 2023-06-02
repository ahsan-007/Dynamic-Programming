# https://leetcode.com/problems/detonate-the-maximum-bombs/

from typing import List
import math


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        info = self.getBombDetonationInfo(bombs)
        max_detonated_bombs = 0
        for bomb in info:
            detonated_bombs = set()
            self.getDetonatedBombs(info, bomb, detonated_bombs)
            max_detonated_bombs = max(
                max_detonated_bombs, len(detonated_bombs))
        return max_detonated_bombs

    def getDetonatedBombs(self, info, bomb, detonated_bombs):
        if bomb in detonated_bombs:
            return
        detonated_bombs.add(bomb)
        for b in info[bomb]:
            self.getDetonatedBombs(info, b, detonated_bombs)

    def getBombDetonationInfo(self, bombs):
        range = {}
        for d_index, detonated_bomb in enumerate(bombs):
            range[d_index] = set()
            for b_index, bomb in enumerate(bombs):
                if d_index != b_index and self.isBombInRange(detonated_bomb, bomb):
                    range[d_index].add(b_index)
        return range

    def isBombInRange(self, detonated_bomb, bomb):
        return math.sqrt(pow(detonated_bomb[0] - bomb[0], 2) + pow(detonated_bomb[1] - bomb[1], 2)) <= detonated_bomb[2]


print(Solution().maximumDetonation(bombs=[[2, 1, 3], [6, 1, 4]]))
print(Solution().maximumDetonation(bombs=[[1, 1, 5], [10, 10, 5]]))
print(Solution().maximumDetonation(
    bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
print(Solution().maximumDetonation(
    bombs=[[1, 1, 100000], [100000, 100000, 1]]))
print(Solution().maximumDetonation(
    bombs=[[647, 457, 91], [483, 716, 37], [426, 119, 35], [355, 588, 40], [850, 874, 49], [232, 568, 46], [886, 1, 30], [54, 377, 3], [933, 986, 50], [305, 790, 49], [372, 961, 67], [671, 314, 58], [577, 221, 29], [380, 147, 91], [600, 535, 1], [806, 329, 64], [536, 753, 18], [906, 88, 23], [436, 783, 82], [652, 674, 45], [449, 668, 20], [419, 13, 66], [853, 767, 60], [169, 288, 33], [871, 608, 66], [337, 445, 35], [388, 623, 39], [723, 503, 81], [14, 19, 19], [98, 648, 72], [147, 565, 93], [655, 434, 1], [407, 663, 22], [805, 947, 83], [942, 160, 70], [959, 496, 93], [30, 988, 53], [187, 849, 60], [980, 483, 41], [663, 150, 76], [268, 39, 50], [513, 522, 75], [61, 450, 90], [115, 231, 12], [346, 304, 74], [385, 540, 23], [905, 178, 19], [336, 896, 81], [751, 811, 94], [527, 783, 78], [635, 965, 19], [334, 290, 39], [748, 460, 77], [414, 134, 22], [955, 485, 29], [925, 787, 43], [243, 771, 75], [675, 223, 29], [788, 618, 82], [462, 544, 30], [999, 259, 50], [210, 146, 12], [789, 442, 70], [286, 36, 55], [451, 953, 6], [719, 914, 14], [664, 452, 14], [933, 637, 29], [206, 926, 16], [100, 422, 98], [97, 333, 4], [505, 631, 26], [908, 287, 65], [907, 316, 86], [949, 185, 16], [639, 735, 62], [401, 739, 18], [605, 926, 21], [25, 391, 69], [80, 24, 9], [435, 874, 92], [940, 381, 18], [260, 740, 87], [727, 515, 17], [361, 152, 16], [512, 470, 67], [189, 27, 27], [517, 439, 94], [159, 543, 76], [373, 698, 38], [781, 836, 97], [584, 190, 23], [383, 367, 86], [825, 141, 63], [117, 926, 85], [169, 588, 60], [56, 981, 100], [294, 716, 100], [781, 370, 89], [373, 44, 78]]))
