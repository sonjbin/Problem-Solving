class Solution:
    def simplifyPath(self, path: str) -> str:
        path_out = []
        path_seq = [s for s in path.split("/") if s]
        for s in path_seq:
            if s == "..":
                if len(path_out) > 0:
                    path_out.pop()
            elif s == ".":
                continue
            else:
                path_out.append(s)
        return "/" + "/".join(path_out)