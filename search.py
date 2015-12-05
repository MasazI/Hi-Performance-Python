def search_1st(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False


def search_2nd(haystack, needle):
    val = False
    for item in haystack:
        if item == needle:
            val = True

    return val
