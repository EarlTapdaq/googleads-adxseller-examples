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

"""This example gets all ad clients for the logged in user's account.

Tags: adclients.list
"""

__author__ = 'api.Dean.Lukies@gmail.com (Dean Lukies)'

import sys

from apiclient import sample_tools
from oauth2client import client

MAX_PAGE_SIZE = 50


def main(argv):
  # Authenticate and construct service.
  service, _ = sample_tools.init(
      argv, 'adexchangeseller', 'v2.0', __doc__, __file__, parents=[],
      scope='https://www.googleapis.com/auth/adexchange.seller.readonly')

  try:
    # Retrieve ad client list in pages and display data as we receive it.
    request = service.accounts().adclients().list(
        accountId='myaccount', maxResults=MAX_PAGE_SIZE)

    while request:
      result = request.execute()
      if 'items' in result:
        ad_clients = result['items']
        for ad_client in ad_clients:
          print ('Ad client for product "%s" with ID "%s" was found. '
                 % (ad_client['productCode'], ad_client['id']))

          print ('\tSupports reporting: %s' %
                 (ad_client['supportsReporting'] and 'Yes' or 'No'))

      request = service.accounts().adclients().list_next(request, result)

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
