def create_rules_to_secutity_groups(sec_group, rules, conn):
    
    example_rule = conn.network.create_security_group_rule(
    security_group_id = sec_group.id,
    direction = rules.direction,
    remote_ip_prefix = rules.remote_ip_prefix,
    protocol = rules.protocol,
    port_range_max = rules.port_range_max,
    port_range_min = rules.port_range_min,
    ethertype = rules.ethertype)
    
    return example_rule