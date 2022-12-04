import subprocess as sp
import os


envs_o = sp.getoutput("conda env list").split('\n')[:-1]

envs = []
for i in envs_o:
    if '#' not in i and i != ' ':
        envs.append(i.split()[0])

d = '/home/solomon/conda_backup'
os.mkdir(d)

for e in envs:
    print("EXPORTING: {}".format(e))
    os.system("conda list -n {} --export > {}/{}.txt".format(e, d, e))
print("### DONE ###")
