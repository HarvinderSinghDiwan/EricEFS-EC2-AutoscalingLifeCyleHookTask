import subprocess as sp
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('hostname', help='hostname of the instance')
parser.add_argument('count', help='Number of nfs to be mounted')

args = vars(parser.parse_args(sys.argv[1:]))

hostname=args['hostname']
_count=args['count']

_,res=sp.getstatusoutput("df -hT")
res=res.split("\n")

_res=[]
count=0

for i in res:
    _res.append(i.split())
for i in _res:
    if i[1] == 'nfs4':
        count+=1
if count==int(_count):
    pass
else:
    if int(count)-int(_count) == 0:
        print("Oops!.... A single EFS is also not found to be mounted. Sorry!! Can't proceed ahead...")
        #raise Exception("Oops!.... A single EFS is also not found to be mounted. Sorry!! Can't proceed ahead...")
    elif int(count)-int(_count) == 1:
        print("Oops!.... {} EFS seems to be missing or unmounted. Sorry!! Can't proceed ahead...")
        #raise Exception("Oops!.... {} EFS seems to be missing or unmounted. Sorry!! Can't proceed ahead...".format(int(count)-int(_count)))
    else: print("Oops!.... {} EFS seems to be missing or unmounted. Sorry!! Can't proceed ahead...")
_,res=sp.getstatusoutput("hostname")
if res==hostname:
    pass
else:
    #raise Exception("Hostname not matched")
    print("HOSTNAME NOT FOUND")
