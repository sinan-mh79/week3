import re #Regular Expression module /library
from tabulate import tabulate #For table formatting tabulate module/library

#log file path
log_file_path = "path of the file"

# regular expression patterns anlaysis
date_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
level_pattern = r"\b(INFO|ERROR|WARNING|DEBUG)\b"

#store the log details in list based on log level_patterns
info_data = []
log_data = []
error_data = []
Warning_data = []
debug_data = []

# open the log file and read the file line by line
with open(log_file_path, "r") as log_file:
        for line in log_file:
                #search for patterns in each line
                date=re.search(date_pattern, line)
                ip=re.search(ip_pattern,line)
                level=re.search(level_pattern,line )
                message=line.strip().split(level.group())[1].strip() if level else line.strip()
                #print(message)

                #store the log details in dictionary
                log_entry={
                        "Date":date.group() if date else "N/A",
                        "IP Address":ip.group() if ip else "N/A",   
                        "Level":level.group() if level else "N/A",
                        "Message":message
                }
                log_data.append(log_entry)

                #categorize the log details based on log level_patterns

                if level and level.group() == "ERROR":
                    error_data.append({
                    "Date": date.group() if date else "N/A",
                    "IP": ip.group() if ip else "N/A",
                    "Error Message": message
                })

                if level and level.group() == "WARNING":
                        Warning_data.append({
                        "Date": date.group() if date else "N/A",
                        "IP": ip.group() if ip else "N/A",  
                        "Warning Message": message
                        })
                if level and level.group() == "DEBUG":
                        debug_data.append({
                        "Date": date.group() if date else "N/A",
                        "IP": ip.group() if ip else "N/A",
                        "Debug Message": message

                               })
                        
                if level and level.group() == "INFO":
                        info_data.append({
                        "Date": date.group() if date else "N/A",
                        "IP": ip.group() if ip else "N/A",
                        "Info Message": message
                               })
#print the log details in tabular format                        
print("\nAll Logs:")
print(tabulate(log_data, headers="keys", tablefmt="grid"))
print("\nError Logs:")
print(tabulate(error_data, headers="keys", tablefmt="grid"))
print("\nWarning Logs:")
print(tabulate(Warning_data, headers="keys", tablefmt="grid"))
print("\nDebug Logs:")
print(tabulate(debug_data, headers="keys", tablefmt="grid"))
print("\nInfo Logs:")
print(tabulate(info_data, headers="keys", tablefmt="grid"))
