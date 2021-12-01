from urllib.request import urlopen
import json
import subprocess, shlex

url = urlopen("http://IP/api/v4/groups/pet-medical/projects?private_token=PRIVATE_TOKEN&per_page=1000")
allProjects = json.loads(url.read().decode())
for project in allProjects: 
    try:
        projectUrl  = project['ssh_url_to_repo']
        command     = shlex.split('git clone --recurse-submodules %s' % projectUrl)
        retCode  = subprocess.Popen(command)

    except Exception as e:
        print("Error on %s: %s" % (projectUrl, e.strerror))