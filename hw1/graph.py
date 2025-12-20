import matplotlib.pyplot as plt


N = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
time_sec = [2.605e-06, 2.2265e-05, 0.000261567, 0.00219196, 0.0259206, 0.230093, 2.16598, 21.3035]

plt.figure(figsize=(10, 6))
plt.plot(N, time_sec, 'bo-', label='Время вставки N элементов')
plt.xlabel('Количество элементов N')
plt.ylabel('Время (секунды)')
plt.title('Время добавления N элементов в пустой std::unordered_map')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show()