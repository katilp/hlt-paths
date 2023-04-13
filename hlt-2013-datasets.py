import json

def main():

    # get the 2013 dataset list (unique names only)
    datasets2013 = []
    for line in open("cms-2013-collision-datasets-hi.txt", "r").readlines():
        line = line.strip()
        first, dataset, process, tier = line.split("/")

        # list only unique entries (different processings have the same hlt path lists)
        if dataset not in datasets2013:
            datasets2013.append(dataset)

    # get the hlt information
    with open('pathInfo_2013-2022.json') as f:
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
    for d in datasets2013:
        prev_hlt = ''
        for key, value in hlt.items() :
            one_hlt = value
            years = one_hlt["years"]
            my_year = 2013
            # choose only those for with year 2013
            if 2013 in years:
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