input_file = "input.txt"
#import csv
import time
out_file = "output.txt"

with open(input_file, "r") as time_file:
    file_line = time_file.readlines()
    out_lines = []
    for line in file_line:
        l = line.split(":")
        epoch_timestamp = l[0]
        print(epoch_timestamp)
        epoch_timestamp = "converted date time"
        l[0] = epoch_timestamp
        ol = ":".join(l)
        out_lines.append(ol)
    
    print(out_lines)    
    with open(out_file, "w") as o_file:
        o_file.writelines(out_lines)

        
            
        
        
    