import subprocess
import json

#one vnet and one subnet in the resourcegroup.
def get_vnet_name(resourcegroup):
    get_vnet_command=["az","network","vnet","list","--resource-group",resourcegroup]
    get_vnet=subprocess.run(get_vnet_command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    a=get_vnet.stdout.decode('utf-8')
    d=json.loads(a)
    for item in d:
        vname=item["name"]
        subnets=item["subnets"]
    for i in subnets:
        subnetname=i["name"]
    return vname,subnetname

def create_vm(vm_resourcegroup,vm_name, vm_image,vm_username, vm_passowrd,vm_vnet,vm_subnet, vm_size):
    create_vm_command=["az","vm","create","--resource-group",vm_resourcegroup,"--name",vm_name,"--image",vm_image, "--admin-username", vm_username,"--admin-password",vm_passowrd,"--vnet-name",vm_vnet,"--subnet",vm_subnet,"--size", vm_size]
    create_vm=subprocess.run(create_vm_command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    return

if __name__=="__main__":
    rscgroup_name="vm-test-group"
    rscgroup_location="West Europe"
    avm_name=""
    avm_image="Win2016Datacenter"
    avm_username=""
    avm_password=""
    avm_size="Standard_B1ls"
     
    avm_vnet,avm_subnet=get_vnet_name(rscgroup_name)
    create_vm(rscgroup_name,avm_name,avm_image,avm_username,avm_password,avm_vnet,avm_subnet,avm_size)

    