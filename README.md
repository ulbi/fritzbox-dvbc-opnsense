# Accessing FRITZ!Box 6591 Cable IPTV Streams Through an OPNsense Firewall: Complete Guide

## Background

We use the FRITZ!Box 6591 Cable modem equipped with DVB-C functionality, providing up to 4 IPTV streams that can be accessed via any compatible IPTV client. Additionally, an OPNsense firewall is implemented between the FRITZ!Box and our internal network. This firewall segregates the network into different segments for IoT devices and other equipment while managing both inbound and outbound access rules.

## Challenge

The specific challenge is the lack of documentation on how to access the FRITZ!Box 6591 Cable IPTV streams through the OPNsense firewall, especially when it involves RTP (Real-time Transport Protocol) streams.

## Objectives

1. Enable the RTP streams from the FRITZ!Box to flow to the end devices through the OPNsense firewall.
2. Document the procedure for this particular scenario.

## Steps

### Prerequisites

**Network Diagram**: Maintain a detailed network diagram outlining device interconnections.

### OPNsense Configuration

1. **Login**: Access the OPNsense admin console.

2. **Port 554 Rule**:
   - Navigate to `Firewall > Rules`.
   - Add a new rule:
     - **Action**: Pass
     - **Interface**: LAN
     - **Protocol**: TCP/UDP
     - **Source**: LAN network
     - **Destination**: WAN address
     - **Destination Ports**: 554
   - Save and apply the configuration.

3. **General Rules**:
   - Navigate to `Firewall > Rules`.
   - Add a new rule:
     - **Action**: Pass
     - **Interface**: Interface connecting to the FRITZ!Box
     - **Protocol**: UDP
     - **Source**: FRITZ!Box IP address
     - **Source Port Range**: 5000-5010
     - **Destination**: Your LAN Net
   - Save and apply the configuration.

4. **One-to-One NAT**:
   - Navigate to `Firewall > NAT > One-to-One`.
   - Add a new rule:
     - **Interface**: WAN
     - **External subnet IP**: 192.168.180.0
     - **Internal IP**: Network 192.168.178.0
   - Save and apply the configuration.

### FRITZ!Box Configuration

1. **IPv4 Routes**:
   - Access the FRITZ!Box admin console.
   - Navigate to `Internet > Permit Access > IPv4 Routes`.
   - Add a new route:
     - **Network**: 192.168.180.0
     - **Subnet Mask**: Appropriate subnet mask
     - **Gateway**: WAN IP address of the firewall
   - Save and apply the changes.

### Testing and Monitoring

1. **Test Streams**: Validate the setup with an IPTV client to ensure the streams pass through the firewall successfully.
2. **Monitoring and Logging**: Activate OPNsense logs specifically for these new rules to monitor the traffic and troubleshoot any issues.

## Final Notes

Upon successful configuration, IPTV clients in the internal network should be able to access the FRITZ!Box 6591 Cable's IPTV streams. Ongoing monitoring and logging are recommended to ensure continuous and smooth operation.
