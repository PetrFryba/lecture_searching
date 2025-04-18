import json
import os

# get current working directory path
cwd_path = os.getcwd()


# def read_data(file_name, field):
#     """
#     Reads json file and returns sequential data.
#     :param file_name: (str), name of json file
#     :param field: (str), field of a dict to return
#     :return: (list, string),
#     """
#     file_path = os.path.join(cwd_path, file_name)
#     # nacteni povolenych klíčů ze souboru
#     with open('sequential.json','r') as f:
#         allowed_key = json.load(f)
#
#     # ověření, zda je zadaný klíč (field) v množině povolených klíčů
#     if field not in allowed_key:
#         return None
#
#     with open(file_name, 'r') as f:
#         data = json.load(f)
#
#     return data.get(field)
def read_data(file_name, field):
     """
     Reads json file and returns sequential data.
     :param file_name: (str), name of json file
     :param field: (str), field of a dict to return
     :return: (list, string),
     """
     if field not in {'unordered_numbers', 'ordered_numbers','dna_sequence'}:
         return None

     with open(file_name,'r') as json_file:
         seq = json.load(json_file)

     return seq[field]

def linear_search(seq, num):
     idx=[]
     count = 0

     for i in range(len(seq)):
          if seq[i] == num:
               idx.append(i)
               count = count+1

     return {'position': idx, 'count': count}


def pattern_search(seq, pattern):
     i = 0
     delka_pattern = len(pattern)

     vyskyt_vzoru = []
     while i <= len(seq)-delka_pattern:
          if seq[i:i+delka_pattern] == pattern:
               vyskyt_vzoru.append(i)

          i +=1

     return vyskyt_vzoru




def main():
     file_name = 'sequential.json'
     field = 'dna_sequence'
     pattern = 'ATA'

     seq = read_data(file_name, field)
     print(pattern_search(seq, pattern))


if __name__ == '__main__':
     main()




















# #
# def linear_search(sekvence, target):
#
#     position = []
#     count = 0
#     for num in enumerate(sekvence):
#         if num == target:
#             position.append(i+1)
#             count += 1
#
#     return {'position': position, 'count': count}
#
#
# def pattern_search(DNA_seq, pattern):
#     position = []
#     for i in range(len(DNA_seq)):
#         if DNA_seq[i:i+len(pattern)] == pattern:
#             pozice = DNA_seq[i:i+len(pattern)]
#             position.append(pozice)
#
#     return position
#
#
# def main():
#     # pass
# # zavolat funkce read_data s požadovanými vstupy
#     sequential_data = read_data("sequential.json", "unordered_numbers")
#     print(sequential_data)
#
#
#
#
# if __name__ == '__main__':
#     main()