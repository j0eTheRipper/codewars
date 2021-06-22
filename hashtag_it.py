def make_hashtag(string):
    if string == '': 
        return None
    else:
        result = '#' + ''.join([word.capitalize() for word in string.split()])
        
        if len(result) > 140:
            return None
        else:
            return result
