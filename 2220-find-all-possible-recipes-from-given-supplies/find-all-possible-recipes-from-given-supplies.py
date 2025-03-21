from collections import deque, defaultdict

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        adj = defaultdict(list)
        in_degree = {recipe: 0 for recipe in recipes}

        # Step 1: Build the graph and calculate in-degrees
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                adj[ingredient].append(recipe)
            in_degree[recipe] = len(ingredients[i])

        # Step 2: Initialize the queue with initial supplies
        result = []
        queue = deque(supplies)

        # Step 3: BFS to find all possible recipes
        while queue:
            curr = queue.popleft()
            for recipe in adj[curr]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)

        return result
