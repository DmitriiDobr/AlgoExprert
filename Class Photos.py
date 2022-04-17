"""Greedy algorithm too long to describe"""

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)


    shirtcolorFirstRow = 'red' if blueShirtHeights[0] > redShirtHeights[0] else 'blue'
    for idx in range(len(redShirtHeights)):

        red = redShirtHeights[idx]
        blue = blueShirtHeights[idx]
        print(red - blue)

        if shirtcolorFirstRow == 'red':
            if (blue - red) <= 0:
                return False

        elif shirtcolorFirstRow == 'blue':
            if (red - blue) <= 0:
                return False
    return True
