#include <map>

int encode(int value) {
    // Map for integer values to seven segment hex codes
    std::map<int, int> intToCode = {
        { 0, 0x02 },
        { 1, 0x67 },
        { 2, 0x48 },
        { 3, 0x60 },
        { 4, 0x25 },
        { 5, 0x30 },
        { 6, 0x10 },
        { 7, 0x66 },
        { 8, 0x00 },
        { 9, 0x24 },
        { -1, 0x7F }
    };


    if (value < 0 || value > 9999){
        return 0x7F7FFD67;
    }

    // Initialize the output register with 0
    int output = 0x7f7f7f02;
    // Initialize digit of input value
    int digit = value % 10;
    // Loop for 4 digits
    for (int i = 0; i < 4; i++) {
        // Shift output right 8 bits and add in new digit hex code on the left
        output = (intToCode[digit] << 24) + (output >> 8);
        value /= 10;
        // If statement for when there are less than 4 digits
        if (value != 0) 
            digit = value % 10;
        else 
            // Blank hex code for leading zeros
            digit = -1;            
    }
        
    // Mask the output so it only returns 32 bits
    return output & 0xFFFFFFFF;
}