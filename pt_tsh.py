import json


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


def output_file(patient_dict):
    filename = patient_dict["First Name"]+' '+patient_dict["Last Name"]+'.json'
    out_file = open(filename, "w")
    json.dump(patient_dict, out_file)
    out_file.close()


def tsh_info_process(lines):
    for i in range(0, len(lines) - 1, 4):
        while lines[i] != 'END':
            tsh_num = lines[i + 3].split(",")[1:-1]
            tsh_num = [float(i) for i in tsh_num]
            tsh_min = min(tsh_num)
            tsh_max = max(tsh_num)
            diagnosis = Diagnosis(tsh_min, tsh_max)
            patient_dict = {"First Name": lines[i].split(" ")[0],
                            "Last Name": lines[i].split(" ")[1],
                            "Age": int(lines[i + 1]),
                            "Gender": lines[i + 2],
                            "Diagnosis": diagnosis,
                            "TSH": tsh_num}
            output_file(patient_dict)
            print(patient_dict)
            break
    return patient_dict


def interface():
    print("Please input the document name:")
    print("Please include the extension,like: .txt")
    doc_name = input("The name is: ")
    data = import_data(doc_name)
    tsh_info_process(data)
if __name__ == "__main__":
    interface()
