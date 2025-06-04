class Solution(object):
    def accountsMerge(self, accounts):
            """
            :type accounts: List[List[str]]
            :rtype: List[List[str]]
            """
            from collections import defaultdict
            parent = {}
            email_to_name = {}

            # Union-Find functions
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]  # Path compression
                    x = parent[x]
                return x

            def union(x, y):
                parent[find(x)] = find(y)

            # Step 1: Build union-find structure and map emails to names
            for account in accounts:
                name = account[0]
                first_email = account[1]
                for email in account[1:]:
                    if email not in parent:
                        parent[email] = email
                    union(email, first_email)
                    email_to_name[email] = name

            # Step 2: Group emails by their root parent
            root_to_emails = defaultdict(list)
            for email in parent:
                root = find(email)
                root_to_emails[root].append(email)

            # Step 3: Build final result
            result = []
            for root, emails in root_to_emails.items():
                name = email_to_name[root]
                result.append([name] + sorted(emails))

            return result
