# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
import sys

def getFileInformation():
    all_lines = fileinput.input()
    list_of_lines = []
    for line in all_lines:
        if(line == '\n'):
            continue
        line = line[:-1]
        list_of_lines.append(line)
    return list_of_lines


def isInRange(date, start_date, end_date):
    ""
    start_year = start_date[:4]
    start_month = start_date[5:7]
    end_year = end_date[:4]
    end_month = end_date[5:7]
    date_year = date[:4]
    date_month = date[5:7]
    if(date_year < start_year or date_year > end_year):
        return false
    if(date_year == start_year):
        if(date_month < start_month):
            return False
    if(date_year == end_year):
        if(date_month >= end_month):
            return False
        
    return True

def output(results_map):
    for date in reversed(sorted(results_map)):
        sys.stdout.write(date)
        for engagement in sorted(results_map[date]):
            sys.stdout.write(", "+engagement+", "+str(results_map[date][engagement]))
        print("")
            
        


def main():
    list_of_lines = getFileInformation()
    dates = [line.strip() for line in list_of_lines[0].split(',')]
    start_date = dates[0]
    end_date = dates[1]
  
    
    list_of_lines = list_of_lines[1:]
    results_map = {}
    for line in list_of_lines:
        list_data = [item.strip() for item in line.split(',')]
        date = list_data[0][:7]
        engagement_type = list_data[1]
        count = int(list_data[2])
        current_map = {engagement_type:count}
        
        if(not isInRange(date,start_date,end_date)):
            continue
        if(date in results_map):
            if(engagement_type in results_map[date]):
                count = count + int(results_map[date][engagement_type])
                current_map ={engagement_type:count}
            results_map[date].update(current_map)
        else:
            results_map[date] = current_map
        #print (date, results_map)
        
    output(results_map)
main()
