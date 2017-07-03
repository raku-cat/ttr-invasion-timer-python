import regex

def get_sec(time_str):
    try:
        h, m, s = time_str.split(':')
    except ValueError:
        try:
            m, s = time_str.split(':')
            h = '0'
        except ValueError:
            s = time_str
            h = '0'
            m = '0'
    return int(h) * 3600 + int(m) * 60 + int(s)

