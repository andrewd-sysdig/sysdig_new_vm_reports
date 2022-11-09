import requests
import os
import json
import csv

API_TOKEN = os.getenv('API_TOKEN')
API_ENDPOINT = os.getenv('API_ENDPOINT')
API_HEADERS = {
  'Authorization': 'Bearer ' + API_TOKEN,
  'Content-Type': 'application/json'
}

url = API_ENDPOINT + '/api/scanning/runtime/v2/workflows/results?limit=2000'
response = requests.request("GET", url, headers=API_HEADERS)

result_list = []
images_passed = 0
images_failed = 0
total_images = 0

results=response.json() # Dict

for image in results['data']:
    total_images+=1
    if (image['policyEvaluationsResult']=='passed'):
        images_passed+=1
    elif (image['policyEvaluationsResult']=='failed'):
        images_failed+=1

    dict_data = {
                "Cluster": image['recordDetails']['labels']['kubernetes.cluster.name'],
                "Namespace": image['recordDetails']['labels']['kubernetes.namespace.name'],
                "Workload": image['recordDetails']['mainAssetName'],
                "Image": image['recordDetails']['mainAssetName'] ,
                "PolicyResult": image['policyEvaluationsResult'],
                "ExploitCount": image['exploitCount'],
                "CriticalInUseVulns": image['runningVulnsBySev'][2],
                "HighInUseVulns": image['runningVulnsBySev'][3],
                "MediumInUseVulns": image['runningVulnsBySev'][5],
                "CriticalVulns": image['vulnsBySev'][2],
                "HighVulns": image['vulnsBySev'][3],
                "MediumVulns": image['vulnsBySev'][5]
            }
    result_list.append(dict_data)

# Output JSON Results to terminal
#print(json.dumps(result_list,indent=4, sort_keys=True))

print (f"Images Passed Policy: {images_passed} / {total_images}")
print (f"Images Failed Policy: {images_failed} / {total_images}")
images_percent_pass = (images_passed / total_images) * 100
print (f"Image Policy Pass Percentage: {images_percent_pass:0.2f}%")

# Write json file
with open('output.json', 'w') as outfile:
    json.dump(result_list, outfile)

# Write CSV file
csv_columns = ['Cluster','Namespace','Workload', 'Image', 'PolicyResult', 'ExploitCount', 'CriticalInUseVulns', 'HighInUseVulns', 'MediumInUseVulns', 'CriticalVulns', 'HighVulns', 'MediumVulns' ]
csv_file = "output.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_list:
        writer.writerow(data)