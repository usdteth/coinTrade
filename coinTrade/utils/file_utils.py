

def write_text(file_name,record_text):
    with open(file_name, 'a') as file:
        file.write(record_text + '\n')