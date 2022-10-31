import torch

def blank_collapse(emission, blank_threshold=0.9, blank_id=0):
    prob = torch.nn.functional.softmax(emission, dim=-1)
    blanks = prob[:, blank_id] > blank_threshold
    first_blanks = 0
    u, c = torch.unique_consecutive(blanks, dim=0, return_counts=True)
    u = u.tolist()
    c = c.tolist()
    cc = []
    for j in range(len(c)):
        if u[j]:    # if blank
            if j == 0:
                first_blanks = c[j]
            elif j == len(c) - 1:
                break
            else:
                cc.append(c[j])
        else:
            cc += [1] * c[j]
    if len(cc) == 0:    # case: every frame is a blank frame
        cc = [0]
        first_blanks = 0
    indices = torch.cumsum(torch.tensor(cc), dim=0) - 1 + first_blanks
    new_emission = emission[indices]
    
    return new_emission, indices
