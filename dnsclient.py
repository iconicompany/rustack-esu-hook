from esu import Manager, DnsRecord
import argparse
parser = argparse.ArgumentParser(description='ESU DNS CLIENT')
parser.add_argument('-z', '--zone', required=True)
parser.add_argument('-t', '--type', required=True)
parser.add_argument('-H', '--host', required=True)
parser.add_argument('-d', '--data', required=True)
parser.add_argument('--ttl',type=int, default=86400)

args = parser.parse_args()
print(vars(args))

zoneName = args.zone;

#print(args.zone)

manager = Manager()
client = manager.get_all_clients()[0]

project = client.get_projects()[0]
dns = None
for zone in project.get_dns_zones():
    #print(f'DNS "{zone.name}"')
    if zone.name == zoneName:
        dns = zone
        break

print(f'Found DNS Zone "{dns.name}"')

record = DnsRecord(type=args.type, host=args.host, data=args.data,
                   dns=dns, ttl=args.ttl)
print(vars(record))
record.create()
