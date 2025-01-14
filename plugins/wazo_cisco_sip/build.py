# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

# Depends on the following external programs:
#  -rsync
from __future__ import annotations

from typing import TYPE_CHECKING, Callable
from subprocess import check_call

if TYPE_CHECKING:

    def target(
        target_id: str, plugin_id: str, std_dirs: bool = True
    ) -> Callable[[str], None]:
        """The `target` method is injected in `exec` call by the build script."""
        return lambda x: None


@target('9.3', 'wazo-cisco-sip-9.3')
def build_9_3(path: str) -> None:
    check_call(['rsync', '-rlp', '--exclude', '.*', 'common/', path])
    check_call(['rsync', '-rlp', '--exclude', '.*', 'v9_3/', path])


@target('11.1.0', 'wazo-cisco-sip-11.1.0')
def build_11_1_0(path: str) -> None:
    check_call(['rsync', '-rlp', '--exclude', '.*', 'v11_1_0/', path])


@target('11.3.1', 'wazo-cisco-sip-11.3.1')
def build_11_3_1(path: str) -> None:
    check_call(['rsync', '-rlp', '--exclude', '.*', 'v11_3_1/', path])


@target('12.0.1', 'wazo-cisco-sip-12.0.1')
def build_12_0_1(path: str) -> None:
    check_call(['rsync', '-rlp', '--exclude', '.*', 'v12_0_1/', path])
