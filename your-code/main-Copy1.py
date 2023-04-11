#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Control-flow" data-toc-modified-id="Control-flow-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Control flow</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#1.-Create-and-print-a-list-of-consecutive-integers-starting-with-1-and-ending-with-50." data-toc-modified-id="1.-Create-and-print-a-list-of-consecutive-integers-starting-with-1-and-ending-with-50.-1.0.0.1"><span class="toc-item-num">1.0.0.1&nbsp;&nbsp;</span>1. Create and print a list of consecutive integers starting with 1 and ending with 50.</a></span></li><li><span><a href="#2.-Create-and-print-a-list-of-even-numbers-starting-with-2-and-ending-with-200." data-toc-modified-id="2.-Create-and-print-a-list-of-even-numbers-starting-with-2-and-ending-with-200.-1.0.0.2"><span class="toc-item-num">1.0.0.2&nbsp;&nbsp;</span>2. Create and print a list of even numbers starting with 2 and ending with 200.</a></span></li><li><span><a href="#3.-Create-and-print-a-list-containing-all-elements-of-the-10-x-4-array-below." data-toc-modified-id="3.-Create-and-print-a-list-containing-all-elements-of-the-10-x-4-array-below.-1.0.0.3"><span class="toc-item-num">1.0.0.3&nbsp;&nbsp;</span>3. Create and print a list containing all elements of the 10 x 4 array below.</a></span></li><li><span><a href="#4.-Add-a-condition-to-the-loop-above-so-that-only-values-greater-than-or-equal-to-0.5-are-printed." data-toc-modified-id="4.-Add-a-condition-to-the-loop-above-so-that-only-values-greater-than-or-equal-to-0.5-are-printed.-1.0.0.4"><span class="toc-item-num">1.0.0.4&nbsp;&nbsp;</span>4. Add a condition to the loop above so that only values greater than or equal to 0.5 are printed.</a></span></li><li><span><a href="#5.-Use-a-loop-to-create-and-print-a-list-containing-all-elements-of-the-5-x-2-x-3-array-below." data-toc-modified-id="5.-Use-a-loop-to-create-and-print-a-list-containing-all-elements-of-the-5-x-2-x-3-array-below.-1.0.0.5"><span class="toc-item-num">1.0.0.5&nbsp;&nbsp;</span>5. Use a loop to create and print a list containing all elements of the 5 x 2 x 3 array below.</a></span></li><li><span><a href="#6.-Add-a-condition-to-the-loop-above-so-that-the-last-value-in-each-subarray-is-printed,-but-only-if-it-is-less-than-or-equal-to-0.5." data-toc-modified-id="6.-Add-a-condition-to-the-loop-above-so-that-the-last-value-in-each-subarray-is-printed,-but-only-if-it-is-less-than-or-equal-to-0.5.-1.0.0.6"><span class="toc-item-num">1.0.0.6&nbsp;&nbsp;</span>6. Add a condition to the loop above so that the last value in each subarray is printed, but only if it is less than or equal to 0.5.</a></span></li><li><span><a href="#7.-Use-a-loop-to-select-and-print-the-names-of-all-CSV-files-in-the-/data-directory." data-toc-modified-id="7.-Use-a-loop-to-select-and-print-the-names-of-all-CSV-files-in-the-/data-directory.-1.0.0.7"><span class="toc-item-num">1.0.0.7&nbsp;&nbsp;</span>7. Use a loop to select and print the names of all CSV files in the <em>/data</em> directory.</a></span></li></ul></li><li><span><a href="#Bonus" data-toc-modified-id="Bonus-1.0.1"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>Bonus</a></span></li></ul></li></ul></li></ul></div>

# # Control flow
# 
# Complete the following set of exercises to solidify your knowledge of list comprehensions.

# In[1]:


import os;


# #### 1. Create and print a list of consecutive integers starting with 1 and ending with 50.

# In[66]:


lista = []

for i in range(1, 51):
    i+=1
    lista.append(i)
    
print(lista)


# In[18]:


list = [i for i in range(51)]
print(list)


# #### 2. Create and print a list of even numbers starting with 2 and ending with 200.

# In[64]:


lista2 = []

for i in range(2, 201):
    if i%2 == False:
        lista2.append(i)
        
print(lista2)


# In[35]:


list2 = [i for i in range(201) if i%2 == 0]
print(list2)


# #### 3. Create and print a list containing all elements of the 10 x 4 array below.

# In[50]:


a = [[0.84062117, 0.48006452, 0.7876326 , 0.77109654],
       [0.44409793, 0.09014516, 0.81835917, 0.87645456],
       [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
       [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
       [0.17003563, 0.46843998, 0.92796258, 0.69814654],
       [0.41290051, 0.19561071, 0.16284783, 0.97016248],
       [0.71725408, 0.87702738, 0.31244595, 0.76615487],
       [0.20754036, 0.57871812, 0.07214068, 0.40356048],
       [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
       [0.80930099, 0.50962849, 0.94555126, 0.33364763]];


# In[87]:


# matriz =[]
# for l in range(len(a)):
#     for c in range(len(a[l])):
#         matriz.append(a[l][c])
# print(matriz)

matriz = [a[l][c] for l in range(len(a)) for c in range(len(a[l]))]
print(matriz)


# #### 4. Add a condition to the loop above so that only values greater than or equal to 0.5 are printed.

# In[79]:


# matriz2 =[]
# for l in range(len(a)):
#     for c in range(len(a[l])):
#         if a[l][c] >= 0.5:
#             matriz.append(a[l][c])
# print(matriz)

matriz2 = [a[l][c] for l in range(len(a)) for c in range(len(a[l])) if a[l][c] >= 0.5]
print(matriz2)


# #### 5. Use a loop to create and print a list containing all elements of the 5 x 2 x 3 array below.

# In[59]:


b = [[[0.55867166, 0.06210792, 0.08147297],
        [0.82579068, 0.91512478, 0.06833034]],

       [[0.05440634, 0.65857693, 0.30296619],
        [0.06769833, 0.96031863, 0.51293743]],

       [[0.09143215, 0.71893382, 0.45850679],
        [0.58256464, 0.59005654, 0.56266457]],

       [[0.71600294, 0.87392666, 0.11434044],
        [0.8694668 , 0.65669313, 0.10708681]],

       [[0.07529684, 0.46470767, 0.47984544],
        [0.65368638, 0.14901286, 0.23760688]]];


# In[89]:


# cubo = []
# for l in range(len(b)):
#     for c in range(len(b[l])):
#         for z in range(len(b[l][c])):
#             cubo.append(b[l][c][z])
# print(cubo)

cubo = [b[l][c][z] for l in range(len(b)) for c in range(len(b[l])) for z in range(len(b[l][c]))]
print(cubo)


# #### 6. Add a condition to the loop above so that the last value in each subarray is printed, but only if it is less than or equal to 0.5.

# In[91]:


# cubo = []
# for l in range(len(b)):
#     for c in range(len(b[l])):
#             if b[l][c][-1] <= 0.5:
#                 cubo.append(b[l][c][-1])
# print(cubo)

cubo = [b[l][c][z] for l in range(len(b)) for c in range(len(b[l])) if b[l][c][-1] <= 0.5]
print(cubo)


# #### 7. Use a loop to select and print the names of all CSV files in the */data* directory.

# In[ ]:




