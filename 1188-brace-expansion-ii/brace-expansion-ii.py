class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i=0
        n=len(expression)
        def parse_factor():
            nonlocal i
            if expression[i]=="{":
                i+=1
                res=parse_expr()
                i+=1
                return res
            start=i
            while i<n and expression[i].isalpha():
                i+=1
            return {expression[start:i]}
        def parse_term():
            nonlocal i
            res=parse_factor()
            while i<n and (expression[i]=="{" or expression[i].isalpha()):
                nxt=parse_factor()
                res={a+b for a in res for b in nxt}
            return res
        def parse_expr():
            nonlocal i
            res=parse_term()
            while i<n and expression[i]==",":
                i+=1
                res=res|parse_term()
            return res
        return sorted(list(parse_expr()))