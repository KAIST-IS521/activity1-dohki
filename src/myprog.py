import sys
import strictcsv as scsv
            

def main():
    assert len(sys.argv) == 3
    [file_name, col_idx] = sys.argv[1:]

    assert col_idx.isdigit()
    col_idx = int(col_idx)

    try:
        sc = scsv.StrictCsv(file_name)
        nth_col = sc.get_nth_col(col_idx)

        for row in nth_col:
            print(row)

    except scsv.NotSameColNumError:
        print('[*] Given csv file does not have same column number for all rows.')
        sys.exit(1)

    except scsv.ColIdxOutOfBoundError:
        print('[*] Given column index exceeds the bound.')
        sys.exit(1)


if __name__ == '__main__':
    main()
