import csv
import statistics

def read_data(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        data = [float(row[1]) for row in csv_reader if row]  # Assume data is in second column
    return data

def compute_statistics(data):
    return {
        'mean': statistics.mean(data),
        'median': statistics.median(data),
        'max': max(data),
        'min': min(data)
    }

def main():
    filename = 'data.csv'
    data = read_data(filename)
    stats = compute_statistics(data)
    print(f"Statistics for {filename}:")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Max: {stats['max']:.2f}")
    print(f"Min: {stats['min']:.2f}")

if __name__ == "__main__":
    main()
