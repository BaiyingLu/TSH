import json


def input_data(filename):
    """Take the Data from a File

    This function reads in the data from a file. The file type could
    be .txt. Each data is seperated by new line (carriage return).
    Then this function transfers the data into a list with each element in it.

    Args:
        filename (string): The name of the file which saves the patient info

    Returns:
        A list with all of the elements in the file
    """
    lines = open(filename).read().splitlines()
    return lines


def Diagnosis(tsh_min, tsh_max):
    """Diagnose based on the TSH result

    Thyroid Stimulating Hormone (TSH) shows the level of the thyroid gland to
    produce thyroxine. In diagnosis, "hyperthyroidism" is defined by any of
    the patient test results being less than 1.0. The "hypothyroidism" is
    defined by any of the patient test results being greater than 4.0.
    And the "normal thyroid function" is defined by all of their test results
    being between 1.0 and 4.0, inclusive. No single patient will have test
    results both above 4.0 and below 1.0, hence will only meet one of the
    diagnoses above. The function only takes in the minimun and the maximum
    from the patient TSH test result list. If the minimum is less than 1.0,
    this patient is hyperthyroidism. If the maximum is mroe than 4.0,
    this patient is hypothyroidism. If the minimum and the maximum are both
    between 1.0 to 4.0, this patient is normal thyroid function.
    The result will be returned.

    Args:
        tsh_min (float): minimum in TSH test result list
        tsh_max (float): maximum in TSH test result list

    Returns:
        string: the diagnosis result
    """
    if tsh_min < 1:
        diagnosis = "hyperthyroidism"
    elif tsh_max > 4:
        diagnosis = "hypothyroidism"
    else:
        diagnosis = "normal thyroid function"
    return diagnosis


def output_file(patient_dict):
    """Output the patient information in dictionary into .json file

    This function takes in the one patient information dictionary and create a
    .json file named by the patient first and last name in this way:
    "Firstname Lastname.json". Then close the created file.

    Args:
        patient_dict (dictionary): stores patient information

    """
    filename = patient_dict["First Name"]+' '+patient_dict["Last Name"]+'.json'
    out_file = open(filename, "w")
    json.dump(patient_dict, out_file)
    out_file.close()


def tsh_info_process(lines):
    """Process the information from a raw list into formed dictionary

    This function takes in a list with patient information in order and
    transfer it into dictionaries.Each four elements in the list will be
    treated as one patient information. The first element in these four is
    the patient's name. This function splits this element into First Name
    and Last Name and gives these two string to the keys named "First Name"
    and "Last Name" seperately. The second is the patient's age, which will
    be transfered from string to int and stored with the key "Age".
    The third is the patient's gender, which will be saved with the key
    "Gender". The fourth is the patient's TSH test result.
    This function will get rid of the first string in this list and give
    out the diagnosis information based on this list, and then sorts it
    from low to high and saves it with the key "TSH". The diagnosis result
    will be stored with the key "Diagnosis". Then the function will call
    the output_file function to output the patient information dictionary
    into .json file.


    Args:
        lines (list): all patients' information

    """
    for i in range(0, len(lines) - 1, 4):
        while lines[i] != 'END':
            tsh_num = lines[i + 3].split(",")[1:-1]
            tsh_num = [float(i) for i in tsh_num]
            tsh_min = min(tsh_num)
            tsh_max = max(tsh_num)
            tsh_num.sort()
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


def interface():
    """Take in the data file name

    This function is an interface which can interact with the user. This
    function takes in the file which user types in with extension.
    Then it calls the function import_data and tsh_info_process

    """
    print("Please input the document name:")
    print("Please include the extension,like: .txt")
    doc_name = input("The name is: ")
    data = import_data(doc_name)
    tsh_info_process(data)
if __name__ == "__main__":
    interface()
