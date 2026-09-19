class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx=xCenter
        if cx<x1:cx=x1
        elif cx>x2:cx=x2
        cy=yCenter
        if cy<y1:cy=y1
        elif cy>y2:cy=y2
        dx=cx-xCenter
        dy=cy-yCenter
        return dx*dx+dy*dy<=radius*radius