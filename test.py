import pdb
pdb.set_trace()

s = {1, 2}
l = [1, 2, 3, 1, 2, 3]

def main():
    for item in l:
        import pdb
        pdb.set_trace()
        methods = {
            "GET",
            "PUT",
            "POST",
            "DELETE",
            "PUT",   # This is a duplicate
        }
        if item in methods:
            print(item)

    t = 1

s2 = {1, 2, 3, 1}  # Has duplicates