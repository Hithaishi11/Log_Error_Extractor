from logfile_messageextractor import error_messages

result={}

for file, lines in error_messages.items():
    result[file] = {
        "ERROR": 0,
        "FAIL": 0,
        "EXCEPTION": 0
    }

    for line in lines:
        for error_type in result[file]:
            if error_type in line:
                result[file][error_type] += 1

print(result)