def identificar_tipo_acl(acl):
    if acl.startswith("access-list"):
        acl_type = acl.split()[2]
        if acl_type.isdigit():
            acl_num = int(acl_type)
            if acl_num >= 1 and acl_num <= 99:
                print("ACL Estándar")
            elif acl_num >= 100 and acl_num <= 199:
                print("ACL Extendida")
            else:
                print("El número no corresponde a una lista de acceso.")
        else:
            print("El número no corresponde a una lista de acceso.")
    elif acl.startswith("ip access-list"):
        acl_type = acl.split()[3]
        if acl_type.isdigit():
            acl_num = int(acl_type)
            if acl_num >= 1 and acl_num <= 99:
                print("ACL Estándar")
            elif acl_num >= 100 and acl_num <= 199:
                print("ACL Extendida")
            else:
                print("El número no corresponde a una lista de acceso.")
        else:
            print("El número no corresponde a una lista de acceso.")
    else:
        print("El número no corresponde a una lista de acceso.")
