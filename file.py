myfile = open('op.txt','w+')
print(type(myfile))
My_dic={"Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-03a933af70fa97ad2",
                    "InstanceId": "i-00f825971843dd1dc",
                    "InstanceType": "t2.medium",
                    "KeyName": "k8",
                    "LaunchTime": "2023-04-12T06:36:09+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "ap-south-1a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-172-31-37-133.ap-south-1.compute.internal",
                    "PrivateIpAddress": "172.31.37.133",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2023-04-12 11:56:01 GMT)",
                    "SubnetId": "subnet-0fb600207d4c29d59",
                    "VpcId": "vpc-0018fbb3177332a32",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2023-04-11T08:48:03+00:00",
                                "DeleteOnTermination": "true",
                                "Status": "attached",
                                "VolumeId": "vol-0615b6ea8bcd46fe4"
                            }
                        }
                    ],
                    "ClientToken": "6724a2bb-c740-4d31-9f48-b1c9aad8c2a7",
                    "EbsOptimized": "false",
                    "EnaSupport": "true",
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2023-04-11T08:48:02+00:00",
                                "AttachmentId": "eni-attach-0c53359ae0d75cd00",
                                "DeleteOnTermination": "true",
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "launch-wizard-1",
                                    "GroupId": "sg-0d50cf0f9b820cc23"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "02:f7:23:9a:03:e4",
                            "NetworkInterfaceId": "eni-0c1a3100cc4bb0207",
                            "OwnerId": "820143247800",
                            "PrivateDnsName": "ip-172-31-37-133.ap-south-1.compute.internal",
                            "PrivateIpAddress": "172.31.37.133",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": "true",
                                    "PrivateDnsName": "ip-172-31-37-133.ap-south-1.compute.internal",
                                    "PrivateIpAddress": "172.31.37.133"
                                }
                            ],
                            "SourceDestCheck": "true",
                            "Status": "in-use",
                            "SubnetId": "subnet-0fb600207d4c29d59",
                            "VpcId": "vpc-0018fbb3177332a32",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-1",
                            "GroupId": "sg-0d50cf0f9b820cc23"
                        }
                    ],
                    "SourceDestCheck": "true",
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "k8w1"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": "false"
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": "false"
                    },
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2023-04-11T08:48:02+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": "true",
                        "EnableResourceNameDnsAAAARecord": "false"
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                },
                {
                    "AmiLaunchIndex": 2,
                    "ImageId": "ami-03a933af70fa97ad2",
                    "InstanceId": "i-0888e23f7a258d0db",
                    "InstanceType": "t2.medium",
                    "KeyName": "k8",
                    "LaunchTime": "2023-04-12T06:36:09+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "ap-south-1a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-172-31-42-223.ap-south-1.compute.internal",
                    "PrivateIpAddress": "172.31.42.223",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2023-04-12 11:56:01 GMT)",
                    "SubnetId": "subnet-0fb600207d4c29d59",
                    "VpcId": "vpc-0018fbb3177332a32",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2023-04-11T08:48:03+00:00",
                                "DeleteOnTermination": "true",
                                "Status": "attached",
                                "VolumeId": "vol-04cc8a1dd9fafbab1"
                            }
                        }
                    ],
                    "ClientToken": "6724a2bb-c740-4d31-9f48-b1c9aad8c2a7",
                    "EbsOptimized": "false",
                    "EnaSupport": "true",
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2023-04-11T08:48:02+00:00",
                                "AttachmentId": "eni-attach-0fd28be41bb729533",
                                "DeleteOnTermination": "true",
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "launch-wizard-1",
                                    "GroupId": "sg-0d50cf0f9b820cc23"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "02:e6:9c:02:09:04",
                            "NetworkInterfaceId": "eni-0461114e9d14070d5",
                            "OwnerId": "820143247800",
                            "PrivateDnsName": "ip-172-31-42-223.ap-south-1.compute.internal",
                            "PrivateIpAddress": "172.31.42.223",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": "true",
                                    "PrivateDnsName": "ip-172-31-42-223.ap-south-1.compute.internal",
                                    "PrivateIpAddress": "172.31.42.223"
                                }
                            ],
                            "SourceDestCheck": "true",
                            "Status": "in-use",
                            "SubnetId": "subnet-0fb600207d4c29d59",
                            "VpcId": "vpc-0018fbb3177332a32",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-1",
                            "GroupId": "sg-0d50cf0f9b820cc23"
                        }
                    ],
                    "SourceDestCheck": "true",
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "k8Master"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": "false"
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": "false"
                    },
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2023-04-11T08:48:02+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": "true",
                        "EnableResourceNameDnsAAAARecord": "false"
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                },
                {
                    "AmiLaunchIndex": 1,
                    "ImageId": "ami-03a933af70fa97ad2",
                    "InstanceId": "i-0b42a4cc6574f5b6d",
                    "InstanceType": "t2.medium",
                    "KeyName": "k8",
                    "LaunchTime": "2023-04-12T06:36:09+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "ap-south-1a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-172-31-39-105.ap-south-1.compute.internal",
                    "PrivateIpAddress": "172.31.39.105",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2023-04-12 11:56:01 GMT)",
                    "SubnetId": "subnet-0fb600207d4c29d59",
                    "VpcId": "vpc-0018fbb3177332a32",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2023-04-11T08:48:03+00:00",
                                "DeleteOnTermination": "true",
                                "Status": "attached",
                                "VolumeId": "vol-0fab3989c4ad7ee47"
                            }
                        }
                    ],
                    "ClientToken": "6724a2bb-c740-4d31-9f48-b1c9aad8c2a7",
                    "EbsOptimized": "false",
                    "EnaSupport": "true",
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2023-04-11T08:48:02+00:00",
                                "AttachmentId": "eni-attach-0bd20767921a93394",
                                "DeleteOnTermination": "true",
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "launch-wizard-1",
                                    "GroupId": "sg-0d50cf0f9b820cc23"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "02:3d:1c:ff:aa:e4",
                            "NetworkInterfaceId": "eni-0dadaeb8081c70d80",
                            "OwnerId": "820143247800",
                            "PrivateDnsName": "ip-172-31-39-105.ap-south-1.compute.internal",
                            "PrivateIpAddress": "172.31.39.105",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": "true",
                                    "PrivateDnsName": "ip-172-31-39-105.ap-south-1.compute.internal",
                                    "PrivateIpAddress": "172.31.39.105"
                                }
                            ],
                            "SourceDestCheck": "true",
                            "Status": "in-use",
                            "SubnetId": "subnet-0fb600207d4c29d59",
                            "VpcId": "vpc-0018fbb3177332a32",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-1",
                            "GroupId": "sg-0d50cf0f9b820cc23"
                        }
                    ],
                    "SourceDestCheck": "true",
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "k8w2"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 2,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": "false"
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": "false"
                    },
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2023-04-11T08:48:02+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": "true",
                        "EnableResourceNameDnsAAAARecord": "false"
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                }
            ],
            "OwnerId": "820143247800",
            "ReservationId": "r-02ce6bf05bb10a255"
        },
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-07d3a50bd29811cd1",
                    "InstanceId": "i-0feb8a2f430d520c2",
                    "InstanceType": "t2.micro",
                    "KeyName": "k8",
                    "LaunchTime": "2023-04-20T08:21:27+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "ap-south-1a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-172-31-41-164.ap-south-1.compute.internal",
                    "PrivateIpAddress": "172.31.41.164",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 80,
                        "Name": "stopped"
                    },
                    "StateTransitionReason": "User initiated (2023-04-20 09:47:40 GMT)",
                    "SubnetId": "subnet-0fb600207d4c29d59",
                    "VpcId": "vpc-0018fbb3177332a32",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2023-04-20T08:21:27+00:00",
                                "DeleteOnTermination": "true",
                                "Status": "attached",
                                "VolumeId": "vol-085f1f59c1ba63c8a"
                            }
                        }
                    ],
                    "ClientToken": "12e989b6-e3d1-4620-b8fa-e42d65682e80",
                    "EbsOptimized": "false",
                    "EnaSupport": "true",
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2023-04-20T08:21:27+00:00",
                                "AttachmentId": "eni-attach-00e316779e2b01fbe",
                                "DeleteOnTermination": "true",
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "allow_http",
                                    "GroupId": "sg-063a7ccd0b3853036"
                                },
                                {
                                    "GroupName": "allow_ssh",
                                    "GroupId": "sg-0c02343b12cf21268"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "02:c0:f5:c7:6e:a6",
                            "NetworkInterfaceId": "eni-00b3b128b9a0a0fe7",
                            "OwnerId": "820143247800",
                            "PrivateDnsName": "ip-172-31-41-164.ap-south-1.compute.internal",
                            "PrivateIpAddress": "172.31.41.164",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": "true",
                                    "PrivateDnsName": "ip-172-31-41-164.ap-south-1.compute.internal",
                                    "PrivateIpAddress": "172.31.41.164"
                                }
                            ],
                            "SourceDestCheck": "true",
                            "Status": "in-use",
                            "SubnetId": "subnet-0fb600207d4c29d59",
                            "VpcId": "vpc-0018fbb3177332a32",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "allow_http",
                            "GroupId": "sg-063a7ccd0b3853036"
                        },
                        {
                            "GroupName": "allow_ssh",
                            "GroupId": "sg-0c02343b12cf21268"
                        }
                    ],
                    "SourceDestCheck": "true",
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Python-pr"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": "false"
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "required",
                        "HttpPutResponseHopLimit": 2,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": "false"
                    },
                    "BootMode": "uefi-preferred",
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2023-04-20T08:21:27+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": "true",
                        "EnableResourceNameDnsAAAARecord": "false"
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                }
            ],
            "OwnerId": "820143247800",
            "ReservationId": "r-054f1d916b538f23f"
        }
    ]
}

print(type(My_dic))
print(f"My lisst of describe instances first sg" , My_dic["Reservations"][0]["Instances"][0]["NetworkInterfaces"][0]["Groups"][0]["GroupId"])
print(f"\n \nMy lisst of describe instances second sg" , My_dic["Reservations"][1]["Instances"][0]["NetworkInterfaces"][0]["Groups"][0]["GroupId"])
instance_id1 =My_dic["Reservations"][0]["Instances"][0]["InstanceId"]
instance_id2 =My_dic["Reservations"][1]["Instances"][0]["InstanceId"]
print(instance_id1)
print("\n")
print(instance_id2)

#print(myfile.read())
myfile.close()