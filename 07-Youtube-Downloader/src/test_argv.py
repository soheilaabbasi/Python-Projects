import sys


def main(url, quality, output_path):
    pass


if __name__ == '__main__':
    # print(sys.argv[1:])     # it is the input arguments that we gave it, It is 
                              # from 1 because the 0 argument in the list is the file name (test_argparser.py)
    
    if len(sys.argv) != 4:
        print("Usage: python test_argparser.py <url> <quality> <output_path>")
        sys.exit(1)
    
    
    url, quality, output_path = sys.argv[1:]   # unpack user's input in this 3 arguments
                                               # but if user gives 1 or 2 arguments, it will give Error
                                                
    main(url, quality, output_path)

