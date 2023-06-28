# input:
# - year 2013, 2015, 2016, 2017, 2018 or 2022
import json
import sys

def main():

    year = int(sys.argv[1])
    
    # get the hlt information
    with open('pathInfo_2013-2022_withHI.json') as f:
        data = f.read()
            
    # reconstructing the data as a dictionary
    all_meta = json.loads(data)
     
    # take the hltpaths dictionary
    hlt = all_meta['hltpaths']

    # a single dictionary would be
    # a_hlt = hlt["HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v"]
    # for key, value in a_hlt.items() :
    #     print (key)
    #     print (type(value))
    # This gives:
    # pathname
    # <class 'str'>
    # versions
    # <class 'list'>
    # years
    # <class 'list'>
    # runs
    # <class 'list'>
    # datasets
    # <class 'list'>
    # l1seeds
    # <class 'list'>
    # prescales
    # <class 'list'>

    # note that "datasets" is a list with one or more of:
    # [{'datasets': 
    #  [{'dataset': 'ExpressPhysics', 'stream_type': 'Express', 'path_ps': 1, 'dataset_ps': 1}, 
    #   {'dataset': 'OnlineHltMonitor', 'stream_type': 'HLTDQM', 'path_ps': 1, 'dataset_ps': 1}, 
    #   {'dataset': 'OnlineMonitor', 'stream_type': 'DQM', 'path_ps': 1, 'dataset_ps': 1}, 
    #   {'dataset': 'PPFSQ', 'stream_type': 'A', 'path_ps': 1, 'dataset_ps': 1}], 
    #   'runs': [211739, 211740, 211752, 211760, 211765, 211792, 211797, 211812, 211821, 211822, 211823, 211831]}]
    # and each list item is a dictionary


    for key, value in hlt.items() :
        one_hlt = value
        years = one_hlt["years"]
        # choose only those for the chosen year
        # SELECTING YEAR SELECTS TRIGGERS THAT SPAN OVER MORE THAN ONE YEAR 
        # NEED TO CHECK WHETHER RUNS ARE IN THAT YEAR'S RANGE AS WELL
        if year in years:
            # print (key) # -> These are HLT paths (with HLT_ ...) 
                        # and some Alca_, DST_ and DQM_ 
            # take only HLT_            
            if "HLT_" in key:
                path=key[:-2]
                print ("High-Level Trigger path information "+path)
                runs = one_hlt["runs"]
                print ("first seen online on run "+str(min(runs)))
                print ("last seen online on run "+str(max(runs)))
                versions = one_hlt["versions"]
                for v in versions :
                #    print (type(v)) # -> is a dictionary
                #    print (v)
                    nversion = str(v["version"])
                    minrun = str(min(v["runs"]))
                    maxrun = str(max(v["runs"]))
                    print ("V"+ nversion+": (runs "+minrun+" - "+maxrun+")")

        
if __name__ == "__main__":
    main()