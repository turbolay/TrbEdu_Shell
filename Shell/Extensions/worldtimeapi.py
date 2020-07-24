# Implementation for worldtimeapi example extension

import json
from Shell.Wrappers.requests import RequestsWrapper as requests

class WorldTimeApi():
    # TrbEdu package contains basic wrappers to ease calls to popular function
    # these wrappers follows TrbEdu code conventions. Here requests wrapper
    r = requests()
    def timezonetotime(self,tz):
        results = None
        # Arg default behaviour must be handled here but documented in main
        # TODO: regroup documentation with implementation

        if(tz == ''):
            return self.iptotime('')

        results = self.r.exec('GET','http://worldtimeapi.org/api/timezone/' + tz)

        # If an error is catch, result is just relayed
        if(not results[0]):
            return results

        # Will load results as json then fetch a particular result
        return self.worldtimeapi_get_result('datetime',results[1])

    def iptotime(self,ip):
        results = None
        if(ip == ''):
            results = self.r.exec('GET','http://worldtimeapi.org/api/ip')
        else:
            results = self.r.exec('GET','http://worldtimeapi.org/api/ip/' + ip)

        if(not results[0]):
            return results

        return self.worldtimeapi_get_result('datetime',results[1])

    def worldtimeapi_get_result(self,wanted_result,apireturn):
        if(apireturn.__len__() <= 0):
            return (0,"EMPTY RESULT SET")
        try:
            data = json.loads(apireturn)
            if('error' in data.keys()):
                return (-1, "ERROR WITH API RESULTS: " + data['error'])
            if(not wanted_result in data.keys()):
                return (-2, "ERROR: KEY " + wanted_result + " NOT IN API RESULTS")

            return (1,data[wanted_result])
        except:
            return (-3,"UNKNOWN ERROR WITH API RESULTS")