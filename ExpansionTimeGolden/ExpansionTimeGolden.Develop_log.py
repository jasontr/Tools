
# coding: utf-8

# # Develop Log

# ## Import

# In[9]:

import re


# ## create Node class

# In[1]:

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child_node(self, obj):
        self.children.append(obj)

# ## File System

# In[93]:

def load_data(path):
    with open(path, "r") as data_file:
        text = data_file.readlines()
    return text

# ## Data Process

# ### Regular Expression Part

# In[114]:

def reg_exp(textline):
    patt = '^\<(\/node)\>$|^\<(node).*TEXT\="(.*)( \[.*\])?"(/)?>'
    regexp = re.compile(patt)
    result = None
    try:
        m = re.search(regexp, textline)
        result = m.groups()
    finally:
        return result


# ### Processing

# In[81]:

def data_process(textdata):
    textprocessed = []
    for line in textdata:
        reg = reg_exp(line)
        if reg is not None:
            textprocessed.append(reg)
    return textprocessed

# 

# In[104]:

def translate_textline2logic(textline):
    if textline[0] is not None:
        return "back"
    else:
        if textline[4] is None:
            have_children = 1
        else:
            have_children = 0
        data = textline[2]
        return [data, have_children]


# In[131]:

def create_tree(data_processed):
    #if len(data_processed) > 1:
        tree = []
        have_children = []
        for line_processed in data_processed:
            tmp = translate_textline2logic(line_processed)
            if tmp is not "back":
                tree.append(Node(tmp[0]))
                have_children.append(tmp[1])
            else:
                tree.append(None)
                have_children.append(None)
        i = 1
        while len(tree) > 1:
            if tree[i] is not None:
                tree[i-1].add_child_node(tree[i])            
                if not have_children[i]:
                        del tree[i]
                        del have_children[i]
                else:
                    i += 1
            else:
                del tree[i]
                del have_children[i]
                if len(tree) != 1:
                    del tree[i-1]
                    del have_children[i-1]
                i -= 1
        return tree[0]
    #else:
        #return tree[0]


# ## Main

# In[132]:

textdata = load_data('TimeGolden_2016_11_30.mm.utf8.txt')
dp = data_process(textdata)
tree = create_tree(dp)


# In[133]:

print tree.children[0].data

