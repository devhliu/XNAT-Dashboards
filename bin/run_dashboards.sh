#!/bin/bash
WORKROOT=/mnt/d/umic/app/umic-dev/proj-xnat/XNAT-Dashboards/bin
python $WORKROOT/download_data.py -c $WORKROOT/xnat.cfg -p $WORKROOT/prod.pickle
python $WORKROOT/stop.py
python $WORKROOT/run_dashboards.py -c $WORKROOT/config.json -p $WORKROOT/prod.pickle -P 8080