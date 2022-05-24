import pandas as pd
import xml.etree.ElementTree as ET
import os

df_covid = pd.DataFrame()
df = pd.DataFrame()
i=0
list_keywords=[]

path = 'COVID-19 CLinical trials studies/COVID-19 CLinical trials studies'
list_of_files = os.listdir(path)

for file in list_of_files:
    file_path = os.path.join(path,file)
    tree = ET.parse(file_path)
    root = tree.getroot()

    trial = {}
    trial['id'] = root.find('id_info').find('nct_id').text
    trial['overall_status'] = root.find('overall_status').text
    trial['study_type'] = root.find('study_type').text

    if root.find('start_date') != None:
        trial['start_date'] = root.find('start_date').text
    else:
        trial['start_date'] = ''

    if root.find('enrollment') != None:
        trial['enrollment'] = root.find('enrollment').text
    else:
        trial['enrollment'] = ''

    if root.find('official_title') == None:
        trial['title'] = root.find('brief_title').text
    else:
        trial['title'] = root.find('official_title').text

    date_string = root.find('required_header').find('download_date').text
    trial['date_processed'] = date_string.replace('ClinicalTrials.gov processed this data on ', '')

    trial['sponsors'] = root.find('sponsors').find('lead_sponsor').find('agency').text

    df = pd.DataFrame(trial, index=[i])
    i = i + 1

    df_covid = pd.concat([df_covid, df])

df_covid.to_csv('COVID_trials.csv')



