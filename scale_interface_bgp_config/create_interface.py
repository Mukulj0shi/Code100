#!usr/bin/env python3


# Create subinterfaces, assign ip address and dot1q encapsulation
increment = 4
def create_interface():
    #interface_config = ["interface eth 1/(no).(subinterface)",  "encapsulation dot1q " + str(subinterface)]
    interface_name = input("Enter interface name(eth1/1): ")
    first_3_octet = input("Enter first 3 octet(192.12.8): ")
    number_of_subinterface = input("Enter number of subinterfaces(1): ")
    device_location = input("Enter device is upstream or downstream(u/d): ").lower()
    ip_for_downstream = 2
    ip_for_upstream = 129
    neighhbor_ip = []
    for subinterface in range(100, 100 + int(number_of_subinterface)):
        print(f"interface {interface_name}.{str(subinterface)}")
        print(f"encapsulation dot1q {str(subinterface)}")
        print(f"no shutdown")
        if device_location == "u":
            neighbor_ip_address = first_3_octet + "." + str(ip_for_upstream+1)
            print(f"ip address {first_3_octet}.{str(ip_for_upstream)}/30")
            ip_for_upstream += increment
            neighhbor_ip.append(neighbor_ip_address)
        if device_location == "d":
            neighbor_ip_address = first_3_octet + "." + str(ip_for_downstream-1)
            print(f"ip address {first_3_octet}.{str(ip_for_downstream)}/30")
            ip_for_downstream += increment
            neighbor_ip.append(neighbor_ip_address)
    return neighhbor_ip

def create_bgp():
    my_as = input("Enter AS number(1): ")
    nei_as = input("Enter nei AS number(1): ")
    neighbor_address = create_interface()
    print(f"router bgp 650{my_as}")
    for ip in neighbor_address:
        print(f"neighbor {ip}")
        print(f"inherit peer-session T3-0{nei_as}")
        print(f"address-family ipv4 unicast")




create_bgp()