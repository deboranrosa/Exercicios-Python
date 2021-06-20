#!/usr/bin/env python
# coding: utf-8

# In[21]:


import sqlite3
db = sqlite3.connect('empresa')


# In[22]:


cursor = db.cursor()


# In[44]:


cursor.execute('SELECT primeiro_nome, segundo_nome, ultimo_nome FROM funcionarios ORDER BY ultimo_nome ASC')
for linha in cursor.fetchall():
    print(linha)


# In[49]:


cursor.execute('SELECT * FROM funcionarios ORDER BY cidade ASC')
for linha in cursor.fetchall():
    print(linha)


# In[65]:


cursor.execute('SELECT salario FROM funcionarios WHERE salario < 1000 ORDER BY primeiro_nome ASC, segundo_nome ASC, ultimo_nome ASC')
for linha in cursor.fetchall():
    print(linha)


# In[66]:


cursor.execute('SELECT data_nasci, primeiro_nome FROM funcionarios ORDER BY data_nasci DESC')
for linha in cursor.fetchall():
    print(linha)


# In[67]:


cursor.execute('SELECT SUM(salario) from funcionarios')
print(cursor.fetchall())


# In[68]:


cursor.execute('SELECT funcionarios.primeiro_nome, funcionarios.funcao, departamentos.nome FROM funcionarios INNER JOIN departamentos ON funcionarios.codigo_departamento = departamentos.codigo')
for linha in cursor.fetchall():
    print(linha)


# In[69]:


cursor.execute('SELECT COUNT(codigo) FROM funcionarios')
print(cursor.fetchall())


# In[63]:


cursor.execute('SELECT departamentos.nome, funcionarios.primeiro_nome FROM departamentos INNER JOIN funcionarios ON departamentos.codigo = funcionarios.codigo_departamento ORDER BY departamentos.codigo ASC, funcionarios.codigo ASC')
for linha in cursor.fetchall():
    print(linha)


# In[64]:





# In[ ]:




