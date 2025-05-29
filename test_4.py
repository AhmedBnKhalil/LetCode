from median_of_two_arrays_4 import Solution


def test_median_of_two_arrays():
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.findMedianSortedArrays([2], []) == 2.0


def test_median_of_two_arrays_2():
    s = Solution()
    assert (
        s.findMedianSortedArrays(
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
            ],
            [0, 6],
        )
        == 10.5
    )
