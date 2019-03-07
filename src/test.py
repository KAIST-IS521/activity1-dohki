import subprocess


#TODO: Make test cases with oracle in SQLite DB.
testcases = [(['csv/rfc-4180-6.csv', '2'], 0, 'b \nbb\nyyy\n'.encode())]


def test(testcase):
    (argv, exp_ret_code, exp_output) = testcase

    ret_code = 0

    try:
        # TODO: Use github repo relative path so that you can in anywhere.
        output = subprocess.check_output(['python', 'src/myprog.py'] + argv)

    except subprocess.CalledProcessError as e:
        ret_code = e.returncode


    assert exp_output == output
    assert exp_ret_code == ret_code

    
def main():
    for testcase in testcases:
        test(testcase)
    

if __name__ == '__main__':
    main()
