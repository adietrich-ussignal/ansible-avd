---
search:
  boost: 2
---

# Endpoint Security

## Global 802.1x Authentication

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dot1x</samp>](## "dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;system_auth_control</samp>](## "dot1x.system_auth_control") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol_lldp_bypass</samp>](## "dot1x.protocol_lldp_bypass") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x.dynamic_authorization") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mac_based_authentication</samp>](## "dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "dot1x.mac_based_authentication.delay") | Integer |  |  | Min: 0<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hold_period</samp>](## "dot1x.mac_based_authentication.hold_period") | Integer |  |  | Min: 1<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;radius_av_pair</samp>](## "dot1x.radius_av_pair") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_type</samp>](## "dot1x.radius_av_pair.service_type") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;framed_mtu</samp>](## "dot1x.radius_av_pair.framed_mtu") | Integer |  |  | Min: 68<br>Max: 9236 |  |

=== "YAML"

    ```yaml
    dot1x:
      system_auth_control: <bool>
      protocol_lldp_bypass: <bool>
      dynamic_authorization: <bool>
      mac_based_authentication:
        delay: <int>
        hold_period: <int>
      radius_av_pair:
        service_type: <bool>
        framed_mtu: <int>
    ```
