#!/usr/bin/env python3
#
# Copyright (c) 2015-2018 Intel, Inc. All rights reserved.
# $COPYRIGHT$
#
# Additional copyrights may follow
#
# $HEADER$
#


from yapsy.IPlugin import IPlugin

## @addtogroup Stages
# @{
# @addtogroup Reporter
# [Ordering 600] Report tests results stage
# @}
class ReporterMTTStage(IPlugin):
    def __init__(self):
        # initialise parent class
        IPlugin.__init__(self)
    def print_name(self):
        print("Report test results stage")

    def ordering(self):
        return 600
