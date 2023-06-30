# CS_logfixer
Stitch back together long output on Cobalt Strike

For stiching back together output in CS logs without splitting it up.

Who needs to drop output to disk anyway? (and then risk getting caught, and then download, and then sync).  Just send the long output to the terminal and use this to see it in its pristine form (looking at you BloodHound json collect)


## In
```
06/22 02:47:14 UTC [task] <T1093> Tasked beacon to spawn Spray-AD
06/22 02:47:14 UTC [checkin] host called home, sent: 127532 bytes
06/22 02:47:19 UTC [output]
received output:
[*] Sprayed Accounts: 100


06/22 02:47:21 UTC [output]
received output:
[*] Sprayed Accounts: 200


06/22 02:47:24 UTC [output]
received output:
[*] Sprayed Accounts: 300


06/22 02:47:27 UTC [output]
received output:
[*] Sprayed Accounts: 400


06/22 02:47:30 UTC [output]
received output:
[*] Sprayed Accounts: 500


06/22 02:47:31 UTC [output]
received output:
--------------------------------------------------------------------
Program execution time: 15.78 seconds

Total AD accounts tested: 420
Failed Kerberos authentications: 420
Successful Kerberos authentications: 0
--------------------------------------------------------------------
```


## Out
```
06/22 02:47:14 UTC [task] <T1093> Tasked beacon to spawn Spray-AD
06/22 02:47:14 UTC [checkin] host called home, sent: 127532 bytes
06/22 02:47:19 UTC [output]
received output:
[*] Sprayed Accounts: 100
[*] Sprayed Accounts: 200
[*] Sprayed Accounts: 300
[*] Sprayed Accounts: 400
[*] Sprayed Accounts: 500
--------------------------------------------------------------------
Program execution time: 15.78 seconds

Total AD accounts tested: 420
Failed Kerberos authentications: 420
Successful Kerberos authentications: 0
--------------------------------------------------------------------
```
