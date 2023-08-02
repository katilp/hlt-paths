# Working with the CMS HLT path json file

Scripts to get information out of the CMS HLT path json.

## Python scripts

`hlt-datasets.py` reads the CMS HLT path json file into a python dictionary. It produces an output of the format that is needed as the input for the CMS open data record preparation, e.g.

```
dataset1,hltpath11
dataset1,hltpath12
[...]
dataset2,htlpath21
dataset2,hltpath22
[...]
```

Usage example:

```
python3 hlt-datasets.py 2015 cms-2015-collision-datasets-hi-ppref.txt > hlt-2015-hi-ppref-datasets.txt
```

`hlt-trigger-path.py` reads the CMS HLT path json file into a python dictionary. It produces an output of the format that is used for the HLT information snippets for CMS open data, e.g.

```
High-Level Trigger path information HLT_NNN
first seen online on run NF
last seen online on run NL
V1: (runs NFV1 - NLV1)
V2: (runs NFV2 - NLV2)
[...]
```

The eventual differences in the run range between the output here and those used earlier for CMS open data are due to the requirement of good runs in the input json file.

Usage example:

```
python3 hlt-trigger-paths.py 2013 > hlt-paths-2013.txt
```

TODO: selecting year does not exclude the versions and runs ranges from other years: to have an output comparable of yearly snippets on the portal, a cut on run range values should be done.

## Inputs

The repository contains dataset lists for the 2013 HI-related data and the 2015 HI pp reference data, but it can be used with any other selected year and a corresponding input dataset list.
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

Versions (above) is a list of dictionaries with:

- version (1,2,3...)
- runs (list)

Looking forward to replacing the description above with a json schema...

The CMS HLT path json file is not in this repository and it is not meant to be accessed by this type of scripts (unless in need of something before a proper frontend has been set up).

