"""
Your finished project must include all of the following requirements:

 Add the CMP instruction and equal flag to your LS-8.
    # Need to add a Flag similar to pc, ir, ect
    # The only one of the three GT, LT, & ET appears to be equal to for the sprint
        # FL bits: 00000LGE
            # L Less-than: during a CMP, set to 1 if registerA is less than registerB, zero otherwise.
            # G Greater-than: during a CMP, set to 1 if registerA is greater than registerB, zero otherwise.
            # E Equal: during a CMP, set to 1 if registerA is equal to registerB, zero otherwise.
    # CMP 0b10100111 handled in the ALU  
        # Compare the two registers - so this will take 3 instructions (code and 2 registers)

        # Reset FL to 0
            # If they are equal, set the Equal E flag to 1, otherwise set it to 0.
            # If registerA is less than registerB, set the Less-than L flag to 1, otherwise set it to 0.
            # If registerA is greater than registerB, set the Greater-than G flag to 1, otherwise set it to 0.

 Add the JMP instruction.
    # JMP 0b01010100
        # Jump to the address stored in the given register.
        # Set the PC to the address stored in the given register.
        # It will have 2 instruction length (code and register)
            # This seems like call without the need to push for a return

 Add the JEQ instruction.
    # JEQ 01010101
        # If equal flag is set (true), jump to the address stored in the given register.
        # It will have 2 instruction length (code and register)
            # We are checking the flag on the equal bit and seeing if it is true (00000LGE)
                # if yes then jump to register
                # if no then continue on with program

 Add the JNE instruction.
    # JNE 01010110
        # If E flag is clear (false, 0), jump to the address stored in the given register.
        # It will have 2 instruction length (code and register)
            # We are checking the flag on the equal bit and seeing if it is false (00000LGE)
                # if yes then jump to register
                # if no then continue with program
"""