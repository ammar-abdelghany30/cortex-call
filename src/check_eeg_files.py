import re
import glob
import os



EEG_FOLDER = "../data/MI CSV"


# --------------------------------------------------
# Find all CSV files
# --------------------------------------------------

file_paths = glob.glob(os.path.join(EEG_FOLDER, "*.csv"))

print("=" * 60)
print("EEG FILE INSPECTION")
print("=" * 60)

print(f"\nFolder: {EEG_FOLDER}")
print(f"Total CSV files found: {len(file_paths)}")


# --------------------------------------------------
# Extract numbers from filenames
# --------------------------------------------------

file_info = []

pattern = re.compile(r"cellula_MI_data_(\d+)\.csv$", re.IGNORECASE)

for file_path in file_paths:

    filename = os.path.basename(file_path)

    match = pattern.match(filename)

    if match:
        file_number = int(match.group(1))

        file_info.append({
            "number": file_number,
            "filename": filename,
            "path": file_path
        })

    else:
        print(f"\n WARNING: Unexpected filename:")
        print(f"  {filename}")


# --------------------------------------------------
# Sort files by their numeric ID
# --------------------------------------------------

file_info.sort(key=lambda x: x["number"])


# --------------------------------------------------
# Display basic information
# --------------------------------------------------

numbers = [item["number"] for item in file_info]

print("\n" + "-" * 60)
print("NUMBER INFORMATION")
print("-" * 60)

if numbers:

    print(f"Number of correctly named files: {len(numbers)}")
    print(f"Smallest file number: {min(numbers)}")
    print(f"Largest file number: {max(numbers)}")


# --------------------------------------------------
# Check for duplicate numbers
# --------------------------------------------------

duplicates = []

for number in set(numbers):

    if numbers.count(number) > 1:
        duplicates.append(number)


print("\n" + "-" * 60)
print("DUPLICATE NUMBERS")
print("-" * 60)

if duplicates:
    print("Duplicate file numbers found:")

    for number in sorted(duplicates):
        print(f"  {number}")

else:
    print("No duplicate file numbers found.")


# --------------------------------------------------
# Check for missing numbers
# --------------------------------------------------

missing_numbers = []

if numbers:

    expected_numbers = set(range(min(numbers), max(numbers) + 1))
    actual_numbers = set(numbers)

    missing_numbers = sorted(expected_numbers - actual_numbers)


print("\n" + "-" * 60)
print("MISSING NUMBERS")
print("-" * 60)

if missing_numbers:

    print(f"Missing {len(missing_numbers)} file numbers:")

    for number in missing_numbers:
        print(f"  {number}")

else:
    print("No missing numbers found.")


# --------------------------------------------------
# Check whether numbering starts from 1
# --------------------------------------------------

print("\n" + "-" * 60)
print("NUMBERING CHECK")
print("-" * 60)

if numbers:

    if min(numbers) == 1:
        print("Numbering starts from 1.")
    else:
        print(f"WARNING: Numbering starts from {min(numbers)}, not 1.")


# --------------------------------------------------
# Show first and last files
# --------------------------------------------------

print("\n" + "-" * 60)
print("FIRST 10 FILES")
print("-" * 60)

for item in file_info[:10]:
    print(f"{item['number']:>5}  {item['filename']}")


print("\n" + "-" * 60)
print("LAST 10 FILES")
print("-" * 60)

for item in file_info[-10:]:
    print(f"{item['number']:>5}  {item['filename']}")


# --------------------------------------------------
# Final conclusion
# --------------------------------------------------

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

if numbers and not duplicates and not missing_numbers and min(numbers) == 1:

    print("The EEG files are numbered continuously from 1 to",
          max(numbers))

else:

    print("There are some issues with the EEG file numbering.")

print("=" * 60)