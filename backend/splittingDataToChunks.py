import os

def split_file(input_file, output_dir, lines_per_file=500):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Split into chunks of 750 lines
    total_lines = len(lines)
    chunks = [lines[i:i + lines_per_file] for i in range(0, total_lines, lines_per_file)]

    # Save each chunk into separate files in the output directory5
    for i, chunk in enumerate(chunks[:20]):  # Create 6 chunks
        output_file = os.path.join(output_dir, f"extracted_chunk{i+1}.txt")
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.writelines(chunk)

    print("File splitting done.")

# Example usage
input_file = r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\everythingTogether.txt"
output_dir = r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\DataChunks"
split_file(input_file, output_dir)

