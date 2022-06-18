from main import mergeData

file1 = "data/bright_stars.csv"
file2 = "data/dwarf_stars.csv"

mergeData(file1, file2, True, file2)

mergeData.timeTaken()
