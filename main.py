def simplify_nested_list(arr: list, integers: list = []) -> list:
    if isinstance(arr, list):
      for i in arr:
          if isinstance(i, int):
              integers.append(i)
          simplify_nested_list(i, integers)
      return integers
    return []