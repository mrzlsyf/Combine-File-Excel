# Import Library
import pandas as pd, glob, os

# Membaca semua file csv
file_csv = glob.glob(os.path.join('*.csv'))

# List kosong untuk menampung data
data = []

# Looping untuk membaca semua file csv
for f in file_csv:
    # Eksrak nama file tanpa ekstensi
    nama_asli = os.path.basename(f)
    nama_file = os.path.splitext(nama_asli)[0]

    # Nama file dinamai dengan format 'ja_per_team'_'mp'_'store'_'tanggal'.csv
    # Contoh: Bm Marketplace EDC_Shopee CPAS_Herbavitshop Official_22 Januari 2025.csv
    # Membagi nama file berdasarkan karakter '_'
    # index 0 = ja_per_team, index 1 = mp, index 2 = store, index 3 = tanggal
    nama_file_split = nama_file.split('_')
    if len(nama_file_split) != 4:
        print(f'Nama file {f} tidak sesuai format.')
        continue

    ja_per_team = nama_file_split[0]
    mp = nama_file_split[1]
    store = nama_file_split[2]

    # Baca file csv
    df = pd.read_csv(f)

    # Sesuaikan kolom:
    # - raw_date diambil dari kolom 'Tanggal'
    # - amount diambil dari kolom 'Pengeluaran(IDR)'
    # - description diatur sebagai string kosong (''/null)
    df = df.rename(columns={'Tanggal': 'raw_date', 'Pengeluaran(IDR)': 'amount'})
    df['description'] = ''

    # Tambahkan kolom mp, ja_per_team, dan store
    df['mp'] = mp
    df['ja_per_team'] = ja_per_team
    df['store'] = store

    # Memilih kolom yang akan diambil
    df = df[['raw_date', 'amount', 'description', 'mp', 'ja_per_team', 'store']]
    
    data.append(df)

# Gabungkan semua data
gabungan_file = pd.concat(data, ignore_index=True)

# Simpan data ke dalam file csv
gabungan_file.to_csv('output.csv', index=False)

# Output
gabungan_file