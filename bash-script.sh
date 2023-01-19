region=ap-south-1
hostname="dre"
efsCount=3
asgName="efs"
hookName="con"
topicArn="arn:aws:sns:ap-south-1:118781765982:neng2"
sudo wget  http://instance-data/latest/meta-data/instance-id && \
id=$(cat instance-id) && \
sudo yum -y install git && \
sudo git clone https://github.com/HarvinderSinghDiwan/EricEFS-EC2-AutoscalingLifeCyleHookTask  && \
mkdir /efs1 /efs2 /efs3 && \
echo "sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0060860cb2b213eae.efs.ap-south-1.amazonaws.com:/ /efs1" >> /etc/fstab && \
echo "sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-014eb1a52de1e7dd2.efs.ap-south-1.amazonaws.com:/ /efs2 " >> /etc/fstab
echo "sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-076d29cd145fbe807.efs.ap-south-1.amazonaws.com:/ /efs3 " >> /etc/fstab && \
sudo hostnamectl set-hostname $hostname
sudo bash /etc/fstab
sleep 1
cd Eric*
sudo chmod +7 ./script.py
res1=$(./script.py $hostname $efsCount) && \
#echo $res1
successMessage="Successfully Launched Instance with id - ${id}" && \
echo $successMessage
failureMessage="Failed to Launch Instance with id - ${id} due to following reason ${res1}" && \
echo $failureMessage
if [ $res1==0 ];
then
sudo aws autoscaling complete-lifecycle-action --lifecycle-action-result CONTINUE --instance-id $id --lifecycle-hook-name $hookName --auto-scaling-group-name $asgName --region $region && \
sudo  aws sns publish  --message $successMessage  --topic-arn $topicArn --region $region;
else
sudo  aws sns publish  --message failureMessage --topic-arn $topicArn --region $region   && \
sudo aws autoscaling complete-lifecycle-action --lifecycle-action-result ABANDON --instance-id $id --lifecycle-hook-name $hookName --auto-scaling-group-name asgName --region $region;
fi

