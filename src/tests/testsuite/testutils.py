#!/usr/bin/python
#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#

# Copyright (c) 2010, 2022, Oracle and/or its affiliates.

import os
import sys

# Set the path so that modules can be found. Force this to
# be a relative path due to Python 3.9 issue 44070 which
# has __file__ always returning an absolute path.
path_to_parent = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, path_to_parent)

import pkg5testenv


def setup_environment(proto):
        pkg5testenv.setup_environment(proto)
