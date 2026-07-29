original_list = []
for i in range(1,11):
    original_list.append(i)
extracted_list = original_list[:5]
print(f"Original list: {original_list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {extracted_list[::-1]}")