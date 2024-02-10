#!/usr/bin/env python3
import os
import time
from esu import Manager, DnsRecord

def main(): 
    manager = Manager()
    client = manager.get_all_clients()[0]
    project = client.get_projects()[0]
    completeDomain = os.getenv('CERTBOT_DOMAIN')
    challenge = os.getenv('CERTBOT_VALIDATION')
    parts = completeDomain.split('.') # [SUB, DOMAIN, SLD, TLD]
    zoneName = parts[-2] + '.' + parts[-1] + '.' # SLD.TLD.
    recordName = "_acme-challenge" + '.' + completeDomain + '.'
    zone = get_zone(project, zoneName)
    #clean_old_challenges(zone, recordName)
    append_challenge_tag(zone, recordName,challenge)
    # time.sleep(60)

def get_zone(project, domain):
    result = None
    for zone in project.get_dns_zones():
        if zone.name == domain:
            result = zone
            break
    return result

def clean_old_challenges(zone, recordName):
    """
    Removes all old _acme-challenge TXT tags.
    """
    records = zone.get_dns_records()

    for record in records:
        if record.host == recordName:
            print(vars(record))
            record.destroy()

def append_challenge_tag(zone, recordName, challenge):
    """
    Generate a new challenge tag and append to records.
    """
    record = DnsRecord(type="TXT", host=recordName, data=challenge,
                   dns=zone, ttl=60)
    record.create()


if __name__ == "__main__":
    main()