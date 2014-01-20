import os
os.rename( "e:/kv.txt", "e:/ag.txt" )
 Delete file test2.txt
os.remove("text2.txt")

#os.mkdir("newdir")
#os.chdir("/home/newdir")
print(os.getcwd())

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )

