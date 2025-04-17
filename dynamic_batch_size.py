import numpy as np
import pandas as pd

def dynamic_batch_size(inp: list[str],thresh:int=20000,single_doc_cap_factor:float=1/2) -> int:
    res,len_count = 1, len(inp[0])
    
    if len_count >= thresh * single_doc_cap_factor:
        return 1
    
    for i in inp[1:]:
        if len(i) >= thresh * single_doc_cap_factor:
            break

        res += 1
        len_count += len(i)

        if len_count >= thresh:
            break

    return res

def main():
    print('This is the main function.')

if __name__ == "__main__":
    main()