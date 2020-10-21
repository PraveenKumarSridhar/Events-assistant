
def convert_time(time_text):
    try:
        if int(time_text.split(':')[0])>=12:
            time = time_text.split(':')[:2]
            time[0]= str(int(time[0]) - 12)
            return ':'.join(time) +' pm'
        else:
            return ':'.join(time_text.split(':')[:2])+' am'
    except:
        return ''