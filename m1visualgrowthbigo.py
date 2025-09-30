import matplotlib.pyplot as plt
import num.p

n_nbs = np.arange(1, 100)
o1_nbs = np.ones_like(n_nbs)
on_nbs = n_nbs
on2_nbs = n_nbs**2

plt.plot(n, o1, label = "O(1)")
plt.plot(n, on, label = "O(n)")
plt.plot(n, on2, label = "O(n^2)")
plt.plot(n, ologn, label = "O(ologn)")
plt.legend()
plt.xlabel("input size(n)")
plt.ylabel("operations")
plt.title("big-o growth rate")
plt.show()