import pandas as pd

header = [1, 2, 3, 4, 5, 6]
index = [1, 2, 3, 4, 5, 6]

main = [["a", "b", "c", "d", "e", "f"],["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"],["a", "b", "c", "d", "e", "f"],
        ["a", "b", "c", "d", "e", "f"],["a", "b", "c", "d", "e", "f"]]

df = pd.DataFrame(main,
                  index=header, columns=index)

df.to_excel('./test.xlsx', sheet_name="test")
