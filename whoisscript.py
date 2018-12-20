from os import system
import nmap
import numpy as np
import whois


def program(domain):
    q = whois.whois(domain)
    print(q)

    name_servers=q["name_servers"]
    print(type(name_servers))
    nservers = np.array([])
    ips = np.array([])

    for i in range(0, len(name_servers)-1):
        nservers = np.append(nservers, name_servers[i].split(" ")[0])
        ips = np.append(ips, name_servers[i].split(" ")[1])

    #print("test",nservers,ips)

    for i in range(0, len(nservers)):
        x = str(nservers[0])
        print("\nСервер: "+x)
        nm = nmap.PortScanner()
        nm.scan(x, '22-443')

        print(nm.scaninfo())

        print("IP хоста: " + nm.all_hosts()[0])

        print("Статус хоста: " + nm[nm.all_hosts()[0]].state())

        protocols = nm[nm.all_hosts()[0]].all_protocols()
        if (len(protocols) > 0):
            print("Протоколы: " + str(protocols))
            print("Tcp: " + str(nm[nm.all_hosts()[0]]['tcp'].keys()))

        else:
            print("Нет поддерживаемых протоколов")

        print("53 tcp: " + str(nm[nm.all_hosts()[0]].has_tcp(53)))
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                print('\nПротокол : %s' % proto)

                lport = list(nm[host][proto].keys())
                lport.sort()
                for port in lport:
                    print('Порт : %s\tСтатус : %s' % (port, nm[host][proto][port]['state']))

if __name__ == "__main__":
    program("devnip.ru")
    system("pause")
