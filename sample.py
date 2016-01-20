from  infrastructure import servers

atclilabbw = servers.BaseServer("actlilabbw","ATC")
atclilabbw.show()

my_servers = servers.load("atc_systems.json")
print "server: %s" % my_servers["systems"][0]["type"]
