from Shell.Wrappers.requests import RequestsWrapper as requests

import re
class DofUtils():
    # TrbEdu package contains basic wrappers to ease calls to popular function
    # these wrappers follows TrbEdu code conventions. Here requests wrapper
    r = requests()
    servers_dict = {'Agride':'2', 'Atcham': '55', 'Brumen': '65', 'Crocabulia': '57', 'Echo': '54', 'Furye': '64', 'Ilyzaelle':'66', 'Jahash':'84', 'Julith':'61', 'Meriana':'58', 'Merkator':'63', 'Nidas':'62', 'Ombre':'35', 'Oto':'36', 'Pandore':'59', 'Rubilax':'56', 'Thanatena':'83', 'Ush':'60'}
    
    def posportails(self,server):
        if(server == ''):
            return(-1,"PLEASE PROVIDE A SERVER")
        if(not server in self.servers_dict.keys()):
            return(-2,"SERVER " + str(server) + " NOT IN LIST")
        response = self.r.exec("GET","https://dofus-portals.fr/portails/" + self.servers_dict[server])
        if(not response[0]):
            return response
        try:
            return(1,re.search("clipboard.*.Copier les positions de",response[1]).group()[16:-26])
        except:
            return(-1,"POS NOT FOUND IN DOFUS PORTALS RESPONSE")
        pass
        