def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    bin=[]
    w=(max(values)-min(values))/num_bins
    if (max(values)==min(values)):
        for i in range(len(values)):
            bin.append(0)
        return bin
    else:
        if w==0 or num_bins==0:
            return [None]
        mini=min(values)
        for i in range(len(values)):
            val=(values[i]-mini)//w
            bin.insert(i,min(val, num_bins-1))
        return bin