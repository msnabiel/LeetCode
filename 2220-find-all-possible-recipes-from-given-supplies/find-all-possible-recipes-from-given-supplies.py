from collections import deque, defaultdict

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = defaultdict(list)  # Adjacency list for recipe dependencies
        in_degree = {}  # To track remaining unmet ingredients for each recipe
        supply_set = set(supplies)  # Convert to set for O(1) lookups
        queue = deque()  # BFS queue
        result = []  # Store final recipes
        
        # Build graph and in-degree count
        for recipe, ing_list in zip(recipes, ingredients):
            in_degree[recipe] = len(ing_list)  # Count dependencies
            for ing in ing_list:
                graph[ing].append(recipe)  # Ingredient → Recipe dependency
            
            # If all ingredients are in supplies, add to queue
            if in_degree[recipe] == 0:
                queue.append(recipe)

        # Process available supplies
        for sup in supplies:
            queue.append(sup)  # Enqueue all initial supplies

        # Topological Sorting (BFS)
        while queue:
            item = queue.popleft()
            if item in in_degree:  # Only recipes should be in the final result
                result.append(item)
            
            for neighbor in graph[item]:
                in_degree[neighbor] -= 1  # Reduce dependency count
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  # Recipe is now possible

        return result
