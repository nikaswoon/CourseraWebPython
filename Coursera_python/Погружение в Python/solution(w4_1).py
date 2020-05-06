import os.path
import tempfile
import uuid


class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.len = 0
        self.start = -1
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, 'tw', encoding='utf-8') as self.f:
                pass

    def __iter__(self):
        return self

    def __next__(self):

        listik = File.inside(self.path_to_file)
        # listik = s.split(sep='\n')
        self.len = len(listik)
        self.start += 1
        if self.len > self.start:
            return listik[self.start]
        raise StopIteration

    def __add__(self, obj2):
        storage_path = os.path.join(tempfile.gettempdir(), f'{uuid.uuid4()}.txt')
        item = File(storage_path)
        with open(storage_path, "w") as fp:
            fp.write(self.read() + obj2.read())
            # print(f"Writtent in file{storage_path} - {self.read() + obj2.read()}")

        return item

    @staticmethod
    def inside(p):
        with open(p, 'r', encoding='utf-8') as f:
            return f.readlines()

    def read(self):
        with open(self.path_to_file, 'r', encoding='utf-8') as self.f:
            inside = self.f.read()
            return inside

    def write(self, nutr):
        with open(self.path_to_file, 'w', encoding='utf-8') as self.f:
            self.f.write(str(nutr))
            return len(nutr)

    def __exit__(self, *args):
        self.f.close()

    def __str__(self):
        return '{}'.format(os.path.abspath(self.path_to_file))


if __name__ == '__main__':
    path_to_file = 'some_filename.txt'
    file_obj = File(path_to_file)
    file_obj.read()
    print(file_obj.read())
    print(file_obj.write("text"))
    file_obj.read()
    file_obj.write('other text')
    file_obj.read()
    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    file_obj_1.write('line 1\n')
    file_obj_2.write('line 2\n')
    new_file_obj = file_obj_1 + file_obj_2
    print(type(new_file_obj), type(file_obj_1), type(file_obj_2))
    print(isinstance(new_file_obj, File))
    print(file_obj_1)
    print(file_obj_2)
    print(new_file_obj)
    print(type(new_file_obj))
    for line in new_file_obj:
        print(ascii(line))
