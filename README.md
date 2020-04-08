# Distributed-KoT-Framework
framework for IRC synchronized, distributed KoT play client using token passing

This framework provides a distributed play client for a tabletop game. 
* Game state is synchronized between clients using a state delta message
* IRC is used as the WAN mechanism
* clients generate a shared session key to encrypt delta messages as a mechanism to deconflict from other play sessions in progress (CDMA over IRC)
* IRC Bot managed token passing to mediate game play (?)

Facility to extend the power card library
* Custom card mechanisms
* Restriction to standard cards option
* Removal of standard cards from deck

"House rules" capability


