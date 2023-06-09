def collecter(arrs):
    result = []

    def helper(arrs):
        for i in arrs:
            print(i)
            if type(i) == list:
                helper(i)
            else:
                result.append(i)

    helper(arrs)
    return result


arrs = [[[["a", [["b", ["c"]], ["d"]]], [["e"]], [[["f", "g", "h"]]]]]]
print(collecter(arrs))
