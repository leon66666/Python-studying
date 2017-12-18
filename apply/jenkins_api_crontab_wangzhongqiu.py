#!/usr/bin/python
# encoding:utf8
# date:2017-08-07
#version:v1.0.0
import sys
import jenkins
import os
#获取release最新分支
#os.chdir("/opt/hxb-core")
#os.system('git pull')
#w = os.popen("git branch -a|grep  release_17*|awk 'BEGIN {FS=\"/\"} END {print $2\"/\"$3}'",'r',1)
#new_branch = w.read().replace('\n','')
new_branch="origin/OPTIMIZE-48_wangzhongqiu"
#END

jenkins_server_url='http://192.168.1.18:8080'
user_id='linux'
api_token='e93502e308c29ad321f6fb5636acd116'
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
choice = sys.argv[1]
def test28_single():
    param_dict1 = {"profile": "test28", "branch": new_branch, "branch_rule_engine": "origin/dev_invite"}
    server.build_job('TEST-schedule-JOB', parameters=param_dict1)
def test28():
    param_dict1 = {"profile": "test28", "branch": new_branch, "branch_rule_engine": "origin/dev_invite"}
    param_dict2 = {"profile": "test28", "branch": new_branch}
    job_name1 = ['Test-core-dubbo-JOB', 'TEST-escrow-retry-JOB', 'TEST-mgmt-JOB', 'TEST-schedule-JOB', 'TEST-web-JOB']
    job_name2 = ['TEST-core-match-JOB', 'TEST-core-repay-JOB', 'TEST-hxb-lend-JOB', 'Test-rule-engine-JOB']
    for i in job_name1:
        server.build_job(i, parameters=param_dict1)
    for j in job_name2:
        server.build_job(j, parameters=param_dict2)
		
if choice == 'test28_single':
    test28_single()
elif choice == 'test28':
    test28()
else:
    print 'Please input your choice'
