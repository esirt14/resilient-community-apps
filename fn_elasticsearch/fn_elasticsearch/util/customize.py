# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Generate the Resilient customizations required for fn_elasticsearch"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     es_doc_type
    #     es_index
    #     es_query
    #   Message Destinations:
    #     fn_elasticsearch
    #   Functions:
    #     fn_elasticsearch_query
    #   Workflows:
    #     example_elasticsearch_query_from_artifact
    #     example_elasticsearch_query_from_incident
    #   Rules:
    #     Example: ElasticSearch Query from Artifact
    #     Example: ElasticSearch Query from Incident


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJl
eGFtcGxlX2VsYXN0aWNzZWFyY2hfcXVlcnlfZnJvbV9pbmNpZGVudCIsICJvYmplY3RfdHlwZSI6
ICJpbmNpZGVudCIsICJleHBvcnRfa2V5IjogImV4YW1wbGVfZWxhc3RpY3NlYXJjaF9xdWVyeV9m
cm9tX2luY2lkZW50IiwgInV1aWQiOiAiOTBjNjUwYTctZGE1NS00YmZkLWI0MDktYzkzOGVjNjA4
ZDJiIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYUBhLmNvbSIsICJuYW1lIjogIkV4YW1wbGU6IEVs
YXN0aWNTZWFyY2ggUXVlcnkgZnJvbSBJbmNpZGVudCIsICJjb250ZW50IjogeyJ4bWwiOiAiPD94
bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5z
PVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJw
bW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpv
bWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21n
ZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2ls
aWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDov
L3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9y
Zy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cu
Y2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiZXhhbXBsZV9lbGFzdGljc2VhcmNoX3F1
ZXJ5X2Zyb21faW5jaWRlbnRcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6
IEVsYXN0aWNTZWFyY2ggUXVlcnkgZnJvbSBJbmNpZGVudFwiPjxkb2N1bWVudGF0aW9uPkFuIGV4
YW1wbGUgd2hpY2ggYXR0ZW1wdHMgdG8gcXVlcnkgRWxhc3RpY1NlYXJjaCB1c2luZyBhIHByZS1k
ZWZpbmVkIHF1ZXJ5LiBRdWVyeSBleGFtcGxlcyBhcmUgcHJvdmlkZWQgZHVyaW5nIHdvcmtmbG93
IGNyZWF0aW9uLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1
YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMWU2aDRtZDwvb3V0Z29pbmc+PC9zdGFydEV2
ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzEyOGx4d3ZcIiBuYW1lPVwiRWxhc3Rp
Y1NlYXJjaCBVdGlsaXRpZXM6IFF1ZXJ5XCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxl
eHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI0ZjEwMzQ5MC01OTVk
LTRhYjktYmEzMC04MjAyYzhkZGZlOWRcIj57XCJpbnB1dHNcIjp7fSxcInJlc3VsdF9uYW1lXCI6
XCJcIixcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcImlmIHJlc3VsdHMubWF0Y2hlZF9yZWNv
cmRzOlxcbiAgbm90ZVRleHQgPSBcXFwiXFxcIlxcXCImbHQ7YiZndDtFbGFzdGljU2VhcmNoIFF1
ZXJ5IHN0YXR1cyZsdDsvYiZndDsmbHQ7YnImZ3Q7VG90YWwgbWF0Y2hlZCByZWNvcmRzIDombHQ7
YiZndDt7MH0mbHQ7L2ImZ3Q7XFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLm1hdGNoZWRfcmVj
b3JkcylcXG4gIGluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0
KSlcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5T
ZXF1ZW5jZUZsb3dfMWU2aDRtZDwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wOGJ1
bjIwPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzBuejVy
NzJcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzA4YnVuMjA8L2luY29taW5nPjwvZW5kRXZlbnQ+
PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xZTZoNG1kXCIgc291cmNlUmVmPVwiU3Rh
cnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMTI4bHh3dlwiLz48c2Vx
dWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzA4YnVuMjBcIiBzb3VyY2VSZWY9XCJTZXJ2aWNl
VGFza18xMjhseHd2XCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMG56NXI3MlwiLz48dGV4dEFubm90
YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3Jr
ZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2Np
YXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJl
Zj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdy
YW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1
bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1l
bnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9XCIxODhc
Ii8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5
MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1O
U2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4
aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWln
aHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1O
U2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFzZXVqNDhc
IiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE2OVwi
IHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwi
MTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTkVk
Z2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18xMjhseHd2XCIg
aWQ9XCJTZXJ2aWNlVGFza18xMjhseHd2X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwi
IHdpZHRoPVwiMTAwXCIgeD1cIjMxOC4wNzc3NTAwMDAwMDAwNFwiIHk9XCIxNjUuNTQ3MjUwMDAw
MDAwMDJcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50
PVwiRW5kRXZlbnRfMG56NXI3MlwiIGlkPVwiRW5kRXZlbnRfMG56NXI3Ml9kaVwiPjxvbWdkYzpC
b3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjU2OC4wNTY3NDQxODYwNDY2XCIg
eT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIg
d2lkdGg9XCIwXCIgeD1cIjU4Ni4wNTY3NDQxODYwNDY2XCIgeT1cIjIyN1wiLz48L2JwbW5kaTpC
UE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9
XCJTZXF1ZW5jZUZsb3dfMWU2aDRtZFwiIGlkPVwiU2VxdWVuY2VGbG93XzFlNmg0bWRfZGlcIj48
b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2
XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzE4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9
XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdp
ZHRoPVwiMFwiIHg9XCIyNThcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5k
aTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzA4
YnVuMjBcIiBpZD1cIlNlcXVlbmNlRmxvd18wOGJ1bjIwX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9
XCI0MThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9p
bnQgeD1cIjU2OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6
QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNDkz
XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1u
ZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgIndvcmtm
bG93X2lkIjogImV4YW1wbGVfZWxhc3RpY3NlYXJjaF9xdWVyeV9mcm9tX2luY2lkZW50IiwgInZl
cnNpb24iOiA3OX0sICJ3b3JrZmxvd19pZCI6IDE4LCAiYWN0aW9ucyI6IFtdLCAibGFzdF9tb2Rp
ZmllZF90aW1lIjogMTUzMzg5MzMyMzc1OCwgImNyZWF0b3JfaWQiOiAiYUBhLmNvbSIsICJkZXNj
cmlwdGlvbiI6ICJBbiBleGFtcGxlIHdoaWNoIGF0dGVtcHRzIHRvIHF1ZXJ5IEVsYXN0aWNTZWFy
Y2ggdXNpbmcgYSBwcmUtZGVmaW5lZCBxdWVyeS4gUXVlcnkgZXhhbXBsZXMgYXJlIHByb3ZpZGVk
IGR1cmluZyB3b3JrZmxvdyBjcmVhdGlvbi4ifSwgeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFt
cGxlX2VsYXN0aWNzZWFyY2hfcXVlcnlfZnJvbV9hcnRpZmFjdCIsICJvYmplY3RfdHlwZSI6ICJh
cnRpZmFjdCIsICJleHBvcnRfa2V5IjogImV4YW1wbGVfZWxhc3RpY3NlYXJjaF9xdWVyeV9mcm9t
X2FydGlmYWN0IiwgInV1aWQiOiAiMjlhZmQxMjItMmUyNC00NTE2LWI3NzktODg3YzUwOTYyZjVm
IiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYUBhLmNvbSIsICJuYW1lIjogIkV4YW1wbGU6IEVsYXN0
aWNTZWFyY2ggUXVlcnkgZnJvbSBBcnRpZmFjdCIsICJjb250ZW50IjogeyJ4bWwiOiAiPD94bWwg
dmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwi
aHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5k
aT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdk
Yz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9
XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVu
dD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3
dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8y
MDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2Ft
dW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiZXhhbXBsZV9lbGFzdGljc2VhcmNoX3F1ZXJ5
X2Zyb21fYXJ0aWZhY3RcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IEVs
YXN0aWNTZWFyY2ggUXVlcnkgZnJvbSBBcnRpZmFjdFwiPjxkb2N1bWVudGF0aW9uPjwhW0NEQVRB
W0FuIGV4YW1wbGUgd2hpY2ggYXR0ZW1wdHMgdG8gcXVlcnkgRWxhc3RpY1NlYXJjaCB1c2luZyBk
YXRhIGdhdGhlcmVkIGZyb20gYW4gYXJ0aWZhY3QuIEludGVuZGVkIHRvIGJlIHVzZWQgb24gYW4g
YXJ0aWZhY3Qgb2YgdHlwZSAnU3RyaW5nJ11dPjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBp
ZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMGFldHNpMzwv
b3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzBlNTZy
MjlcIiBuYW1lPVwiRWxhc3RpY1NlYXJjaCBVdGlsaXRpZXM6IFF1ZXJ5XCIgcmVzaWxpZW50OnR5
cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1
aWQ9XCI0ZjEwMzQ5MC01OTVkLTRhYjktYmEzMC04MjAyYzhkZGZlOWRcIj57XCJpbnB1dHNcIjp7
fSxcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiaWYgYXJ0aWZhY3QudmFsdWUgaXMgbm90IE5v
bmU6XFxuICBpbnB1dHMuZXNfcXVlcnkgPSBhcnRpZmFjdC52YWx1ZVwiLFwicG9zdF9wcm9jZXNz
aW5nX3NjcmlwdFwiOlwiaWYgcmVzdWx0cy5tYXRjaGVkX3JlY29yZHM6XFxuICBub3RlVGV4dCA9
IFxcXCJcXFwiXFxcIiZsdDtiJmd0O0VsYXN0aWNTZWFyY2ggUXVlcnkgc3RhdHVzJmx0Oy9iJmd0
OyZsdDticiZndDtUb3RhbCBtYXRjaGVkIHJlY29yZHMgOiZsdDtiJmd0O3swfSZsdDsvYiZndDtc
XFwiXFxcIlxcXCIuZm9ybWF0KHJlc3VsdHMubWF0Y2hlZF9yZWNvcmRzKVxcbiAgaW5jaWRlbnQu
YWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwifTwvcmVzaWxpZW50OmZ1
bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18wYWV0c2kz
PC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzF5ejc3cHc8L291dGdvaW5nPjwvc2Vy
dmljZVRhc2s+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMGdpenFyZFwiPjxpbmNvbWluZz5TZXF1
ZW5jZUZsb3dfMXl6NzdwdzwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwi
U2VxdWVuY2VGbG93XzBhZXRzaTNcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0
YXJnZXRSZWY9XCJTZXJ2aWNlVGFza18wZTU2cjI5XCIvPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1
ZW5jZUZsb3dfMXl6Nzdwd1wiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzBlNTZyMjlcIiB0YXJn
ZXRSZWY9XCJFbmRFdmVudF8wZ2l6cXJkXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5v
dGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90
ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291
cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25f
MWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFt
XzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBN
TlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1
YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9
XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJl
bD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIy
MjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5T
aGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5v
dGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIx
MDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5F
ZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25f
MXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFw
ZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzBlNTZyMjlcIiBpZD1cIlNlcnZpY2VUYXNrXzBl
NTZyMjlfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwi
MzY5XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBt
bkVsZW1lbnQ9XCJFbmRFdmVudF8wZ2l6cXJkXCIgaWQ9XCJFbmRFdmVudF8wZ2l6cXJkX2RpXCI+
PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjQ0XCIgeT1cIjE4
OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9
XCIwXCIgeD1cIjY2MlwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQ
TU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBhZXRz
aTNcIiBpZD1cIlNlcXVlbmNlRmxvd18wYWV0c2kzX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIx
OThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQg
eD1cIjM2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBN
TkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjgzLjVc
IiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRp
OkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzF5ejc3cHdcIiBpZD1cIlNlcXVl
bmNlRmxvd18xeXo3N3B3X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NjlcIiB4c2k6dHlwZT1c
Im9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjY0NFwiIHhzaTp0
eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpC
b3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTU2LjVcIiB5PVwiMTg0XCIvPjwv
YnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9i
cG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAid29ya2Zsb3dfaWQiOiAiZXhhbXBs
ZV9lbGFzdGljc2VhcmNoX3F1ZXJ5X2Zyb21fYXJ0aWZhY3QiLCAidmVyc2lvbiI6IDg4fSwgIndv
cmtmbG93X2lkIjogMTksICJhY3Rpb25zIjogW10sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTMz
ODkzMzM3MTI3LCAiY3JlYXRvcl9pZCI6ICJhQGEuY29tIiwgImRlc2NyaXB0aW9uIjogIkFuIGV4
YW1wbGUgd2hpY2ggYXR0ZW1wdHMgdG8gcXVlcnkgRWxhc3RpY1NlYXJjaCB1c2luZyBkYXRhIGdh
dGhlcmVkIGZyb20gYW4gYXJ0aWZhY3QuIEludGVuZGVkIHRvIGJlIHVzZWQgb24gYW4gYXJ0aWZh
Y3Qgb2YgdHlwZSAnU3RyaW5nJyJ9XSwgImFjdGlvbnMiOiBbeyJsb2dpY190eXBlIjogImFsbCIs
ICJuYW1lIjogIkV4YW1wbGU6IEVsYXN0aWNTZWFyY2ggUXVlcnkgZnJvbSBBcnRpZmFjdCIsICJ2
aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMSwgIndvcmtmbG93cyI6IFsiZXhhbXBsZV9lbGFzdGlj
c2VhcmNoX3F1ZXJ5X2Zyb21fYXJ0aWZhY3QiXSwgIm9iamVjdF90eXBlIjogImFydGlmYWN0Iiwg
InRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidXVpZCI6ICIxZDBkNTBlMy0yYmZjLTQ1ZGUtOTBl
Yy1mMmY0NGE3MTk5ZjQiLCAiYXV0b21hdGlvbnMiOiBbXSwgImV4cG9ydF9rZXkiOiAiRXhhbXBs
ZTogRWxhc3RpY1NlYXJjaCBRdWVyeSBmcm9tIEFydGlmYWN0IiwgImNvbmRpdGlvbnMiOiBbeyJ0
eXBlIjogbnVsbCwgImV2YWx1YXRpb25faWQiOiBudWxsLCAiZmllbGRfbmFtZSI6ICJhcnRpZmFj
dC50eXBlIiwgIm1ldGhvZCI6ICJlcXVhbHMiLCAidmFsdWUiOiAiU3RyaW5nIn1dLCAiaWQiOiAz
MiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW119LCB7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5h
bWUiOiAiRXhhbXBsZTogRWxhc3RpY1NlYXJjaCBRdWVyeSBmcm9tIEluY2lkZW50IiwgInZpZXdf
aXRlbXMiOiBbXSwgInR5cGUiOiAxLCAid29ya2Zsb3dzIjogWyJleGFtcGxlX2VsYXN0aWNzZWFy
Y2hfcXVlcnlfZnJvbV9pbmNpZGVudCJdLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAidGlt
ZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogIjU2MjUyMjZhLTM5MTktNGUxNi05NjZlLTJk
ODlmYTIxZDIxNyIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBF
bGFzdGljU2VhcmNoIFF1ZXJ5IGZyb20gSW5jaWRlbnQiLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQi
OiAzMywgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW119XSwgImxheW91dHMiOiBbXSwgImV4cG9y
dF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDUxLCAiaW5kdXN0cmllcyI6IG51bGwsICJwaGFz
ZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGwsICJzZXJ2ZXJfdmVyc2lv
biI6IHsibWFqb3IiOiAzMCwgInZlcnNpb24iOiAiMzAuMC4zNDc2IiwgImJ1aWxkX251bWJlciI6
IDM0NzYsICJtaW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3BhY2VzIjogW10s
ICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImRpc3BsYXlfbmFtZSI6ICJF
bGFzdGljU2VhcmNoIFV0aWxpdGllczogUXVlcnkiLCAidXVpZCI6ICI0ZjEwMzQ5MC01OTVkLTRh
YjktYmEzMC04MjAyYzhkZGZlOWQiLCAiY3JlYXRvciI6IHsiZGlzcGxheV9uYW1lIjogIlJlc2ls
aWVudCBTeXNhZG1pbiIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAyLCAibmFtZSI6ICJhQGEuY29t
In0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVu
Y3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlk
IiwgImNvbnRlbnQiOiAiYjkyY2MzZWQtMjg3OC00NjMwLTgxYTctNTgzMDc4MGZhNWQ5IiwgInN0
ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5j
dGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQi
LCAiY29udGVudCI6ICIxZTA0MTc3NS1jOWJhLTQzYWUtYThjZi0zZjRkZGE5YTA2ODEiLCAic3Rl
cF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0
aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIs
ICJjb250ZW50IjogImVlZDU1NDQzLTdkODAtNDQ1MS1iMjc1LTMxZjJlMDljM2E4NCIsICJzdGVw
X2xhYmVsIjogbnVsbH1dLCAiZXhwb3J0X2tleSI6ICJmbl9lbGFzdGljc2VhcmNoX3F1ZXJ5Iiwg
Imxhc3RfbW9kaWZpZWRfYnkiOiB7ImRpc3BsYXlfbmFtZSI6ICJSZXNpbGllbnQgU3lzYWRtaW4i
LCAidHlwZSI6ICJ1c2VyIiwgImlkIjogMiwgIm5hbWUiOiAiYUBhLmNvbSJ9LCAibmFtZSI6ICJm
bl9lbGFzdGljc2VhcmNoX3F1ZXJ5IiwgInZlcnNpb24iOiA3NiwgIndvcmtmbG93cyI6IFt7InBy
b2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfZWxhc3RpY3NlYXJjaF9xdWVyeV9mcm9tX2FydGlm
YWN0IiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgInV1aWQiOiBudWxsLCAiYWN0aW9ucyI6
IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBFbGFzdGljU2VhcmNoIFF1ZXJ5IGZyb20gQXJ0aWZhY3Qi
LCAid29ya2Zsb3dfaWQiOiAxOSwgImRlc2NyaXB0aW9uIjogbnVsbH0sIHsicHJvZ3JhbW1hdGlj
X25hbWUiOiAiZXhhbXBsZV9lbGFzdGljc2VhcmNoX3F1ZXJ5X2Zyb21faW5jaWRlbnQiLCAib2Jq
ZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW10sICJuYW1l
IjogIkV4YW1wbGU6IEVsYXN0aWNTZWFyY2ggUXVlcnkgZnJvbSBJbmNpZGVudCIsICJ3b3JrZmxv
d19pZCI6IDE4LCAiZGVzY3JpcHRpb24iOiBudWxsfV0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAx
NTMzODkxNzMxNDYyLCAiZGVzdGluYXRpb25faGFuZGxlIjogImZuX2VsYXN0aWNzZWFyY2giLCAi
aWQiOiAyMSwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50IjogIkEgZnVuY3Rpb24gdGhhdCBhbGxv
d3MgYSB1c2VyIHRvIHF1ZXJ5IGEgc3BlY2lmaWVkIEVsYXN0aWNTZWFyY2ggZGF0YXN0b3JlIGZv
ciBkYXRhLiIsICJmb3JtYXQiOiAidGV4dCJ9fV0sICJub3RpZmljYXRpb25zIjogbnVsbCwgInJl
Z3VsYXRvcnMiOiBudWxsLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVfZGF0ZSI6IDE1MzM4
OTM0ODA4MjIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5h
bCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAi
aWQiOiAwLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAidXBk
YXRlX2RhdGUiOiAxNTMzODkzNDgwODIyLCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQz
OS00YTAwMDQwNDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJl
bnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBbXSwgInR5cGVzIjog
W10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7InV1aWQiOiAiMjhlMmU4YTItZWE2NS00MzBi
LWFiYzMtNDhkMmJiM2Q2MGRiIiwgImV4cG9ydF9rZXkiOiAiZm5fZWxhc3RpY3NlYXJjaCIsICJu
YW1lIjogImZuX2VsYXN0aWNzZWFyY2giLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJwcm9ncmFt
bWF0aWNfbmFtZSI6ICJmbl9lbGFzdGljc2VhcmNoIiwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNl
cnMiOiBbImFAYS5jb20iXX1dLCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVz
IjogW10sICJmaWVsZHMiOiBbeyJvcGVyYXRpb25zIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAi
dXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EiLCAidGVtcGxhdGVz
IjogW10sICJ0eXBlX2lkIjogMCwgImNob3NlbiI6IGZhbHNlLCAidGV4dCI6ICJTaW11bGF0aW9u
IiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNp
ZGVudC9pbmNfdHJhaW5pbmciLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBpcyBh
IHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBpcyByZWFkLW9u
bHkuIiwgInJpY2hfdGV4dCI6IGZhbHNlLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJwcmVmaXgi
OiBudWxsLCAiaW50ZXJuYWwiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAiYmxhbmtfb3B0aW9uIjog
ZmFsc2UsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAiY2hhbmdlYWJsZSI6IHRydWUsICJoaWRl
X25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzOCwgIm5hbWUiOiAiaW5jX3RyYWluaW5nIn0s
IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30s
ICJ0ZXh0IjogImVzX2luZGV4IiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVs
bCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxMDcsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1
aWQiOiAiZWVkNTU0NDMtN2Q4MC00NDUxLWIyNzUtMzFmMmUwOWMzYTg0IiwgImNob3NlbiI6IGZh
bHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiVGhlIGluZGV4IHRoYXQgd2ls
bCBiZSBzZWFyY2hlZCBmb3IgZGF0YS4gSWYgbGVmdCBibGFuayBhbGwgaW5kaWNlcyB3aWxsIGJl
IHNlYXJjaGVkLiIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1w
bGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9lc19pbmRleCIsICJoaWRlX25v
dGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiZXNfaW5kZXgi
LCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0sIHsib3Bl
cmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0
IjogImVzX2RvY190eXBlIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwg
ImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxMDksICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQi
OiAiMWUwNDE3NzUtYzliYS00M2FlLWE4Y2YtM2Y0ZGRhOWEwNjgxIiwgImNob3NlbiI6IGZhbHNl
LCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiVGhlIGRvY3VtZW50IHR5cGUgdGhh
dCB3aWxsIGJlIHNlYXJjaC4iLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNl
LCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vZXNfZG9jX3R5cGUi
LCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjog
ImVzX2RvY190eXBlIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVz
IjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJt
cyI6IHt9LCAidGV4dCI6ICJlc19xdWVyeSIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZp
eCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTA4LCAicmVhZF9vbmx5IjogZmFs
c2UsICJ1dWlkIjogImI5MmNjM2VkLTI4NzgtNDYzMC04MWE3LTU4MzA3ODBmYTVkOSIsICJjaG9z
ZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dGFyZWEiLCAidG9vbHRpcCI6ICJUaGUgcXVl
cnkgdGhhdCB3aWxsIGJlIHN1Ym1pdHRlZCB0byBFbGFzdGljU2VhcmNoIiwgImludGVybmFsIjog
ZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFt7InRlbXBsYXRlIjogeyJj
b250ZW50IjogIntcbiAgICBcInF1ZXJ5XCI6IHtcbiAgICAgICAgXCJtYXRjaF9hbGxcIjoge31c
biAgICB9XG59IiwgImZvcm1hdCI6ICJ0ZXh0In0sICJ1dWlkIjogIjI0NTdjOGQwLTJiMTktNDc1
Ni05YTFhLTRlNjQxMDY5ZDIzOSIsICJuYW1lIjogIm1hdGNoX2FsbCIsICJpZCI6IDh9LCB7InRl
bXBsYXRlIjogeyJjb250ZW50IjogIntcbiAgICBcInNvcnRcIiA6IFtcbiAgICAgICAgeyBcIjxT
T1JUX1ZBTFVFPlwiIDogXCJkZXNjXCIgfVxuICAgIF0sXG4gICAgXCJxdWVyeVwiIDoge1xuICAg
ICAgICBcInRlcm1cIiA6IDxURVJNX1RPX0JFX1NFQVJDSEVEPlxuICAgIH1cbn0iLCAiZm9ybWF0
IjogInRleHQifSwgInV1aWQiOiAiMjRhMzE5MWItZDFiMy00MWIxLTk5YzAtMWQyMjkwYmEzNmVk
IiwgIm5hbWUiOiAibWF0Y2hfdGVybV9zb3J0ZWQiLCAiaWQiOiA2fSwgeyJ0ZW1wbGF0ZSI6IHsi
Y29udGVudCI6ICJ7XG4gICAgXCJxdWVyeVwiIDoge1xuICAgICAgICBcInRlcm1cIiA6IHs8VEVS
TV9UT19CRV9TRUFSQ0hFRD59XG4gICAgfVxufSIsICJmb3JtYXQiOiAidGV4dCJ9LCAidXVpZCI6
ICIyYzk5ZDgwNC0zNmI3LTRkYTctYThjYi1hZmEwMjRlZDZiNWQiLCAibmFtZSI6ICJtYXRjaF90
ZXJtIiwgImlkIjogN31dLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2VzX3F1ZXJ5IiwgImhp
ZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJlc19x
dWVyeSIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInJlcXVpcmVkIjogImFs
d2F5cyIsICJ2YWx1ZXMiOiBbXX1dLCAib3ZlcnJpZGVzIjogW10sICJleHBvcnRfZGF0ZSI6IDE1
MzM4OTMzNjYxOTd9
"""
    )
