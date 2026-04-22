# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing_extensions import Final

from opentelemetry.metrics import Counter, Meter, UpDownCounter

NFS_CLIENT_NET_COUNT = "nfs.client.net.count"
"""
Reports the count of kernel NFS client TCP segments and UDP datagrams handled
Instrument
Unit: {record}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.netudpcnt and svc_stat.nettcpcnt.
"""


def create_nfs_client_net_count(meter):
    """Reports the count of kernel NFS client TCP segments and UDP datagrams handled"""
    return meter.create_counter(
        name=NFS_CLIENT_NET_COUNT,
        description="Reports the count of kernel NFS client TCP segments and UDP datagrams handled.",
        unit="{record}",
    )


NFS_CLIENT_NET_TCP_CONNECTION_ACCEPTED = (
    "nfs.client.net.tcp.connection.accepted"
)
"""
Reports the count of kernel NFS client TCP connections accepted
Instrument
Unit: {connection}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.nettcpconn.
"""


def create_nfs_client_net_tcp_connection_accepted(meter):
    """Reports the count of kernel NFS client TCP connections accepted"""
    return meter.create_counter(
        name=NFS_CLIENT_NET_TCP_CONNECTION_ACCEPTED,
        description="Reports the count of kernel NFS client TCP connections accepted.",
        unit="{connection}",
    )


NFS_CLIENT_OPERATION_COUNT = "nfs.client.operation.count"
"""
Reports the count of kernel NFSv4+ client operations
Instrument
Unit: {operation}
"""


def create_nfs_client_operation_count(meter):
    """Reports the count of kernel NFSv4+ client operations"""
    return meter.create_counter(
        name=NFS_CLIENT_OPERATION_COUNT,
        description="Reports the count of kernel NFSv4+ client operations.",
        unit="{operation}",
    )


NFS_CLIENT_PROCEDURE_COUNT = "nfs.client.procedure.count"
"""
Reports the count of kernel NFS client procedures
Instrument
Unit: {procedure}
"""


def create_nfs_client_procedure_count(meter):
    """Reports the count of kernel NFS client procedures"""
    return meter.create_counter(
        name=NFS_CLIENT_PROCEDURE_COUNT,
        description="Reports the count of kernel NFS client procedures.",
        unit="{procedure}",
    )


NFS_CLIENT_RPC_AUTHREFRESH_COUNT = "nfs.client.rpc.authrefresh.count"
"""
Reports the count of kernel NFS client RPC authentication refreshes
Instrument
Unit: {authrefresh}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.rpcauthrefresh.
"""


def create_nfs_client_rpc_authrefresh_count(meter):
    """Reports the count of kernel NFS client RPC authentication refreshes"""
    return meter.create_counter(
        name=NFS_CLIENT_RPC_AUTHREFRESH_COUNT,
        description="Reports the count of kernel NFS client RPC authentication refreshes.",
        unit="{authrefresh}",
    )


NFS_CLIENT_RPC_COUNT = "nfs.client.rpc.count"
"""
Reports the count of kernel NFS client RPCs sent, regardless of whether they're accepted/rejected by the server
Instrument
Unit: {request}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.rpccnt.
"""


def create_nfs_client_rpc_count(meter):
    """Reports the count of kernel NFS client RPCs sent, regardless of whether they're accepted/rejected by the server"""
    return meter.create_counter(
        name=NFS_CLIENT_RPC_COUNT,
        description="Reports the count of kernel NFS client RPCs sent, regardless of whether they're accepted/rejected by the server.",
        unit="{request}",
    )


NFS_CLIENT_RPC_RETRANSMIT_COUNT = "nfs.client.rpc.retransmit.count"
"""
Reports the count of kernel NFS client RPC retransmits
Instrument
Unit: {retransmit}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.rpcretrans.
"""


def create_nfs_client_rpc_retransmit_count(meter):
    """Reports the count of kernel NFS client RPC retransmits"""
    return meter.create_counter(
        name=NFS_CLIENT_RPC_RETRANSMIT_COUNT,
        description="Reports the count of kernel NFS client RPC retransmits.",
        unit="{retransmit}",
    )


NFS_SERVER_FH_STALE_COUNT = "nfs.server.fh.stale.count"
"""
Reports the count of kernel NFS server stale file handles
Instrument
Unit: {fh}
Note: Linux: this metric is taken from the Linux kernel NFSD_STATS_FH_STALE counter in the nfsd_net struct.
"""


def create_nfs_server_fh_stale_count(meter):
    """Reports the count of kernel NFS server stale file handles"""
    return meter.create_counter(
        name=NFS_SERVER_FH_STALE_COUNT,
        description="Reports the count of kernel NFS server stale file handles.",
        unit="{fh}",
    )


NFS_SERVER_IO = "nfs.server.io"
"""
Reports the count of kernel NFS server bytes returned to receive and transmit (read and write) requests
Instrument
Unit
Note: Linux: this metric is taken from the Linux kernel NFSD_STATS_IO_READ and NFSD_STATS_IO_WRITE counters in the nfsd_net struct.
"""


def create_nfs_server_io(meter):
    """Reports the count of kernel NFS server bytes returned to receive and transmit (read and write) requests"""
    return meter.create_counter(
        name=NFS_SERVER_IO,
        description="Reports the count of kernel NFS server bytes returned to receive and transmit (read and write) requests.",
        unit="By",
    )


NFS_SERVER_NET_COUNT = "nfs.server.net.count"
"""
Reports the count of kernel NFS server TCP segments and UDP datagrams handled
Instrument
Unit: {record}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.nettcpcnt and svc_stat.netudpcnt.
"""


def create_nfs_server_net_count(meter):
    """Reports the count of kernel NFS server TCP segments and UDP datagrams handled"""
    return meter.create_counter(
        name=NFS_SERVER_NET_COUNT,
        description="Reports the count of kernel NFS server TCP segments and UDP datagrams handled.",
        unit="{record}",
    )


NFS_SERVER_NET_TCP_CONNECTION_ACCEPTED = (
    "nfs.server.net.tcp.connection.accepted"
)
"""
Reports the count of kernel NFS server TCP connections accepted
Instrument
Unit: {connection}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.nettcpconn.
"""


def create_nfs_server_net_tcp_connection_accepted(meter):
    """Reports the count of kernel NFS server TCP connections accepted"""
    return meter.create_counter(
        name=NFS_SERVER_NET_TCP_CONNECTION_ACCEPTED,
        description="Reports the count of kernel NFS server TCP connections accepted.",
        unit="{connection}",
    )


NFS_SERVER_OPERATION_COUNT = "nfs.server.operation.count"
"""
Reports the count of kernel NFSv4+ server operations
Instrument
Unit: {operation}
"""


def create_nfs_server_operation_count(meter):
    """Reports the count of kernel NFSv4+ server operations"""
    return meter.create_counter(
        name=NFS_SERVER_OPERATION_COUNT,
        description="Reports the count of kernel NFSv4+ server operations.",
        unit="{operation}",
    )


NFS_SERVER_PROCEDURE_COUNT = "nfs.server.procedure.count"
"""
Reports the count of kernel NFS server procedures
Instrument
Unit: {procedure}
"""


def create_nfs_server_procedure_count(meter):
    """Reports the count of kernel NFS server procedures"""
    return meter.create_counter(
        name=NFS_SERVER_PROCEDURE_COUNT,
        description="Reports the count of kernel NFS server procedures.",
        unit="{procedure}",
    )


NFS_SERVER_REPCACHE_REQUESTS = "nfs.server.repcache.requests"
"""
Reports the kernel NFS server reply cache request count by cache hit status
Instrument
Unit: {request}
"""


def create_nfs_server_repcache_requests(meter):
    """Reports the kernel NFS server reply cache request count by cache hit status"""
    return meter.create_counter(
        name=NFS_SERVER_REPCACHE_REQUESTS,
        description="Reports the kernel NFS server reply cache request count by cache hit status.",
        unit="{request}",
    )


NFS_SERVER_RPC_COUNT = "nfs.server.rpc.count"
"""
Reports the count of kernel NFS server RPCs handled
Instrument
Unit: {request}
Note: Linux: this metric is taken from the Linux kernel's svc_stat.rpccnt, the count of good RPCs. This metric can have
an error.type of "format", "auth", or "client" for svc_stat.badfmt, svc_stat.badauth, and svc_stat.badclnt.
"""


def create_nfs_server_rpc_count(meter):
    """Reports the count of kernel NFS server RPCs handled"""
    return meter.create_counter(
        name=NFS_SERVER_RPC_COUNT,
        description="Reports the count of kernel NFS server RPCs handled.",
        unit="{request}",
    )


NFS_SERVER_THREAD_COUNT = "nfs.server.thread.count"
"""
Reports the count of kernel NFS server available threads
Instrument
Unit: {thread}
Note: Linux: this metric is taken from the Linux kernel nfsd_th_cnt variable.
"""


def create_nfs_server_thread_count(meter):
    """Reports the count of kernel NFS server available threads"""
    return meter.create_up_down_counter(
        name=NFS_SERVER_THREAD_COUNT,
        description="Reports the count of kernel NFS server available threads.",
        unit="{thread}",
    )
