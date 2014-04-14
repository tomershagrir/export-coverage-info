#!/usr/bin/env python
import argparse
import importlib
import requests
from coverage import coverage


def get_coverage(filename):
    cov = coverage(filename)
    cov.load()
    return int(round(cov.xml_report()))


def get_version(package):
    version = importlib.import_module("%s.version" % package)
    return version.version_number


def send_to_url(url, package, coverage_amount, version, status):
    params = {
        "package": package,
        "coverage": coverage_amount,
        "version": version,
        "status": status,
        }
    resp = requests.post(url, params)
    print resp.status_code, resp.content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default=".coverage")
    parser.add_argument("-p", "--package", type=str)
    parser.add_argument("-u", "--url", type=str)
    parser.add_argument("-s", "--status", type=str)
    args = parser.parse_args()

    send_to_url(args.url, args.package, get_coverage(args.file), get_version(args.package), args.status)

