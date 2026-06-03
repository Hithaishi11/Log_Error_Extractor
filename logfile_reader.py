import yaml

log_contents = {}

with open("inputfile.yaml","r") as f:
    config= yaml.safe_load(f)

print(config)

for key,filename in config.items():
    print(f"Reading {key}: {filename}")
    with open(filename,"r") as logfile:
        log_contents[key]= logfile.readlines()

print(log_contents)