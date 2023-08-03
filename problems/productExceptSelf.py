
def productExceptSelf(nums):
    final = []

    for num in nums:
        produto = []
        produtoProd = 0
        for i in range(0, len(nums)):
            if nums.index(num) == i:
                continue
            else:
                produto.append(nums[i])
                if len(produto) == 1:
                    produtoProd = produto[0]
                else:
                    produtoProd *= nums[i]
        final.append(produtoProd)

    return final
