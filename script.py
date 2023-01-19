#!/usr/bin/python3
import subprocess as sp
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('hostname', help='hostname of the instance')
parser.add_argument('count', help='Number of nfs to be mounted')

args = vars(parser.parse_args(sys.argv[1:]))

hostname=args['hostname']
_count=int(args['count'])

_,res=sp.getstatusoutput("df -hT")
res=res.split("\n")

_res=[]
count=0
fres=[]
for i in res:
    _res.append(i.split())
for i in _res:
    if i[1] == 'nfs4':
        count+=1
_r=0
if count==int(_count):
    _r+=1
else:
    if int(count)-int(_count) == 0:
        fres.append("A single EFS is also not found to be mounted.")
        #raise Exception("Oops!.... A single EFS is also not found to be mounted. Sorry!! Can't proceed ahead...")
    elif int(count)-int(_count) == 1:
        fres.append("{} EFS seems to be missing or unmounted.".format(count-_count))
        #raise Exception("Oops!.... {} EFS seems to be missing or unmounted. Sorry!! Can't proceed ahead...".format(int(count)-int(_count)))
    else: fres.append(" {} EFS seems to be missing or unmounted. Sorry!! Can't proceed ahead...".format(count-_count))
_,res=sp.getstatusoutput("hostname")
if res==hostname:
    _r+=1
else:
    #raise Exception("Hostname not matched")
    fres.append("Current hostname of the instance doesn't seems to match with the desired hostname provided where CURRENT_HOSTNAME is {} and DESIRED_HOSTNAME IS {}".format(res,hostname))
if _r==2:
    print(0)
else:
    if len(fres) is 2:
        print(fres[0]+" and "+fres[1])
    else: print(fres[0])

