def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


# Example usage
arr = [1, 2, 3, 4, 2, 7, 8, 3, 4,8,2,2,2,4,]
print("Duplicates:", find_duplicates(arr))