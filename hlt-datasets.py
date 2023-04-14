# input:
# - year 2013, 2015, 2016, 2017, 2018 or 2022
# - dataset listing
import json
import sys

def main():

    year = int(sys.argv[1])
    ds_list = sys.argv[2]
    # get the yearly dataset list (unique names only)
    datasets_for_year = []
    for line in open(ds_list, "r").readlines():
        line = line.strip()
        first, dataset, process, tier = line.split("/")

        # list only unique entries (different processings have the same hlt path lists)
        if dataset not in datasets_for_year:
            datasets_for_year.append(dataset)

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


    # loop over the dataset to be released:
    for d in datasets_for_year:
        prev_hlt = ''
        for key, value in hlt.items() :
            one_hlt = value
            years = one_hlt["years"]
            # choose only those for the chosen year
            if year in years:
                datasets = one_hlt["datasets"] # this is a list of dictionaries
                for i in datasets : # datasets is list, most often one, sometimes more
                #   for key, value in i.items() : # dictionary contains:
                #      print (key) # -> datasets, runs
                #      print (type(value)) # -> and they are lists
                    runs = i["runs"]
                    # This is the list of dataset dictionaries for datasets where a HLT stream is
                    # (Datasets dict has: "dataset", "stream_type", "path_ps", "dataset_ps")
                    for ds in i["datasets"] : 
                        dataset = ds["dataset"] # dictionary, see 
                        if  dataset == d :
                            if one_hlt["pathname"] != prev_hlt :
                                print (d+","+one_hlt["pathname"])
                            prev_hlt = one_hlt["pathname"]
                            # print also "runs" to see why multiple entries of pathname
                            #print (d+","+one_hlt["pathname"],runs)
                            # these correspond to the different hlt path versions
                            # which are recorded in one_hlt["versions"] e.g.:
                            #  [{'version': '1', 'runs': [210986, 210998, 211000, 211001, 211561, 
                            #                             211587, 211739, 211740, 211812, 211821, 
                            #                             211822, 211823]},
                            #   {'version': '2', 'runs': [254790, ...


        
if __name__ == "__main__":
    main()