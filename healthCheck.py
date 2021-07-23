import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print("disk " + str(free))
    print(free > 25)
    return(free > 25) 

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print("cpu" + str(usage))
    return usage < 75

print("running")

if not check_disk_usage("C:\\") or not check_cpu_usage():
    print("Error!")
else:
    print("All Good!")

# chmod +x <filename>
