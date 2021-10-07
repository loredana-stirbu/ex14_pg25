n=int(input("Dati dimensiunea matricei: "))

matrice=[]
diagonala_principala=[]
diagonala_secundara=[] 
m_s_dp=[]
m_j_dp=[]
m_s_ds=[]
m_j_ds=[]

if(n>=2)and(n<=10):
    for i in range(n):
        k=[]
        for j in range(n):
            k.append(int(input("Dati elemente: ")))
        matrice.append(k)
    print(matrice)

    for i in range(len(matrice)):
        for j in range(len(matrice[0])) :
            if i==j :
                diagonala_principala.append(matrice[i][j])
    print("Suma diagonala principala:",sum(diagonala_principala))

    
    for i in range(len(matrice)):
        for j in range(len(matrice[0])) :
            if i+j==n-1:
                diagonala_secundara.append(matrice[i][j])
    print("Suma diagonala secundara:",sum(diagonala_secundara)) 

    for i in range(len(matrice)):
        for j in range(len(matrice[0])) :
            if i-j<0 :
                m_s_dp.append(matrice[i][j])
    print("Suma mai sus de diagonala principala:",sum(m_s_dp))

    
    for i in range(len(matrice)):
        for j in range(len(matrice[0])) :
            if i-j>0 :
                m_j_dp.append(matrice[i][j])
    print("Suma mai jos de diagonala principala:",sum(m_j_dp))

    
    for i in range(len(matrice)):
        for j in range(len(matrice[0])) :
            if i+j<n-1 :
                m_s_ds.append(matrice[i][j])
    print("Suma mai sus de diagonala secundara:",sum(m_s_ds))

    for i in range(len(matrice)):
        for j in range(len(matrice[0])) :
            if i+j>n-1 :
                m_j_ds.append(matrice[i][j])
    print("Suma mai sus de diagonala secundara:",sum(m_j_ds))

else:
    print("Recititi conditia initiala")
