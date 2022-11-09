# Sysdig Runtime Overview Report


## ! Warning !
* This is hardcoded to only fetch maximum of 2000 image results from runtime
* This script is using unsupported, undocumented Sysdig API's that may change at any time

## Description

This script will create a CSV and JSON file in the local directory the script is run named output.json and output.csv that gives you the following fields for each image in runtime

* Cluster
* Namespace
* Workload
* Image
* Policy Result
* # of Exploit Count
* # of Critical In Use Vulnerabilities
* # of High In Use Vulnerabilities
* # of Medium In Use Vulnerabilities
* # of Critical Vulnerabilities
* # of High  Vulnerabilities
* # of Medium  Vulnerabilities

## Example Usage & Output
```
$ API_TOKEN=xxxx API_ENDPOINT=https://app.au1.sysdig.com python3 sysdig_runtime_overview_report.py
Images Passed Policy: 0 / 2
Images Failed Policy: 2 / 2
Image Policy Pass Percentage: 0.00%

$ cat output.csv
Cluster,Namespace,Workload,Image,PolicyResult,ExploitCount,CriticalInUseVulns,HighInUseVulns,MediumInUseVulns,CriticalVulns,HighVulns,MediumVulns
lab2,temp,sysdiglabs/security-playground,sysdiglabs/security-playground,failed,164,20,22,16,183,1124,1252
lab1,sysdig,quay.io/sysdig/elasticsearch:6.8.6.15,quay.io/sysdig/elasticsearch:6.8.6.15,failed,26,66,47,42,66,49,44

$ cat output.json
[
    {
        "Cluster": "lab2",
        "Namespace": "temp",
        "Workload": "sysdiglabs/security-playground",
        "Image": "sysdiglabs/security-playground",
        "PolicyResult": "failed",
        "ExploitCount": 164,
        "CriticalInUseVulns": 20,
        "HighInUseVulns": 22,
        "MediumInUseVulns": 16,
        "CriticalVulns": 183,
        "HighVulns": 1124,
        "MediumVulns": 1252
    },
    {
        "Cluster": "lab1",
        "Namespace": "sysdig",
        "Workload": "quay.io/sysdig/elasticsearch:6.8.6.15",
        "Image": "quay.io/sysdig/elasticsearch:6.8.6.15",
        "PolicyResult": "failed",
        "ExploitCount": 26,
        "CriticalInUseVulns": 66,
        "HighInUseVulns": 47,
        "MediumInUseVulns": 42,
        "CriticalVulns": 66,
        "HighVulns": 49,
        "MediumVulns": 44
    }
]
```


