import csv,uuid

# def convert_to_csv(data):
#     output = io.BytesIO()
#     fieldnames = data[0].keys()
#     writer = csv.DictWriter(io.TextIOWrapper(output, encoding='utf-8'), fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)
#     output.seek(0)
#     return output.getvalue()
# def convert_to_csv(data):
#     fields = ['id', 'phone', 'username']
#     output = io.BytesIO()
#     writer = csv.DictWriter(io.TextIOWrapper(output, encoding='utf-8'), fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

#     return output

def convert_to_csv(data,id):
    fields = ['id', 'phone', 'username']

    output = f"{id}_{uuid.uuid4()}_stats.csv"

    with open(output, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
    
    return output