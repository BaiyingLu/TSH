

def interface():
    print("Please input the document name:")
    print("Please include the extension,like: .txt")
    doc_name = input("The name is:")
    data = import_data(doc_name)
if __name__ == "__main__":
    interface()
