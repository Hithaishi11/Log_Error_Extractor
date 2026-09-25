from logfile_reader import log_contents

keywords=("FAIL","ERROR","EXCEPTION")

error_messages={}

for filename,lines in log_contents.items():
    error_messages[filename]=[]

    for line in lines:
        if any(keyword in line for keyword in keywords):
            error_messages[filename].append(line.strip())

print(error_messages)
