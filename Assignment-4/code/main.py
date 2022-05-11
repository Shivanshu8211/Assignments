# Given data
S = {1,2,3,4,5,6}

E = {1,3,5}
prob_E = float(len(E)/len(S))

F = {2,3}
prob_F = float(len(F)/len(S))

G = {2,3,4,5}
prob_G = float(len(G)/len(S))

prob_E_And_F = float(len(E and F)/len(S))

# (i)
# p(E/F)
prob_E_by_F = float(prob_E_And_F/prob_F)
print("p(E/F) = ",prob_E_by_F)

# p(F/E)
prob_F_by_E = float(prob_E_And_F/prob_E)
print("p(F/E) = ",prob_F_by_E)

prob_E_And_G = float(len(E and G)/len(S))

# (ii)
# p(E/G)
prob_E_by_G = float(prob_E_And_G/prob_G)
print("p(E/G) = ",prob_E_by_G)

# p(G/E) 
prob_G_by_E = float(prob_E_And_G/prob_E)
print("p(G/E) = ",prob_G_by_E)

# (iii)
A = E or F
prob_A_and_G = float(len(A and G)/len(S))

# p((E∪F)/G)
prob_EUF_by_G = float(prob_A_and_G/prob_G)
print("p((E∪F)/G) = ",prob_EUF_by_G)

B = E and F
prob_B_and_G = float(len(B and G)/len(S))

# p((E∩F)/G)
prob_E_and_F_by_G = float(prob_B_and_G/prob_G)
print("p((E∩F)/G) = ",prob_E_and_F_by_G)
