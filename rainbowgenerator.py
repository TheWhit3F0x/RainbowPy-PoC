import hashlib
import string
import random
import base64
from argparse import ArgumentParser

class ChainLengthError(Exception):
    pass
class PoCIndexError(Exception):
    pass

def main(seed = None, *, chainlength, pocindex):

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
    if pocindex < 1 or pocindex > chainlength:
        raise PoCIndexError("The PoC index is too short or too long")

    if seed is None:
        seed = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    print(f'Seed: {seed}')

    for x in range(chainlength):
        if x == pocindex-1:
            print(f"PoC hash: {hash.hexdigest()}")

        hash = hashlib.md5(seed.encode('UTF-8'))
        seed = base64.b64encode(hash.digest()).decode('UTF-8')[:7]
    
    print(f'End-Hash: {hash.hexdigest()}')
    
if __name__ == '__main__':
    parser = ArgumentParser(
    description='''Simple Python script to demonstrate the concept of Rainbow Tables.
        Generates a hash chain from a seed (random if not provided) and returns the seed, a PoC hash obtained
        through the process and the final hash''')

    parser.add_argument('--seed', '-s', help='The seed to initilize the chain [Default: Random]')
    parser.add_argument('--chainlength', '-c', type=int, help="The chain's length [Required]", required=True)
    parser.add_argument('--pocindex', '-p', type=int, help="The index from which to get the PoC hash [Required]", required=True)

    args = parser.parse_args()

    main(args.seed, chainlength=args.chainlength, pocindex=args.pocindex)