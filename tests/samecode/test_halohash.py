#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import, print_function

from os.path import join
from os.path import os
from unittest import skipIf
from unittest.case import skipUnless

from bitarray import bitarray

import commoncode
from commoncode.testcase import FileBasedTesting

from samecode import halohash
from samecode import hash as commoncode_hash

# un-comment to run perf tests
PERF_TEST_ENABLED = False


class TestHalohash(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')
    def test_BaseHaloHash(self):
        class TestBaseHaloHash(halohash.BaseHaloHash):
            def __init__(self):
                halohash.BaseHaloHash.__init__(self)
            def compute(self):
                return bitarray([1] * len(self.hashes))

        tbhh = TestBaseHaloHash()
        assert [] == tbhh.hashes

        tbhh.update('1')
        assert ['1'] == tbhh.hashes

        tbhh.update(['2', '3'])
        assert ['1', '2', '3'] == tbhh.hashes

        assert '111' == tbhh.hash().to01()
        assert 7 == tbhh.intdigest()
        assert '\xe0' == tbhh.digest()
        assert 'e0' == tbhh.hexdigest()
        assert 3 == tbhh.elements_count()

    def test_BaseBucketHaloHash(self):
        class BaseBucketHaloHashSubclass(halohash.BaseBucketHaloHash):

            def __init__(self, size_in_bits):
                halohash.BaseBucketHaloHash.__init__(self, size_in_bits=size_in_bits)

            def compute(self):
                return bitarray([1] * len(self.hashes))

        tbbhh = BaseBucketHaloHashSubclass(size_in_bits=32)
        assert commoncode_hash.get_hasher(160) == tbbhh.hashmodule

        tbbhh.update(['1', '2', '3'])
        buck = tbbhh.build_buckets()
        expected = [
            None, None, None, None, None, None,
            [bitarray('1010110101000011001001010110111100100010011101'
                      '1000001001100010101000101011101001101000110001'
                      '1000010100011010100011011100110001110010101010'
                      '00010100010101011')],
            None, None, None, None, None, None, None,
            [bitarray('1111101111001101000110110101110110011011000001'
                      '0001110111010101110111011010110001110110110110'
                      '0011100100011100001010011010111000100000110111'
                      '01000001110111011')],
            None, None, None, None, None, None, None,
            None, None, None, None, None,
            [bitarray('0100100101110010010001101111011101011001100110'
                      '0110111110001100111000000011101100000110010101'
                      '0110111101011101100010010101000001101011001000'
                      '00001000010110000')],
            None, None, None, None]
        assert expected == buck

        hashsize = 2 ** 7
        tbbhh = BaseBucketHaloHashSubclass(size_in_bits=hashsize)
        tbbhh.update([ str(x) for x in range(1024)])
        buck = tbbhh.build_buckets()
        assert hashsize == len(buck)

    def test_BucketAverageHaloHash_file_matching(self):
        base = self.get_test_loc('halohash/neardupe1')

        def geth(fn, size_in_bits=32):
            f = open(join(base, fn)).read()
            return halohash.BucketAverageHaloHash(f.split(), size_in_bits).hash()

        h1 = geth('djc1')
        h2 = geth('djc2')
        h3 = geth('djc3')
        h4 = geth('djc4')
        h5 = geth('annotations.txt')
        assert 0 == halohash.hamming_distance(h1, h1)
        assert 0 == halohash.hamming_distance(h1, h2)
        assert 5 == halohash.hamming_distance(h1, h3)
        assert 5 == halohash.hamming_distance(h1, h4)
        assert 5 == halohash.hamming_distance(h2, h3)
        assert 17 == halohash.hamming_distance(h1, h5)

        h1 = geth('djc1', size_in_bits=256)
        h2 = geth('djc2', size_in_bits=256)
        h3 = geth('djc3', size_in_bits=256)
        h4 = geth('djc4', size_in_bits=256)
        h5 = geth('annotations.txt', size_in_bits=256)
        assert 0 == halohash.hamming_distance(h1, h1)
        assert 0 == halohash.hamming_distance(h1, h2)
        assert 5 == halohash.hamming_distance(h1, h3)
        assert 17 == halohash.hamming_distance(h1, h4)
        assert 5 == halohash.hamming_distance(h2, h3)
        assert 78 == halohash.hamming_distance(h1, h5)

    def test_BitAverageHaloHash_file_matching(self):
        base = self.get_test_loc('halohash/neardupe1')

        def geth(fn, size=32):
            f = open(join(base, fn)).read()
            return halohash.BitAverageHaloHash(f.split(), size).hash()

        h1 = geth('djc1')
        h2 = geth('djc2')
        h3 = geth('djc3')
        h4 = geth('djc4')
        h5 = geth('annotations.txt')
        assert 0 == halohash.hamming_distance(h1, h1)
        assert 2 == halohash.hamming_distance(h1, h2)
        assert 4 == halohash.hamming_distance(h1, h3)
        assert 7 == halohash.hamming_distance(h1, h4)
        assert 2 == halohash.hamming_distance(h2, h3)
        assert 16 == halohash.hamming_distance(h1, h5)

    def test_BitAverageHaloHash_simple(self):
        a = halohash.BitAverageHaloHash(None, size_in_bits=512)
        [a.update(str(x)) for x in xrange(4096)]
        expected = '1c61001246514d1bea84fb65df08d71f2d3181ae1ac9d67c1bd38b988e5b2d6ea4b3e1b2cc2f66cd08de7ec269210c0e94f551f13425291572bf38892136a71c'
        assert expected == a.hexdigest()

    def test_BitAverageHaloHash_elements_count_unicode(self):
        a = halohash.BitAverageHaloHash(None, size_in_bits=512)
        [a.update(unicode(x)) for x in xrange(4096)]
        assert 4096 == a.elements_count()

    def _random_HaloHash_test(self, module, size_in_bits, chunk_size):
        """
        Using two files created with dd from a Linux /dev/urandom as an input,
        this test split each file in chunks. A halohash is computed over the
        chunks and the hamming distance is computed for each file. The second
        files is progressively injected one chunk at a time from the first
        file, mimicking a gradual buildup of similarity
        """
        # the two random files are exactly 70000 bytes... use a chunk size that
        # is a divider of it
        assert 70000 % chunk_size == 0

        base = self.get_test_loc('halohash/random')

        def chunks(seq, n):
            """
            Return a sequence of contiguous non-overlapping chunks of size n.
            """
            return [seq[i : i + n] for i in range(len(seq))[::n]]

        random1 = open(join(base, 'random1.txt'), 'rb').read()
        random_chunks_1 = chunks(random1, chunk_size)
        hash_on_random1 = module(size_in_bits=size_in_bits)
        for x in random_chunks_1:
            hash_on_random1.update(x)

        hash1 = hash_on_random1.hash()

        random2 = open(join(base, 'random2.txt'), 'rb').read()
        random_chunks_2 = chunks(random2, chunk_size)

        res = []
        for i in range(len(random_chunks_1)):
            # create a new halohash on the the second list
            hash_on_random2 = module(size_in_bits=size_in_bits)
            for y in random_chunks_2:
                hash_on_random2.update(y)
                hash2 = hash_on_random2.hash()
            # compare with the original under bit hamming distance
            res.append((i, halohash.hamming_distance(hash1, hash2)))
            # replace one chunk to mimic similarity buildup
            random_chunks_2[i] = random_chunks_1[i]
        return res

    def test_random_BitAverageHaloHash(self):
        result = self._random_HaloHash_test(halohash.BitAverageHaloHash, 256, 1000)
        expected = [
            (0, 132), (1, 134), (2, 133), (3, 127), (4, 125), (5, 124), (6, 122), (7,
            121), (8, 116), (9, 114), (10, 113), (11, 111), (12, 113), (13, 113),
            (14, 114), (15, 114), (16, 107), (17, 104), (18, 104), (19, 98), (20,
            104), (21, 102), (22, 98), (23, 92), (24, 93), (25, 88), (26, 89), (27,
            83), (28, 87), (29, 87), (30, 95), (31, 90), (32, 91), (33, 86), (34,
            81), (35, 82), (36, 86), (37, 90), (38, 88), (39, 81), (40, 81), (41,
            78), (42, 74), (43, 74), (44, 68), (45, 70), (46, 69), (47, 66), (48,
            63), (49, 62), (50, 58), (51, 57), (52, 51), (53, 51), (54, 52), (55,
            53), (56, 55), (57, 49), (58, 46), (59, 44), (60, 36), (61, 41), (62,
            34), (63, 35), (64, 29), (65, 27), (66, 28), (67, 21), (68, 15), (69,
            12)]
        assert expected == result

    def test_random_BucketAverageHaloHash(self):
        result = self._random_HaloHash_test(halohash.BucketAverageHaloHash, 256, 1000)
        expected = [
            (0, 54), (1, 52), (2, 51), (3, 50), (4, 49), (5, 47), (6, 46), (7, 47),
            (8, 45), (9, 44), (10, 43), (11, 42), (12, 42), (13, 42), (14, 41), (15,
            41), (16, 40), (17, 38), (18, 38), (19, 38), (20, 36), (21, 35), (22,
            34), (23, 33), (24, 33), (25, 32), (26, 31), (27, 33), (28, 33), (29,
            31), (30, 31), (31, 29), (32, 29), (33, 27), (34, 28), (35, 28), (36,
            28), (37, 27), (38, 25), (39, 23), (40, 22), (41, 21), (42, 20), (43,
            18), (44, 18), (45, 17), (46, 16), (47, 16), (48, 16), (49, 16), (50,
            14), (51, 13), (52, 13), (53, 12), (54, 12), (55, 11), (56, 10), (57, 9),
            (58, 9), (59, 7), (60, 5), (61, 4), (62, 4), (63, 4), (64, 3), (65, 2),
            (66, 2), (67, 1), (68, 0), (69, 0)]
        assert expected == result


if PERF_TEST_ENABLED:

    try:
        import numpy
    except ImportError:
        numpy = None


    @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
    class TestBitAvgHaloHashPerformance(FileBasedTesting):

        def check_perf_for_obj(self, a):
            import cProfile as profile
            import pstats
            stats = 'profile_log_txt'
            profile.runctx('''
    for x in range(100000):
        a.update("/project/path/test/a/" + str(x))
    b = a.hexdigest()
    ''',
                        globals(), locals(), stats)
            p = pstats.Stats(stats)
            p.sort_stats('cumulative').print_stats(100)
            os.remove(stats)

            try:
                from pympler import asizeof  # @UnresolvedImport
                print('Size of object:', asizeof.asizeof(a))
                print()
            except:
                pass
            expected = 'fe01e1389b43d115fb6b8f9a13eee937b599eebf4d4fac33866741bd33819466c38dc8c2cabdeb415179bb9fcff570d57d8ea80db21def5ebe7cc4b1b078c1e7'
            assert expected == a.hexdigest()

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        def test_profile_bit_average_1(self):
            # use the current implementation using numpy if present
            # or the next best pure python if no numpy
            a = halohash.BitAverageHaloHash(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        def test_optimization_hashup_using_map_no_numpy(self):
            from operator import add
            # NOTE: this twice slower than numpy
            class OptimizedBitAvgHaloHashMap(halohash.BitAverageHaloHash):
                def __hashup__(self, m):
                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())
                    self.hashes = map(add, self.hashes, ba)
                    self.hashed_elements += 1

            a = OptimizedBitAvgHaloHashMap(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        def test_optimization_hashup_using_imap_and_bitarrayaccumulation(self):
            # NOTE: this is as fast as numpy and uses only a tad more more memory
            # because of the hashes accumulation
            # we consume iterators now and then to keep the memory consumption low
            from itertools import izip, imap
            class OptimizedBitAvgHaloHashMapDelayed(halohash.BitAverageHaloHash):
                def __init__(self, msg=None, size_in_bits=128):
                    halohash.BaseHaloHash.__init__(self)
                    self.size_in_bits = size_in_bits
                    self.digest_size = self.size_in_bits / 8
                    self.hashes = []
                    self.hashed_elements = 0
                    try:
                        self.hashmodule = commoncode.hash.get_hasher(size_in_bits)
                    except:
                        msg = ('No available hash module for the requested hash '
                             'size in bits: %(size_in_bits)d' % locals())
                        raise Exception(msg)
                    self.update(msg)

                def __hashup__(self, m):
                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())
                    self.hashes.append(ba)
                    self.hashed_elements += 1
                    if self.hashed_elements % 50000 == 0:
                        # every now and then consume iterators to avoid memory
                        # exhaustion on large collections
                        self.sum_up()

                def sum_up(self):
                    """
                    Sum each bit column.
                    """
                    self.hashes = [list(imap(sum, izip(*self.hashes)))]

                def compute(self):
                    """
                    Computes the bit average hash. The mean is global to a hash as
                    it depends on the number of hashed values.

                    # FIXME: this is not using FLOATs and therefore the division IS
                    # wrong, but only by one... this is however likely incorrectly
                    # introducing a BIAS but we cannot change this since we have
                    # fingerprints indexed and computed with this wrong algorithm
                    """
                    mean = self.elements_count() / 2
                    self.sum_up()
                    averaged = [1 if s > mean else 0 for s in self.hashes[0]]
                    return bitarray(averaged)

            a = OptimizedBitAvgHaloHashMapDelayed(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        @skipIf(not numpy, 'Numpy is not installed')
        def test_optimization_1_numpy_bit_avg(self):
            class OptimizedBitAvgHaloHash(halohash.BitAverageHaloHash):
                def __hashup__(self, m):
                    if self.hashes == []:
                        self.hashes = [0] * self.size_in_bits
                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())
                    self.hashes = (numpy.vstack(
                                    (self.hashes,
                                     numpy.asarray(ba.tolist())))
                                   .sum(axis=0))
                    self.hashed_elements += 1

            a = OptimizedBitAvgHaloHash(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        @skipIf(not numpy, 'Numpy is not installed')
        def test_optimization_2_numpy_bit_avg(self):
            class OptimizedBitAvgHaloHash2(halohash.BitAverageHaloHash):
                vectors = []
                def __hashup__(self, m):
                    if self.hashes == []:
                        self.hashes = [0] * self.size_in_bits

                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())

                    self.vectors.append(numpy.array(ba.tolist()))
                    self.hashed_elements += 1

                    if self.hashed_elements % 100 == 0:
                        self.hashes = numpy.vstack((self.hashes, numpy.vstack(tuple(self.vectors)))).sum(axis=0)
                        self.vectors = []

            a = OptimizedBitAvgHaloHash2(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        @skipIf(not numpy, 'Numpy is not installed')
        def test_optimization_3_numpy_bit_avg(self):
            class OptimizedBitAvgHaloHash3(halohash.BitAverageHaloHash):
                vectors = []
                def __hashup__(self, m):
                    if self.hashes == []:
                        self.hashes = [0] * self.size_in_bits
                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())
                    self.vectors.append(ba.tolist())
                    self.hashed_elements += 1

                    if self.hashed_elements % 100 == 0:
                        s = numpy.cumsum(self.vectors, axis=0)
                        self.hashes = numpy.vstack((self.hashes, s)).sum(axis=0)
                        self.vectors = []

            a = OptimizedBitAvgHaloHash3(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        @skipIf(not numpy, 'Numpy is not installed')
        def test_optimization_4_numpy_bit_avg(self):
            class OptimizedBitAvgHaloHash4(halohash.BitAverageHaloHash):
                vectors = []
                def __hashup__(self, m):
                    if self.hashes == []:
                        self.hashes = [0] * self.size_in_bits

                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())

                    self.vectors.append(ba.tolist())
                    self.hashed_elements += 1

                    if self.hashed_elements % 10000 == 0:
                        self.hashes = numpy.vstack((self.hashes,
                                                    numpy.matrix(self.vectors)
                                                    .sum(axis=0))).sum(axis=0)
                        self.vectors = []

            a = OptimizedBitAvgHaloHash4(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        def test_optimization_5_native_arrays(self):
            class OptimizedBitAvgHaloHash5(halohash.BitAverageHaloHash):
                vectors = []
                def __hashup__(self, m):
                    if self.hashes == []:
                        self.hashes = [0] * self.size_in_bits
                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())

                    self.vectors.append(ba)
                    self.hashed_elements += 1
                    if self.hashed_elements % 10000 == 0:
                        for v in self.vectors:
                            for i in range(self.size_in_bits):
                                self.hashes[i] += v[i]
                        self.vectors = []

            a = OptimizedBitAvgHaloHash5(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        @skipIf(not numpy, 'Numpy is not installed')
        def test_optimization_5_native_dicts(self):
            class OptimizedBitAvgHaloHash5(halohash.BitAverageHaloHash):
                def __hashup__(self, m):
                    if self.hashes == []:
                        self.hashes = [0] * self.size_in_bits
                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())

                    self.hashes = (numpy.vstack((self.hashes,
                                                 numpy.array(ba.tolist())))
                                   .sum(axis=0))
                    self.hashed_elements += 1

            a = OptimizedBitAvgHaloHash5(None, size_in_bits=512)
            self.check_perf_for_obj(a)

        @skipUnless(PERF_TEST_ENABLED, 'Perf test disabled')
        @skipIf(not numpy, 'Numpy is not installed')
        def test_optimization_numpy_fast_array_conversion(self):
            class OptimizedBitAvgHaloHash(halohash.BitAverageHaloHash):
                def __hashup__(self, m):
                    if self.hashes == []:
                        self.hashes = [0] * self.size_in_bits
                    h = self.hashmodule(m)
                    ba = bitarray()
                    ba.fromstring(h.digest())
                    b = numpy.fromstring(ba.unpack(), dtype=bool)
                    self.hashes = numpy.vstack((self.hashes, b)).sum(axis=0)
                    self.hashed_elements += 1

            a = OptimizedBitAvgHaloHash(None, size_in_bits=512)
            self.check_perf_for_obj(a)
