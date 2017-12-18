#!/usr/bin/python
# encoding:utf8
# date:2017-08-07
# version:v1.0.0
import sys
import jenkins
import os

# 获取release最新分支
# os.chdir("/opt/hxb-core")
# os.system('git pull')
# w = os.popen("git branch -a|grep  release_17*|awk 'BEGIN {FS=\"/\"} END {print $2\"/\"$3}'",'r',1)
# new_branch = w.read().replace('\n','')
new_branch = "origin/OPTIMIZE-48_wangzhongqiu"
branch_invite = "origin/dev_invite"
# END

jenkins_server_url = 'http://192.168.1.18:8080'
user_id = 'linux'
api_token = 'e93502e308c29ad321f6fb5636acd116'
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
choice = sys.argv[1]


def test28_schedule():
    param_dict1 = {"profile": "test28", "branch": new_branch, "branch_rule_engine": branch_invite, "message": new_branch}
    server.build_job('TEST-schedule-JOB', parameters=param_dict1)


def test28_web():
    param_dict1 = {"profile": "test28", "branch": new_branch, "branch_rule_engine": branch_invite}
    server.build_job('TEST-web-JOB', parameters=param_dict1)


def test28_mgmt():
    param_dict1 = {"profile": "test28", "branch": new_branch, "branch_rule_engine": branch_invite}
    server.build_job('TEST-mgmt-JOB', parameters=param_dict1)


def test28_all():
    param_dict1 = {"profile": "test28", "branch": new_branch, "branch_rule_engine": branch_invite}
    param_dict2 = {"profile": "test28", "branch": new_branch, "branch_rule_engine": branch_invite, "message": new_branch}
    param_dict3 = {"profile": "test28", "branch": branch_invite}

    job_name1 = ['Test-core-dubbo-JOB', 'TEST-escrow-retry-JOB', 'TEST-mgmt-JOB', 'TEST-core-match-JOB', 'TEST-core-repay-JOB',
                 'TEST-hxb-lend-JOB', 'TEST-web-JOB']
    job_name2 = ['TEST-schedule-JOB']
    job_name3 = ['Test-rule-engine-JOB']
    for i in job_name1:
        server.build_job(i, parameters=param_dict1)
    for j in job_name2:
        server.build_job(j, parameters=param_dict2)
    for j in job_name3:
        server.build_job(j, parameters=param_dict3)


if choice == 'test28_schedule':
    test28_schedule()
elif choice == 'test28_web':
    test28_web()
elif choice == 'test28_mgmt':
    test28_mgmt()
elif choice == 'test28_all':
    test28_all()
else:
    print 'Please input your choice'
