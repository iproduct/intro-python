
def traverse_depth_first(list_: list[str | list]) -> list[str]:
    pass

if __name__ == '__main__':
    l = [["a",[["b","c", ["d", ["e"], "f", [["g", "h"],"i"], "g"]], ["k",["l",["m"],"n","o"]]]], "p"]
    print(traverse_depth_first(l))