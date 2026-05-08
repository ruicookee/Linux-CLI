### can you tell that i just learnt about the caeser cipher and the scytale ###
### combines something you know and something you have ###
### but now everyone has i guess... ###

def encrypt(p: str, shift: int, swap: bool):
    # Pre Check
    if not isinstance(p, str):
        raise TypeError("p must be the password str")
    if not isinstance(shift, int):
        raise TypeError("shift must be secret int")
    if not isinstance(swap, bool):
        raise TypeError("swap must be secret bool")
    
    # Step 1: Shift
    shifted = []
    for char in p:
        if ord("A") <= ord(char) <= ord("Z"):
            new_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
        elif ord("a") <= ord(char) <= ord("z"):
            new_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
        else:
            new_char = char
        shifted.append(new_char)
    # Step 2: Swap
    if swap:
        swapped = [char.upper() if char.islower() else char.lower() for char in shifted]
    else:
        swapped = shifted[::-1]
    # Step 3: Print Encrypted Text
    return "".join(swapped)

def decrypt(p: str, shift: int, swap: bool):
    # Pre Check
    if not isinstance(p, str):
        raise TypeError("p must be the password str")
    if not isinstance(shift, int):
        raise TypeError("shift must be secret int")
    if not isinstance(swap, bool):
        raise TypeError("swap must be secret bool")    
    # Step 1: Unswap
    if swap:
        unswapped = [char.upper() if char.islower() else char.lower() for char in p]
    else:
        unswapped = list(p[::-1])
    
    # Step 2: Unshift
    unshifted = []
    for char in unswapped:
        if ord("A") <= ord(char) <= ord("Z"):
            new_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))
        elif ord("a") <= ord(char) <= ord("z"):
            new_char = chr(((ord(char) - ord("a") - shift) % 26) + ord("a"))
        else:
            new_char = char 
        unshifted.append(new_char)
    return "".join(unshifted)  