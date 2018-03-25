#coding=utf-8

# 一次性分割多种分隔符的情况

import re

s = 'ad,fhd|fdknj,,fdh\tfdg\tgd|gdf|\t,gfd'

print s

new_s = re.split(r'[,|\t]+', s)
print new_s