Mydic["Reservations"][0]["Instances"][0]
["Reservations"][0]["Instances"][0]["NetworkInterfaces"][0]["Groups"][0]["GroupId"]

instance_id =["Reservations"][0]["Instances"][0]["InstanceId"]

IPrule=mysgdic["SecurityGroups"][0]["IpPermissions"][0]["IpRanges"][0]["CidrIp"]
Grpname=mysgdic["SecurityGroups"][0]["GroupName"]
GRPID