import boto3
from botocore.config import Config


my_config = Config(
   region_name = 'us-west-1', 
)
efs_client = boto3.client('efs',config=my_config)

# Create a list of efs in amazon
def list_filesystems ():
   efs_data = efs_client.describe_file_systems(MaxItems=123,)
   efs_Idlist = []

   for efsid in efs_data['FileSystems']:
      efs_Idlist.append(efsid['FileSystemId'])
   return efs_Idlist

#checks skips over any efs with active point and delete any with zero mount points. 
def delete_efs(file_system_id): 
   

   response = efs_client.describe_mount_targets(FileSystemId=file_system_id)
   if 'MountTargets' in response and len(response['MountTargets']) > 0:
        print("Cannot delete file system", file_system_id, "because it has active mount targets.")
        return
   efs_client.delete_file_system(FileSystemId=file_system_id)
   return("Deleting",file_system_id,)
        

list_ofIds = list_filesystems()
for eid in list_ofIds:
    delete_efs(eid)

