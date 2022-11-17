from datetime import datetime, timezone


input_file = "input.txt"
out_file = "output.txt"

with open(input_file, "r") as time_file:
    file_line = time_file.readlines()
    out_lines = []
    for line in file_line:
        l = line.split(":")
        epoch_timestamp = l[0]
        print("Raw epoch timestamp: " + epoch_timestamp)
        # epoch_timestamp = "converted date time" inserting format conversion
        epoch_timestamp = datetime.fromtimestamp(float(epoch_timestamp), tz=timezone.utc)
        epoch_timestamp = epoch_timestamp.strftime("%a %d %b %H:%M:%S:%f000 %Z %Y")
        print("Converted epoch timestamp: " + epoch_timestamp)
        l[0] = epoch_timestamp
        ol = ":".join(l)
        out_lines.append(ol)
    
    with open(out_file, "w") as o_file:
        o_file.writelines(out_lines)

        
            
        
        
    