import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
ages = np.random.randint(18, 70, size=100)  
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in Population')
plt.grid(True)
plt.show()