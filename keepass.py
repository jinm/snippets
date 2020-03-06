import os
import os.path
import libkeepass


def keepass(kpfile, keyfile, password):
  
  if os.path.exists(kpfile) and os.access(kpfile, os.R_OK) and
     os.path.exists(keyfile) and os.access(keyfile, os.R_OK):
      with libkeepass.open(kpfile, password=password, keyfile=keyfile) as kp:
          result = kp.pretty_print()
          kp.protect()
          
          # obj_root to search
          # kp.obj_root.findall(".//Entry")
   else:
       print(f'Keepass file {kpfile} or keyfile {keyfile} are not accessible')
       raise
       
   return result
