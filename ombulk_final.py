#!/usr/bin/python

import sys
import os
import psycopg2

# get terminal width for correct working on small terminal-windows
def get_terminal_width():
    width = os.popen('tput cols', 'r').readline()

    return int(width)

term_width = get_terminal_width()

# on terminal-windows with amount of columns < 58 correct output is impossible
if term_width <= 58:
        print("ERROR: terminal is too narrow")
        exit (1)

# for fullscreen putty-terminal (on 24' monitor) amount of columns is 237; width of table header is 39: 237-39=198
# now calculating number of output columns (not symbol columns!)
n_columns = int(((term_width - 39) / 198.0) * 10)

newline = ''
line_list = []

# formatting dates like 180215224156 to human readable format 18-02-15 22:41:56
def omdate(s):
       new_s = "{0}-{1}-{2} {3}:{4}:{5}".format(s[0:2], s[2:4], s[4:6], s[6:8], s[8:10], s[10:12])
       return new_s


i = 0
for line in sys.stdin:
        line_list.append([])

        # deleting filename header in input line after grep without option "-h"
        h = line.find(":", 0, len(line)) + 1
        if h == -1:
                h = 0

        newline = line[h:len(line)]
        
        line = ''
        line = newline.replace(" ","_")
        newline = ''
        newline = line.replace("Outbound_ESME_Messages_-_Failure","OEM-Failure")
        line = ''
        # need for make output columns narrower
        line = newline.replace("Outbound_ESME_Messages_-_Successful","OEM-Success")
        newline = ''
        newline = line.replace("|"," ")
        
        
        # getting from result-line elements without space-symbols
        j = 0
        h = 0
        n = ''
        for n in newline:

                if n != " ":
                        j = j + 1
                else:
                        line_list[i].append(newline[h:j])
                        j = j + 1
                        h = j
        line_list[i].append(newline[h:len(newline)].replace('\n', ''))
        i = i + 1

# fields with dates contains in 10- & 12-elements of including lists
i = 0
while i < len(line_list):
        print i
        line_list[i][10] = omdate(line_list[i][10])
        line_list[i][12] = omdate(line_list[i][12])
        if line_list[i][15] != "":
            line_list[i][15] = omdate(line_list[i][15])
        i = i + 1

# sorting columns by date-field in 10th element of include list
line_list_sorted = []
line_list_sorted = sorted(line_list, key=lambda date: date[10])


####################################################
# filling list with static content
head_list = []

head_list.append('OMN-RECORD-ID')
head_list.append('(strp) str')
head_list.append('THREAD ID')
head_list.append('MESSAGE ID')
head_list.append('(int) val')
head_list.append('(int) val')
head_list.append('Inbound Transaction Start Time')
head_list.append('(int) usecs')
head_list.append('Inbound Transaction End Time')
head_list.append('(int) usecs')
head_list.append('Outbound Transaction Start Time')
head_list.append('(int) usecs')
head_list.append('Outbound Transaction End Time')
head_list.append('(int) usecs')
head_list.append('LIFE_SCHDEL_TIME')
head_list.append('LIFE_EXPDEL_TIME')
head_list.append('(int) oa_pre_trans.ton')
head_list.append('(int) oa_pre_trans.npi')
head_list.append('(strp) oa_pre_trans.addr')
head_list.append('(int) oa.ton')
head_list.append('(int) oa.npi')
head_list.append('(strp) oa.addr')
head_list.append('(int) da_pre_trans.ton')
head_list.append('(int) da_pre_trans.npi')
head_list.append('(strp) da_pre_trans.addr')
head_list.append('(int) da.ton')
head_list.append('(int) da.npi')
head_list.append('(strp) da.addr')
head_list.append('LIFE_SYSTEM_ID')
head_list.append('LIFE_DELRCPT_LOC')
head_list.append('(int) registered_delivery')
head_list.append('(int) total_delivery_attempts')
head_list.append('(int) data_coding')
head_list.append('(int) esm_class')
head_list.append('(int) pre_submission_len')
head_list.append('(int) final_state')
head_list.append('orig_msg_info.error.o_error.type')
head_list.append('orig_msg_info.error.o_error.value')
head_list.append('orig_msg_info.error.i_error.type')
head_list.append('orig_msg_info.error.i_error.value')
head_list.append('(int) error.o_error.type')
head_list.append('(int) error.o_error.value')
head_list.append('(int) error.i_error.type')
head_list.append('(int) error.i_error.value')
head_list.append('(int) o_error.type')
head_list.append('(int) o_error.value')
head_list.append('(int) i_error.type')
head_list.append('(int) i_error.value')
head_list.append('(int) ib_seg_info.seg_reference')
head_list.append('(int) ib_seg_info.seg_total')
head_list.append('(int) ob_seg_info.seg_number')
head_list.append('LIFE_CONCAT_NUMBER')
head_list.append('LIFE_CONCAT')
head_list.append('SCCP Calling Party GT')
head_list.append('SCCP Called Party GT')
head_list.append('TCAP Invoke Opcode')
head_list.append('TCAP Transaction ID')
head_list.append('MAP Service Center Address')
head_list.append('MAP MSISDN')
head_list.append('MAP IMSI')
head_list.append('GSM Error')
head_list.append('(int) val')
head_list.append('(strp) str')
head_list.append('(int) value')
head_list.append('(strp) id')
head_list.append('(strp) profile')
head_list.append('(int) action')
head_list.append('(int) o_error_type')
head_list.append('(int) o_error_val')

####################################################

# 1 screen = 10 columns; now i = number of input lines = len(line_list)
if i % n_columns != 0:
        screens = i / n_columns + 1
else:
        screens = i / n_columns

print ("-" * 58 + '\n' + 'Columns is sorted by "Outbound Transaction Start Time"' + '\n' + "-" * 58)
i = 1
h = 1
c = 1
while i <= screens:
        # print main header
        print("{0:^36}".format("#")),
        while h <= (i * n_columns):
                print("{0:1}".format("|")),
                print("{0:^17}".format(h)),
                h = h + 1
        print
        print("-" * 39),
        print("-" * 18 * n_columns)

        # calculation for numbers of columns for each screen
        j = 0
        start_point = (i - 1) * n_columns
        if (i * n_columns) >= len(line_list):
                stop_point = len(line_list)
        else:
                stop_point = i * n_columns

        # lenght of input lines is fixed and it is 69
        while j < 69:
                #printing the name of parameter
                print("{0:2} {1:33}".format(j + 1, head_list[j])),
                # print elements of included lists according to parameter
                for n in range(start_point, stop_point):
                        print("{0:1}".format("|")),
                        print("{0:17}".format(line_list_sorted[n][j])),
                print

                # on middle of the output table printing of second "lite" header
                if j == 33:
                        print("{0:^36}".format("#")),
                        while c <= (i * n_columns):
                                print("{0:1}".format("|")),
                                print("{0:^17}".format(c)),
                                c = c + 1
                        print

                j = j + 1

        print('\n')
        i = i + 1
        
        
########################################
try:
    conn = psycopg2.connect("dbname='ombulk' user='roma' host='172.22.22.100' password='chloroform-'")
except:
    print "I am unable to connect to the database"
    
cur = conn.cursor()
i = 0
while i < len(line_list):
        if line_list_sorted[i][15] == "":
                LIFE_EXPDEL_TIME = "0000-00-00 00:00:00"
        else:
                LIFE_EXPDEL_TIME = line_list_sorted[i][15]
        cur.execute("""INSERT INTO ombulktable VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (line_list_sorted[i][0], line_list_sorted[i][1], \
                    line_list_sorted[i][2], line_list_sorted[i][3], line_list_sorted[i][10], line_list_sorted[i][11], line_list_sorted[i][12], line_list_sorted[i][13], LIFE_EXPDEL_TIME, \
                    line_list_sorted[i][16], line_list_sorted[i][18], line_list_sorted[i][22], line_list_sorted[i][24], line_list_sorted[i][28], line_list_sorted[i][53], line_list_sorted[i][54], \
                        line_list_sorted[i][55], line_list_sorted[i][57], line_list_sorted[i][58], line_list_sorted[i][59], line_list_sorted[i][60]))
        i = i + 1
conn.commit()
cur.close()
conn.close()

