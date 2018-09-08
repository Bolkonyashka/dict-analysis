from time import time
import random
from dict import BFDict, BSDict, BTDict, BBTDict, HDict
import sys
import math
import timeit


class AnalyzData:
    def __init__(self):
        try:
            data_text = open("data//ruwords.txt", "r", encoding="utf-8")
        except IOError as e:
            print('Не удалось открыть файл')
        else:
            self.sorted_data = data_text.readlines()
            self.sorted_data.pop(0)
            self.random_data = self.sorted_data.copy()
            random.seed()
            random.shuffle(self.random_data)
            data_text.close()



class TimeAnalyzer:
    def __init__(self, dict_type):
        self.s_data = AnalyzData().sorted_data
        self.r_data = AnalyzData().random_data
        self.dict = dict_type
        self.results = {}
        self.data_count = 250

    def dict_init(self, data):
        for i in range(0, self.data_count):
            self.dict.add((data[i][:-1], "test"))

    def stdrt_dict_init(self, data):
        for i in range(0, self.data_count):
            self.dict[data[i][:-1]] = "test"

    def analysis_maker(self, dict_ind, oper_type, dict_type, data_type, init_func, analysis_func):
        for k in range(0, 6):
            self.data_count *= 2
            if dict_ind == 0:
                self.dict = BFDict()
            elif dict_ind == 1:
                self.dict = BSDict()
            elif dict_ind == 2:
                self.dict = BTDict()
            elif dict_ind == 3:
                self.dict = BBTDict()
            elif dict_ind == 4:
                self.dict = HDict()
            elif dict_ind == 5:
                self.dict = {}
            init_func(data_type)

            res_list = []
            res_sum = 0
            n = 1000
            for i in range(0, n):
                res_list.append(analysis_func())
            for j in res_list:
                res_sum += j
            av_res = res_sum / n
            self.results[self.data_count] = av_res

        res_file = open("results//" + oper_type + dict_type + ".txt", "a")
        counter = 250
        for h in range(0, 6):
            counter *= 2
            res_file.write(str(self.results[counter]) + "\n")
        res_file.write("---------\n")
        res_file.close()

    def make_add(self):
        tic1 = timeit.default_timer()
        self.dict.add(("яяяяя", "test"))
        tic2 = timeit.default_timer()
        k = self.dict.pop("яяяяя")
        return tic2 - tic1

    def stdrt_make_add(self):
        tic1 = timeit.default_timer()
        self.dict["яяяяя"] = "test"
        tic2 = timeit.default_timer()
        k = self.dict.pop("яяяяя")
        return tic2 - tic1

    def make_get(self):
        self.dict.add(("яяяяя", "test"))
        tic1 = timeit.default_timer()
        res = self.dict.get("яяяяя")
        tic2 = timeit.default_timer()
        k = self.dict.pop("яяяяя")
        return tic2 - tic1

    def stdrt_make_get(self):
        self.dict["яяяяя"] = "test"
        tic1 = timeit.default_timer()
        res = self.dict["яяяяя"]
        tic2 = timeit.default_timer()
        k = self.dict.pop("яяяяя")
        return tic2 - tic1

    def make_items(self):
        tic1 = timeit.default_timer()
        res = self.dict.items()
        return timeit.default_timer() - tic1

    def make_pop(self):
        self.dict.add(("яяяяя", "test"))
        tic1 = timeit.default_timer()
        res = self.dict.pop("яяяяя")
        return timeit.default_timer() - tic1

    def stdrt_make_pop(self):
        self.dict["яяяяя"] = "test"
        tic1 = timeit.default_timer()
        res = self.dict.pop("яяяяя")
        return timeit.default_timer() - tic1

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    analyser = TimeAnalyzer(BFDict())
    analyser.analysis_maker(0, "POP", "BFDict", analyser.s_data, analyser.dict_init, analyser.make_pop)
    analyser.data_count = 250
    analyser.results.clear()
    analyser.analysis_maker(1, "POP", "BSDict", analyser.s_data, analyser.dict_init, analyser.make_pop)
    analyser.data_count = 250
    analyser.results.clear()
    analyser.analysis_maker(2, "POP", "BTDict", analyser.s_data, analyser.dict_init, analyser.make_pop)
    analyser.data_count = 250
    analyser.results.clear()
    analyser.analysis_maker(3, "POP", "BBTDict", analyser.s_data, analyser.dict_init, analyser.make_pop)
    analyser.data_count = 250
    analyser.results.clear()
    analyser.analysis_maker(4, "POP", "HDict", analyser.s_data, analyser.dict_init, analyser.make_pop)
    analyser.data_count = 250
    analyser.results.clear()
    analyser.analysis_maker(5, "POP", "Dict", analyser.s_data, analyser.stdrt_dict_init, analyser.stdrt_make_pop)
