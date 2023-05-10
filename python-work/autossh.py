import boto3 
import paramiko
import time


instance_id =''
ec2 = boto3.resource('ec2', region_name='us-east-2')
instance = ec2.Instance(id=instance_id)
instance.wait_until_running()
current_instance = list(ec2.instances.filter(InstanceIds=[instance_id]))
ip_address = current_instance[0].public_ip_address
print (ip_address)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())

def ssh_connect(ssh,ip_address,retries):
    if retries > 3:
        return False
    privkey = paramiko.RSAKey.from_private_key_file(
        ''
    )
    interval = 5 
    try: 
     retries += 1    
     ssh.connect(hostname=ip_address,
                username='ubuntu',pkey=privkey)
              
    
     return True

    except Exception as e: 
        print(e)
        time.sleep(interval)
        print('trying again {}'.format(ip_address))
        ssh_connect(ssh,ip_address,retries)

ssh_connect(ssh,ip_address,0)

stdin, stdout, stderr = ssh.exec_command("sudo bio sup status")
print(stderr.read())
print(stdout.read())     
