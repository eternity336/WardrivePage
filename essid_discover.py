import subprocess, os
import threading

captured = []

def lookup_wifi():
    while True:
        proc = str(subprocess.check_output(['iwlist', 'wlan0', 'scan'])).split("Cell")

        for p in proc:
            _p = parse_cell(p)
            if check_captured(_p):
                captured.append(_p)
            
def parse_cell(_data) -> dict:
    clean_data = {}
    split_data = _data.split('\\n')
    for d in split_data:
        d = d.strip()
        if d and len(d) > 1:
            if 'ESSID' in d:
                clean_data["ESSID"] = d.split(':')[-1].strip().replace('\\','')
            if 'Frequency' in d:
                d = d.split(':')[-1].strip()
                if len(d.split(' (')) == 2:
                    fc_split = d.split(' (Channel ')
                    clean_data["Frequency"] = fc_split[0]
                    clean_data["Channel"] = fc_split[1][0:-1]
                else:
                    clean_data["Frequency"] = d
                    clean_data["Channel"] = "N/A"
            if 'Quality' in d:
                qs_split = d.replace('Quality=','').replace('Signal level=','').split('  ')
                clean_data['Quality'] = qs_split[0]
                clean_data['Signal Level'] = qs_split[1]
                
    if clean_data:
        return clean_data

def check_captured(_p) -> bool:
    if not _p or _p["Channel"] == "N/A":
        return False
    for cap_data in captured:
        if cap_data["Channel"] == _p["Channel"] and cap_data["ESSID"] == _p["ESSID"]:
            captured[captured.index(cap_data)] = _p
            return False
    return True 

def print_devices():
    for d in captured:
        print(d)

def get_devices():
    return [[clean_data["ESSID"],clean_data["Frequency"],clean_data["Channel"],clean_data["Quality"],clean_data["Signal Level"]] for clean_data in captured]

t1 = threading.Thread(target=lookup_wifi)
t1.start()
