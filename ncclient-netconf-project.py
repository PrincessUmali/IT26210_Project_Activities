from ncclient import manager
import xml.dom.minidom
m = manager.connect(
 host="192.168.56.101",
 port=830,
 username="cisco",
 password="cisco123!",
 hostkey_verify=False
 )
# '''
# print("#Supported Capabilities (YANG models):")
# for capability in m.server_capabilities:
#  print(capability)
# '''

# '''netconf_reply = m.get_config(source="running")
# print(netconf_reply)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
# '''

netconf_filter = """
<filter>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_banner = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<banner>
<motd>
    <banner>#WARNING: Use of this system should only be for official purposes only and
            unauthorized access or use of this equipment is prohibited and constitutes an offence
            under the Computer Misuse Act 1990.#</banner>
</motd>
</banner>
</native>
</config>
"""
# netconf_reply = m.edit_config(target="running", config=netconf_banner)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_pw = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<enable>
<password>
<type>0</type>
<secret>cisco</secret>
</password>
</enable>
</native>
</config>
"""

# netconf_reply = m.edit_config(target="running", config=netconf_pw)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


netconf_encryp = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<service>
<password-encryption/>
</service>
</native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_encryp)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())