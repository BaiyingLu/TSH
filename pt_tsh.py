

def input_data(filename):
    lines = open(filename).read().splitlines()
    return lines


def Diagnosis(tsh_min, tsh_max):
    if tsh_min < 1:
        diagnosis = "hyperthyroidism"
    elif tsh_max > 4:
        diagnosis = "hypothyroidism"
    else:
        diagnosis = "normal thyroid function"
    return diagnosis


def interface():
    print("Please input the document name:")
    print("Please include the extension,like: .txt")
    doc_name = input("The name is:")
    data = import_data(doc_name)
if __name__ == "__main__":
    interface()
