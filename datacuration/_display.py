import humanize

def fileNaturalSize(file_size_bytes):
    '''
    Takes a number of bytes and returns a my human readable generalized value representing the file size.
    
     Parameters
     ----------
     file_size_bytes : int "The bytes size to convert to a more generalized size."

     Returns
     ----------
     String
    '''
    return humanize.naturalsize(file_size_bytes)

def numIntComma(intVal):
    '''
    Converts an integer number to a string a more human readable number with commas.

     Parameters
     ----------
     intVal : int "The integer value to add commas to."

     Returns
     ----------
     String
    '''
    return humanize.intcomma(intVal)