# -*- coding: utf-8 -*-
import json
import datetime

class ProjectResult:
    def __init__(self,name):
        self.name=name
        self.test_run_results=[]

    def add_run_reult(self,run_result):
        self.test_run_results.append(run_result)

    def reprJSON(self):
        return dict([
            ('name',self.name),
            ('test_run_results',self.test_run_results),
        ])

class RunResult:
    def __init__(self,name):
        self.test_run_name=name
        self.case_results=[]

    def add_case_result(self,case_result):
        self.case_results.append(case_result)

    def reprJSON(self):
        fail=0
        passed=0
        unknown=0
        skip=0
        status="Pass"
        time=0
        for case_result in self.case_results:
            time+=case_result.time
            if case_result.status=="Pass":
                passed+=1
            elif case_result.status=="Fail":
                fail+=1
            else:
                unknown+=1
        if fail>0:
            status="Fail"
        return dict([
            ('test_run_name',self.test_run_name),
            ('case_results',self.case_results),
            ('fail',fail),
            ('pass',passed),
            ('skip',0),
            ('status',status),
            ('time',time),
            ('total',len(self.case_results)),
            ('unknown',unknown),
        ])

class CaseResult:
    def __init__(self,name):
        self.name=name
        self.status="Pass"
        self.error_log="None"

    def begin_execute(self):
        self.start_time=datetime.datetime.now()

    def end_execute(self):
        self.time=(datetime.datetime.now()-self.start_time).total_seconds()

    def failed(self,log):
        self.error_log=log
        self.status="Fail"

    def reprJSON(self):
        return dict([
            ('case_name',self.name),
            ('error_log',self.error_log),
            ('status',self.status),
            ('time',self.time),
        ])

class TianjiEncoder(json.JSONEncoder):
    def default(self,obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self,obj)

if __name__ == '__main__':
    import time
    project_result=ProjectResult("dnsGlobalTrafficManagerSR")
    run_result=RunResult("gtmInterfaceTest")
    case1=CaseResult("test_01")
    case1.begin_execute()
    time.sleep(3)
    case1.end_execute()
    run_result.add_case_result(case1)

    project_result.add_run_reult(run_result)
    print(json.dumps(project_result.reprJSON(),cls=TianjiEncoder))