#!/bin/sh
# An example script for running in Unix-based environments.

# The EVENTDATA environment variable is the location
# of a temporary file containing the incident data in JSON.
# You can read the contents of that file using tools such as:
#      jq (https://stedolan.github.io/jq/),
#      jsawk (https://github.com/micha/jsawk), etc.

echo "this is $EVENTDATA"
cat "$EVENTDATA"
 
# The result (i.e. the console output) is attached as a file.
# With different "disposition" configured in the integration config-file,
# you can instead return JSON structures that update the incident,
# add artifacts, and other operations.
