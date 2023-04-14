# Working with the CMS HLT path json file

Scripts to get information out of the CMS HLT path json.

Usage example:

```
python3 hlt-datasets.py 2015 cms-2015-collision-datasets-hi-ppref.txt > hlt-2015-hi-ppref-datasets.txt
```

`hlt-datasets.py` reads the CMS HLT path json file into a python dictionary. It produces an output of the format that is needed as the input for the CMS open data record preparation, e.g.

```
dataset1,hltpath11
dataset1,hltpath12
[...]
dataset2,htlpath21
dataset2,hltpath22
[...]
```

The repository containes dataset lists for the 2013 HI-related data and the 2015 HI pp reference data, but it can be used with a selected year and a corresponding input dataset list.
Outputs for these lists have been uploaded to this repository.


The relevant part of the CMS HLT path json is:

- hltpaths (dict)
  - dictionaries with the HLT path name (e.g. `HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v`)
  
Each single HLT path dictionary contains:

- pathname `<class 'str'>`
- versions `<class 'list'>`
- years `<class 'list'>`
- runs `<class 'list'>`
- datasets `<class 'list'>`
- l1seeds `<class 'list'>`
- prescales `<class 'list'>`

Datasets (above) is a list of dictionaries with:

- datasets (list of dicts) with in each dict
  - dataset
  - stream_type
  - path_ps
  - dataset_ps
- runs (list)

Looking forward to replacing the description above with a json schema...

The CMS HLT path json file is not in this repository and it is not meant to be accessed by this type of scripts (unless in need of something before a proper frontend has been set up).

