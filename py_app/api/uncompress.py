# RA, 2019-01-22
# Compress and decompress a JSON object

# License: CC0 -- "No rights reserved"

# For zlib license, see https://docs.python.org/3/license.html
import zlib

import json, base64

ZIPJSON_KEY = 'base64(zip(o))'


def json_unzip(j, insist=True):
    try:
        assert (j[ZIPJSON_KEY])
        assert (set(j.keys()) == {ZIPJSON_KEY})
    except:
        if insist:
            raise RuntimeError("JSON not in the expected format {" + str(ZIPJSON_KEY) + ": zipstring}")
        else:
            return j

    try:
        j = zlib.decompress(base64.b64decode(j[ZIPJSON_KEY]))
    except:
        raise RuntimeError("Could not decode/unzip the contents")

    try:
        j = json.loads(j)
    except:
        raise RuntimeError("Could interpret the unzipped contents")

    return j


def main(datacompress):
    datacompress = datacompress.replace("\'", "\"")
    datacompress = json.loads(datacompress)
    
    outdata = json_unzip(datacompress)
    # print(outdata)
    return outdata