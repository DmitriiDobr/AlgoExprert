class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    sums = calculateBranchSums(root, 0, sums)
    print('da', sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        print('cc', sums)
        return sums

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        print('gghh', sums)
        return sums

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
# return sums