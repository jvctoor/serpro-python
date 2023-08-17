class Solution(object):
    def flipAndInvertImage(self, image):
        reversedArray = []
        final = []
        for array in image:
            reversedArray.append(self.reverseLine(array))
        for array in reversedArray:
            final.append(self.invertZeros(array))
        return final

    def reverseLine(self, line):
        result = []
        for i in range(len(line) - 1, -1, -1):
            result.append(line[i])
        return result

    def invertZeros(self, line):
        result = []
        for i in line:
            if i == 0:
                result.append(1)
            elif i == 1:
                result.append(0)
        return result
