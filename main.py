import csv
import os


class mergeData:
    def __init__(self, file1, file2, slotData=bool, slotDataFile=str) -> None:
        print("\nOptions selected ⬇⬇")
        print("\nfile1 ->", file1)
        print("file2 ->", file2, "\n")

        checkThat = {"slotted": "", "not_slotted": ""}
        if slotData == True:
            print("Slot Data ->", slotData)
            print("Slot Data file ->", slotDataFile, "\n")

            check = [file1, file2]
            for i in range(0, 2):
                if slotDataFile == check[i]:
                    checkThat.update({"slotted": check[i]})
                else:
                    checkThat.update({"not_slotted": check[i]})

            file1 = checkThat.get("not_slotted")
            file2 = self.slotData(checkThat.get("slotted"))
            self.merge(file1, file2)

        else:
            self.merge(file1, file2)
            exit()

    def merge(self, file1, file2):
        print("Combining your Data ...", "\n")

        data1 = []
        data2 = []

        with open(file1, "r") as f:
            a = csv.reader(f)
            for i in a:
                data1.append(i)

        with open(file2, "r") as f:
            b = csv.reader(f)
            for i in b:
                data2.append(i)

        header1 = data1[0]
        header2 = data2[0]

        stars1 = data1[1:]
        stars2 = data2[1:]

        headers = header1 + header2
        stars = []

        for i, data in enumerate(stars1):
            stars.append(stars1[i] + stars2[i])

        print("Data is merged !", "\n")

        with open("merged.csv", "a+") as f:
            a = csv.writer(f)
            a.writerow(headers)
            a.writerows(stars)

            print("Data has been saved !", "\n")

        cwd = os.getcwd()
        path = cwd + "\merged.csv"
        print("Your Data is saved at ->", path)

        if os.path.isfile("slotted.csv") == True:
            os.remove("slotted.csv")
        else:
            pass

    def slotData(self, file):
        print("Data is sorting ...", "\n")

        data = []
        with open(file, "r") as f:
            df = csv.reader(f)
            for i in df:
                data.append(i)

        headers = data[0]
        starsData = data[1:]
        for i in starsData:
            i[2] = i[2].lower()

        starsData.sort(key=lambda starsData: starsData[2])

        with open("slotted.csv", "a+") as f:
            a = csv.writer(f)
            a.writerow(headers)
            a.writerows(starsData)
            print("Data has been sorted !", "\n")

        cwd = os.getcwd()
        path = cwd + "\slotted.csv"
        return path

    def timeTaken():
        print("\nProcess completed ✅ ->", "0.01 sec", "\n")
