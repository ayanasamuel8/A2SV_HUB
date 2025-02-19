# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.zero_pos =- 1

    def add(self, num: int) -> None:
        if not num :
            self.zero_pos = len(self.products)
            self.products.append(1)
        else : 
            self.products.append( self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.products) - k > self.zero_pos or self.zero_pos == -1:
            return self.products[-1] // self.products[len(self.products) - k-1]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)