


def batch(l:list, sample:int):
    """
    Processes a splicable object in chunks of sample size
    until only the tail is left
    """
    while l:
        # prova a tornare il primo sample e riassegna a l il restante
        try:
          ret = l[:sample]
          yield ret
          l = l[sample:]
        # se l'indice e' fuori dal range allora ritorna tutta la l rimanente
        except IndexError:
          return l
    return None