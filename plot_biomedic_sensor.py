import matplotlib.pyplot as plt


def main():
    data_x1: list[str] = ['Lihat Kanan', 'Lihat Kiri', 'Lihat Atas', 'Lihat Bawah', 'Berkedip']
    data_y1: list[float] = [459, 737.6, 725.3, 995.6, 812.3]

    data_x2: list[str] = ['Relaksasi', '1/2 Relaksasi', 'Kontraksi']
    data_y2: list[float] = [522, 770.3, 1158]

    data_x3: list[str] = ['Olahraga', 'Bermain Game', 'Istirahat']
    data_y3: list[float] = [4.74, 3.803, 3.42]


    plt.figure(figsize=[6,8])
    plt.subplot(3,1,1)
    plt.plot(data_x1, data_y1)
    plt.ylabel('Vrms (mikrovolt)')
    plt.title('Sensor EMG di Wajah')
    plt.grid()
    
    plt.subplot(3,1,2)
    plt.plot(data_x2, data_y2)
    plt.ylabel('Vrms (mikrovolt)')
    plt.title('Sensor EMG di Tangan')
    plt.grid()

    plt.subplot(3,1,3)
    plt.plot(data_x3, data_y3)
    plt.ylabel('Vrms (milivolt)')
    plt.title('Sensor GSR')
    plt.grid()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()