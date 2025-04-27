# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        parent = set()
        can_make = defaultdict(lambda:False)
        for i in supplies:
            can_make[i] = True
        index_map = {val: idx for idx, val in enumerate(recipes)}
        supply = set(supplies)

        def dfs(idx):
            if recipes[idx] in parent:
                parent.clear()
                return False
            if can_make[recipes[idx]]:
            
                return True
            parent.add(recipes[idx])
            for ingredient in ingredients[idx]:
                if not can_make[ingredient]:
                    if ingredient not in index_map or  not dfs(index_map[ingredient]):
                        return False
            parent.remove(recipes[idx])
            return True
        ans = []
        for i in recipes:
            if can_make[i] or  dfs(index_map[i]):
                can_make[i] = True
                ans.append(i)
        return ans