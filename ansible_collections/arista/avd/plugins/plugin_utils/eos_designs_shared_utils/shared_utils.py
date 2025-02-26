from .bgp_peer_groups import BgpPeerGroupsMixin
from .inband_management import InbandManagementMixin
from .interface_descriptions import InterfaceDescriptionsMixin
from .ip_addressing import IpAddressingMixin
from .link_tracking_groups import LinkTrackingGroupsMixin
from .mgmt import MgmtMixin
from .misc import MiscMixin
from .mlag import MlagMixin
from .node_type_key import NodeTypeKeyMixin
from .overlay import OverlayMixin
from .platform import PlatformMixin
from .ptp import PtpMixin
from .routing import RoutingMixin
from .switch_data import SwitchDataMixin
from .underlay import UnderlayMixin
from .utils import UtilsMixin


class SharedUtils(
    BgpPeerGroupsMixin,
    InbandManagementMixin,
    InterfaceDescriptionsMixin,
    IpAddressingMixin,
    LinkTrackingGroupsMixin,
    MgmtMixin,
    MlagMixin,
    MiscMixin,
    NodeTypeKeyMixin,
    OverlayMixin,
    PlatformMixin,
    PtpMixin,
    SwitchDataMixin,
    RoutingMixin,
    UnderlayMixin,
    UtilsMixin,
):
    """
    Class with commonly used methods / cached_properties to be shared between all the python_modules
    loaded in eos_designs.

    This class is instatiated in 'EosDesignsFacts' class and set as 'shared_utils' property.
    This class is also instaticated in 'yaml_templates_to_facts' and the instance is given as argument to
    each python module. The base class '__init__' will set the instance as 'shared_utils' property.

    Since these methods / cached_properties will not be rendered automatically, we can avoid some of the
    general conditions and just return the value. We expect the logic that determines the relevancy of the
    value to be handled in calling function.

    The class cannot be overriden.
    """

    def __init__(self, hostvars: dict, templar) -> None:
        self.hostvars = hostvars
        self.templar = templar
