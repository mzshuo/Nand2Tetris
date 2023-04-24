'''
This Module is to help to translate Hack assembly language mnemonics into binary codes
'''


def dest(str):
    '''
    This function is to translate the dest part of the assembly command into binary code
    :param str: the dest part of the assembly command
    :return: 3 binary bits translated from the dest assembly command
    '''
    hash_dest = {
        '': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }
    dst = hash_dest[str]
    return dst


def comp(str):
    '''
    This function is to translate the comp part of the assembly command into binary code
    :param str: the comp part of the assembly command
    :return: 7 binary bits translated from the comp assembly command
    '''
    hash_comp = {
        '0': '0' + '101010',
        '1': '0' + '111111',
        '-1': '0' + '111010',
        'D': '0' + '001100',
        'A': '0' + '110000',
        '!D': '0' + '001101',
        '!A': '0' + '110001',
        '-D': '0' + '001111',
        '-A': '0' + '110011',
        'D+1': '0' + '011111',
        'A+1': '0' + '110111',
        'D-1': '0' + '001110',
        'A-1': '0' + '110010',
        'D+A': '0' + '000010',
        'D-A': '0' + '010011',
        'A-D': '0' + '000111',
        'D&A': '0' + '000000',
        'D|A': '0' + '010101',

        'M': '1' + '110000',
        '!M': '1' + '110001',
        '-M': '1' + '110011',
        'M+1': '1' + '110111',
        'M-1': '1' + '110010',
        'D+M': '1' + '000010',
        'D-M': '1' + '010011',
        'M-D': '1' + '000111',
        'D&M': '1' + '000000',
        'D|M': '1' + '010101'
    }

    str = ''.join(str.split(' '))    # remove the blank space within command
    cmp = hash_comp[str]
    return cmp


def jump(str):
    '''
    This function is to translate the jump part of the assembly command into binary code
    :param str: the jump part of the assembly command
    :return: 3 binary bits translated from the jump assembly command
    '''
    hash_jump = {
        '': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }
    jmp = hash_jump[str]
    return jmp

