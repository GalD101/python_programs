import pwn
import re

# bytes_arr = [0b01110011, 0b01110101, 0b01100010, 0b01101101, 0b01100001, 0b01110010, 0b01101001, 0b01101110, 0b01100101]

url, port = "jupiter.challenges.picoctf.org", 15130

p = pwn.remote(url, port)
message = p.recv().decode('utf-8')

message = re.sub(r'\D', ' ', message)
message = message.split()[:-1]

bytes_arr1 = [ chr(int(x, 2)) for x in message if not (x.isalpha())]
payload = ''.join(bytes_arr1)
p.sendline(payload)

message2 = p.recv().decode('utf-8')

message2 = re.sub('\D', ' ', message2)
message2 = message2.split()

bytes_arr2 = [chr(int(x, 8)) for x in message2 if not (x.isalpha())]
payload2 = ''.join(bytes_arr2)
p.sendline(payload2)


message3 = p.recv().decode('utf-8')
payload3 = message3.split()[4]
payload3 = bytearray.fromhex(payload3).decode()
p.sendline(payload3)

print(p.recv().decode('utf-8'))
p.close()

# message = message.replace("\n", " ")
# message = message[52:-49]
# message = message.replace(" 0", " 0b0")
# message = message.split(" ")

# for byte in bytes_arr:
#     payload.append(chr(byte))
# p.sendline(''.join(payload))

# print(p.recv())
