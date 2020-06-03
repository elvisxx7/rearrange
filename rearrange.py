#!/usr/bin/env python3

import re

def rearrange_name(name):
	result = re.search(r"([\w]*),?\s*(\w*)\s*(\w\.)?$", name)
	if result.group(3) != None:
		return "{} {} {}".format(result[2], result[3], result[1])
	elif result.group(2) != '':
		return "{} {}".format(result[2], result[1])
	elif result.group(1) != None:
		return  "{}".format(result[1])
