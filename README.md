# Paper

## Matkul: Research Methodolohgy in CS

---

Structure:

1. Introduction -> tambahin referensi definisi
2. Literature Review -> kurangin yang unrelated
3. Methodology

   1. penjelasan algoritmanya (pseudocode/flowchart)
   2. jelasin dataset, library, sama spek pc yang dipake

4. Result and Discussion -> jelasin tabel/grafik dari hasil code
5. Conclusions -> bandingin running time dan number of iteration, jelasin algo mana yang bagus buat small/medium/big

## 4. Result and Discussion

### Working steps

- [x] Pilih algo & dataset
- ~~[x] Cari parser TSPLIB & algo buat python~~ gajadi, jadinya copas repo orang
- [x] Implementasi (janlup itung running time & iterations)

### 1. Material

**algo:**

- greedy (S)
- simulated annealing (M)
- particle swarm optimization (L)

**dataset TSPLIB:**

- Eil76 (S)
- D657 (M)
- Nrw1379 (L)

files: (<http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/>)

dokumentasi: (<http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf>)

**implementasi: jupyter notebook or python**

## Implementasi

Ada di folder program

Pake program dari <https://github.com/rameziophobia/Travelling_Salesman_Optimization>

Catatan:

- PSO buat D657 sama NRW1357 masih terlalu lama, mungkin butuh optimisasi
- SA parameternya masih bisa di tuning
- Buat paper, algo PSO sama SA run 20x terus catet min, max, sama avg dari hasil route, running time, sama iterations nya

### References (Uncategorized)

<https://www.ripublication.com/ijaer18/ijaerv13n9_42.pdf>
