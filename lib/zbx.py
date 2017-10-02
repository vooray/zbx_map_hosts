from zabbix.api import ZabbixAPI

class Zbx:
    """
    Zabbix communication class
    """
    def __init__(self, zbx_uri, zbx_user, zbx_passwd):
        self.zbx_uri = zbx_uri
        self.zbx_uri = zbx_user
        self.zbx_passwd = zbx_passwd
        self.zapi = ZabbixAPI(url=zbx_uri, user=zbx_user, password=zbx_passwd)

    def map_hosts(self, map_name):
        """
        Hosts on map
        :param map_name: string, map name
        :return: dict[list]
        """
        map_elements = self.zapi.map.get(filter={'name': map_name}, selectSelements=['elementid'])[0]['selements']
        hosts = self.zapi.host.get(output=['hostid', 'name'])

        hostnames = []

        for i in map_elements:
            for j in hosts:
                if i['elementid'] == j['hostid']:
                    hostnames.append(j['name'])

        return hostnames

