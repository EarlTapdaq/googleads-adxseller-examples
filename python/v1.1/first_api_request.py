#!/usr/bin/python
# coding: utf-8
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Runs a report using the Ad Exchange Seller REST API.

Tags: reports.generate
"""

__author__ = 'api.Dean.Lukies@google.com (Dean Lukies)'

import sys

from apiclient import sample_tools
from oauth2client import client


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'adexchangeseller', 'v1.1', __doc__, __file__,
      scope='https://www.googleapis.com/auth/adexchange.seller.readonly')

  try:
    # Retrieve report.
    result = service.reports().generate(
        startDate='today-6d', endDate='today',
        metric=['AD_REQUESTS', 'CLICKS'],
        dimension=['DATE', 'WINNING_BID_RULE_NAME'],
        sort=['+DATE']).execute()

    # Display headers.
    for header in result['headers']:
      print '%25s' % header['name'],
    print

    # Display results.
    for row in result['rows']:
      for column in row:
        print '%25s' % column,
      print

    # Display totals
    for total in result['totals']:
      print '%25s' % total,
    print

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')


if __name__ == '__main__':
  main(sys.argv)
