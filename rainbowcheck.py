import hashlib
import base64
import sys
from argparse import ArgumentParser

class ChainLengthError(Exception):
    pass

def main(seed, endhash, pochash, chainlength):
    
    print(r"""
                                            .-'''-.                                                       
                                           '   _    \                                                     
                 .--.   _..._   /|       /   /` '.   \              _________   _...._                    
                 |__| .'     '. ||      .   |     \  '       _     _\        |.'      '-. .-.          .- 
.-,.--.          .--..   .-.   .||      |   '      |  '/\    \\   // \        .'```'.    '.\ \        / / 
|  .-. |    __   |  ||  '   '  |||  __  \    \     / / `\\  //\\ //   \      |       \     \\ \      / /  
| |  | | .:--.'. |  ||  |   |  |||/'__ '.`.   ` ..' /    \`//  \'/     |     |        |    | \ \    / /   
| |  | |/ |   \ ||  ||  |   |  ||:/`  '. '  '-...-'`      \|   |/      |      \      /    .   \ \  / /    
| |  '- `" __ | ||  ||  |   |  |||     | |                 '           |     |\`'-.-'   .'     \ `  /     
| |      .'.''| ||__||  |   |  |||\    / '                             |     | '-....-'`        \  /      
| |     / /   | |_   |  |   |  ||/\'..' /                             .'     '.                 / /       
|_|     \ \._,\ '/   |  |   |  |'  `'-'`                            '-----------'           |`-' /        
         `--'  `"    '--'   '--'                                                             '..'         

                                                                                         by WhiteFox
                                                                                         
    """)

    if chainlength < 1:
        raise ChainLengthError("The chain's length is too short")
    
    endhash = bytes.fromhex(endhash)
    pochash = bytes.fromhex(pochash)

    tryhash = pochash

    for _ in range(chainlength):
        tryhash = base64.b64encode(tryhash).decode('UTF-8')[:7]
        tryhash = hashlib.md5(tryhash.encode('UTF-8')).digest()

        if tryhash == endhash:
            found = True
            print("Found it!")
            break
    
    if not found:
        print("Not found in the chain")
        sys.exit()

    for _ in range(chainlength):
        tryhash = hashlib.md5(seed.encode('UTF-8')).digest()
        if tryhash == pochash:
            print(f"The original string is: {seed}")
            break
        seed = base64.b64encode(tryhash).decode('UTF-8')[:7]

if __name__ == '__main__':
    parser = ArgumentParser(
    description='''Simple Python script to demonstrate the concept of Rainbow Tables.
        Checks if a PoC hash is in a chain of determined length and returns the original string if found.
        To define a chain, its seed, final hash and length must be provided''')

    parser.add_argument('--seed', '-s', help='The seed of the corresponding chain [Required]', required=True)
    parser.add_argument('--endhash', '-e', help="The final hash of the chain [Required]", required=True)
    parser.add_argument('--pochash', '-p', help="The PoC hash from which to get the original string [Required]", required=True)
    parser.add_argument('--chainlength', '-c', type=int, help="The chain's length [Required]", required=True)

    args = parser.parse_args()

    main(args.seed, args.endhash, args.pochash, args.chainlength)
