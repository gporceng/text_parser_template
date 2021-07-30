import os
import csv
import pandas as pd
import xlsxwriter


ECG_f = 1000
PPG_f = 30

def main():

    IDs = []
    entry_no = 0
    PPG_Filenames = []
    ECG_Filenames = []

    with open("subject-info.csv", "r") as ledger:
        ledger_reader = csv.reader(ledger, delimiter = ",")
        for lines in ledger_reader:
            entry_no += 1
            IDs.append(lines[0])

            #Initiate filenames
            ECG_Filenames.append(lines[0]+"_ECG.hea")
            PPG_Filenames.append(lines[0]+"_PPG.hea")


    """Test for lines to be added correctly
    for lines in IDs:
        print(lines)
        """

    #Specify path to directories
    path = "brno-university-of-technology-smartphone-ppg-database-but-ppg-1.0.0"

    entry = 0
    for ID in IDs:
        ECG_path = os.path.join(path, ID,ECG_Filenames[entry])

        #ECG Import

        if entry != 0:
            with open(ECG_path) as f:

                lines = f.readlines()

                line_no = 0
                for cur_line in lines:
                    line_no += 1

                cur_line_no = 0

                ECG_vals = []
                ECG_time = []

                for cur_line in lines:

                    if(cur_line_no > 0 and cur_line_no < line_no-1):
                        split_line = cur_line.split()
                        split_line = split_line[2].split("(")
                        print(split_line[0])
                        ECG_vals.append(float(split_line[0]))
                        ECG_time.append((cur_line_no-1) * (1/ECG_f))
                        #print(entry)

                    cur_line_no += 1

                #Translate to xlsx
                #print(ECG_vals[10])
                print("Here")

                ecg_filename = IDs[entry] + "_ECG.xlsx"
                workbook = xlsxwriter.Workbook(ecg_filename)
                worksheet = workbook.add_worksheet()

                data = {'Time_':ECG_time,
                        'ECG_':ECG_time,
                        'Time':ECG_time,
                        'ECG':ECG_vals}

                col_num = 0
                for key, value in data.items():
                    worksheet.write(0, col_num, key)
                    worksheet.write_column(1, col_num, value)
                    col_num += 1

                workbook.close()

        entry += 1


    """
    #PPG Import
    entry = 0
    for ID in IDs:
        PPG_path = os.path.join(path, ID, PPG_Filenames[entry])
        if entry != 0:
            with open(PPG_path) as f:

                lines = f.readlines()

                line_no = 0
                for cur_line in lines:
                    line_no += 1

                cur_line_no = 0

                PPG_vals = []
                PPG_time = []

                for cur_line in lines:

                    if (cur_line_no > 0 and cur_line_no < line_no - 1):
                        split_line = cur_line.split()
                        split_line = split_line[2].split("(")
                        print(split_line[0])
                        PPG_vals.append(float(split_line[0]))
                        PPG_time.append((cur_line_no - 1) * (1 / PPG_f))
                        # print(entry)

                    cur_line_no += 1

                # Translate to xlsx
                # print(ECG_vals[10])
                print("Here")

                ppg_filename = IDs[entry] + "_PPG.xlsx"
                workbook = xlsxwriter.Workbook(ppg_filename)
                worksheet = workbook.add_worksheet()

                data = {'Time_': PPG_time,
                        'Time': PPG_time,
                        'PPG': PPG_vals}

                col_num = 0
                for key, value in data.items():
                    worksheet.write(0, col_num, key)
                    worksheet.write_column(1, col_num, value)
                    col_num += 1

                workbook.close()





        entry = entry + 1

"""




main()
