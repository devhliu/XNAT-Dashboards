from xnat_dashboards import data_fetcher as df
import pyxnat
import os.path as op
import xnat_dashboards

fp = op.join(op.dirname(xnat_dashboards.__file__), '..', '.xnat.cfg')
x = pyxnat.Interface(config=fp)


def test_data_fetcher():

    details = df.get_instance_details(x)

    assert len(details['projects']) != 0
    assert len(details['subjects']) != 0
    assert len(details['experiments']) != 0
    assert len(details['scans']) != 0

    resources, bbrc_resources = df.get_resources(x)

    assert len(resources) != 0
    assert len(bbrc_resources) != 0

    longitudinal_data = df.longitudinal_data(details, resources)

    assert len(longitudinal_data) != 0