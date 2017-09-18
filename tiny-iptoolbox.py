#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
print "\n"
print "#################################"
print "\n"
print "It's Tiny IP toolbox"
print "\n"
print "#################################"
def subnet_calc():
    try:
        print "\n"
        
        # IP Bestatigen
        while True:
            ip_address = raw_input("Geben Sie eine IP-Addresse: ")
        # Eine slicer !

            
            #Überprüfen Oktetts           
            a = ip_address.split('.')
                        
            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                break
            
            else:
                print "\nWas zum Teufel?!\n"
                continue
        
        # definieren subnets
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        
        #Checking Subnet Mask validity
        while True:
            subnet_mask = raw_input("Geben Sie eine Netmask auf IP-Addressen: ")
            
            #Checking octets            
            b = subnet_mask.split('.')
            
            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break
            
            else:
                print "\nWas zum Teufel?!\n"
                continue
         
		 
        # Algorithmus für Subnetz Identifizierung, basierend auf IP und Subnet Mask
        
        # Konvertieren Maske, um Binär-String
        mask_octets_padded = []
        mask_octets_decimal = subnet_mask.split(".")
        # print mask_octets_decimal
        
        for octet_index in range(0, len(mask_octets_decimal)):
            
            #print bin(int(mask_octets_decimal[octet_index]))
            
            binary_octet = bin(int(mask_octets_decimal[octet_index])).split("b")[1]
            #print binary_octet
            
            if len(binary_octet) == 8:
                mask_octets_padded.append(binary_octet)
            
            elif len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                mask_octets_padded.append(binary_octet_padded)
                
        #print mask_octets_padded
        
        decimal_mask = "".join(mask_octets_padded)
        #print decimal_mask   #Example: for 255.255.255.0 => 11111111111111111111111100000000
        
        # Zählen Host-Bits in der Maske und der Berechnung Anzahl Rechner / Subnetz
        no_of_zeros = decimal_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        # Rück positiven Wert für Maske / 32
        no_of_hosts = abs(2 ** no_of_zeros - 2) 
        
        #print no_of_zeros
        #print no_of_ones
        #print no_of_hosts
        
        # Beziehen Wildcard-Maske
        wildcard_octets = []
        for w_octet in mask_octets_decimal:
            wild_octet = 255 - int(w_octet)
            wildcard_octets.append(str(wild_octet))
            
        #print wildcard_octets
        
        wildcard_mask = ".".join(wildcard_octets)
        #print wildcard_mask
        
        
        # Konvertieren Sie IP, um Binär-String
        ip_octets_padded = []
        ip_octets_decimal = ip_address.split(".")
        
        for octet_index in range(0, len(ip_octets_decimal)):
            
            binary_octet = bin(int(ip_octets_decimal[octet_index])).split("b")[1]
            
            if len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                ip_octets_padded.append(binary_octet_padded)
            
            else:
                ip_octets_padded.append(binary_octet)
    
        #print ip_octets_padded
        
        binary_ip = "".join(ip_octets_padded)
    
        #print binary_ip   #Beispiel: für 192.168.2.100 => 11000000101010000000001001100100
        
        # Besorgen Sie sich die Netzwerkadresse und Broadcast-Adresse aus den binären Strings oben erhalten
        
        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        #print network_address_binary
        
        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        #print broadcast_address_binary
        
        net_ip_octets = []
        for octet in range(0, len(network_address_binary), 8):
            net_ip_octet = network_address_binary[octet:octet+8]
            net_ip_octets.append(net_ip_octet)
        
        #print net_ip_octets
        
        net_ip_address = []
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))
            
        #print net_ip_address
        
        network_address = ".".join(net_ip_address)
        #print network_address
        
        bst_ip_octets = []
        for octet in range(0, len(broadcast_address_binary), 8):
            bst_ip_octet = broadcast_address_binary[octet:octet+8]
            bst_ip_octets.append(bst_ip_octet)
        
        #print bst_ip_octets
        
        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))
            
        #print bst_ip_address
        
        broadcast_address = ".".join(bst_ip_address)
        
        #print broadcast_address
        

        
        # Ergebnisse für selected IP/mask
        print "\n"
                # Berechnung der Klasse der IP-Adresse
        firstoctet, secondoctet, thirdocted, fourthocted = ip_address.split('.')
        if int(firstoctet) <= 126:
            print 'IP-Addresse klass ist: A'
        elif 128 >= int(firstoctet) <=  191:
            print "IP-Addresse klass ist: B"
        elif 192 >= int(firstoctet) <= 223:
            print "IP-Addresse klass ist: C"
        elif 224 >= int(firstoctet) <= 239:
            print "IP-Addresse klass ist: D"
        else:
            print "IP-Addresse klass ist: E"
        print "Netzwerkadresse ist: %s" % network_address
        print "Broadcast-Adresse ist: %s" % broadcast_address
        print "Anzahl der gültigen Hosts pro Subnetz: %s" % no_of_hosts
        print "Wildcard-Maske: %s" % wildcard_mask
        print "Maskenbits(Standard CIDR): %s" % no_of_ones
        print "\n"
    except KeyboardInterrupt:
        print "\n\nProgramm vom Benutzer abgebrochen. Beendet .....\n"
        sys.exit()

subnet_calc()
