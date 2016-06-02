import sys


def instrument(file_name):
    with open(file_name, 'r') as f:
        source_lines = f.read().splitlines()
    instrumented = 'import instrumentation'
    instrumented += '\n'
    instrumented += '\n'
    instrument_line = False
    fn_name = ''

    for source_line in source_lines:
        stripped_source_line = source_line.strip()

        if len(stripped_source_line) > 0 and stripped_source_line[0] == '#':
            stripped_source_line = ''

        if len(stripped_source_line) == 0:
            instrumented += source_line
            instrumented += '\n'
        else:
            if instrument_line:
                num_whitespace_chars = len(source_line) - len(stripped_source_line)
                whitespace = source_line[0:num_whitespace_chars]
                injected_line = whitespace
                injected_line += "instrumentation.trace_fn('%s','%s','%s')" % (file_name, '', fn_name)
                instrumented += injected_line
                instrumented += '\n'
                instrument_line = False
                fn_name = ''
            pos_def = stripped_source_line.find('def ')
            if pos_def == 0:
                instrumented += source_line
                instrumented += '\n'
                pos_paren = stripped_source_line.find('(')
                if pos_paren > 0:
                    fn_name = stripped_source_line[4:pos_paren]
                    instrument_line = True
                else:
                    print('error: unable to parse python source')
                    sys.exit(1)
            else:
                instrumented += source_line
                instrumented += '\n'

    return instrumented


def main():
    input_source_file = 'uninstrumented.py'
    output_source_file = 'instrumented.py'
    instrumented_code = instrument(input_source_file)
    with open(output_source_file, 'w') as f:
        f.write(instrumented_code)
    print(instrumented_code)


if __name__=='__main__':
    main()
