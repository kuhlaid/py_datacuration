import humanize

def fileNaturalSize(file_size_bytes):
    return humanize.naturalsize(file_size_bytes)

def numIntComma(intVal):
    return humanize.intcomma(intVal)