#!/usr/bin/python
import pexpect
child = pexpect.spawn('ssh -q -o StrictHostKeyChecking=no admin@10.192.33.12')
child.expect("assword")
child.sendline("infoblox")
child.expect(">")
child.sendline ("set support_access")
child.expect (":")
child.sendline("y")
child.expect (":")
child.sendline("y")
print child.read()

print(out)
