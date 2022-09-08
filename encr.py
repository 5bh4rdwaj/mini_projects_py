## Reverse Engineering CTF titled "Transformation" on PICO ctf

## Given in CTF
their_encrypted_flag = ''.join(
              [chr(
                       (ord(flag[i]) << 8) + 
                       ord(flag[i + 1])            
                )
                    for i in range(0, len(flag), 2)
              ]
)
 # decryption
	
i = 0; 
encrypted_char_list = []
while i<len(flag): 
    first = ord(flag[i] << 8)
    second =ord(flag[i + 1])
    combined = first + second
    encrypted_char =chr(combined)
    encrypted_char_list.append(encrypted_char)


    i = i+2 
    

    our_encrypted_flag = ''.join(encrypted_char_list)
    print(our_encrypted_flag)

    print(our_encrypted_flag == their_encrypted_flag)