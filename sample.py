from  infrastructure import servers

systems = [];

my_servers = servers.load("atc_systems.json")
print "Loading Infrastructure:"
for server in my_servers["systems"]:
    if server["type"] == "linux":
        x = servers.LinuxServer(
                server["servername"],
                server["location"],
                server["kernel"]
                )
        x.show()
        systems.append(x)
