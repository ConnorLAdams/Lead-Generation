from dotenv import load_dotenv
load_dotenv('.env')
import requests
import json
import os


n8n_workflow_url = os.environ['N8N-WORKFLOW-URL']
n8n_project_ul  = os.environ['N8N-PROJECT-URL']
project_ids = os.getenv('N8N-COMMA-SEPARATED-PROJECT-IDS', None)
n8n_api_key = os.environ['N8N-API-KEY']

hdrs = {
    'accept': 'application/json',
    'X-N8N-API-KEY': n8n_api_key
}

if project_ids is None:
    r = requests.get(n8n_workflow_url, headers=hdrs)
    data = r.json()
    prjt_name = 'all_workflows'
    if os.path.isdir(f'./{prjt_name}') == False:
        os.mkdir(f'./{prjt_name}')

    for wf in data['data']:
        with open(f'./{prjt_name}/{wf['name']}.json', 'w') as f:
            json.dump(wf, f, indent=4)

else:
    project_ids_ls = [pid.strip() for pid in project_ids.split(',')]
    r_prjts = requests.get(n8n_project_ul, headers=hdrs)
    prjts_data = r_prjts.json()['data']
    for pid in project_ids_ls:
        prjt_name = [prjt for prjt in prjts_data if prjt['id']==pid][0]['name']
        prms = {'projectId': pid}
        r = requests.get(n8n_workflow_url, headers=hdrs, params=prms)
        data = r.json()
        if os.path.isdir(f'./{prjt_name}') == False:
            os.mkdir(f'./{prjt_name}')

        for wf in data['data']:
            with open(f'./{prjt_name}/{wf['name']}.json', 'w') as f:
                json.dump(wf, f, indent=4)


