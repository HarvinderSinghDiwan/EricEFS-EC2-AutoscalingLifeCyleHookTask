#!/usr/bin/bash
sudo wget  http://instance-data/latest/meta-data/instance-id && \
sudo yum -y install git && \
sudo git clone https://github.com/HarvinderSinghDiwan/EricEFS-EC2-AutoscalingLifeCyleHookTask  && \
mkdir /efs1 /efs2 /efs3 && \
echo "sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-076d29cd145fbe807.efs.ap-south-1.amazonaws.com:/ /efs1" >> /etc/fstab && \
echo "sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-014eb1a52de1e7dd2.efs.ap-south-1.amazonaws.com:/ /efs2" >> /etc/fstab
echo "sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0060860cb2b213eae.efs.ap-south-1.amazonaws.com:/ /efs3" >> /etc/fstab && \
hostnamectl set-hostname dre
bash /etc/fstab
sleep 1
id=$(cat instance-id)
cd Eric*
chmod +7 ./script.py
res1=$(./script.py fre 3) && \
if [ $res1==0 ];
then 
sudo aws autoscaling complete-lifecycle-action --lifecycle-action-result CONTINUE --instance-id $(cat ../instance-id) --lifecycle-hook-name con --auto-scaling-group-name efs --region ap-south-1 && \
sudo  aws sns publish  --message "Successfully launched instance with id ${id}"  --topic-arn arn:aws:sns:ap-south-1:118781765982:neng2 --region ap-south-1; 
else 
res=$(./script.py fre 4) && sudo  aws sns publish  --message "Failed to Launch instance having id ${id} ${res}"  --topic-arn arn:aws:sns:ap-south-1:118781765982:neng2 --region ap-south-1 && \
sudo aws autoscaling complete-lifecycle-action --lifecycle-action-result ABANDON --instance-id $(cat ../instance-id) --lifecycle-hook-name con --auto-scaling-group-name efs --region ap-south-1; 
fi

