#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 17:40:01 2025

@author: mike
"""
import os
import booklet
from time import time
import urllib3
# from s3cdsapi import Manager


##############################################
### Parameters

save_path = os.path.realpath(os.path.dirname(__file__))

cds_url_endpoint = 'https://cds.climate.copernicus.eu/api'

s3_base_key = 'reanalysis-era5-land/'

variables = ['2m_dewpoint_temperature']
from_date = '1950-01-01'
to_date = '1950-01-31'
to_date = '1990-12-31'
bbox = [-34.3, 166.3, -47.3, 178.6]
product = 'reanalysis-era5-land'
freq_interval = 'Y'
product_types = None
pressure_levels = None
output_format = 'netcdf'

key = 'bfe6e61db232a76f2f0af9'



##############################################
### Tests

# stager = Stager(save_path)

# staged_file = stager.stage_jobs(product, variables, from_date, to_date, bbox, freq_interval, product_types, pressure_levels, output_format)

self = Manager(save_path, cds_url_endpoint, cds_key)
self = Manager(save_path, cds_url_endpoint, cds_key, s3_base_key, access_key_id=access_key_id, access_key=access_key, bucket=bucket, endpoint_url=endpoint_url)

staged_file_path = self.stage_jobs(product, variables, from_date, to_date, bbox, freq_interval, product_types, pressure_levels, output_format)

staged_dict = self.read_staged_file()

removed_job_ids = self.clear_jobs()

submitted_jobs = self.submit_jobs(3)

jobs = self.get_jobs()

job = jobs[0]

results_path = job.download_results(chunk_size=2**21, delete_job=True)


n_completed = self.run_jobs(5)

removed_job_ids = self.clear_jobs(True)

jobs_list = self._get_jobs_list()

job_id = '1e8e0da9-e4da-4f9f-afd0-8ac9e2ff61a9'

job_status_url = f'{cds_url_endpoint}/retrieve/v1/jobs/{job_id}?request=true'
headers = {'PRIVATE-TOKEN': f'{cds_key}'}

http_session = urllib3.PoolManager()
job_resp = http_session.request('get', job_status_url, headers=headers)

job_dict = job_resp.json()


jobs_url = f'{cds_url_endpoint}/retrieve/v1/jobs?limit=100&request=true'

jobs_resp = http_session.request('get', jobs_url, headers=headers)

jobs_dict = jobs_resp.json()

# f = booklet.open(self.staged_file_path)

# f = booklet.open(self.job_file_path)

# list(f.keys())

# f.close()

# with booklet.open(staged_file_path, 'n', 'str', 'bytes') as f:
#     # f[key] = b'1'
#     f['1'] = b'22'
#     f['2'] = b'22'
#     f['3'] = b'22'

# with booklet.open(self.staged_file_path) as f:
#     keys = list(f.keys())
#     print(keys)

# with booklet.open(self.staged_file_path, 'w') as f:
#     del f['1']

# with booklet.open(self.staged_file_path, 'w') as f:
#     f['1'] = b'1'

# with booklet.open(self.staged_file_path) as f:
#     keys = list(f.keys())
#     val = f['1']
#     print(keys)


# with open(self.staged_file_path, 'rb') as f:
#     init_bytes = f.read(16)




















































































